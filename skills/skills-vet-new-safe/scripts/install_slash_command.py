#!/usr/bin/env python3
"""
Install slash-command wrappers for the skills-vet-new-safe workflow.

By default installs `weekly-sync-skills.md` into:
- ~/.agent/commands
- ~/.claude/commands
- ~/.codex/commands

Use --target to install into one or more explicit command directories.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import List


def _expand(path: str) -> Path:
    return Path(os.path.expanduser(path)).resolve()


def _default_targets() -> List[Path]:
    return [
        _expand("~/.agent/commands"),
        _expand("~/.claude/commands"),
        _expand("~/.codex/commands"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Install weekly-sync-skills slash command wrapper.")
    parser.add_argument(
        "--template",
        default=None,
        help="Optional template path (default: ../assets/commands/weekly-sync-skills.md relative to this script).",
    )
    parser.add_argument(
        "--target",
        action="append",
        default=[],
        help="Command directory target (repeatable). If omitted, installs to ~/.agent/.claude/.codex command dirs.",
    )
    parser.add_argument(
        "--name",
        default="weekly-sync-skills.md",
        help="Filename for installed command (default: weekly-sync-skills.md).",
    )

    args = parser.parse_args()
    script_dir = Path(__file__).resolve().parent
    template_path = _expand(args.template) if args.template else (script_dir.parent / "assets" / "commands" / "weekly-sync-skills.md")
    if not template_path.exists():
        print(f"[!] Template not found: {template_path}")
        return 1

    template_text = template_path.read_text(encoding="utf-8")
    targets = [_expand(t) for t in args.target] if args.target else _default_targets()

    installed = 0
    for target in targets:
        target.mkdir(parents=True, exist_ok=True)
        destination = target / args.name
        destination.write_text(template_text, encoding="utf-8")
        print(f"[*] Installed: {destination}")
        installed += 1

    print(f"[*] Completed. Installed {installed} command file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

