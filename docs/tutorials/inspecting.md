# Inspecting a Reconstruction

These steps inspect the reconstruction from [Getting Started](getting-started.md).
All the output on this page comes from one run of those steps. The solve gives
slightly different results each time it runs, so your counts and numbers will
differ, and so will the date in your file name.

## 1. Reconstruction summary

Use `sfm inspect -v` to get a detailed summary of a reconstruction from the
command line. Even from the command line, you can get an idea about the 3D
points from this output. The bounding box extents are accompanied by histograms
that show the point density projected to each axis. Similarly, you can see a
histogram of the reprojection error, track lengths, and 3D distance to the
nearest other point. The observation statistics give the least, greatest, mean
and median number of images that see each point. The output also lists the
sharpness of the photos (**Image readings**), how well the depths of the points
are determined (**Depth reliability**), whether a statistical test agrees with
how each point is stored, as a point at a finite distance or as a direction
(**Point or bearing**), and the result of the file's integrity check. (Without
`-v`, `sfm inspect` prints a one-screen summary.)

```
$ sfm inspect -v sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr

Reconstruction file: 20260413-00-solve-dino_dog_toy_1-85.sfmr
======================================================================

Metadata:
  Operation: sfm_solve
  Tool: colmap
  Tool version: 4.2.1
  Timestamp: 2026-11-14T18:23:08.198815600-08:00
  Tool options:
    algorithm: global
    max_features: 2000

Workspace:
  Absolute path: .../dino
  Relative path: ..
  Resolved workspace: .../dino
  Feature tool: sfmtool

Reconstruction summary:
  Images: 85
  Thumbnails: yes
  Patch bitmaps: no
  Image paths:
    images\dino_dog_toy_%02d.jpg (85 files, sequence 1-85)
  Cameras: 1
  3D points: 10321
  Observations: 74840
  Mean observations per point: 7.25

Cameras:
  Camera 0: SIMPLE_RADIAL 2040x1536
    Parameter                      Value
    --------------------  --------------
    focal_length             1470.782761
    principal_point_x        1020.000000
    principal_point_y         768.000000
    radial_distortion_k1        0.020072

Rig configuration: none

Image readings:
  Conversion: 0.2126*R + 0.7152*G + 0.0722*B
  Sharpness: min 0.002941, median 0.01117, max 0.0257
    Sharpness distribution:
      ▁▂▁▁▁▃▄▅▂▂▄▇█▃▁▄▄▁▁▄ ▁▁  ▁     ▁
      0.002941                  0.0257
  Least sharp 5 images:
    0.002941  images/dino_dog_toy_53.jpg
    0.003769  images/dino_dog_toy_26.jpg
    0.003822  images/dino_dog_toy_27.jpg
    0.004192  images/dino_dog_toy_01.jpg
    0.004478  images/dino_dog_toy_25.jpg

3D Point statistics:
  Position range:
    X: [-14.808, 33.875]
    X distribution:
      ▁▁ ▁▁▁     ▁▁▁▁▁▁▁▄█▇▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁ ▁▁           ▁▁        ▁
      -14.808                                                   33.875
    Y: [-7.940, 14.073]
    Y distribution:
      ▁▁▁▁ ▁▁▁▁▁ ▁ ▁▁        ▁▁▁▁▁▃▇█▆▅▃▂▃▂▂▁▁▁▁▁▁▁▁▁  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
      -7.940                                                    14.073
    Z: [-17.154, 6.703]
    Z distribution:
      ▁   ▁▁▁▁▁▁▁   ▁  ▁   ▁▁        ▁▁▁▁▁▁▁▃█▇▆▄▇▇▅▃▂▁▁▁▁▁▁▁  ▁▁▁▁  ▁
      -17.154                                                    6.703
  Reprojection error:
    Mean: 1.587 pixels
    Median: 1.510 pixels
    Min: 0.032 pixels
    Max: 13.861 pixels
    Error distribution:
      ▁▂▄▅▆▇▇█▆▅▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁▁ ▁  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁▁▁▁▁▁▁▁▁▁▁ ▁ ▁▁
      0.032                                                     13.861
  Depth reliability (finite, >=2-view points):
    Diagnosed points: 10,321
    Inverse-depth z (depth/sigma; low => near-infinity):
      Median: 481.16
      Min: 3.49   Max: 4170.81
      Below z=4 (near-infinity): 2 (0.0%)
    Inverse-depth z:
      ▂▄▆▆▇▇▇█▆▆▅▅▅▄▃▃▃▂▃▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
      0.000                                                   2704.199
    Condition number (median): 22.6
  Point or bearing (likelihood-ratio test, threshold 25):
    Noise level: 1.244 px, measured over 74,840 observations of finite points, 0 excluded as outliers
    Finite points called bearings: 0 of 10,321 scored
    Points at infinity called finite: 0 of 0 scored

Observation statistics:
  Min observations per point: 2
  Max observations per point: 53
  Mean observations per point: 7.25
  Median observations per point: 5
    Track length distribution:
      ▁█▄▂ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁  ▁  ▁
      2.000                                                     53.000

Nearest neighbor distances:
  Min: 0.000000
  Max: 5.889717
  Mean: 0.041137
  Median: 0.025569
    NN distance distribution:
      █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁ ▁       ▁▁        ▁                        ▁
      0.000                                                      5.890

Integrity: OK
Completed in 0.15s
```

