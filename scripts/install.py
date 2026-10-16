#!/usr/bin/env python3
"""Copy the manifest's skills without replacing existing paths. Preview by default."""

import argparse
import json
from pathlib import Path
import re
import shutil
import sys

KIT = Path(__file__).resolve().parents[1]


def install(destination, apply=False, runtime="codex"):
    manifest = json.loads((KIT / "kit.json").read_text())
    if runtime not in manifest["installer_runtimes"]:
        raise ValueError("Unsupported runtime")
    names = manifest["skills"]
    if not names or len(names) != len(set(names)):
        raise ValueError("Invalid skill manifest")
    for name in names:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError("Invalid skill name")
        source = KIT / "skills" / name
        if source.is_symlink() or not (source / "SKILL.md").is_file():
            raise ValueError("Missing skill or linked source")
        if any(p.is_symlink() for p in source.rglob("*")):
            raise ValueError("Linked files are not installable")

    destination = Path(destination).expanduser().absolute()
    if destination.is_symlink():
        raise ValueError("Destination must not be a symlink")
    destination = destination.resolve()
    if destination == KIT or KIT in destination.parents:
        raise ValueError("Destination must be outside the kit")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination must be a directory")
    if any((destination / name).exists() or (destination / name).is_symlink() for name in names):
        raise ValueError("An installed skill name already exists; nothing was replaced")

    if not apply:
        print(json.dumps({"action": "preview", "runtime": runtime, "destination": str(destination), "skills": names}))
        return

    destination_existed = destination.exists()
    reserved = []
    try:
        destination.mkdir(parents=True, exist_ok=True)
        for name in names:
            target = destination / name
            target.mkdir()
            reserved.append(target)
        for target in reserved:
            shutil.copytree(KIT / "skills" / target.name, target, dirs_exist_ok=True)
            if runtime == "claude-code" and target.name in manifest["explicit_only_skills"]:
                skill = target / "SKILL.md"
                text = skill.read_text()
                match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
                if not match:
                    raise ValueError("Cannot adapt missing skill frontmatter")
                skill.write_text(text[:match.end(1)] + "\ndisable-model-invocation: true" + text[match.end(1):])
    except (OSError, ValueError):
        for target in reversed(reserved):
            shutil.rmtree(target)
        if not destination_existed:
            try:
                destination.rmdir()
            except OSError:
                pass
        raise
    print(json.dumps({"action": "installed", "runtime": runtime, "destination": str(destination), "skills": names}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", required=True, choices=["codex", "claude-code"])
    parser.add_argument("--destination", required=True, help="Explicit skill-directory path")
    parser.add_argument("--apply", action="store_true", help="Copy after all collision checks pass")
    args = parser.parse_args()
    try:
        install(args.destination, args.apply, args.runtime)
    except (OSError, ValueError, KeyError) as error:
        print("Installation refused: " + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
