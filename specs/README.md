# The SfM Tool documentation site

This site teaches people new to Structure from Motion (SfM) how to turn photos
or a video into a 3D reconstruction with SfM Tool and look at it in SfM
Explorer. This file says who the site is for, what it covers and leaves to
others, which kind of page each page is, and the rules every page follows. Each
page has its own spec in [`pages/`](pages/), which says what that page is for
and what it leaves out. These specs sit outside `docs/`, so the site does not
publish them.

## Audience

- **People new to SfM** who have photos or a video of a scene and want a 3D
  model. They can run a command in a terminal but know neither SfM nor
  sfmtool's vocabulary.
- **Agents** following the same steps over SfM Explorer's MCP endpoint. They
  need no separate text; they need the viewer's exact words (see `AGENTS.md`
  § "Steps that a person or an agent can follow").

## What the site does and what lives elsewhere

The site gives a reader the few paths that matter, in order, with the key
points explained in a short narrative. It does not document every option,
every output line or how each behaviour works. Those live in sfmtool:

| Need | Where it lives |
|---|---|
| Every option of a command | `sfm <command> --help` |
| What a command, output line, panel or format does, in full | sfmtool's [`specs/`](https://github.com/sfmtool/sfmtool/tree/main/specs) |
| The words for a concept | sfmtool's [`specs/GLOSSARY.md`](https://github.com/sfmtool/sfmtool/blob/main/specs/GLOSSARY.md) |

A page links to these rather than restating them.

## Page types

The site uses the [Diátaxis](https://diataxis.fr/) types. Its
[compass](https://diataxis.fr/compass/) asks two questions: is the page about
doing or knowing, and is the reader learning or working?

- **Tutorial**: a guided lesson with one path and a visible result at each
  step. It keeps explanation to what the next step needs and links out for the
  rest.
- **How-to guide**: steps to one goal for a reader who already knows the basics.
- **Reference**: facts to look up. On this site, that is sfmtool's `--help` and
  specs.
- **Explanation**: background on why things are as they are.

The navigation in `zensical.toml` has a section per type: **Tutorials**
holds Getting Started and Viewing 3D Point Tracks, and **How-to guides** holds
Inspecting a Reconstruction and Converting Video to Image Sequences. Each
section's title links to a short section page that lists its pages; the arrow
beside the title expands and collapses the section.

| Page | Type | Spec |
|---|---|---|
| `docs/index.md` | Landing page (short explanation, then where to start) | [index.md](pages/index.md) |
| `docs/tutorials/index.md` | Section page for Tutorials | [tutorials-index.md](pages/tutorials-index.md) |
| `docs/how-to/index.md` | Section page for How-to guides | [how-to-index.md](pages/how-to-index.md) |
| `docs/tutorials/getting-started.md` | Tutorial | [getting-started.md](pages/getting-started.md) |
| `docs/tutorials/point-tracks.md` | Tutorial | [point-tracks.md](pages/point-tracks.md) |
| `docs/tutorials/inspecting.md` | How-to guide | [inspecting.md](pages/inspecting.md) |
| `docs/tutorials/video-to-images.md` | How-to guide | [video-to-images.md](pages/video-to-images.md) |

The site has no explanation page (what a track, a patch or a solve is) and no
how-to guide for driving SfM Explorer with an agent. Reference stays in
sfmtool.

## Shared rules

**Brevity.** These follow Diátaxis, the
[Google developer documentation style guide](https://developers.google.com/style)
(no pre-announcing, the condition before the instruction, numbered steps) and
minimalist instruction (J. M. Carroll, *The Nurnberg Funnel*, MIT Press, 1990:
start the reader on real work at once, and cut text that does not support the
next action).

- One job per page, stated in its first paragraph.
- Only the explanation the next step needs. Link to a spec, `--help` or
  another page for the rest.
- Trim an output block to the lines the text refers to, and mark each cut
  with `...`. A full listing of a command's output belongs in its spec.
- Explain an output line only when the reader acts on it or might take it for
  an error.
- State a caveat once on the site, on the page where the reader first meets
  it, and link to it from later pages. Two examples: a solve's counts differ
  from run to run, and the solver's warnings do not mean failure.
- Do not describe in words what a screenshot next to the text already shows.
  The words name what to look for in it.

**Captured output and screenshots.** The tutorials and how-to guides take
them from one shared run: the Getting Started steps on a copy of
`test-data/images/dino_dog_toy` from sfmtool `main`, with the later pages
working on that run's `.sfmr` file. The pages then quote the same file name
and counts. When a refresh changes the captured output, re-capture every page
that quotes the run. The home page's screenshot shows sfmtool's newest
checked-in Seoul Bull ground truth instead, as its page spec says. `AGENTS.md`
says how to take screenshots on copies and what to crop out.

**Light and dark.** The site opens in the reader's operating-system scheme,
light or dark, and has a toggle (`zensical.toml`). An image or diagram must
read on both backgrounds.

**Links.** Each tutorial links the page before it and ends with what to read
next. Link sfmtool specs by their GitHub URL on `main`. Link text says where
it goes.

**Wording.** Plain language, the viewer's exact words, and steps an agent can
follow, as `AGENTS.md` says.

**Sentences that read easily.** Plain words are not enough: each sentence
should read naturally aloud on the first pass.

- One idea per sentence. Split a sentence that defines a term and also says
  what follows from it.
- Keep the subject near its verb, and put the verb early. Do not front the
  object of a relative clause ("a directory whose settings … every command
  uses"); say it in the usual order ("Every command uses its settings").
- Put examples and asides at the end of a sentence, not between the subject
  and the verb.
- Brevity means fewer ideas, not denser sentences: two short sentences beat
  one compressed one.

**Author-owned passages.** Some passages are the maintainer's own writing,
named as author-owned in their page's spec (on the home page: why the project
exists, and about the author). Nobody else rewrites them; an audit may suggest
a change, with the proposed text, for the maintainer to decide.

## Page specs

A page spec in `pages/` gives the page's type, the reader's goal, what the
reader can do afterwards, the pages before and after, the dataset and
commands, each output block and screenshot and why it is there, and what the
page leaves out and where that lives. It describes the page's purpose, not
the page's current state: where a page falls short of its spec is a finding
in a report under `reports/`. Read a page's spec before changing the page,
and change the spec first when the page's purpose changes. The `audit-docs`
skill (`skills/audit-docs/SKILL.md`) checks the pages against these specs.
