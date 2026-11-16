# Inspecting a Reconstruction

Look at the properties of a reconstruction from the command line: what it
holds, how its points and errors are distributed, how its images compare, how
far the scene is from each camera, and how the camera moves from photograph to
photograph.

| Question | Command |
|---|---|
| What does it hold, and how are its points distributed? | `sfm inspect` (`-v` for the distributions) |
| How do the images compare? | `sfm analyze --metrics` |
| How far away is the scene from each camera? | `sfm analyze --z-range` |
| How does the camera move between photographs? | `sfm motion` |

The examples run on the file from [Getting Started](getting-started.md#3-solve).
Each output is cut to the lines that answer its question, with `...` marking
the cuts.

## What does it hold, and how are its points distributed?

```
$ sfm inspect -v sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
...
Reconstruction summary:
  Images: 85
...
  3D points: 10331
  Observations: 74835
...
3D Point statistics:
  Position range:
    X: [-14.305, 33.646]
    X distribution:
      ▁ ▁▁▁      ▁▁▁▁▁▁▂▆█▆▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁ ▁▁            ▁▁       ▁
      -14.305                                                   33.646
...
  Reprojection error:
    Mean: 1.584 pixels
    Median: 1.509 pixels
...
    Error distribution:
      ▁▂▃▅▆▆▇█▆▅▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ ▁▁▁▁▁ ▁▁ ▁▁▁▁▁▁▁▁▁▁ ▁▁▁ ▁▁▁▁ ▁▁ ▁▁
      0.031                                                     13.702
...
Observation statistics:
...
  Mean observations per point: 7.24
  Median observations per point: 5
    Track length distribution:
      ▁█▄▂ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁  ▁
      2.000                                                     53.000
...
Integrity: OK
...
```

- **Images** is the number of photographs the solve placed; here all 85.
- Each **distribution** is a histogram between the two values printed under
  it. The X distribution shows most points in a narrow band, the toy, with a
  thin spread of farther points around it; `-v` prints Y and Z the same way.
- **Reprojection error** is the distance, in pixels, from each feature to
  where its 3D point projects in that photograph.
- **Observations per point** is the track length: the number of photographs
  that see a point. Half the points here are seen in 5 photographs or fewer.
- **Integrity: OK** says the file's contents match the hashes stored in it.

Without `-v`, `sfm inspect` prints these counts and the integrity check on one
screen. [`inspect-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/inspect-command.md)
describes every section.

## How do the images compare?

```
$ sfm analyze --metrics sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
...
Image (by mean error desc)                           Obs   MeanErr    MedErr    MaxErr  MeanTL  Flag
----------------------------------------------------------------------------------------------------
images/dino_dog_toy_15.jpg                          1212     2.065     1.941    11.454    15.5
      ▁▄▅▄▅▅█▆▆▃▃▃▂▁▁▁▁▁▁▁ ▁ ▁    ▁      ▁ ▁ ▁
images/dino_dog_toy_16.jpg                          1005     1.970     1.757     7.210    13.6
      ▂▆▇█▇█▆▆▆▄▄▃▂▂▂▁▁▁▁ ▁▁  ▁▁
...
!!  mean error > 3.018 px (2x reconstruction median of 1.509 px)
!   mean error > 2.263 px (1.5x reconstruction median of 1.509 px)
--  no observations (image registered but no points)
...
```

Each image has a row with its observation count, its reprojection errors and
a histogram of them, sorted by mean error, highest first. An image whose error
is well above the rest gets `!` or `!!` in the **Flag** column, and a placed
image that sees no points gets `--`. No image is flagged here.

## How far away is the scene from each camera?

```
$ sfm analyze --z-range sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
...
Summary statistics:
  Images with data: 85/85
  Min Z range: [0.738, 8.900]
  Max Z range: [1.817, 37.250]
  Observed points per image: [101, 1607]

Per-image Z ranges:
...
  images/dino_dog_toy_03.jpg:
    Z range: [3.841, 14.409]
    Observed:  n=1468, med=4.781, mean=5.045
...
  images/dino_dog_toy_85.jpg:
    Z range: [1.078, 1.817]
    Observed:  n= 156, med=1.334, mean=1.383
...
```

`med=` is the median depth of the points a camera sees. It is in the
reconstruction's units, which have no set scale. Here `dino_dog_toy_85.jpg`
was taken about a quarter as far from the toy as `dino_dog_toy_03.jpg`.

## How does the camera move between photographs?

`sfm motion` follows the photographs in file-number order and measures each
step of the camera's motion. It lists the discontinuities, the places where
that motion is irregular. A **break** is a discontinuity where the solve
placed the camera path on its two sides inconsistently.

```
$ sfm motion sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
...
  images/dino_dog_toy: 10 discontinuities, 0 breaks
...
              Edge      Dist      Rot    StepR      CovR       ObsZ(A/B)  SharedPts    Err(A)    Err(B)  Signals  NearPts    RotR  Break
    ------------------------------------------------------------------------------------------------------------------------------------
              7->8    0.7195    1.01°    <1.51>     0.86       -0.6/-1.1        579   1.540px   1.380px  P S         3202    0.10  -
            16->17    0.1844   30.89°    <1.65>     1.01       -0.6/+0.4        568   1.970px   1.288px  P S         3011    3.10  -
            27->28    9.1302    6.56°    <1.95>     0.94       -1.6/-1.9         99   1.538px   1.547px  P S         2249    0.66  -
            37->38    4.6109   63.93°     1.43      1.15       -0.8/-0.3         33   1.426px   1.268px  P           2050    6.41  -
            52->53    0.7651   16.96°    <1.85>     0.91     -1.2/<-3.3>         93   1.375px   1.553px  P S O       1174    1.70  -
            56->57    0.7327   11.43°     1.32      1.20       +0.4/+0.4        351   1.407px   1.585px  P            621    1.15  -
            68->69    0.8805    5.31°    <1.55>     1.57     -1.6/<-3.1>        119   1.477px   1.777px  S O          467    0.53  -
            70->71    1.0824   10.78°     1.27      1.55       -0.8/-0.1        315   1.630px   1.559px  P            544    1.08  -
            75->76    1.2163   12.07°    <1.51>     0.88       +0.3/+0.0        284   1.205px   1.520px  S            923    1.21  -
            82->83    0.7373    8.47°    <1.59>     0.48       -1.1/-2.5        171   1.358px   1.533px  S            217    0.85  -
...
Verdict: no breaks
...
```

Each row is a discontinuity between two photographs. The **Break** column
says `BREAK` for a break. The last line, `Verdict:`, names the breaks or says
`no breaks`. These photographs were taken around the toy, not as a video, so
the jumps in viewpoint are expected discontinuities, and there are no breaks.
[`motion-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/motion-command.md)
gives the break rule and what each column and signal means.
