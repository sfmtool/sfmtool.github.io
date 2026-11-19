---
name: audit-docs
description: Audit the documentation pages under docs/ against their specs in specs/ (each page's spec and the site spec's shared rules on brevity, trimmed output, caveats and links) and against sfmtool main (commands, viewer words, output from a real run on copies of test-data), and write a dated report of verified findings to reports/. Use when the user asks to audit or review the docs, check them for drift or verbosity, or find what the next docs refresh should fix.
---

# Audit the docs against their specs and sfmtool

Compare each page under `docs/` with its spec in `specs/pages/`, with the
shared rules in `specs/README.md` (the site spec) and with sfmtool `main`, and
write one report. The code, its specs and its `--help` are in the `sfmtool`
repository, checked out beside this one as `../sfmtool`. This skill is
read-only: it changes no page, spec or code.

## Scope

The audit runs at two depths, as sfmtool's `audit-specs` does:

- **Every page, mechanically.** The checks under "Mechanical checks" run over
  the whole site on every run. They are cheap, and they are the evidence that
  covers a page no one read this run.
- **A sample, deeply.** Each sampled page is read against its spec, the site
  spec and sfmtool, and its commands are run (see "The shared run").

### Choosing the sample

While the site has at most eight pages, every page is read in full. Above
that, read eight, in this order:

1. Pages the user names.
2. Pages with a mechanical hit (below): a missing spec, a broken link or image,
   an output block over its limit, a repeated caveat, a command or viewer word
   not found in sfmtool.
3. Pages whose sfmtool sources changed since the last audit: the commands and
   viewer specs a page's spec links, checked with `git log --since=<last audit
   date>` over those paths in `../sfmtool`.
4. A seeded draw from the pages audited least recently. Prior coverage comes
   from the `### docs/…` headings of earlier audit reports, which are the
   reports under `reports/` with such a heading:

```bash
w=$(mktemp -d); SEED=${SEED:-$RANDOM}; N=8   # record SEED in the report
find docs -name '*.md' | sort > "$w/all.txt"
grep -hoE '^### docs/[a-zA-Z0-9/_.-]+\.md' reports/*.md 2>/dev/null \
  | sed 's/^### //' | sort -u > "$w/done.txt"
comm -23 "$w/all.txt" "$w/done.txt" > "$w/pool.txt"   # never audited first
[ -s "$w/pool.txt" ] || cp "$w/all.txt" "$w/pool.txt"
shuf -n "$N" --random-source=<(yes "$SEED") "$w/pool.txt"
```

Report the seed, the pool and the pages read.

## What to check

1. **Purpose drift.** The page does a different job from the one its spec
   states: a tutorial that has grown into reference, a how-to guide that
   teaches, a second walkthrough of what another page covers. Quote the part
   that drifted and name the page or sfmtool spec it belongs in.
2. **Content the spec leaves out.** The page includes something the spec's
   "Leaves out" list sends elsewhere. Name where it lives.
3. **Missing key points.** The page lacks a step, an outcome, an output or a
   screenshot that the spec says it has, or the reader cannot reach the
   stated "Afterwards" from the text.
4. **Brevity rules** (site spec § "Shared rules"): an output block not trimmed
   to the lines the text refers to; an explanation of an output line the
   reader neither acts on nor might take for an error; a caveat stated on a
   page other than its home; prose that describes what the next screenshot
   shows. Quote the text and give the shorter version.
5. **Wrong facts.** A command, flag, menu, panel, column or status text that
   sfmtool `main` does not have or spells differently; an output block whose
   lines or layout differ from a real run; a screenshot that no longer
   matches the viewer. Numbers that vary from run to run are not findings;
   a changed line format, heading or column is.
6. **The `AGENTS.md` rules**: plain language, the viewer's exact words in
   bold, an operation named with each gesture, something to check at the end
   of each step, nothing named by a point ID.
7. **Specs and pages out of step**: a page with no spec, a spec with no page,
   a page missing from the site spec's table or from `zensical.toml`'s nav,
   a spec type that disagrees with the table or with the page's section in
   the nav.

Weigh a finding by what a reader would do wrong believing the page: a command
that fails outranks a paragraph that is too long.

## How to work

### The sfmtool checkout

Before any check, run or agent, prepare `../sfmtool` once, as
`skills/implement-change/SKILL.md` § "The sfmtool checkout" says: require it,
bring it to upstream `main` and build it. The agents below run in parallel on
that checkout as it is; they do not update or rebuild it.

### Mechanical checks

Run these over every page and cite the numbers, including zeros.

1. **Pairing.** Each `docs/**/*.md` against `specs/pages/<name>.md`, the site
   spec's table and the nav in `zensical.toml`.
2. **Build.** `pixi run docs-build`; report its warnings (broken links and
   missing images among them), and confirm `site/` holds nothing from
   `specs/` or `skills/`.
3. **Images.** Every image a page references exists, has alt text, and every
   file under an `images/` directory is referenced by some page.
4. **Size.** Words per page, lines in fenced output blocks per page and the
   longest block, against the previous audit report's figures, so growth
   shows.
5. **Repeated text.** Normalized sentences that appear on more than one page,
   and the run-to-run caveat (`grep -n "differ"`) outside its home page.
