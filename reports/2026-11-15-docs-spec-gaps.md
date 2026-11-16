# Docs spec gaps, 2026-11-15

This report records where each page does not yet meet the spec written for it
in `specs/` (branch `docs-specs`). It is the first snapshot in the format the
`audit-docs` skill writes, and the next content PR works from it. Mark a
finding off in place with a dated status line, as `AGENTS.md` describes.

**Sample:** 5 of 5 pages read in full against their specs. No seed (every
page). sfmtool audited at `origin/main` `f65e5e22` by reading its code, specs
and PRs; no shared run was made for this snapshot, so output blocks were
checked for content against the specs, not re-captured. The mechanical
numbers below cover all 5 pages.

## Mechanical findings

| Page | Words | Output lines | Longest block | Images | Spec | Nav section |
|---|---|---|---|---|---|---|
| `docs/index.md` | 741 | 35 | 27 | 1 | yes | Home |
| `docs/tutorials/getting-started.md` | 565 | 24 | 10 | 1 | yes | Tutorials |
| `docs/tutorials/point-tracks.md` | 1,304 | 0 | 0 | 13 | yes | Tutorials |
| `docs/tutorials/inspecting.md` | 1,895 | 250 | 112 | 0 | yes | Tutorials (spec: How-to guides) |
| `docs/tutorials/video-to-images.md` | 89 | 10 | 10 | 0 | yes | Tutorials (spec: How-to guides) |

- `pixi run docs-build`: no issues; `site/` holds nothing from `specs/` or
  `skills/`.
- Images: 15 files, all referenced, all with alt text.
- The run-to-run caveat ("your counts … will differ") appears on Getting
  Started (its home) and on Inspecting.
- `GLOMAP` appears in captured output or prose on three pages: `index.md`
  line 61, `getting-started.md` lines 48–53, `point-tracks.md` line 90.

### docs/index.md

**Spec:** specs/pages/index.md (landing page). **Recommendation:** change the
page; the spec's order and three-command sketch are settled.

1. **The CLI section is a second walkthrough** (check 1). § "The `sfm` CLI
   command" runs `mkdir`, `cp`, `sfm ws init .` and `sfm solve -g images/`
   with captured output from a `seoul_bull_sculpture` run (file
   `20260404-00-solve-…`, `max_num_features: 8192`) that is not the shared
   run. The spec asks for a three-command sketch (`sfm ws init`, `sfm solve`,
   `sfm explorer`) with no output, linking Getting Started. Proposed: replace
   the section and its two code blocks with that sketch.

   > _Status (2026-11-15): **Done** — the CLI walkthrough and its seoul_bull output are replaced by a three-command sketch with no output that links Getting Started, branch docs-content-refresh._

2. **The GLOMAP progress line** (check 5). Line 61 quotes `Running global SfM
   with GLOMAP...`. sfmtool PR #1288 (open) changes it to `Running global SfM
   with COLMAP's global mapper...`. Finding 1's fix removes the line; if it
   lands first, this finding closes with it.

   > _Status (2026-11-15): **Done** — the line went with finding 1's walkthrough; sfmtool PR #1288 has since merged, and Getting Started shows the new line, branch docs-content-refresh._

3. **An output block with no output** (check 4). The `sfm inspect` and
   `sfm analyze --metrics` block shows only `...` for each command. The spec
   sends both commands to Inspecting a Reconstruction. Proposed: drop the
   block and link that page.

   > _Status (2026-11-15): **Done** — the empty `sfm inspect` / `sfm analyze --metrics` block is gone; the sketch links Getting Started, which links Inspecting, branch docs-content-refresh._

4. **Order** (check 3). "The SfM Explorer GUI" refers to "the below `sfm solve`
   command", and "What is Structure from Motion?" and "Installation" come
   after the commands. The spec's order is: what SfM Tool is, why, what SfM
   is, installation, the sketch and the link to Getting Started.

   > _Status (2026-11-15): **Done** — the page now runs what SfM Tool is, why the project exists, what SfM is, installation, the sketch with its link, and About Me, with the author-owned passages unchanged, branch docs-content-refresh._

5. **The screenshot is not from the shared run** (check 3). It shows the
   Seoul Bull; the spec asks for the shared run's reconstruction with a
   selected track.

   > _Status (2026-11-15): **Done** — the screenshot is now `images/sfm-explorer-dino-selected-track.jpg`, the shared run with the longest track in `dino_dog_toy_03.jpg` selected, branch docs-content-refresh._

### docs/tutorials/getting-started.md

**Spec:** specs/pages/getting-started.md (tutorial). **Recommendation:**
change the page.

1. **No command to get the images** (check 3). Step 1 runs `cp
   path/to/dino_dog_toy/*.jpg` after linking the GitHub tree. The spec asks
   for a command the reader can copy. Also open as bug bash finding 13 in
   `reports/2026-10-05-gui-bugbash-docs-findings.md`.

   > _Status (2026-11-15): **Done** — step 1 gives a blob-filtered sparse `git clone` of `test-data/images/dino_dog_toy` (about 40 MB, tested) and copies the 85 images into `dino/images/`, branch docs-content-refresh._

