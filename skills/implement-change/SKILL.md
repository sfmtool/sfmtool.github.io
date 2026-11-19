---
name: implement-change
description: Implement one change to the docs site on a branch — an implementer agent evaluates the change and makes it, an independent auditor checks it against the specs, sfmtool and a real run, and the loop repeats until only simple issues remain. Use whenever you are about to change this repository (a page, its spec, its screenshots, the site spec, the theme or build, a skill), and when another skill hands you a change to implement.
---

# Implement a change to the docs site

Make one change on one branch. An implementer agent evaluates the change and
either makes it or declines it, and then an independent auditor agent verifies
the result against the specs, sfmtool and a real run. The loop repeats until
the auditor finds nothing that needs rework. The coordinating session (you)
sets up the branch, launches the agents, and pushes when asked; it does not
write the change itself.

This is the site's copy of sfmtool's `skills/implement-change/SKILL.md`, with
the docs build, the shared run and the browser in place of the Rust and
Python suites. The implementer and auditor agents launched by this skill do
their work directly. They do not invoke this skill again.

Run **one agent at a time**. Agents share the checkout, its `site/`
directory, the `docs-serve` port and any SfM Explorer they launch; running
two at once makes their builds, edits and viewers collide. Launch every agent
without a model override, so it runs on the session's model.

## Inputs

Take these from the user's request, or from the skill that called this one:

- **The change.** What to change and why, where it applies (pages, specs,
  report findings, an sfmtool change the docs must follow), and what counts
  as done. A change that is too large for one agent to finish and check in
  one pass is split into steps first, and each step goes through this skill
  on its own.
- **A draft** (optional): a patch, a proposed sentence or a page someone
  already wrote. Pass its path or text to the implementer as a draft to
  verify, never as the answer.
- **The branch.** Either the branch already checked out, or a new branch to
  cut from `<base>/main`. When the checkout is on `main`, always cut a new
  branch. Pick a short descriptive name that no local branch and no branch on
  the upstream or fork remote uses.
- **Whether to push.** Push only when the user or the calling skill asks.
- **Task-specific instructions** (optional). Extra rules from the calling
  skill for the implementer and the auditor, such as how to record the outcome
  in a report. Pass them into both briefs in place of the
  `<task-specific instructions>` placeholder, or delete the placeholder when
  there are none.

## 1. Find the upstream and fork remotes

Do this when a new branch is cut or the branch is pushed. Skip it when the
calling skill already found the remotes and gave you `<base>` and `<fork>`.

Branches are created from the upstream repository's `main` (or the fork's,
when upstream cannot be fetched) and pushed to the user's fork, never to
upstream. Identify both remotes from their URLs:

```bash
git remote -v
gh api user --jq .login   # the user's GitHub login, if gh is signed in
```

- **Upstream** is the remote whose URL points at
  `sfmtool/sfmtool.github.io` on GitHub, in either form:
  `git@github.com:sfmtool/sfmtool.github.io.git` or
  `https://github.com/sfmtool/sfmtool.github.io(.git)`. It is often named
  `origin` or `upstream`.
- **Fork** is the remote whose URL points at a GitHub repository owned by the
  user, usually `<login>/sfmtool.github.io`. It is often named `fork`. When
  `gh` gives a login, the fork is the remote whose URL owner matches it.
  Without a login, a single GitHub remote other than upstream is the fork.

When no remote points at upstream, add one for fetching (named `upstream`,
or another unused name if `upstream` points elsewhere), in the URL form the
fork uses, and tell the user you added it. If upstream cannot be fetched, use
the fork's `main` as the base and tell the user before the first agent starts
that the branch may lack upstream's newer commits. If the fork is missing or
ambiguous and the branch is to be pushed, ask the user which remote to push
to. Never push to upstream.

Call the fork's name `<fork>`, and the remote whose `main` is the base
`<base>`. Give every agent the base remote's name, so that `<base>/main`
refers to the right ref. When working on an existing branch that was not cut
from `<base>/main`, give the agents the commit the branch's own work starts
from instead.

## 2. Set up the branch

