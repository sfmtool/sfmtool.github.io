# Getting Started

Make your first 3D reconstruction from a set of photographs and look at it in
SfM Explorer. SfM Tool extracts the SIFT features itself. It uses
[COLMAP](https://colmap.github.io/) to match them and to solve, through
COLMAP's Python bindings, pycolmap.

The photographs are the
[dino dog toy dataset](https://github.com/sfmtool/sfmtool/tree/main/test-data/images/dino_dog_toy):
85 photographs of a dog toy on a table, taken from different angles. The toy
and the table have enough texture to give many SIFT features.

## 1. Install and get the photographs

```
$ pip install sfmtool
```

SfM Tool needs Python 3.14.
[Installation](../index.md#installation) on the home page lists the platforms
it has wheels for.

Download the photographs,
[`dino_dog_toy.zip`](https://github.com/sfmtool/sfmtool/releases/download/v0.3/dino_dog_toy.zip)
(42 MB), and unzip it. It holds the 85 photographs in `dino/images/`.

```
$ curl -LO https://github.com/sfmtool/sfmtool/releases/download/v0.3/dino_dog_toy.zip
$ unzip dino_dog_toy.zip
$ cd dino
```

In Windows PowerShell, use
`Invoke-WebRequest <link> -OutFile dino_dog_toy.zip` and
`Expand-Archive dino_dog_toy.zip .` for the first two commands.

## 2. Initialize the workspace

A workspace is a directory with its own settings, such as how features are
extracted. Every `sfm` command you run inside it uses those settings.

```
$ sfm ws init --max-features 4000
Initialized workspace: .../dino
...
  feature_prefix_dir: features/sift-sfmtool-321fc2aaf62cc4697adafe94c11e4642
```

The workspace extracts at most 4000 SIFT features from each image. It stores
them inside the images directory, under the `feature_prefix_dir` that
`sfm ws init` printed.

## 3. Solve

The solve extracts the features, matches them across the photographs, and
works out where each camera stood and where the 3D points are.
`--max-features 2000` makes the solve use the 2000 largest of each image's
4000 features. Fewer features match faster. The workspace still stores all
4000, so a later solve can use more without extracting them again.

```
$ sfm solve -g images/ --max-features 2000
Running global SfM with COLMAP's global mapper...
...
Found reconstruction 0:
  Cameras: 1, Images: 85, Points: 10331
Saved reconstruction to: .../dino/sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
Completed in 54.25s
```

The `...` stands for about a hundred lines that feature extraction and COLMAP
print. Those lines include warnings, such as *"Less than 50% of cameras have
prior focal lengths"*. The warnings do not mean the solve failed: the last
lines say how many images and points the solve found and where it saved them.
The solve gives slightly different results each time it runs, so your counts
and time will differ. The date that starts the file name will differ too.

## 4. Explore in 3D

Open the saved reconstruction in SfM Explorer:

```
$ sfm explorer sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
```

On Linux, SfM Explorer needs a Vulkan driver.

![SfM Explorer with the dino dog toy reconstruction](images/dino-in-sfm-explorer.jpg)

## Next steps

- [Viewing 3D Point Tracks](point-tracks.md): follow one 3D point through the
  photographs that see it, and move around the scene in SfM Explorer.
- [Inspecting a Reconstruction](inspecting.md): check a reconstruction from
  the command line.
- [Converting Video to Image Sequences](video-to-images.md): turn a video into
  the images `sfm` works with.
