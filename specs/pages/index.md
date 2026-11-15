# Home page (`docs/index.md`)

**Type:** landing page: a short explanation, then where to start.

**Reader's goal:** decide whether SfM Tool is for them, install it, and find
the first page to follow.

**Afterwards the reader** knows in a paragraph what SfM does and needs (a
static scene, photos from many positions), knows that `sfm` builds
reconstructions and SfM Explorer shows them, has installed `sfmtool`, and goes
to Getting Started.

**Before / after:** first page of the site / [Getting Started](getting-started.md).

## Content

- What SfM Tool is: the `sfm` command and the SfM Explorer viewer, and that
  it builds on COLMAP and OpenCV.
- Why the project exists, in the author's voice.
- What SfM is: the paragraph a newcomer needs to take usable photos.
- Installation: `pip install sfmtool`, and which platforms have wheels.
- A link to Getting Started as the place to start.
- About the author.

**Screenshot:** SfM Explorer with a reconstruction and a selected track, to
show the reader what they will get. Any shared-run reconstruction serves.

**Commands:** at most a short sketch of the workflow (`sfm ws init`,
`sfm solve`, `sfm explorer`) with no output, linking Getting Started for the
real run. Whether the page carries even that is a maintainer decision.

## Leaves out

- Captured output and step-by-step commands: Getting Started.
- `sfm inspect` and `sfm analyze`: [Inspecting a Reconstruction](inspecting.md).
- How the solver works: sfmtool's
  [`solve-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/solve-command.md).

## Current gaps

- The CLI section is a second walkthrough with captured output from an older
  run on `seoul_bull_sculpture` (file dated `20260404`, `max_num_features:
  8192`), not from the shared run, and it duplicates Getting Started.
- It quotes `Running global SfM with GLOMAP...`, which sfmtool PR #1288
  changes to `Running global SfM with COLMAP's global mapper...`.
- The `sfm inspect` / `sfm analyze` block shows only `...` as output.
- Order: the GUI section refers to "the below `sfm solve` command", and
  installation and "What is Structure from Motion?" come after the commands.
