# Command Reference (`docs/reference/commands.md`)

**Type:** reference, listed as **Command Reference** at the end of the
site's navigation.

**Reader's goal:** look up a command's arguments and options without
installing sfmtool or opening a terminal.

**Afterwards the reader** has found the command and option they need, and
knows which sfmtool release the help comes from.

**Before / after:** none; a reader arrives from the navigation or from
search.

## Content

`scripts/generate_cli_reference.py` writes the page before every build and
serve, so nobody edits it and Git ignores it. It runs the `sfm` from the
sfmtool release that `pixi.toml` pins, so the page matches what
`pip install sfmtool` gives at that release. The page holds:

- A sentence naming the sfmtool version, read from the installed package.
- A sentence linking sfmtool's
  [`specs/cli/`](https://github.com/sfmtool/sfmtool/tree/main/specs/cli) for
  what a command does in full.
- `sfm --help`, then one section per category heading that `sfm --help`
  prints, in its order (**Workspace Commands** first).
- Under each category, one heading per command in the order `sfm --help`
  lists them, such as **sfm solve**, with that command's `--help` in a
  `text` block. A command group, such as `sfm ws`, has its own `--help`,
  followed by one heading per command in the group (**sfm ws init**).

The help is copied verbatim, as Click wraps it for an 80-column terminal.
The site spec's rule on trimming output blocks does not apply: this page is
the full listing. The script finds the categories, commands and groups in
the help output itself, so a new command or category in sfmtool appears when
the pin moves, without a change here.

## Leaves out

- Per-command links to sfmtool's specs: the spec files are not named in a way
  the script can derive from the command name.
- Explanation, examples beyond those in the help, and how a command works:
  sfmtool's [`specs/cli/`](https://github.com/sfmtool/sfmtool/tree/main/specs/cli).
