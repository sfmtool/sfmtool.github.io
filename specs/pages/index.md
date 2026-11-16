# Home page (`docs/index.md`)

**Type:** landing page: a short explanation, then where to start.

**Reader's goal:** decide whether SfM Tool is for them, learn who made it and
why, install it, and find the first page to follow.

**Afterwards the reader** knows in a paragraph what SfM does and needs (a
static scene, photos from many positions), knows that `sfm` builds
reconstructions and SfM Explorer shows them, knows who made it and why, has
installed `sfmtool`, and goes to Getting Started.

**Before / after:** first page of the site / [Getting Started](getting-started.md).

## Content

- What SfM Tool is: the `sfm` command and the SfM Explorer viewer, and that
  it builds on COLMAP and OpenCV.
- Why the project exists, in the author's voice (author-owned, see below).
- What the project is not about (feedforward image-to-3D methods such as
  VGGT), in the author's voice (author-owned, see below).
- What SfM is: the paragraph a newcomer needs to take usable photos.
- Installation: `pip install sfmtool`, and which platforms have wheels.
- A link to Getting Started as the place to start.
- About the author, under the heading **About Mark Wiebe**: who made SfM
  Tool and their background (author-owned, see below).

**Screenshot:** SfM Explorer showing the newest ground-truth reconstruction
checked in to sfmtool's `test-data/images/seoul_bull_sculpture/` (today
`seoul_bull_sculpture_ground_truth_v02.sfmr`), drawn as patches with a
selected point and its track, to show the reader what they will get. The
maintainer chooses the view and the point. It is retaken when a newer
ground-truth version is checked in.

**Commands:** a three-command sketch of the workflow (`sfm ws init`,
`sfm solve`, `sfm explorer`) with no output, linking Getting Started for the
real run.

## Author-owned passages

The **why the project exists**, **what the project is not about** and
**About the author** passages are written
by the maintainer, in their own voice. A refresh or a fix leaves their wording
alone, and an audit does not rewrite them: where an improvement is apparent
(a stale fact, a broken link, a passage that no longer reads well beside the
rest of the page), it goes in the report as a suggestion for the maintainer,
with the proposed text, and the maintainer decides.

## Leaves out

- Captured output and step-by-step commands: Getting Started.
- `sfm inspect` and `sfm analyze`: [Inspecting a Reconstruction](inspecting.md).
- How the solver works: sfmtool's
  [`solve-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/solve-command.md).
