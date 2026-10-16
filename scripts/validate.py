#!/usr/bin/env python3
"""Check kit structure, skill metadata, local links and common publication risks."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

KIT = Path(__file__).resolve().parents[1]


def validate(root=KIT):
    errors = []
    paths = [p for p in root.rglob("*") if ".git" not in p.relative_to(root).parts]
    files = sorted(p for p in paths if p.is_file())
    manifest = json.loads((root / "kit.json").read_text())
    expected = set(manifest["skills"])
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if actual != expected:
        errors.append("Skill manifest differs from files")
    for p in paths:
        if p.is_symlink():
            errors.append("Symlink: " + str(p.relative_to(root)))
        if p.name in {".DS_Store", "__pycache__", "auth.json", ".env"}:
            errors.append("Private/generated path: " + str(p.relative_to(root)))
    links = 0
    patterns = {
        "personal path": r"/(?:Users|home)/[^\s`<>]+",
        "private email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "private task URL": r"https?://(?:app\.)?clickup\.com/[^\s)]+",
        "credential candidate": r"(?i)(?:pk_[A-Za-z0-9_]{16,}|(?:api[_-]?key|password|secret|access_token)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{24,})",
        "private key candidate": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "provider token candidate": r"(?:AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{40,}|xox[baprs]-[A-Za-z0-9-]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{32,})",
    }
    for p in files:
        if p.suffix not in {".md", ".py", ".json", ".yaml", ".txt"} and p.name not in {".gitignore", "LICENSE"}:
            errors.append("Unexpected file type: " + str(p.relative_to(root)))
            continue
        text = p.read_text()
        if p.name == "SKILL.md":
            match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
            if not match:
                errors.append("Missing frontmatter: " + str(p.relative_to(root)))
                continue
            fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", match[1], re.M))
            if fields.get("name") != p.parent.name or not fields.get("description"):
                errors.append("Invalid skill metadata: " + str(p.relative_to(root)))
        if p.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                parsed = urlsplit(target.strip("<>"))
                if parsed.scheme:
                    if parsed.scheme != "https":
                        errors.append("Unsupported link scheme: " + str(p.relative_to(root)))
                    continue
                local = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
                links += 1
                if not local.is_relative_to(root) or not local.exists():
                    errors.append("Broken or escaping link: " + str(p.relative_to(root)))
        for label, pattern in patterns.items():
            if re.search(pattern, text):
                errors.append(label + ": " + str(p.relative_to(root)))
    return {"ok": not errors, "skills": len(actual), "files": len(files), "local_links": links, "errors": errors}


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["ok"] else 1)