6. **Commands.** Every `$ sfm …` line and every `sfm …` in a code span: the
   subcommand is listed by `pixi run sfm --help`, or for one in a group
   (`ws init`, `camrig create`) by `pixi run sfm <group> --help`, and each
   flag appears in `pixi run sfm <command> --help`, all run in `../sfmtool`.
7. **Viewer words.** Every bold term on a GUI page, searched for in
   `../sfmtool/crates/sfm-explorer/src`. A term not found there is a lead,
   not yet a finding: read the viewer or walk the step to settle it.
8. **Status of sfmtool.** Note the commit the prepared checkout is at
   (`git -C ../sfmtool rev-parse --short=8 HEAD`) and whether it is upstream
   `main` (`<upstream>/main`, where `<upstream>` is the remote whose URL
   points at `sfmtool/sfmtool`).

### The shared run

Factual checks of output and screenshots use one run, as the site spec says
pages are made: the Getting Started steps on a copy of sfmtool's
`test-data/images/dino_dog_toy`, in a scratch directory, never in
`test-data`. Run the commands of every sampled page from that workspace with
`pixi run --manifest-path ../sfmtool/pixi.toml sfm …`, and compare each page's
output blocks line by line for format, headings and columns. For a sampled
GUI page, open a copy of the run's `.sfmr` in a viewer launched and driven
as sfmtool's `skills/gui-bug-bash/SKILL.md` § "Tools" describes, and follow
the page's steps literally, as `AGENTS.md` describes; an operation the text
does not let you find is a finding under check 6.
Compare what the viewer shows with each screenshot. Do not replace any
screenshot.

### Agents

Run the mechanical checks and the shared run yourself first. Then dispatch one
`Agent` subagent per sampled page, in parallel. Give each the page, its spec,
the site spec, `AGENTS.md`, the mechanical hits for its page, the shared run's
directory and command outputs, and the "What to check" list. Each returns its
page's section in the report shape below, with the evidence for each finding:
the quoted page text, and the sfmtool file and line, `--help` text or run
output that contradicts it.

### Verification

Before a finding goes in the report, check it yourself: re-read the quoted
text in the page, re-run the command or re-grep the viewer source it cites.
Drop a finding whose evidence does not hold, and drop one already open in
another report under `reports/` (cite that report instead). A finding states a
fact about the page and the evidence for it; never write a claim for a
reviewer to confirm.

## Report format

Open with a **Sample** block:

```
**Sample:** N of M pages read in full. Seed `<seed>` (or "every page"). Pulled
in: <pages and why>. sfmtool at `<commit>` (upstream `main`, or what it is
instead). The mechanical checks below cover all M pages.
```

Then **Mechanical findings**: the numbers of each check, with a table of one
row per page (words, output lines, longest block, images, spec, nav).

Then one section per page read, with the heading `### docs/<path>` exactly
(the sampler greps for it), and its findings numbered within the section:

```
### docs/<path>

**Spec:** specs/pages/<name>.md (<type>). **Recommendation:** <change the
page | change the spec | discuss>, one line why.

1. **<short title>** (check <n>). <What is wrong and where: the quoted page
   text or the section number.> <The evidence: an sfmtool path, `--help`
   text or a line of run output.> <What the spec or site spec asks.>
   Proposed: <the shorter or corrected text, or where the content moves>.
```

A finding is referred to as `docs/<path>` finding `<n>`, and its status lines
go directly under it.

Read every sentence of a page for how it reads, not only for its words, as
the site spec's "Sentences that read easily" asks: a sentence a reader must
re-read to parse (an inverted relative clause, the verb held back to the end,
an aside between subject and verb, two ideas compressed into one) is a
finding, with the rewritten sentence as the proposed fix.

A finding on a passage the page's spec names as **author-owned** is a
suggestion only: say what looks improvable and give the proposed text, marked
`Suggestion for the maintainer`, and never edit the passage or propose it as a
fix for another session to make.

A page that is right and its spec wrong (the spec describes a job the page no
longer needs to do) is **change the spec**; a page that drifts from a spec the
maintainer still wants is **change the page**.

Then **Specs and pages** (check 7's pairing table), and end with **Top
priorities**: the three to five fixes that most change what a reader gets
right. Keep the report under about 400 lines.

## Saving the report

Write it to `reports/<date>-docs-audit.md`, with `<date>` from `date +%F`, and
do not overwrite an earlier report. Findings are marked off in place with a
dated status line, as `AGENTS.md` describes, and naming the PR or branch:
`> _Status (YYYY-MM-DD): **Done** — <what changed>, PR #<n>._` (also
`Partially done`, `Not done`, `Declined` with the reason, `Needs decision`
naming the choice). A run that read every page carries each still-open finding
of the previous audit report (the newest report under `reports/` with a
`### docs/` section, whatever its name) into its own, with its status lines, and
deletes the previous report in the same commit; a sampled run leaves the
previous report in place, since it holds the only reading of the pages this
run skipped. After saving, give the user the path and the top priorities.

## Guidelines

- Quote the page and cite the evidence (an sfmtool path and line, the
  `--help` text, a line of run output). "The page is out of date" is not a
  finding.
- Never call a page consistent because it was not read; say "N of M read".
- The site spec's rules and the page specs are the standard. A page that
  meets them is not a finding, however differently you would have written it.
  A rule that seems wrong is a proposal to change the spec, stated as such.
- Report findings in plain language, as `AGENTS.md` asks of the pages.
