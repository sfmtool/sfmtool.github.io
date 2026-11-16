# Inspecting a Reconstruction (`docs/tutorials/inspecting.md`)

**Type:** how-to guide, listed in the site's **How-to guides** navigation section.

**Reader's goal:** understand a reconstruction's properties from the command
line: what it holds, how its points and errors are distributed, how its images
compare, how far the scene is from each camera, and how the camera moves
between photographs.

**Afterwards the reader** knows which command answers which question:

| Question | Command |
|---|---|
| What does it hold, and how are its points distributed? | `sfm inspect` (`-v` for the distributions) |
| How do the images compare? | `sfm analyze --metrics` |
| How far away is the scene from each camera? | `sfm analyze --z-range` |
| How does the camera move between photographs? | `sfm motion` |

and can read the few lines of each output that answer it.

**Prerequisites:** a `.sfmr` file; the examples use the shared run's.
**Before / after:** [Getting Started](getting-started.md) (or Viewing 3D Point
Tracks) / none yet.

## Output

One block per command, from the shared run, each trimmed with `...` to the
lines the text explains:

- `sfm inspect -v`: the summary counts, one position distribution, the
  reprojection error with its distribution, the track length lines with their
  distribution, and `Integrity: OK`.
- `sfm analyze --metrics`: the header, the first rows and the flag legend,
  so the reader sees how a flagged image would show.
- `sfm analyze --z-range`: the summary and one or two images.
- `sfm motion`: the discontinuity table and the `Verdict:` line, with a short
  note on what a discontinuity and a break are, and that a photo set taken
  around an object has expected discontinuities and no breaks.

The run-to-run caveat is linked to Getting Started, not repeated.

## Leaves out

- What every section and column of each output means: sfmtool's
  [`inspect-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/inspect-command.md),
  [`analyze-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/analyze-command.md)
  and
  [`motion-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/motion-command.md).
- The break rule's thresholds and the signal legend: `motion-command.md`.
- What to do about a flagged image or a break: no page yet.
