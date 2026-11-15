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
  Timestamp: 2026-11-14T22:53:37.188324100-08:00
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
    images/dino_dog_toy_%02d.jpg (85 files, sequence 1-85)
  Cameras: 1
  3D points: 10362
  Observations: 74894
  Mean observations per point: 7.23

Cameras:
  Camera 0: SIMPLE_RADIAL 2040x1536
    Parameter                      Value
    --------------------  --------------
    focal_length             1471.029552
    principal_point_x        1020.000000
    principal_point_y         768.000000
    radial_distortion_k1        0.020113

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
    X: [-14.799, 33.001]
    X distribution:
      ▁▁ ▁ ▁      ▁▁▁▁▁▁▃█▇▆▄▁▁▁▁▁▁▁▁▁▁▁▁▁▁  ▁ ▁▁            ▁       ▁
      -14.799                                                   33.001
    Y: [-7.884, 31.800]
    Y distribution:
      ▁▁▁▁▁▁▁▁▁    ▁▁▂█▆▃▃▂▁▁▁▁▁ ▁▁▁▁▁▁▁▁▁                           ▁
      -7.884                                                    31.800
    Z: [-17.194, 7.122]
    Z distribution:
      ▁   ▁▁▁▁▁▁▁   ▁  ▁   ▁▁        ▁▁▁▁▁▁▁▇▇▆▄▅█▅▃▂▁▁▁▁▁▁▁  ▁▁▁▁  ▁▁
      -17.194                                                    7.122
  Reprojection error:
    Mean: 1.595 pixels
    Median: 1.512 pixels
    Min: 0.038 pixels
    Max: 14.587 pixels
    Error distribution:
      ▁▂▄▅▆▇█▇▆▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁▁▁▁▁ ▁▁ ▁▁ ▁▁  ▁
      0.038                                                     14.587
  Depth reliability (finite, >=2-view points):
    Diagnosed points: 10,362
    Inverse-depth z (depth/sigma; low => near-infinity):
      Median: 477.58
      Min: 3.15   Max: 4204.24
      Below z=4 (near-infinity): 4 (0.0%)
    Inverse-depth z:
      ▂▄▆▆▇▇▇█▅▆▅▅▅▄▃▃▃▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
      0.000                                                   2701.704
    Condition number (median): 22.9
  Point or bearing (likelihood-ratio test, threshold 25):
    Noise level: 1.246 px, measured over 74,894 observations of finite points, 0 excluded as outliers
    Finite points called bearings: 0 of 10,362 scored
    Points at infinity called finite: 0 of 0 scored

Observation statistics:
  Min observations per point: 2
  Max observations per point: 53
  Mean observations per point: 7.23
  Median observations per point: 5
    Track length distribution:
      ▁█▄▂ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁  ▁  ▁
      2.000                                                     53.000

Nearest neighbor distances:
  Min: 0.000000
  Max: 3.598056
  Mean: 0.040651
  Median: 0.025561
    NN distance distribution:
      █▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁  ▁ ▁▁ ▁▁  ▁   ▁         ▁▁  ▁              ▁
      0.000                                                      3.598

Integrity: OK
Completed in 0.14s
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
Reconstruction: 85 images, 10,362 points, 74,894 observations
Mean reprojection error: 1.595 px (median: 1.512 px)

Image (by mean error desc)                           Obs   MeanErr    MedErr    MaxErr  MeanTL  Flag
----------------------------------------------------------------------------------------------------
images/dino_dog_toy_15.jpg                          1203     2.033     1.927     8.937    15.6
      ▁▄▅▄▆▅█▅▆▃▃▃▂▁▁▁▁▁▁▁ ▁     ▁  ▁
images/dino_dog_toy_16.jpg                          1003     1.963     1.769     6.300    13.6
      ▂▅▇█▇▆▆▅▅▄▃▂▂▂▁▁▁▁▁▁▁▁
images/dino_dog_toy_09.jpg                           942     1.842     1.627    13.260    11.5
      ▂██▆▅▆▅▆▃▄▃▂▁▁▁▁▁▁▁▁▁▁         ▁ ▁▁         ▁
