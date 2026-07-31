---
status: ok
seed: 17
fetched: 2026-07-31
rungs: R2 api.github.com (the ONLY seed in session scope — full authenticated #git) ·
       R1 raw.githubusercontent (file bodies, pinned by SHA)
frozen-at: 6c1763a3 — head of the repository's default branch, which PRE-DATES every
       commit this run has made. seed 17 is the run's own home; pinning to this SHA is
       what keeps the run from citing material the run itself is writing.
---

# anselmetbrl/skill-construction

    url          https://github.com/anselmetbrl/skill-construction
    description  #void — the repository's About field is null (R2). there is no
                 one-line self-description anywhere in the repo.
    site         #void — homepage null (R2)

## #git

    ── seed 17 is the one repo where the authenticated API answers, so these fields are
       exact rather than page-scraped, and the fields that are VOID elsewhere in this
       run are actually PRESENT here. ──

    stars          0                       (R2)
    forks          0                       (R2)
    watchers       0                       (R2, subscribers_count)
    license        #void — license null (R2). no LICENSE file at root.
    open-issues    0                       (R2)
    releases       NONE — the releases endpoint returns an empty array (R2)
    tags           NONE — the tags endpoint returns an empty array (R2)
    created        2026-07-29T17:04:58Z    (R2)
    pushed         2026-07-31T15:47:17Z    (R2)
    age-at-fetch   2 days
    commits        47 on the default branch (R2, Link-header last page at per_page=1)
    branches       6, ALL agent-generated names (R2):
                   claude/bootstrap-github-repo-ga6flk · claude/bootstrap-github-repo-zk4iwr
                   claude/holistic-meta-index-ffge4u   · claude/holistic-meta-index-sw3uem
                   claude/llm-prompt-engineering-40bttw · claude/llm-prompt-engineering-w6jxv2
    default-branch claude/llm-prompt-engineering-40bttw — an agent-generated branch name
                   is the repository DEFAULT. recorded as a fact.
    archived       false                   (R2)
    language       null (R2) — GitHub detects no programming language
    topics         none                    (R2)
    lang-roles     markdown ONLY. no manifest of any kind at root (R1 sweep, phase 2).
                   nine files, all prose:
                     CLAUDE.md 9,658 · spec.md 23,515 · ledger.md 63,650 ·
                     vocabulary.md 6,491 · bootstrap.md 4,705 · bootstrap-build.md 3,727 ·
                     indexing_autoinfo_hg_v0.1.md 14,575 ·
                     complementarcontextualizinginformations_extractedfromchat.md 27,008 ·
                     .claude/skills/holistic-meta-index/SKILL.md 11,123
    README         ABSENT — raw README.md returns 404 (R1 sweep). the only seed of 25
                   with no readme. this is why its span bank below comes from spec.md,
                   CLAUDE.md and vocabulary.md instead.
    deep-links     spec    <base>/spec.md
                   claude  <base>/CLAUDE.md
                   ledger  <base>/ledger.md
                   vocab   <base>/vocabulary.md
                   skill   <base>/.claude/skills/holistic-meta-index/SKILL.md
                   where <base> = https://raw.githubusercontent.com/anselmetbrl/skill-construction/6c1763a3

## spans — verbatim quote bank (R1 at the pinned SHA)

    S1  "# spec — holistic-meta-index, v1"                              ← spec.md
    S2  "> **the name.** `holistic-meta-indexing_of_multi-project-research_as_dataset-
         graph_for_human-attention` / > four modules — ACT · OBJECT · FORM · PURPOSE.
         `-` binds a compound, `_` marks a module boundary. invocation handle:
         `holistic-meta-index`."                                        ← spec.md
    S3  "> **what this is.** a declarative v1 spec for a pipeline that turns a
         hand-curated list of github repos into a navigable meta-index giving BIRD'S-EYE
         orientation. one file. syntax-agnostic. the WHAT; `CLAUDE.md` holds the
         HOW-to-work-with-the-user."                                    ← spec.md
    S4  "## 0 · root — orientation, not substitution / > the purpose every node below
         serves. the index gives POSITION and ACCESS. the user still reads the repos
         themselves."                                                   ← spec.md
    S5  "why    the bottleneck is attention and access, not storage         (R9 R10) /
         reading repo-by-repo yields only depth, never position — position exists only
         in the collection"                                             ← spec.md
    S6  "[S4]  sharpened by the test run: position is not delivered BY the agent — it
         emerges IN the user, at a co-construction session; the index RECORDS the
         position taken. see ledger S4-S5."                             ← spec.md
    S7  "> **audit before trusting.** a blueprint to BUILD FROM and to DISTRUST.
         source-refs (`A7`, `R9`, `S2.8`, `v0.1 L177`) point back to `ledger.md` and the
         original mess — trace them, don't take them. the map is not the territory."
                                                                        ← spec.md
    S8  "> **how to read it.** one node per claim, named by what it does. keys are
         aligned, atomic, foldable. each node folds into a **falsification**: / -
         `moderation(~invalidation)` — when this decision becomes mistaken. / -
         `modification(~verification)` — how to re-read, what nuance recontextualises it
         then."                                                         ← spec.md
    S9  "nodes **cross-link by name** (`links`), not by id. hierarchy is a reading-view;
         the real shape is a graph."                                    ← spec.md
    S10 "### capture-over-judge — gather wide, decide nothing while gathering / why
         judgment at fetch-time silently discards what a later pass would need"
                                                                        ← spec.md
    S11 "### evidence-over-verdict — describe what IS, quote-grounded; refuse the verdict
         / why  the index orients; it never ranks or judges on the user's behalf"
                                                                        ← spec.md
    S12 "# CLAUDE.md — stance for co-(de)constructing with this user / > **what this
         is.** a standing stance for how to work with this user, auto-loaded each
         session. written TO you, the model. it governs HOW you act — not WHAT is
         built."                                                        ← CLAUDE.md
    S13 "## 0 · root — self-humility / > the repo-lens turned inward. LLMs are
         pre-designed with marketing biases; distrust your own hype first."
                                                                        ← CLAUDE.md
    S14 "each node is named `meta-<quality> · virtue over/against vice` … `over/against`
         is a **lean, not a law** — the vice is sometimes legitimate and needs
         awareness."                                                    ← CLAUDE.md
    S15 "> **audit before trusting.** this file is a blueprint to build from AND to
         distrust. it is not finished."                                 ← CLAUDE.md
    S16 "# vocabulary — the generative root-language (complementary sensemaking module)"
                                                                        ← vocabulary.md
    S17 "> **the reframe.** this is not a repo-tag whitelist (that stays deferred). it is
         a generative meta-language: `term = prefix(es) · ROOT · suffix`. so this module
         heals the GRAMMAR — roots + affixes + rule — not the saturated word-dump.
         distilling words chases infinity; distilling the generator is finite."
                                                                        ← vocabulary.md
    S18 "term   =   prefix(es) · ROOT · suffix / example    re · con · STRUCT · ion   =
         again + together + build + (act/result of)"                    ← vocabulary.md
    S19 "> families EMERGE from meaning; they are not the empty 4×4 grid (that stays
         unfilled). roots overlap families on purpose — that overlap is the heterarchy,
         not a defect."                                                 ← vocabulary.md
    S20 "> **read it as a scaffold to CORRECT.** the meanings below are STANDARD Latin
         etymology. your idiolect may assign a root a different essential sense — yours
         wins."                                                         ← vocabulary.md
    S21 "- as repo-TAGS this vocabulary stays deferred (A18). here it lives only as the
         meta-language — for your thinking, and for the model's grasp of your idiolect."
                                                                        ← vocabulary.md
    S22 "- the original file is unchanged. this module only references it."
                                                                        ← vocabulary.md

## potential-relation spans — collected, NOT resolved

    NONE. no span in this repo names any other project — inside this collection or
    outside it. its references point exclusively at its OWN files (spec.md, ledger.md,
    CLAUDE.md, indexing_autoinfo_hg_v0.1.md) and at internal source-refs (`A7`, `R9`,
    `S2.8`). the repo is entirely self-referential in its citations.
    → 0 edge candidates. said plainly rather than manufactured.

## flags-raw — what fetch itself revealed

    thin?          NOT thin in prose — 164 KB of markdown across nine files. but thin in
                   every conventional repo signal: no README, no license, no
                   description, no topics, no releases, no tags, no detected language,
                   0 stars / 0 forks / 0 watchers / 0 issues, 2 days old. the two
                   readings are both true and are recorded together.
    index-repo?    no. it is a spec-and-ledger repo for one skill, not a list of others.
    archived/moved no. archived=false, pushed 2026-07-31.
    SELF-REFERENCE  this seed is the home of the skill executing this run, and one of its
                   six branches is the branch this run is committing to. its dossier is
                   pinned to 6c1763a3 so that nothing this run writes can become
                   evidence about this run's own subject. flag F1 from phase 1 is
                   therefore RESOLVED-BY-CONSTRUCTION for the fetch phase — but whether
                   the seed belongs in the INDEX at all remains the user's ruling,
                   still unanswered, still defaulting to "in".
    note-for-gist  NO PROMOTIONAL REGISTER ANYWHERE. the repo's own documents instruct
                   the reader to distrust them: "a blueprint to BUILD FROM and to
                   DISTRUST" (S7), "this file is a blueprint to build from AND to
                   distrust. it is not finished" (S15), "the map is not the territory"
                   (S7). recorded as a fact about the material.
    note-for-gist  the default branch carries an agent-generated name, and all six
                   branches do. recorded as a fact about how the repo was produced.
    note-for-gist  ledger.md is 63,650 bytes — the largest single file in the repo and
                   larger than any readme fetched in this run. it was NOT read in full
                   here; only spec.md, CLAUDE.md and vocabulary.md were read end to end.
                   any gist claim needing a ledger span must re-fetch it into a new
                   record first. stated so the gap is visible rather than assumed away.
