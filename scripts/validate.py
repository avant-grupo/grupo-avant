"""Validate the exact public Git index without printing sensitive matches."""

import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def fail(path, reason):
    errors.append(f"{path}: {reason}")


entries = {}
for row in git("ls-files", "--stage", "-z").split(b"\0"):
    if not row:
        continue
    metadata, raw_path = row.split(b"\t", 1)
    mode, _, stage = metadata.decode().split()
    path = raw_path.decode()
    if stage != "0" or mode != "100644":
        fail(path, "only regular text files without conflicts are permitted")
        continue
    entries[path] = git("show", f":{path}")

try:
    manifest = json.loads(entries["publication-manifest.json"])
    allowed = manifest["files"]
    if not isinstance(allowed, list) or any(not isinstance(p, str) for p in allowed):
        raise ValueError("invalid file list")
    if len(allowed) != len(set(allowed)):
        raise ValueError("duplicate paths")
    for path in allowed:
        parts = PurePosixPath(path).parts
        if not parts or path.startswith("/") or ".." in parts or "\\" in path:
            raise ValueError("unsafe path")
    if manifest["schema_version"] != 1:
        raise ValueError("unsupported schema")
except (KeyError, ValueError, TypeError):
    print("FAIL: invalid or missing publication manifest")
    sys.exit(1)

if set(entries) != set(allowed):
    for path in sorted(set(entries) - set(allowed)):
        fail(path, "not in the publication allowlist")
    for path in sorted(set(allowed) - set(entries)):
        fail(path, "allowed file missing from the index")

patterns = {
    "local path or session link": r"(?:/Users/|/home/|file://|t3-thread:|plugin://)",
    "email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "IPv4 address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "phone number": r"(?<!\d)(?:\+?55[ .-]?)?\(?\d{2}\)?[ .-]?9\d{4}[ .-]?\d{4}(?!\d)",
    "message timestamp": r"(?m)^\s*\[?\d{1,2}:\d{2}(?::\d{2})?\]?\s*[-:]",
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "credential-like value": r"(?:sk-(?:or-v1-|proj-)?[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})",
    "JWT-like value": r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
}

texts = {}
for path, blob in entries.items():
    if len(blob) > 128_000:
        fail(path, "file exceeds the text size limit")
    try:
        text = blob.decode("utf-8")
    except UnicodeDecodeError:
        fail(path, "non UTF-8 content")
        continue
    if "\0" in text:
        fail(path, "binary content")
    texts[path] = text
    disk = ROOT / path
    if disk.is_symlink() or not disk.is_file() or disk.read_bytes() != blob:
        fail(path, "working file differs from the prepared public index")
    if not path.endswith(".md"):
        continue
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            fail(path, label)
    for match in re.finditer(r"!?\[[^\]]*\]\(<?([^\s)>]+)>?\)", text):
        target = unquote(match.group(1))
        url = urlsplit(target)
        if url.scheme or url.netloc:
            if url.scheme != "https" or url.hostname != "github.com" or url.username or url.password or url.query:
                fail(path, "external link outside the permitted GitHub context")
            continue
        if target.startswith("/"):
            fail(path, "absolute link")
            continue
        if url.path:
            resolved = (ROOT / path).parent.joinpath(url.path).resolve()
            if not resolved.is_relative_to(ROOT) or resolved.relative_to(ROOT).as_posix() not in entries:
                fail(path, "local link is not a published file")

expected_ignore = {f"!/{p}" for p in allowed}
ignore_lines = set(texts.get(".gitignore", "").splitlines())
for rule in sorted(expected_ignore - ignore_lines):
    fail(".gitignore", "missing an explicit allowed-file exception")
if "*" not in ignore_lines:
    fail(".gitignore", "default exclusion missing")

backlog_text = texts.get("backlog/README.md", "")
ids = re.findall(r"^\| (BL-\d{3}) \|", backlog_text, re.MULTILINE)
if ids != [f"BL-{n:03d}" for n in range(1, 70)]:
    fail("backlog/README.md", "the original 69 unique backlog IDs must remain in order")

if errors:
    print("FAIL: publication validation")
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(entries)} allowlisted text files, local links and 69 backlog IDs; no configured privacy patterns found")
