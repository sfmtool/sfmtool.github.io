# Inspecting a Reconstruction

Find out from the command line whether a reconstruction is sound, and which
images or parts of the camera path to look at in SfM Explorer.

| Question | Command |
|---|---|
| How big is it, how accurate, is the file intact? | `sfm inspect` (`-v` for detail) |
| Which images fit worst? | `sfm analyze --metrics` |
| How far away is the scene from each camera? | `sfm analyze --z-range` |
| Is the camera path broken anywhere? | `sfm motion` |

The examples run on the file from [Getting Started](getting-started.md#3-solve),
and the output is cut with `...` to the lines that answer each question.

## How big is it, how accurate, is the file intact?

```
$ sfm inspect -v sfmr/20261115-00-solve-dino_dog_toy_1-85.sfmr
...
Reconstruction summary:
  Images: 85
...
  3D points: 10331
  Observations: 74835
...
  Reprojection error:
    Mean: 1.584 pixels
    Median: 1.509 pixels
...
Observation statistics:
  Min observations per point: 2
  Max observations per point: 53
  Mean observations per point: 7.24
  Median observations per point: 5
...
Integrity: OK
...
```

- **Images** is the number of photographs the solve placed; here all 85.
- **Reprojection error** is how far, in pixels, each 3D point lands from the
  feature it was seen at, when projected into that photograph. Smaller is
  better.
- **Observations per point** is the track length: the number of photographs
  that see a point. Longer tracks pin a point down better.
- **Integrity: OK** says the file's contents match the hashes stored in it.

Without `-v`, `sfm inspect` prints these counts and the integrity check on one
screen. [`inspect-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/inspect-command.md)
describes every section.

## Which images fit worst?

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

The images are listed worst first, by mean reprojection error. An image whose
error is well above the rest gets `!` or `!!` in the **Flag** column, and one
the solve placed but that sees no points gets `--`; those are the images to
look at. No image is flagged here.

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

`med=` is the median depth of the points a camera sees, in the
reconstruction's units, which have no set scale. Here `dino_dog_toy_85.jpg`
was taken at about a quarter of the distance from the toy that
`dino_dog_toy_03.jpg` was.

## Is the camera path broken anywhere?

`sfm motion` follows the photographs in file-number order and lists the places
where the camera's motion is irregular, the discontinuities. A **break** is
a discontinuity where the solve put the camera path on either side in
inconsistent places; it is the result that matters.

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

Each row is a discontinuity between two photographs, and the **Break** column
says `BREAK` for a break. The last line, `Verdict:`, names the breaks or says
`no breaks`. These photographs were taken around the toy, not as a video, so
the jumps in viewpoint are expected discontinuities, and there are no breaks.
[`motion-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/motion-command.md)
gives the break rule and what each column and signal means.