## 2. Image reprojection statistics

The `sfm analyze --metrics` report shows per-image reprojection error
statistics, sorted by mean error descending. Each row includes a histogram of
that image's error distribution, plus the observation count, mean track length,
and a flag for images with elevated error (no image is flagged in this run).
The output below is cut at the `...` line to the five images with the highest
mean error and the two with the lowest.

```
$ sfm analyze --metrics sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr

Per-image metrics analysis for: 20260413-00-solve-dino_dog_toy_1-85.sfmr
====================================================================================================
Reconstruction: 85 images, 10,321 points, 74,840 observations
Mean reprojection error: 1.587 px (median: 1.510 px)

Image (by mean error desc)                           Obs   MeanErr    MedErr    MaxErr  MeanTL  Flag
----------------------------------------------------------------------------------------------------
images/dino_dog_toy_15.jpg                          1203     2.056     1.935    11.807    15.6
      ▁▄▅▄▆▅█▆▆▃▃▃▂▁▁▁▁▁▁▁ ▁    ▁         ▁▁ ▁
images/dino_dog_toy_16.jpg                          1002     1.968     1.761     7.602    13.6
      ▂▆▇█▇▇▆▅▆▄▃▂▂▂▁▁▁▁▁▁▁▁   ▁
images/dino_dog_toy_09.jpg                           948     1.835     1.606    13.832    11.6
      ▂█▇▆▅▅▅▆▃▄▃▂▁▁▁▁▁▁▁▁▁▁                      ▁ ▁
images/dino_dog_toy_43.jpg                          1056     1.797     1.643     6.716    15.0
      ▂▅█▆▅▅▅▄▄▄▃▂▁▁▁▁▁▁ ▁  ▁
images/dino_dog_toy_34.jpg                          1015     1.776     1.562    10.107    15.0
      ▂▆█▆▇▅▄▄▄▃▃▂▁▁▁▁▁▁  ▁             ▁
...
images/dino_dog_toy_26.jpg                           773     1.020     0.713    12.890    13.7
      ▄█▆▃▂▁▁▁▁▁▁▁▁▁ ▁▁    ▁▁           ▁  ▁ ▁ ▁ ▁
images/dino_dog_toy_13.jpg                          1581     0.972     0.765    14.515    16.3
      ▃▇█▅▂▁▁▁▁▁▁▁▁▁▁                         ▁        ▁
----------------------------------------------------------------------------------------------------
      0                                             14.8 px
!!  mean error > 3.020 px (2x reconstruction median of 1.510 px)
!   mean error > 2.265 px (1.5x reconstruction median of 1.510 px)
--  no observations (image registered but no points)
MeanTL = mean track length (avg number of images observing each point)

Completed in 0.16s
```

## 3. Depth range per image

The `sfm analyze --z-range` report shows the range of 3D point depths as seen
from each camera, with a histogram of the depth distribution. The output below
is cut at the `...` line to the first five images and the last two.

