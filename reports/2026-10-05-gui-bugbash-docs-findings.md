# Docs findings from the 2026-10-05 SfM Explorer bug bash

These findings come from `reports/2026-10-05-gui-bugbash.md` in the
[sfmtool](https://github.com/sfmtool/sfmtool) repository, a bug bash that
followed the user docs step by step on a release build of the viewer and
rebuilt each of their screenshots over the viewer's MCP endpoint. Every
viewer finding in that report is now resolved or declined, so it was retired
there, and the documentation findings that were still open moved here, where
the pages now live. Finding 15 ("Write each GUI step as a card") is not carried
over: this repository's `AGENTS.md` superseded it.

Each finding keeps its original number, body and status lines. Other numbers
in the text ("finding 7", "finding 3", "the step cards" of finding 15) refer to
that report, and a PR number without a repository name, such as PR #1058, is a
pull request in `sfmtool/sfmtool`. The `dino` reconstruction the findings
mention is a fresh `sfm solve -g images/ --max-features 2000` of the 85
`test-data/images/dino_dog_toy` images, run as the Getting Started tutorial
says.

Mark a finding off in place when a change addresses it, with a dated status
line in the same style, for example
`> _Status (YYYY-MM-DD): **Done** — <what changed>, PR #<n>._`, and delete
this file once nothing in it is still worth tracking.

## 13. CLI quickstart gaps (docs)

> _Status (2026-10-28): **Not done** — the docs moved to the
> sfmtool/sfmtool.github.io repository (PR #1058);
> the fix goes in a PR there._
>
> _Status (2026-10-29): **Partially done** — Getting Started's step 4 now
> opens the file with `sfm explorer sfmr/<file>.sfmr`, PR
> sfmtool/sfmtool.github.io#3. The other three remain: step 1 still gives no
> command to download the 85 images, steps 2 and 3 still use
> `--max-features 4000` and `2000` without saying why, and the solver's log
> lines and warnings are still not mentioned._

The CLI steps run word for word: 85 of 85 images registered in 51 s. Four
things would help a new reader:

- Step 1 says `cp path/to/dino_dog_toy/*.jpg` and links the GitHub tree, but
  gives no command to download or clone the 85 images.
- Step 2 runs `sfm ws init --max-features 4000` and step 3
  `sfm solve -g images/ --max-features 2000`, without saying why the values
  differ or which applies (the solve records `max_features: 2000`).
- The solve prints several hundred COLMAP and GLOMAP log lines, including
  *"Requested to use GPU for bundle adjustment, but COLMAP was compiled without
  CUDA support"* and *"Less than 50% of cameras have prior focal lengths"*. The
  docs show a clean summary, so a beginner may take the warnings for a
  failure.
- Step 4 runs `sfm explorer` and then opens the file through the menu;
  `sfm explorer sfmr/<file>.sfmr` does it in one step and is what
  `docs/index.md` shows.

## 14. CLI output in the docs is out of date (docs)

> _Status (2026-10-28): **Not done** — the docs moved to the
> sfmtool/sfmtool.github.io repository (PR #1058);
> the fix goes in a PR there._

- `sfm inspect -v` now also prints *Tool options*, *Depth reliability*,
  *Point or bearing* and *Integrity: OK*.
- `sfm motion`'s summary table now has the columns Dist, Rot, StepR, CovR,
  ObsZ(A/B), SharedPts, Err(A), Err(B) and Signals, with a P/S/C/O legend and a
  single-signal / multi-signal confidence split. The docs show the older
  Dist(prev) / Dist / Dist(next) layout.
- The numbers differ from run to run (9,941 points and 2 flagged images here,
  10,580 and 1 in the docs), and the docs do not say to expect that.

Recommendation: cut each output block to the lines the text discusses, say
that counts vary, and add a docs test that runs the quickstart on
`seoul_bull_sculpture` and checks the section headings of `inspect -v`,
`analyze --metrics`, `analyze --z-range` and `motion`. A new section then fails
a test instead of leaving the docs stale.

## 16. Use a ground-truth reconstruction for the GUI tutorial (docs)

> _Status (2026-10-28): **Not done** — the docs moved to the
> sfmtool/sfmtool.github.io repository (PR #1058);
> the fix goes in a PR there._

Distances and angles in a step card only mean something in a reconstruction
with a known scale and up direction. `seoul_bull_sculpture_ground_truth_v01.sfmr`
and `kerry_park_ground_truth_v01.sfmr` are in metres with Z up. The dino has no
ground truth, and its solves come out tilted and at an arbitrary scale
(finding 7). Make one: level it with the mean camera up vector (about 20 lines
during this bash) and scale it from one measured length, such as the table
width or the toy's height. Alternatively, move the GUI tutorial to the Seoul
Bull.

## 17. Generate the docs screenshots from stored scene recipes (docs)

> _Status (2026-10-28): **Not done** — the docs moved to the
> sfmtool/sfmtool.github.io repository (PR #1058);
> the fix goes in a PR there._

All six GUI screenshots drifted and nothing noticed. Store each one's state
(window size, layout, selection, view, Image Detail overlay and view, display
settings) as a JSON recipe beside the image, for example
`docs/recipes/<shot>.json`, and add a task that launches a viewer on a random
port, applies each recipe over MCP and writes the PNGs. Run it before a
release, or in the `ui-test-windows` job with an image-difference threshold,
so a UI change that invalidates a screenshot is reported.

An `apply_recipe` / `capture_recipe` pair of MCP tools would make the recipe
one call; until then the recipe is a list of existing calls
(`set_window_layout`, `select_*`, `set_image_detail_display`,
`set_image_detail_view`, `set_view`).

## 18. Add a page on exploring a reconstruction with an agent (docs)

> _Status (2026-10-28): **Not done** — the docs moved to the
> sfmtool/sfmtool.github.io repository (PR #1058);
> the fix goes in a PR there._

The user docs never mention the MCP endpoint. A short page should cover
`pixi run gui-mcp <file>.sfmr` (or `sfm explorer --mcp`), registering it with
`claude mcp add --transport http sfm-explorer http://127.0.0.1:8787/mcp`, and a
few example requests built on the step cards ("open the bull, look through
image 5, show me the longest track"). The material is in AGENTS.md and
`specs/gui/mcp-server.md` but not on the docs site.