For a new branch:

```bash
git fetch <base> main
git checkout -b <branch> <base>/main
```

For the current branch, check that the working tree is clean
(`git status --porcelain` prints nothing). If it is not, ask the user what to
do with the uncommitted changes rather than letting an agent commit them.

### The sfmtool checkout

The agents check every command, viewer word and output block against
sfmtool, checked out beside this repository as `../sfmtool`. Prepare it once,
before the first agent starts. The agents use it as it is: they do not update
or rebuild it.

- **Require it.** When `../sfmtool` is missing, ask the user where their
  sfmtool checkout is, or whether to clone
  `https://github.com/sfmtool/sfmtool` there. Start no agent without one.
- **Bring it to upstream `main`.** Its upstream is the remote whose URL points
  at `sfmtool/sfmtool`, found as in step 1. Fetch its `main` and compare
  `HEAD` with it. When `HEAD` is upstream `main`, use it. When the checkout
  is on its `main` branch, its working tree is clean and `HEAD` is behind
  upstream `main`, fast-forward it
  (`git -C ../sfmtool merge --ff-only <its upstream>/main`). Otherwise it
  holds the user's own work: do not switch its branch, reset it or stash it.
  Ask the user whether to run against it as it is, or against a worktree of
  upstream `main` in the scratchpad
  (`git -C ../sfmtool worktree add <scratchpad>/sfmtool <its upstream>/main`).
  A worktree builds its own Pixi environment and Rust targets, which takes a
  while, and its path takes the place of `../sfmtool` in the briefs and the
  [Checks](#checks). Remove it when the change is finished.
- **Build it**, every time, even when nothing was fetched: both sfmtool's
  Python extension, which `sfm` and `sfm explorer` run, and the
  `sfm-explorer` binary, which the agents' `viewer.py` launcher runs. Build
  them as sfmtool's `skills/gui-bug-bash/SKILL.md` § "1. Setup" step 2 says.
  sfmtool's `AGENTS.md` § "Things that can surprise you" says why the
  extension needs its own build (the entries on the native extension and on
  `sfm explorer`).
- **Pass it on.** Give the agents the checkout's path, its commit, and
  whether that commit is upstream `main`.

## 3. Implementer

Launch one agent with the [implementer brief](#implementer-brief) below, the
branch name, the base, the change, the draft if there is one, the sfmtool
checkout's path and commit, the [Checks](#checks) section pasted in place of
`<checks>`, and any task-specific instructions. Wait for it to finish before
doing anything else.

The implementer returns DONE or DECLINE. A decline is a valid outcome: the
change is wrong, already made, needs the maintainer's decision, or would cost
more than it is worth. When the task-specific instructions say how to record a
decline (for example a status line in a report), the decline is committed and
goes through the audit and push like any other change. Otherwise the
implementer commits nothing for a decline; skip the audit and report the
reason to the user.

## 4. Auditor

Launch a fresh agent with the [auditor brief](#auditor-brief) below, the
branch name, the base, the change, the sfmtool checkout's path and commit,
the same Checks section and the same task-specific instructions. Tell it
what the implementer said it changed and what it deliberately left out, what
it said to screenshot, and name the claims most worth checking (a command or
its output, a viewer word, a step followed over MCP, a theme behaviour
checked in a browser, anything the implementer says it inferred). For a
decline, tell it the implementer's decision and stated reason. Do not give
it the draft or any other part of the implementer's reasoning; it should
verify, not agree.

The auditor returns CLEAN or NEEDS-FIX.

- **NEEDS-FIX**: send the auditor's list back to an implementer (resume the
  original implementer agent if it is still available, otherwise a fresh one
  with the implementer brief's "later rounds" instruction), then audit again.
- **CLEAN, but the auditor changed more than its brief allows** (its
  "Audit fix:" commits rewrote a paragraph or a step, replaced a screenshot,
  or changed the theme or build, instead of SIMPLE sentence-level fixes): run
  one more audit round on those commits before accepting.
- **CLEAN** otherwise: go to step 5.

Between agents, check that nothing an agent started is still running: a
`docs-serve`, an `sfm` command or an SfM Explorer. On Linux and macOS use
`ps aux | grep -E 'zensical|sfm|sfm-explorer'`. On Windows, `ps aux` in Git
Bash lists only MSYS processes, so use
`tasklist | grep -iE 'python|zensical|sfm'` instead. An agent that left a
background command can report back late, after the next agent has started;
when that happens, check that the checkout holds only the current agent's
work.

## 5. Finish

```bash
test -z "$(git status --porcelain)"   # the agents commit their own work
git push -u <fork> <branch>           # only when asked to push
```

Push only once the checks the change requires have passed on the branch's
last commit. The auditor of the last round runs them before it returns
CLEAN. A check that did not run or failed blocks the push.

Report to the user, or return to the calling skill:

- the branch, and which remote's `main` it was cut from;
- the outcome (done or declined, and why), with the audit outcome (clean,
  number of simple audit fixes, a second audit round);
- the changes to pages and screenshots, separately from the spec and site
  edits (theme, build, skills);
- what to show in the PR, as the implementer and auditor agreed, and the
  screenshot links once they are taken;
- the checks run and their results;
- anything the agents noticed outside the change.

Do not open a pull request unless the user asks. When asked, launch one more
agent with the [screenshot brief](#screenshot-brief), after the audit and on
its own like the others, and open the pull request once it has returned the
image links. Every change to this repository except one to `specs/`,
`skills/`, `reports/` or `AGENTS.md` alone shows on the site, so its PR has
screenshots. Write the body with the sections the earlier PRs use:

- **Summary**: what the PR does and why, in one or two sentences.
- **Changes**: one bullet per file or group of files.
- **Testing**: the checks run, the commands run and on what, and the steps
  followed over MCP or in a browser.
- **Screenshots**: the pictures, as a table of before and after where
  something that existed changed. For a change with nothing on the site,
  `n/a` and what was checked.

End the body with the attribution lines the session gives, if any. PRs are
squash-merged.

## Checks

Paste this section into both briefs in place of `<checks>`. Choose the checks
by what the change touches, not only by the files it edits. They all run on
the branch's last commit.

- **Every change:** `pixi run docs-build` finishes with *No issues found* and
  the redirect script writes its pages without error. `site/` holds nothing
  from `specs/`, `skills/` or `reports/`, and no page lives under
  `docs/sfmtool/`.
- **A page, or anything on one:** the page still meets its spec in
  `specs/pages/` and the site spec's shared rules in `specs/README.md`
  (brevity, trimmed output, a caveat stated once, sentences that read
  easily). When the page's purpose changed, its spec changed in the same
  branch. A new page has a spec, a row in the site spec's table and an entry
  in `zensical.toml`'s nav.
- **A command or output block the change adds or alters:** run it for real
  and compare. An `sfm` command runs in the shared run (the Getting Started
  steps on a copy of `../sfmtool/test-data/images/dino_dog_toy` in the
  scratchpad, never in `test-data`), through sfmtool's Pixi environment
  (`pixi run --manifest-path ../sfmtool/pixi.toml sfm …` when run from the
  scratchpad); each flag appears in its `--help`. A command for another
  shell (PowerShell, a download) runs in that shell, in the scratchpad. An
  output block's lines, headings and columns match the run; counts and times
  that vary from run to run are not differences.
- **A step in SfM Explorer:** follow the text literally over the viewer's MCP
  endpoint, on a copy of the run's `.sfmr`, as `AGENTS.md` § "Steps that a
  person or an agent can follow" describes. Launch, drive and stop the viewer
  as sfmtool's `skills/gui-bug-bash/SKILL.md` § "Tools" describes, with its
  `viewer.py` and `sfm explorer-call`
  (`specs/cli/automation/explorer-call-command.md`); skip its build, which the
  coordinator did. Each bold viewer word is text the viewer shows, on screen
  or as a widget's name in `get_widgets` (`specs/gui/mcp-server.md`
  § "`get_widgets`"). An operation or argument you have to guess is a finding
  against the text.
- **A screenshot on a page:** taken from that run on copies of `test-data`
  in the scratchpad, with the viewer driven as sfmtool's
  `skills/implement-change/SKILL.md` § "Screenshots" steps 1, 2 and 4
  describe (without step 2's build), and placed, referenced and cropped as
  `AGENTS.md` says. Look at every image. Every file under an `images/`
  directory is referenced by some page.
- **The theme, `zensical.toml`, CSS or JavaScript:** the build does not check
  what these do, so open the built page in a headless browser
  ([Browser](#browser)) and check the behaviour the change is for, in the
  light and the dark scheme when it touches colours.
- **A link:** an internal link or `#anchor` resolves in the build; a link
  into sfmtool names a path that exists on its `main`.
- **A finding in `reports/`:** it has a dated status line, as `AGENTS.md`
  describes.
- **Commits:** every commit carries a DCO sign-off (`git commit -s`).

When `../sfmtool`'s `HEAD` is not its upstream `main`, say which commit the
runs used. Leave nothing running: no `docs-serve`, viewer or `sfm` command.

## Browser

A headless Chromium-based browser renders a built page for a check or a
screenshot: `msedge` on Windows (`/c/Program Files
(x86)/Microsoft/Edge/Application/msedge.exe` in Git Bash), `google-chrome`
or `chromium` elsewhere. Copy the built `site/` to the scratchpad and open
the copy with a `file://` URL; `pixi run docs-serve` cannot serve a page
with a script appended. Pass `--headless --hide-scrollbars
--user-data-dir=<scratchpad>/browser` every time, so the browser does not
use the person's own profile.

- **A page in a given state** (a tab selected, an attribute set): append
  `<style>*,*::before,*::after{transition:none!important}</style>` and a
  `<script>` that acts in a `setTimeout(…,300)` and then calls
  `document.activeElement.blur()`. Without them a picture catches a tab half
  switched, in its focus colour or without its underline.
- **What a page does:** `--virtual-time-budget=5000 --dump-dom <url>`, with
  the script writing the result into an element, then read that element from
  the dumped DOM. An element that is hidden, such as the content of a tab
  not selected, has no rendered text, so CSS does not apply to its
  `innerText`: select the tab first. `--dump-dom` lays the page out smaller
  than `--window-size` (976×708 for `1000,800` with Edge on Windows), so
  also write `innerWidth` and `innerHeight`, and enlarge the window until
  they equal the picture's `--window-size` before measuring.
- **A picture:** `--force-device-scale-factor=2 --virtual-time-budget=3000
  --blink-settings=preferredColorScheme=1 --window-size=W,H
  --screenshot=<file>.png <url>`, with `preferredColorScheme=0` for the dark
  scheme. Without the setting the browser takes the operating system's
  scheme, as the site does. `W` is 1000, or at least 1220 when the picture
  shows the left-hand nav: the theme hides the nav in a narrower window.
  Do not put a `#anchor` in the URL or scroll from the script: the picture
  comes out blank. For a part far down a page, have the script set
  `display:none` on every element before the part's heading (its
  `previousElementSibling`s, and those of each element that holds it, up to
  the page's `article`), so the heading is at the top. The header and the
  left-hand nav stay as they were, but **On this page** still shows the
  start of its list, with no entry marked: crop it out. Make the window tall
  enough to hold the part to show and crop it afterwards, at twice the CSS
  pixels that `getBoundingClientRect()` gives from a `--dump-dom` of the
  same copy: on Windows with PowerShell's `System.Drawing`
  (`$i=[System.Drawing.Bitmap]::FromFile(<in>)`,
  `$i.Clone((New-Object System.Drawing.Rectangle X,Y,W,H),$i.PixelFormat).Save(<out>)`
  after `Add-Type -AssemblyName System.Drawing`), elsewhere with ImageMagick
  (`magick <in> -crop WxH+X+Y <out>`). `--hide-scrollbars` also hides a code
  block's own scrollbar: when a line runs past the block's edge, the caption
  says that the block scrolls sideways. Look at the picture before using it.

## Screenshots

What the PR shows, as the screenshot agent takes it:

1. **What to show.** A page's new or changed screenshot is already in the
   branch: link it at the branch's commit on the fork, as
   `https://raw.githubusercontent.com/<fork owner>/sfmtool.github.io/<sha>/docs/<path>`,
   and the screenshot it replaced at `<base>/main`'s commit on upstream. A
   change to how a page reads or behaves (text, layout, the theme, a code
   block) is shown by a picture of the rendered page, cropped to the part
   that changed, taken with the [Browser](#browser) from the built `site/`.
2. **Before**, when something that already existed changed: build
   `<base>/main` in a worktree in the scratchpad (`git worktree add
   <scratchpad>/before <base>/main`, then `pixi run docs-build` there) and
   take the same picture of it. Remove the worktree afterwards.
3. **Privacy.** Look at every PNG before using it: no local path, username
   or personal data may show, including a `file://` address.
4. **Hosting.** Pictures of the rendered page go in one orphan commit
   "Screenshots for <branch>" on a `pr-<branch>-screenshots` branch of the
   fork, built without touching the checkout:

   ```bash
   tree=$(for f in <dir>/*.png; do
     printf '100644 blob %s\t%s\n' "$(git hash-object -w "$f")" "$(basename "$f")"
   done | git mktree)
   sha=$(git commit-tree "$tree" -m "Screenshots for <branch>" \
     -m "Signed-off-by: $(git config user.name) <$(git config user.email)>")
   git push <fork> "$sha:refs/heads/pr-<branch>-screenshots"
   ```

   Link each one as
   `https://raw.githubusercontent.com/<fork owner>/sfmtool.github.io/<sha>/<file>.png`.
   PR #14's Screenshots section is an example.
5. Stop any `docs-serve`, browser or viewer started.

## Implementer brief

> You are implementing ONE change in the sfmtool.github.io repository, on the
> branch already checked out. You are the only agent running, so building,
> serving the site and running sfmtool are allowed. Do not invoke the
> `implement-change` skill; you are the implementer it launched. Read
> `AGENTS.md` first (the writing style and the rules for steps), then
> `specs/README.md` (who the site is for, each page's type, the shared rules)
> and the spec in `specs/pages/` of every page you change. Use the terms in
> `../sfmtool/specs/GLOSSARY.md`. The code, its specs and its `--help` are in
> `../sfmtool`, at commit `<sfmtool commit>`, built by the coordinator; do
> not update or rebuild it.
>
> **The change:** <the change>
>
> **Draft:** <the draft's path or text, or "none">
>
> <task-specific instructions>
>
> **Evaluate, then implement or decline.** Check the change against the
> pages, the specs and sfmtool: that the problem it addresses exists, and that
> the approach fits the site. Decide DONE or DECLINE. Decline when the change
> is wrong, already made, needs the maintainer's decision (a page's purpose,
> the site's structure, a passage a page spec marks author-owned), or would
> cost more than it is worth, and explain why. Where a page cannot be written
> truthfully because the viewer or a command breaks a rule (a control whose
> name lacks its visible text, say), do not write around it: name the problem
> to report in sfmtool. Record a decline as the task-specific instructions
> say; when they say nothing, commit nothing and explain.
>
> **If implementing:** make a minimal change, for this change only. A draft
> you were given, and any proposed sentence or command, is a draft: verify
> every word, command and output line against sfmtool or a real run before
> using it. Change a page's spec in the same branch when its purpose changes,
> and the site spec when a shared rule changes. When moving or renaming a
> heading, fix every link and `#anchor` that pointed at it. Take every
> screenshot from a real run on copies of `test-data`, as `AGENTS.md` says.
> Commit with a plain-language message, signed off (`git commit -s`), with no
> attribution lines. Do not push.
>
> **Later rounds:** if you are given an auditor's findings, fix each one or
> explain precisely why it is wrong, commit, and change nothing else.
>
> <checks>
>
> **Final answer:** DECISION (DONE or DECLINE, and for a decline which kind),
> a short rationale, SHOW (what the PR's screenshots should show: the page
> images the change adds or replaces, and the parts of rendered pages that
> look or behave differently, with whether a before picture is needed; or
> `n/a` and why nothing shows on the site), files changed, commits
> (`git log --oneline <base>/main..HEAD`), the checks run and their results,
> what you ran for real and on what, and anything you noticed outside the
> change.

## Auditor brief

> You are independently auditing a change committed on the branch checked
> out in the sfmtool.github.io repository. You did not write it. You are the
> only agent running, so building, serving the site and running sfmtool are
> allowed. Do not invoke the `implement-change` skill; you are the auditor it
> launched. Read `AGENTS.md` first, then `specs/README.md` and the spec in
> `specs/pages/` of every page the change touches. The code, its specs and
> its `--help` are in `../sfmtool`, at commit `<sfmtool commit>`, built by
> the coordinator; do not update or rebuild it.
>
> **The change that was asked for:** <the change>
>
> <task-specific instructions>
>
> 1. Read the diff (`git diff <base>/main...HEAD`) and the commit messages,
>    and the files the change was about as they stand on `<base>/main`.
> 2. If the implementer declined the change, check the decline itself: that
>    the change really is wrong, already made, or needs the maintainer, as
>    claimed. A decline you can show is mistaken is SUBSTANTIVE.
> 3. Verify every factual claim in the change yourself: each command and
>    flag, each output line, each viewer word, each link and anchor, each
>    count, and what each screenshot shows. Run the commands and follow the
>    steps; do not take the implementer's run on trust. For removed or moved
>    text, compare it with the original and confirm no fact that is still true
>    was lost. Check that the change does what was asked, stays in scope,
>    keeps each page's spec and the site spec in step with the pages, and
>    follows `AGENTS.md` and the site spec's shared rules (plain, literal
>    language; the viewer's exact words in bold; brevity; a caveat stated
>    once). Read every changed sentence for how it reads. Check the
>    implementer's SHOW answer against the diff.
> 4. Run the checks below that the diff requires, on the branch's last
>    commit, after any "Audit fix:" commits of your own. A failing check is
>    SUBSTANTIVE unless the fix is SIMPLE. If you already have a SUBSTANTIVE
>    finding, you may skip the long checks (the shared run, a walk over MCP),
>    since the next round's auditor runs them; say which you skipped. Never
>    push.
> 5. Classify each issue:
>    - **SIMPLE**: a wrong count, a wording or style slip, a broken link, a
>      wrap, a small factual correction in a sentence, missing alt text. Fix
>      these yourself and commit, signed off (`git commit -s`), with a
>      message starting "Audit fix:".
>    - **SUBSTANTIVE**: the change is wrong in a way that needs rework (a
>      command that fails or prints something else, a step that cannot be
>      followed as written, a screenshot that does not match the run or shows
>      a local path, a page that drifts from its spec, scope creep, a change
>      that does not do what was asked). Do not fix these; describe each
>      precisely, with evidence.
>
> <checks>
>
> Leave nothing running. **Final answer:** VERDICT = CLEAN (no issues, or
> only SIMPLE ones that you fixed) or NEEDS-FIX (one or more SUBSTANTIVE
> issues, listed). Then SHOW (correcting the implementer's answer if it was
> wrong), the issues, what you fixed, and the check results. Be concise.

## Screenshot brief

> You are taking the screenshots for a change committed on the branch checked
> out in the sfmtool.github.io repository, for its pull request. You are the
> only agent running. Do not invoke the `implement-change` skill. Read
> `skills/implement-change/SKILL.md` § "Screenshots" and § "Browser", and
> follow them. If the branch does not have that file, the coordinator pastes
> both sections below.
>
> **The change:** <the change>
>
> **What to show:** <the SHOW answers of the implementer and auditor>
>
> The base is `<base>/main` and the fork remote is `<fork>`. Change nothing
> on the branch and leave the checkout as you found it.
>
> **Final answer:** for each picture, its link and a one-sentence caption
> saying what it shows and in what state, and the `pr-<branch>-screenshots`
> commit if you made one. Leave no server, browser or worktree behind.
