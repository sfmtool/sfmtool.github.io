# Viewing 3D Point Tracks (`docs/tutorials/point-tracks.md`)

**Type:** tutorial.

**Reader's goal:** learn to use SfM Explorer by following one 3D point
through the photos that see it.

**Afterwards the reader** can give a reconstruction embedded patches, prune
the observations that smaller ones cover, arrange
**Image Detail** beside **Track View**, look through a photo, colour its
features by track length, select the point with the longest track from the
**Track Table**, and move around the 3D view in camera view and freely.

**Prerequisites:** the shared run's `.sfmr` open in SfM Explorer.
**Before / after:** [Getting Started](getting-started.md) /
[Inspecting a Reconstruction](inspecting.md).

## Steps

The dataset is the shared run's dino reconstruction; the photo is
`dino_dog_toy_03.jpg` (camera image 2), and the point is "the longest track in
that photo", never an ID. Each step names the operation, uses the viewer's
words and ends with something to check on screen (`AGENTS.md`).

1. Convert to embedded patches (**Scene** panel context menu), so Track View
   has patches to compare.
2. Prune covered observations (**Scene** panel context menu). Large patches
   clutter the view, and a smaller observation in the same pixels is
   generally more accurate, so the step retires the larger ones. The later
   steps, their numbers and their screenshots come from the pruned
   reconstruction.
3. Dock **Image Detail** between the **3D Viewer** and **Track View**.
4. Look through the photo from the **Image Browser**; set **Overlay** to
   **Track Length**.
5. In the **Track Table**, show the points seen in the selected image, sort by
   **Track**, select the top row; read Track View's header.
6. Navigate in camera view.
7. Navigate freely.
8. Move the target and show it with **Target indicator**.

## Output and screenshots

No command output. Each screenshot shows the thing the sentence before it
tells the reader to look at (`AGENTS.md`): the context menu, the Scene row
after conversion, the menu entry that prunes, the 3D view after pruning with
its status line, the layout, the selected thumbnail, the overlay, the sorted
table, Track View, the camera view with the track, free navigation, the
**Display** box and the target compass. Screenshots come from the shared run.

## Leaves out

- What each Track View column measures: name the columns the lesson uses and
  link sfmtool's
  [`track-view.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/gui/track-view.md).
- Every key binding:
  [`viewport-navigation.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/gui/viewport-navigation.md).
  The page lists the keys the steps use.
- Which observations the prune retires, in full:
  [`prune-covered-observations.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/gui/edits/prune-covered-observations.md).
- How patches are made:
  [`embed-patches-command.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/cli/reconstruction/embed-patches-command.md).