images/dino_dog_toy_43.jpg                          1045     1.788     1.636     6.615    14.9
      ▃▅█▆▆▅▅▅▄▃▃▂▁▁▁▁▁▁ ▁  ▁
images/dino_dog_toy_44.jpg                           874     1.773     1.525     6.804    14.6
      ▂▆█▅▅▃▄▄▃▂▂▁▁▁▁▁▁▁▁▁▁ ▁
...
images/dino_dog_toy_26.jpg                           771     1.004     0.704    12.185    13.6
      ▄█▆▃▁▁▁▁▁▁▁▁▁▁ ▁▁▁   ▁   ▁▁▁ ▁ ▁        ▁
images/dino_dog_toy_13.jpg                          1586     0.994     0.769    12.551    16.2
      ▃▇█▅▂▁▁▁▁▁▁▁▁▁▁              ▁      ▁▁    ▁
----------------------------------------------------------------------------------------------------
      0                                             14.9 px
!!  mean error > 3.023 px (2x reconstruction median of 1.512 px)
!   mean error > 2.267 px (1.5x reconstruction median of 1.512 px)
--  no observations (image registered but no points)
MeanTL = mean track length (avg number of images observing each point)

Completed in 0.05s
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
3D points: 10362
Histogram buckets: 128

Summary statistics:
  Images with data: 85/85
  Min Z range: [0.740, 8.902]
  Max Z range: [1.818, 36.932]
  Observed points per image: [104, 1606]

Per-image Z ranges:
  images/dino_dog_toy_01.jpg:
    Z range: [4.261, 14.250]
    Observed:  n= 757, med=5.492, mean=5.866
               [▁▂▆▅▇▇█▆▅▃▂▂▂▃▃▂▂▂▂▁▁▁▁▁▁▁▁▁                  ▁           ▁▁   ▁]
  images/dino_dog_toy_02.jpg:
    Z range: [3.847, 16.462]
    Observed:  n=1212, med=4.861, mean=5.162
               [▃▁▃▇█▅▅▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁                 ▁   ▁ ▁▁▁ ▁          ▁]
  images/dino_dog_toy_03.jpg:
    Z range: [3.842, 14.408]
    Observed:  n=1466, med=4.780, mean=5.044
               [▂▁▃▇█▇▄▄▃▂▂▁▁▁▁▁▁▁▁ ▁▁▁▁▁▁▁▁ ▁▁   ▁                   ▁▁▁ ▁▁▁  ▁]
  images/dino_dog_toy_04.jpg:
    Z range: [3.819, 14.708]
    Observed:  n=1606, med=4.757, mean=5.030
               [▂▁▃█▇▆▄▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁                        ▁▁▁▁▁ ▁ ▁ ▁]
  images/dino_dog_toy_05.jpg:
    Z range: [3.847, 14.205]
    Observed:  n=1363, med=4.786, mean=5.026
               [▃▁▂▇▇█▅▄▄▂▃▂▁▁▁▁▁▁▁  ▁▁  ▁  ▁▁                       ▁▁▁▁▁▁▁▁▁ ▁]
  ...
  images/dino_dog_toy_84.jpg:
    Z range: [0.952, 1.967]
    Observed:  n= 217, med=1.291, mean=1.356
               [▁▂▁ ▁▃▂▁▁▂▂▁▃▁▃▃▃▂█▄▅▂▂▁▃▃▂▃▁▂▃ ▁▁▁ ▁▁▁▁ ▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁ ▁ ▂▁]
  images/dino_dog_toy_85.jpg:
    Z range: [1.079, 1.818]
    Observed:  n= 152, med=1.327, mean=1.379
               [▁▂▁ ▁▁▁▂▁▁▂▂▄▂▂▁█▄▄▂▄▁▂▃▂▁▄▁▂▃▂▂▁▂ ▁ ▁▂ ▁▁  ▁▁▁▁▁ ▂▁▁▂▁ ▂▂▁▁▁ ▁▁]

Completed in 0.03s
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
Reconstruction: 85 images, 10,362 points, 74,894 observations
Found 1 sequence

