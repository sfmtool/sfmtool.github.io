# Converting Video to Image Sequences

To try many different things with a particular 3D reconstruction, having the
data as a video complicates individual frame access. Therefore the `sfm` command expects you
to always convert to images first.

Here's an example of using [ffmpeg](https://www.ffmpeg.org/) to convert a
single video in the current directory into a sequence of images in a `frames`
subdirectory:

```bash
# Assumes there's one video in the current directory
VIDEO_FILE=$(echo *.mp4)

IMAGE_BASE=$(basename "$VIDEO_FILE")
IMAGE_BASE=${IMAGE_BASE%.*}

mkdir -p frames
ffmpeg -i "$VIDEO_FILE" \
    -qscale:v 2 \
    frames/"${IMAGE_BASE}_%04d.jpg"
```

