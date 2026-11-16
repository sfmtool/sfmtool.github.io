# Converting Video to Image Sequences (`docs/tutorials/video-to-images.md`)

**Type:** how-to guide, listed in the site's **How-to guides** navigation section.

**Reader's goal:** turn a video of a scene into numbered images that `sfm`
can solve.

**Afterwards the reader** has a directory of frames from their video, made
with `sfm extract-frames`, and knows to put it under the workspace's images
directory and continue as in Getting Started.

**Prerequisites:** a video file, and ffmpeg 5.1 or newer with ffprobe on the
`PATH` (`sfm extract-frames` runs them; a `pip` install does not bring them). **Before / after:** [Getting Started](getting-started.md) / Getting
Started step 2 with the frames as images.

## Content

- One sentence on why `sfm` works on images, not video.
- `sfm extract-frames VIDEO -o DIR`, with the two defaults a reader may want
  to change (frames per second, maximum frame size) named and linked to
  `--help`.
- What to expect in the output directory, enough to check it worked.

No captured output and no screenshot unless the reader needs one to check
the result.

## Leaves out

- Every option, HDR handling and the frame-time record: sfmtool's
  [`extract-frames-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/workspace/extract-frames-command.md)
  and `sfm extract-frames --help`.
- Choosing a subset of a long video's frames: `sfm pick-images`
  ([`pick-images-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/image-feature/pick-images-command.md)),
  linked when the site has a page for it.
- Filming advice beyond what the home page says about SfM.