Analyzing sequence: images/dino_dog_toy_%02d.jpg (85 frames)

  Successive motion -- median translation: 0.8873, median rotation: 10.02°
  Signal thresholds:
    Pose extrapolation:  trans>2.6620 (3x median step)  rot>15.0°
    Step-size ratio  (w=8):  max(pre/post, post/pre) > 1.5
    Coviz drop       (w=16):  baseline/cross-overlap > 1.8
    Obs-count outlier (w=24):  z-score < -2.5

    Frame  Image                                     L.trans    L.rot  R.trans    R.rot   StepR    CovR    ObsZ  Flag
  -------------------------------------------------------------------------------------------------------------------
        1  images/dino_dog_toy_01.jpg                      -        -   0.3611    2.14°       -       -    -1.8
        2  images/dino_dog_toy_02.jpg                      -        -   0.2889    3.84°       -    0.99    -0.4
        3  images/dino_dog_toy_03.jpg                 0.3611    2.14°   0.1167    2.32°       -    0.97    +0.9
        4  images/dino_dog_toy_04.jpg                 0.2889    3.84°   0.1057    1.34°    1.09    0.88    +1.3
        5  images/dino_dog_toy_05.jpg                 0.1167    2.32°   0.0806    1.64°    1.11    0.87    +0.4
        6  images/dino_dog_toy_06.jpg                 0.1057    1.34°   0.3192    0.97°    1.26    0.86    +0.3
        7  images/dino_dog_toy_07.jpg                 0.0806    1.64°   0.6679   22.49°    1.43    0.85    -0.6  R.r
        ...
       83  images/dino_dog_toy_83.jpg                 0.1740    3.89°   0.2594    5.15°    1.58    0.48    -2.6  Step,Obs
       84  images/dino_dog_toy_84.jpg                 0.3092    5.95°        -        -       -    0.43    -3.7  Obs
       85  images/dino_dog_toy_85.jpg                 0.2594    4.87°        -        -       -    0.43    -3.8  Obs

  images/dino_dog_toy: 10 discontinuities, 0 breaks
    Break rule: RotR > 4 and SharedPts < 88.8 and NearPts < 285.5, where expected rotation = 10.020° per frame number x max(gap, 1)
              Edge      Dist      Rot    StepR      CovR       ObsZ(A/B)  SharedPts    Err(A)    Err(B)  Signals  NearPts    RotR  Break
    ------------------------------------------------------------------------------------------------------------------------------------
              7->8    0.7194    1.01°    <1.51>     0.85       -0.6/-1.1        578   1.552px   1.407px  P S         3202    0.10  -
            16->17    0.1840   30.89°    <1.65>     1.01       -0.6/+0.4        568   1.963px   1.272px  P S         3009    3.08  -
            27->28    9.1293    6.54°    <1.95>     0.94       -1.6/-2.0         99   1.535px   1.547px  P S         2254    0.65  -
            37->38    4.6123   63.94°     1.42      1.15       -0.8/-0.3         34   1.408px   1.255px  P           2040    6.38  -
            52->53    0.7664   17.15°    <1.85>     0.91     -1.3/<-3.6>         97   1.360px   1.673px  P S O       1190    1.71  -
            56->57    0.7328   11.43°     1.32      1.19       +0.4/+0.4        353   1.402px   1.587px  P            624    1.14  -
            68->69    0.8797    5.30°    <1.55>     1.59     -1.5/<-3.1>        122   1.474px   1.755px  S O          461    0.53  -
            70->71    1.0833   10.79°     1.27      1.57       -0.8/-0.1        314   1.626px   1.565px  P            538    1.08  -
            75->76    1.2159   12.06°    <1.51>     0.88       +0.3/+0.1        285   1.246px   1.530px  S            931    1.20  -
            82->83    0.7372    8.47°    <1.58>     0.48     -1.2/<-2.6>        168   1.349px   1.517px  S O          211    0.85  -

================================================================================
Summary
================================================================================

Total: 10 discontinuities in 1 sequence, 0 breaks.
  Found by one signal:          4
  Found by two or more signals: 6
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
Completed in 0.33s
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
its two images share only 34 points, but the 8 photos before it and the 8
after it still share 2040 points, so the solve has tied the two stretches
together.
