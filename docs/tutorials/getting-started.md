# Getting Started

With a good set of photographs, use SfM Tool to create and view a sparse
reconstruction in a few steps. This uses COLMAP and GLOMAP under the hood.

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
```

## 3. Solve

Run the global SfM solver (GLOMAP). This automatically extracts SIFT features,
matches them across images, and solves for camera poses and 3D structure.

```
$ sfm solve -g images/ --max-features 2000
Running global SfM with GLOMAP...
Image files:
  .../dino/images/dino_dog_toy_%02d.jpg (85 files, sequence 1-85)
...
Found reconstruction 0:
  Cameras: 1, Images: 85, Points: 10580
Saved reconstruction to: .../dino/sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr
Completed in 1m 4.75s
```

## 4. Explore in 3D

Open the reconstruction in the SfM Explorer GUI by giving it the `.sfmr` file
the solve wrote to the `sfmr/` directory. Its name starts with the date of the
solve, so yours differs from the one below.

```
$ sfm explorer sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr
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