2. **The GLOMAP lines** (check 5). The solve output's first line is `Running
   global SfM with GLOMAP...`, and the paragraph before it explains that the
   line "still names it GLOMAP" and tells the solver's history. sfmtool PR
   #1288 (open) changes the line to `Running global SfM with COLMAP's global
   mapper...`. The spec leaves the solver's history to `solve-command.md`.
   Proposed: once #1288 merges, re-capture the line and cut the paragraph to
   one sentence on what the solve does.

   > _Status (2026-11-15): **Done** — the output shows the new first line, `Running global SfM with COLMAP's global mapper...`, from the shared run on sfmtool `main` e2f8e9a1c, and the history paragraph is gone, branch docs-content-refresh._

3. **The `Dropped` line is explained** (check 2). The paragraph after the
   solve output spends three sentences on `Dropped 926 repeat observation(s)
   from 586 point(s)`. The spec leaves it out: the reader does not act on it.
   Proposed: trim it from the block, or keep it unexplained.

   > _Status (2026-11-15): **Done** — the `Dropped` line is cut from the block and not explained, branch docs-content-refresh._

4. **`sfm ws init` output in full** (check 4). All eight lines are shown; the
   text refers to `feature_prefix_dir` only. The spec asks for the workspace
   line and `feature_prefix_dir`, with `...` between.

   > _Status (2026-11-15): **Done** — the block shows the workspace line, `...` and `feature_prefix_dir`, branch docs-content-refresh._

5. **The viewer note** (check 4). The note under step 4 describes where the
   viewer's window tests run and where it has been used most. The reader needs
   only "On Linux it needs a Vulkan driver."

   > _Status (2026-11-15): **Done** — the note is one sentence: on Linux, SfM Explorer needs a Vulkan driver, branch docs-content-refresh._

### docs/tutorials/point-tracks.md

**Spec:** specs/pages/point-tracks.md (tutorial). **Recommendation:** change
the page, from a re-capture on the shared run.

1. **Step 1 describes the old Patches row** (check 5). The page says a
   **Patches** row appears under the reconstruction and the 3D view draws the
   patches, with two screenshots of that. Since sfmtool PR #1285 the Scene
   panel shows a **Style** line with **Dots** and **Patches** under the
   Points row, and after a conversion the node stays in Dots
   (`specs/gui/scene-graph.md` § "Point style" and line 505 on `f65e5e22`).
   Proposed: add the step "set **Style** to **Patches**", and re-take
   `point-tracks-scene-patches-row.jpg` and
   `point-tracks-patches-in-3d-view.jpg`.

   > _Status (2026-11-15): **Done** — step 1 ends with clicking **Patches** on the **Style** line; `point-tracks-scene-style-line.jpg` replaces the Patches row picture and the 3D view picture is re-taken, branch docs-content-refresh._

2. **Repeat observations** (check 5). § 4's last paragraph says one photo can
   hold several observations of a point, "which a GLOMAP solve can produce",
   and describes the **Repeat obs.** column. A solve now drops repeat
   observations (the `Dropped …` line in Getting Started), so the shared run
   has none and the column does not appear. Proposed: delete the paragraph;
   the screenshot `point-tracks-track-view.jpg` (alt text: "with Img 5 on two
   rows") needs re-taking.

   > _Status (2026-11-15): **Done** — the repeat-observation paragraph is gone, and Track View is described as one row per photograph that sees the point; its screenshot is re-taken, branch docs-content-refresh._

3. **Not from the shared run** (check 3). The file name
   `20260413-00-solve-dino_dog_toy_1-85` and the screenshots come from an
   older run than the `20261114` run Getting Started quotes. The site spec
   asks every page to use the shared run.

   > _Status (2026-11-15): **Done** — every screenshot and the file name come from the shared run, `20261115-00-solve-dino_dog_toy_1-85`; the steps were followed over MCP to take them, branch docs-content-refresh._

4. **Every Track View column described** (check 2). § 4 lists all twelve
   columns with a description of each. The spec asks for the columns the
   lesson uses, with a link to sfmtool's `specs/gui/track-view.md`.

   > _Status (2026-11-15): **Done** — the column list is cut to **Img**, **Crop** and **Patch**, with a link to `track-view.md` for the rest, branch docs-content-refresh._

### docs/tutorials/inspecting.md

**Spec:** specs/pages/inspecting.md (how-to guide). **Recommendation:** change
the page.

1. **Listed under Tutorials** (check 7). `zensical.toml` lists the page under
   **Tutorials**; the site spec puts it under a **How-to guides** section. The
   nav change goes in the next content PR. If the page's URL moves (out of
   `tutorials/`), check that `scripts/add_legacy_redirects.py` still covers
   the old URLs, or keep the file where it is and change only the nav.

   > _Status (2026-11-15): **Done** — the page is listed under **How-to guides**; its file stays in `docs/tutorials/`, so its URL and the legacy redirects are unchanged, branch docs-content-refresh._

