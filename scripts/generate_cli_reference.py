# Copyright The SfM Tool Authors
# SPDX-License-Identifier: Apache-2.0
"""Write the Command Reference page from the installed ``sfm``'s help.

It runs ``sfm --help``, then ``--help`` for every command and command group
that help lists, and for every command in each group, and writes the help
verbatim to ``docs/reference/commands.md``, grouped under the headings that
``sfm --help`` prints. The page is not committed: the docs tasks in
``pixi.toml`` run this script before Zensical, so the page always matches the
sfmtool that ``pixi.toml`` pins.

Usage: ``python scripts/generate_cli_reference.py``
"""

import os
import re
import subprocess
from importlib.metadata import version
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs" / "reference" / "commands.md"
SPECS_URL = "https://github.com/sfmtool/sfmtool/tree/main/specs/cli"

# Click wraps help to the terminal width, up to 80 columns. A fixed width
# keeps the page the same on every machine.
ENV = {**os.environ, "COLUMNS": "80", "PYTHONUTF8": "1"}

HEADING = re.compile(r"^(\S.*):$")
ROW = re.compile(r"^  (\S+)")


def help_text(words: list[str]) -> str:
    result = subprocess.run(
        ["sfm", *words, "--help"],
        env=ENV,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout.rstrip() + "\n"


def sections(text: str) -> dict[str, list[str]]:
    """Map each heading in a help text, such as ``Commands``, to the names
    listed under it."""
    found: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        if heading := HEADING.match(line):
            current = heading[1]
            found[current] = []
        elif current is not None and (row := ROW.match(line)):
            found[current].append(row[1])
    return found


def code_block(text: str) -> str:
    fence = "`" * max([3] + [len(run) + 1 for run in re.findall(r"`+", text)])
    return f"{fence}text\n{text}{fence}\n"


def command(words: list[str], level: int) -> str:
    text = help_text(words)
    out = f"{'#' * level} sfm {' '.join(words)}\n\n{code_block(text)}\n"
    if text.startswith(f"Usage: sfm {' '.join(words)} [OPTIONS] COMMAND"):
        for name in sections(text).get("Commands", []):
            out += command([*words, name], level + 1)
    return out


def main() -> None:
    text = help_text([])
    page = (
        "# Command Reference\n\n"
        "This page shows what `sfm --help` and each command's `--help` print"
        f" in sfmtool {version('sfmtool')}. For what a command does in full,"
        f" see its spec in sfmtool's [`specs/cli/`]({SPECS_URL}).\n\n"
        f"## sfm\n\n{code_block(text)}\n"
    )
    for heading, names in sections(text).items():
        if heading == "Options":
            continue
        page += f"## {heading}\n\n"
        for name in names:
            page += command([name], 3)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