```
$ sfm analyze --z-range sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr

Z range statistics for: 20260413-00-solve-dino_dog_toy_1-85.sfmr
======================================================================
Images: 85
3D points: 10321
Histogram buckets: 128

Summary statistics:
  Images with data: 85/85
  Min Z range: [0.738, 8.951]
  Max Z range: [1.817, 37.484]
  Observed points per image: [102, 1603]

Per-image Z ranges:
  images/dino_dog_toy_01.jpg:
    Z range: [4.262, 14.255]
    Observed:  n= 764, med=5.476, mean=5.863
               [▁▃▆▆▇▇█▆▅▃▂▂▃▃▃▂▂▂▂▂▁▁▁▁▁▁▁▁                  ▁          ▁▁▁   ▁]
  images/dino_dog_toy_02.jpg:
    Z range: [3.829, 16.473]
    Observed:  n=1215, med=4.866, mean=5.164
               [▂▁▂▆█▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁                 ▁   ▁ ▁▁▁ ▁          ▁]
  images/dino_dog_toy_03.jpg:
    Z range: [3.814, 14.414]
    Observed:  n=1472, med=4.780, mean=5.045
               [▂▁▂▇▇█▄▄▃▂▂▁▁▁▁▁▁▁▁ ▁▁▁▁▁▁▁▁ ▁▁   ▁                   ▁ ▁ ▁▁▁  ▁]
  images/dino_dog_toy_04.jpg:
    Z range: [3.818, 14.692]
    Observed:  n=1603, med=4.758, mean=5.038
               [▂▁▃█▇▆▄▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁                        ▁▁▁▁▁▁▁▁▁ ▁]
  images/dino_dog_toy_05.jpg:
    Z range: [3.847, 14.371]
    Observed:  n=1360, med=4.786, mean=5.021
               [▃▁▂▇▇█▄▄▄▂▃▁▁▁▁▁▁▁▁ ▁▁▁  ▁  ▁▁                      ▁▁▁▁▁▁▁ ▁ ▁▁]
  ...
  images/dino_dog_toy_84.jpg:
    Z range: [0.952, 1.968]
    Observed:  n= 218, med=1.291, mean=1.354
               [▁▂▁ ▁▄▂▁▁▃▂▁▄▁▄▃▃▂█▄▆▂▂▁▄▄▂▄▁▂▄ ▁▂▁ ▁▁▁▁ ▁▁▁ ▁▁▁▁▂▁▁▁▁▁▁▁▁▁ ▁ ▂▁]
  images/dino_dog_toy_85.jpg:
    Z range: [1.078, 1.817]
    Observed:  n= 156, med=1.339, mean=1.382
               [▁▂▁▁▁ ▂▂▁ ▂▂▄▂▁▂█▄▅▂▅▁▂▃▂▁▅▁▂▂▂▃▁▂ ▁ ▁▂ ▁▁  ▁▂▁▁▁ ▂ ▁▂ ▁▂▂▁▁▁ ▁▁]

Completed in 0.04s
```

## 4. Detect sequence discontinuities

The `sfm motion` command analyzes successive camera motions in image
sequences and flags jumps in translation or rotation, along with sudden
changes in step size and in the number of points the images see. This is
especially useful for reconstructions made from video footage, where a
discontinuity can indicate a problem with the solve. The per-frame table in the
output below is cut at the `...` line to frames 1-7 and 83-85.

