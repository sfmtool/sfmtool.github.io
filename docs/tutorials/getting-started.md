# Getting Started

With a good set of photographs, use SfM Tool to create and view a sparse
reconstruction in a few steps. SfM Tool extracts the SIFT features itself,
and uses [COLMAP](https://colmap.github.io/), run through its Python bindings
pycolmap, to match them and to solve.

We'll use the [dino dog toy dataset](https://github.com/sfmtool/sfmtool/tree/main/test-data/images/dino_dog_toy)
— 85 photographs of a dog toy taken from different angles. The table and the
toy have texture detail that gives a rich set of SIFT features for the solve.

## 1. Install and set up

```
$ pip install sfmtool
```

Create a workspace directory and copy your images into it.

```
$ mkdir -p dino/images
$ cp path/to/dino_dog_toy/*.jpg dino/images/
$ cd dino
```

## 2. Initialize the workspace

```
$ sfm ws init --max-features 4000
Initialized workspace: .../dino
Configuration file: .../dino/.sfm-workspace.json
  feature_tool: sfmtool
  contrast_threshold: 0.0067
  octave_layers: 3
  max_num_features: 4000
  image_to_gray: 0.2126*R + 0.7152*G + 0.0722*B
  feature_prefix_dir: features/sift-sfmtool-321fc2aaf62cc4697adafe94c11e4642
```

The workspace extracts at most 4000 SIFT features from each image, and stores
them under the `feature_prefix_dir` it prints, inside the images directory.

## 3. Solve

Run the global SfM solver. It extracts the SIFT features, matches them across
images, and solves for the camera poses and the 3D points. `--max-features 2000`
uses at most 2000 of each image's features in the solve. The solve is COLMAP's
global mapper, which was once the separate GLOMAP project and is now part of
COLMAP; the first line of the output still names it GLOMAP.

```
$ sfm solve -g images/ --max-features 2000
Running global SfM with GLOMAP...
Image files:
  .../dino/images/dino_dog_toy_%02d.jpg (85 files, sequence 1-85)
...
  Dropped 926 repeat observation(s) from 586 point(s)
Found reconstruction 0:
  Cameras: 1, Images: 85, Points: 10362
Saved reconstruction to: .../dino/sfmr/20261114-00-solve-dino_dog_toy_1-85.sfmr
Completed in 1m 17.81s
```

The `...` stands for the feature extraction messages and about a hundred lines
of COLMAP's own log, which include warnings such as *"Requested to use GPU for
bundle adjustment, but COLMAP was compiled without CUDA support"* and *"Less
than 50% of cameras have prior focal lengths"*. They do not mean the solve
failed: the last lines say how many images and points it found and where it
saved them. The `Dropped` line is about points that COLMAP observed more than
once in the same photograph: SfM Tool keeps the observation with the lowest
reprojection error in each such photograph, and the line counts the
observations it dropped and the points they belonged to. The solve gives
slightly different results each time it runs, so your counts and time will
differ.

## 4. Explore in 3D

Open the reconstruction in the SfM Explorer GUI by giving it the `.sfmr` file
the solve wrote to the `sfmr/` directory. Its name starts with the date of the
solve, so yours differs from the one below.

```
$ sfm explorer sfmr/20261114-00-solve-dino_dog_toy_1-85.sfmr
```

!!! note
    Use the latest version of sfmtool, which includes SfM Explorer. Its
    automated window tests run on Windows, macOS and
    Linux, but most hands-on use has been on Windows. On Linux it needs a
    Vulkan driver.

![SfM Explorer with dino dog toy reconstruction](images/dino-in-sfm-explorer.jpg)

## Next steps

- [Viewing 3D Point Tracks](point-tracks.md): follow one 3D point through the
  photographs that see it, and move around the scene in SfM Explorer.
- [Inspecting a Reconstruction](inspecting.md): summaries and per-image
  statistics from the command line.
- [Converting Video to Image Sequences](video-to-images.md): turn a video into
  the images `sfm` works with.