2. **Output blocks nearly complete** (check 4). `sfm inspect -v` is shown in
   112 lines and `sfm motion` in about 60; the spec asks for each block
   trimmed to the lines the text explains (for `inspect -v`: the summary
   counts, the reprojection error and track length lines, `Integrity: OK`;
   for `motion`: the discontinuity table and `Verdict:`).

   > _Status (2026-11-15): **Done** — each block is cut to the lines that answer its question: 250 output lines down to 68, branch docs-content-refresh._

3. **Explains most sections of the output** (check 2). The prose covers
   depth reliability, point-or-bearing, sharpness, the signal thresholds and
   the full break rule. The spec leaves these to sfmtool's
   `inspect-command.md` and `motion-command.md`.

   > _Status (2026-11-15): **Done** — the explanations of depth reliability, point-or-bearing, sharpness, the signal thresholds and the break rule are gone, with links to `inspect-command.md` and `motion-command.md`, branch docs-content-refresh._

4. **Repeated caveat** (check 4). The opening paragraph repeats that "your
   counts and numbers will differ"; the site spec states that caveat once, on
   Getting Started. Proposed: a link to it.

   > _Status (2026-11-15): **Done** — the caveat is replaced by a link to Getting Started's solve step, branch docs-content-refresh._

5. **File name disagrees with the run** (check 5). Every command uses
   `20260413-00-solve-dino_dog_toy_1-85.sfmr`, while the `inspect -v` output
   shows `Timestamp: 2026-11-14…` and Getting Started's run is
   `20261114-00-solve-…`.

   > _Status (2026-11-15): **Done** — every command and output block uses the shared run's `20261115-00-solve-dino_dog_toy_1-85.sfmr`, branch docs-content-refresh._

6. **No map from questions to commands** (check 3). The spec's "Afterwards"
   is a reader who knows which command answers which question; the page has
   no table or sentence that says so.

   > _Status (2026-11-15): **Done** — the page opens with the spec's question-to-command table, and each section is headed by its question, branch docs-content-refresh._

### docs/tutorials/video-to-images.md

**Spec:** specs/pages/video-to-images.md (how-to guide). **Recommendation:**
change the page.

1. **Uses a hand-written ffmpeg script** (check 5). The page runs `ffmpeg -i
   … -qscale:v 2`. sfmtool has `sfm extract-frames`
   (`specs/cli/workspace/extract-frames-command.md`), which handles rotation,
   variable frame rate and file naming. The spec asks for `sfm extract-frames
   VIDEO -o DIR`, its two main defaults, and ffmpeg 5.1 with ffprobe as a
   prerequisite.

   > _Status (2026-11-15): **Done** — the page uses `sfm extract-frames VIDEO -o DIR`, names `--fps` and `--max-frame-size` with their defaults, and states the ffmpeg 5.1 and ffprobe prerequisite; its output is from a real run, branch docs-content-refresh._

2. **Listed under Tutorials** (check 7). As for Inspecting: the site spec puts
   it under **How-to guides**; same redirect check if the URL moves.

   > _Status (2026-11-15): **Done** — listed under **How-to guides**, URL unchanged, as for Inspecting finding 1, branch docs-content-refresh._

3. **No next step** (check 3). The page does not say where the frames go or
   link Getting Started.

   > _Status (2026-11-15): **Done** — the page ends with Getting Started step 2 as the next step, branch docs-content-refresh._

## Specs and pages

| Page | Spec | Site spec table | Nav |
|---|---|---|---|
| `docs/index.md` | `specs/pages/index.md` | yes | yes |
| `docs/tutorials/getting-started.md` | `specs/pages/getting-started.md` | yes | yes |
| `docs/tutorials/point-tracks.md` | `specs/pages/point-tracks.md` | yes | yes |
| `docs/tutorials/inspecting.md` | `specs/pages/inspecting.md` | yes | under Tutorials, spec says How-to guides |
| `docs/tutorials/video-to-images.md` | `specs/pages/video-to-images.md` | yes | under Tutorials, spec says How-to guides |

No spec without a page, and no page without a spec.

## Top priorities

1. Point Tracks findings 1 and 2: step 1 and § 4 describe viewer behaviour
   that changed (the **Style** line, no repeat observations), so a reader
   following the page does not see what it says.
2. Re-capture every page from one shared run, after sfmtool PR #1288 merges,
   so the GLOMAP lines go (index finding 2, Getting Started finding 2) and
   the file names agree (Point Tracks finding 3, Inspecting finding 5).
3. Video to Images finding 1: use `sfm extract-frames`.
4. Inspecting findings 2 and 3: cut the page to the lines that answer the
   reader's questions.
5. The navigation: a **How-to guides** section (Inspecting finding 1, Video
   to Images finding 2).