```
$ sfm motion sfmr/20260413-00-solve-dino_dog_toy_1-85.sfmr
Reconstruction: 85 images, 10,321 points, 74,840 observations
Found 1 sequence

Analyzing sequence: images/dino_dog_toy_%02d.jpg (85 frames)

  Successive motion -- median translation: 0.8869, median rotation: 9.99°
  Signal thresholds:
    Pose extrapolation:  trans>2.6607 (3x median step)  rot>15.0°
    Step-size ratio  (w=8):  max(pre/post, post/pre) > 1.5
    Coviz drop       (w=16):  baseline/cross-overlap > 1.8
    Obs-count outlier (w=24):  z-score < -2.5

    Frame  Image                                     L.trans    L.rot  R.trans    R.rot   StepR    CovR    ObsZ  Flag
  -------------------------------------------------------------------------------------------------------------------
        1  images/dino_dog_toy_01.jpg                      -        -   0.3600    2.12°       -       -    -1.8
        2  images/dino_dog_toy_02.jpg                      -        -   0.2885    3.84°       -    0.99    -0.3
        3  images/dino_dog_toy_03.jpg                 0.3600    2.12°   0.1168    2.32°       -    0.97    +0.9
        4  images/dino_dog_toy_04.jpg                 0.2885    3.84°   0.1064    1.35°    1.10    0.89    +1.2
        5  images/dino_dog_toy_05.jpg                 0.1168    2.32°   0.0810    1.63°    1.12    0.87    +0.4
        6  images/dino_dog_toy_06.jpg                 0.1064    1.35°   0.3181    0.96°    1.27    0.86    +0.3
        7  images/dino_dog_toy_07.jpg                 0.0810    1.63°   0.6690   22.50°    1.43    0.86    -0.6  R.r
        ...
       83  images/dino_dog_toy_83.jpg                 0.1740    3.88°   0.2594    5.15°    1.59    0.48    -2.4  Step
       84  images/dino_dog_toy_84.jpg                 0.3085    5.92°        -        -       -    0.43    -3.6  Obs
       85  images/dino_dog_toy_85.jpg                 0.2594    4.86°        -        -       -    0.43    -3.5  Obs

  images/dino_dog_toy: 10 discontinuities, 0 breaks
    Break rule: RotR > 4 and SharedPts < 89.4 and NearPts < 284.5, where expected rotation = 9.994° per frame number x max(gap, 1)
              Edge      Dist      Rot    StepR      CovR       ObsZ(A/B)  SharedPts    Err(A)    Err(B)  Signals  NearPts    RotR  Break
    ------------------------------------------------------------------------------------------------------------------------------------
              7->8    0.7206    1.00°    <1.51>     0.85       -0.6/-1.2        580   1.545px   1.362px  P S         3204    0.10  -
            16->17    0.1838   30.89°    <1.65>     1.00       -0.6/+0.4        563   1.968px   1.289px  P S         3009    3.09  -
            27->28    9.1279    6.56°    <1.95>     0.94       -1.6/-2.0         98   1.558px   1.528px  P S         2250    0.66  -
            37->38    4.6117   63.94°     1.43      1.16       -0.8/-0.3         33   1.413px   1.284px  P           2048    6.40  -
            52->53    0.7660   16.95°    <1.85>     0.91     -1.2/<-3.4>         94   1.370px   1.584px  P S O       1181    1.70  -
            56->57    0.7327   11.43°     1.32      1.20       +0.4/+0.4        350   1.424px   1.578px  P            623    1.14  -
            68->69    0.8794    5.27°    <1.54>     1.57     -1.5/<-3.0>        119   1.489px   1.764px  S O          468    0.53  -
            70->71    1.0839   10.80°     1.27      1.55       -0.8/-0.1        313   1.649px   1.561px  P            547    1.08  -
            75->76    1.2181   12.08°    <1.51>     0.88       +0.3/+0.0        281   1.246px   1.474px  S            919    1.21  -
            82->83    0.7371    8.47°    <1.59>     0.48       -1.1/-2.4        169   1.326px   1.481px  S            214    0.85  -

================================================================================
Summary
================================================================================

Total: 10 discontinuities in 1 sequence, 0 breaks.
  Found by one signal:          5
  Found by two or more signals: 5
  A discontinuity is an edge where at least one signal found the
  camera motion irregular; the two counts above say how many signals
  agree on that, not whether it is a break. A break is a
  discontinuity that passes the break rule, a place where the solve put
  the parts of the camera path on either side in inconsistent places;
  the number of signals is not part of that rule.
  Legend: P=pose residual, S=step-size ratio, C=coviz drop, O=obs-count outlier.
  < > marks a value past its signal's threshold. Dist and Rot are the step between the edge's two images.
  NearPts = points seen both in the 8 images up to the edge and the 8 after it. RotR = rotation / expected rotation. BREAK = RotR, SharedPts and NearPts all past the break rule.
Verdict: no breaks
Completed in 0.34s
```

The per-frame table shows how far each pose is from where its neighbours on
the left and right predict it, and the **Flag** column names the signals that
fired. Below each sequence's frame table, a table lists one row per
discontinuity in that sequence, with the signals that found it in the
**Signals** column, and `< >` marks each value past its signal's threshold.
The `Summary` at the end counts the discontinuities found by one signal and
those found by two or more. As the report says, these counts say how many
signals agree that the camera motion is irregular, not whether there is a
break: the number of signals is not part of the break rule.

Each discontinuity is then checked for a break. A break is a place where the
solve put the two stretches of the camera path on either side in inconsistent
places. The reconstruction's other numbers, such as the registered image
count, the points per image and the reprojection error, can look normal
across one. An edge is a break when the camera turns more than 4 times the
usual rotation (**RotR**), and the two images share few points
(**SharedPts**), and the 8 images before the edge share few points with the 8
after it (**NearPts**). The `Break rule:` line above each sequence's table gives
that sequence's limits, the **Break** column marks each break with `BREAK`, and
the last line, `Verdict:`, names the breaks or says `no breaks`.

This dataset isn't from video — the images were taken from different angles
around the toy — so the detected discontinuities here are expected large
changes in viewpoint rather than actual problems, and the verdict is
`no breaks`. For example, edge 37->38 turns 6.4 times the usual rotation and
its two images share only 33 points, but the 8 photos before it and the 8
after it still share 2048 points, so the solve has tied the two stretches
together.
