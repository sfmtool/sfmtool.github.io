# Converting Video to Image Sequences

Turn a video of a scene into a directory of numbered images that `sfm` can
solve. Every `sfm` command reads still images, not video, so `sfm extract-frames`
writes the frames out first.

`sfm extract-frames` runs [ffmpeg](https://ffmpeg.org/download.html) 5.1 or
newer and ffprobe. Both must be on your `PATH`. `pip install sfmtool` does not
install them.

## 1. Extract the frames

Write the frames into the `images/` directory of a new workspace directory.
Here the workspace is `dino_orbit/`, for a 6-second video, `dino_orbit.mp4`:

```
$ sfm extract-frames dino_orbit.mp4 -o dino_orbit/images
...
dino_orbit.mp4: h264 2040x1536, 30.00 fps, 6.0 s
  -> dino_orbit/images/dino_orbit/ at 10 fps
  60 frames written, 1920x1446, in 0.6s
...
```

By default it keeps 10 frames for each second of video (`--fps`). It scales
a frame down until its long side is at most 1920 pixels (`--max-frame-size`).
`sfm extract-frames --help` lists these and the other options.

The frames are in `dino_orbit/images/dino_orbit/`. They are named
`frame_000001.jpg`, `frame_000002.jpg` and so on, in the order they appear in
the video.

## 2. Solve the frames

`dino_orbit/` now holds its images the way the `dino/` workspace in Getting
Started does. Change into it and continue from
[Getting Started step 2](getting-started.md#2-initialize-the-workspace),
`sfm ws init`.
