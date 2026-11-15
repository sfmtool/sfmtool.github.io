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

**Screenshot:** SfM Explorer with the shared run's reconstruction and a
selected track, to show the reader what they will get.

**Commands:** a three-command sketch of the workflow (`sfm ws init`,
`sfm solve`, `sfm explorer`) with no output, linking Getting Started for the
real run.

## Leaves out

- Captured output and step-by-step commands: Getting Started.
- `sfm inspect` and `sfm analyze`: [Inspecting a Reconstruction](inspecting.md).
- How the solver works: sfmtool's
  [`solve-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/solve-command.md).
