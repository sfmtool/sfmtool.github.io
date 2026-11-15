# Inspecting a Reconstruction (`docs/tutorials/inspecting.md`)

**Type:** how-to guide, listed in the site's **How-to guides** navigation section.

**Reader's goal:** find out from the command line whether a reconstruction is
sound, and which images or parts of the camera path to look at.

**Afterwards the reader** knows which command answers which question:

| Question | Command |
|---|---|
| How big is it, how accurate, is the file intact? | `sfm inspect` (`-v` for detail) |
| Which images fit worst? | `sfm analyze --metrics` |
| How far away is the scene from each camera? | `sfm analyze --z-range` |
| Is the camera path broken anywhere? | `sfm motion` |

and can read the few lines of each output that answer it.

**Prerequisites:** a `.sfmr` file; the examples use the shared run's.
**Before / after:** [Getting Started](getting-started.md) (or Viewing 3D Point
Tracks) / none yet.

## Output

One block per command, from the shared run, each trimmed with `...` to the
lines the text explains:

- `sfm inspect -v`: the summary counts, the reprojection error and track
  length lines, and `Integrity: OK`.
- `sfm analyze --metrics`: the header, the worst images and the flag legend,
  so the reader sees how a flagged image would show.
- `sfm analyze --z-range`: the summary and one or two images.
- `sfm motion`: the discontinuity table and the `Verdict:` line, with a short
  note that a break is the result that matters and that a photo set taken
  around an object has expected discontinuities and no breaks.

The run-to-run caveat is linked to Getting Started, not repeated.

## Leaves out

- What every section and column of each output means: sfmtool's
  [`inspect-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/inspect-command.md),
  [`analyze-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/analyze-command.md)
  and
  [`motion-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/motion-command.md).
- The break rule's thresholds and the signal legend: `motion-command.md`.
- Fixing a flagged image or a break: no page yet.
