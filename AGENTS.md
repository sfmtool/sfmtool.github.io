# Working in the sfmtool.github.io Repository

The documentation site for [SfM Tool](https://github.com/sfmtool/sfmtool),
deployed to <https://sfmtool.github.io/>. Pages are Markdown under `docs/`, the
navigation is in `zensical.toml`, and the build runs through Pixi:
`pixi run docs-build` and `pixi run docs-serve`.

- The code, its specs and `AGENTS.md` live in the `sfmtool` repository, which
  is usually checked out beside this one. Check every command, menu name,
  panel name and output block a page shows against that code or a real run,
  not against memory.
- Screenshots live beside the page that uses them, in an `images/` directory.
  Take them on copies of the `sfmtool` repository's `test-data`, never on the
  originals. No local path, username, MCP status text (*MCP: …*) or stale
  hover label may show: crop them out, or end the run on a real step so the
  status line shows that step's message.
- `scripts/add_legacy_redirects.py` keeps the old
  `https://sfmtool.github.io/sfmtool/...` links working. No page may live
  under `docs/sfmtool/`; the script fails the build if one does.
- Write in plain language: no metaphors or idioms where a literal phrase says
  the same thing. Name the thing and say what it does.
- Pull requests are squash-merged, and every commit needs a DCO sign-off
  (`git commit -s`).

## Steps that a person or an agent can follow

Tutorials are written for people. An agent connected to SfM Explorer's MCP
endpoint should be able to follow the same text, because the endpoint's tools
use the viewer's own words (`specs/gui/mcp-server.md` § "The wire
vocabulary" in `sfmtool`). Make that work through exact wording, not through
agent sections, collapsed tool-call blocks, hidden comments or tool names on
the page.

- **Use the viewer's exact words.** Write panel, menu, toolbar and column
  names exactly as the viewer shows them, in bold (**Image Detail**, **Reproj
  Error**). The viewer names each control by the text it shows (the
  **Track** heading is `Sort by Track` to an agent), so the visible word is
  the one to write. A control whose name lacks its visible text is a viewer
  bug: report it in `sfmtool` rather than writing around it. Use the same
  word for the same thing on every page; when a concept has a term in
  `specs/GLOSSARY.md`, use that term.
- **Pair each gesture with the name of the operation.** "Double-click its
  thumbnail to select it and look through it", not "double-click the third
  image". The gesture is for the person; the verb (*select*, *look through*,
  *zoom to fit*, *convert to embedded patches*) is the operation an agent
  looks for. When one gesture does several operations, name each of them.
- **Describe places and layouts in words.** A gesture with no operation name,
  such as dragging a panel's tab to dock it, needs the place it acts on
  ("the right-hand one of the five drop targets in the middle of the 3D
  Viewer") and the layout that results ("3D Viewer on the left, Image Detail
  in the middle, Track View on the right").
- **Name what to act on so that it holds on every solve.** Name an image by
  what the viewer shows and by file: "the thumbnail numbered 2,
  `dino_dog_toy_03.jpg` (camera image 2)". Point IDs change from solve to
  solve, so name a point by a property the reader can look up ("the point
  with the longest track in that image"), never by its ID. Where a file name,
  date or count on the page comes from the example run, say that the
  reader's will differ.
- **End each step with something to check on screen.** Quote text the viewer
  shows ("Track View's header shows *track: N obs*") or describe a
  visible change ("the track turns orange"), so the reader knows the step
  worked.
- **Show what the text describes.** Wherever a step tells the reader to look
  at something (a menu entry, a panel's state, an overlay, a row, a box of
  settings), put a screenshot of that thing right after the sentence,
  cropped to it, with alt text that says what it shows. One wide shot at
  the end of a step does not replace these. A state that cannot be captured,
  such as the middle of a drag, is described in words, never staged.
- **Test a step by doing it.** Before a step is merged, follow its text
  literally against the viewer, and take its screenshot from that run. If an
  agent driving the viewer over MCP has to guess an operation or an argument,
  rewrite the text rather than adding a hint for agents.
