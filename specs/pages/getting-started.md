# Getting Started (`docs/tutorials/getting-started.md`)

**Type:** tutorial.

**Reader's goal:** make a first reconstruction from a set of photos and see it
in 3D.

**Afterwards the reader** has made a workspace, solved 85 photos into a
`.sfmr` file and opened it in SfM Explorer, and knows that the solve's counts
vary from run to run and that its log warnings do not mean it failed.

**Prerequisites:** Python 3.14 and a terminal. **Before / after:**
[Home](index.md) / [Viewing 3D Point Tracks](point-tracks.md), with
[Inspecting a Reconstruction](inspecting.md) and
[Converting Video to Image Sequences](video-to-images.md) as further next
steps.

## Steps

The dataset is `test-data/images/dino_dog_toy` (85 photos, about a minute to
solve). This page's run is the shared run (see the [site spec](../README.md)).

1. Install: `pip install sfmtool`; get the images into `dino/images/` with a
   command the reader can copy.
2. `sfm ws init --max-features 4000`, with one sentence on what a workspace is
   for.
3. `sfm solve -g images/ --max-features 2000`, with one sentence each on what
   the solve does and why the two feature limits differ.
4. `sfm explorer sfmr/<file>.sfmr`.

## Output and screenshots

- `sfm ws init`: trimmed to the lines the text names (the workspace and
  `feature_prefix_dir`), so the reader can confirm it worked.
- `sfm solve`: the first line, `...`, then the image and point counts and
  the saved path. The text names the path, which step 4 opens. This page is
  the site's one place for two caveats: the counts and time vary from run to
  run, and the warnings in the log do not mean failure.
- One screenshot of SfM Explorer with the dino, the result of the lesson.

## Leaves out

- Each workspace setting:
  [`ws-init-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/workspace/ws-init-command.md)
  and `sfm ws init --help`.
- Incremental solving (`-i`), solver options and the solver's history:
  [`solve-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/solve-command.md).
- The `Dropped … repeat observation(s)` line: the reader does not act on it
  ([`drop-repeat-observations.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/core/reconstruction/drop-repeat-observations.md)).
- How to use the viewer: Viewing 3D Point Tracks.
