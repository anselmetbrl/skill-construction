---
name: holistic-meta-index
description: Turn a hand-curated list of GitHub repos into ONE navigable meta-index — co-constructed, never batch-authored. The agent batches span-level evidence (frozen dossiers, quote+link-grounded gists, harvested relation quotes, machine-checked counts); the user rules every set-level judgment (tags, relations, order, emergence) in a working session; the index RECORDS the position the user took, with the evidence arranged. Invoked explicitly by name. Full name — holistic-meta-indexing_of_multi-project-research_as_dataset-graph_for_human-attention.
---

# holistic-meta-index

> **orientation, not substitution.** the index gives POSITION and ACCESS. the user still
> reads the repos. and position is not delivered BY the agent — it emerges IN the user,
> at the session; the index RECORDS the position taken, with the evidence arranged.

> **the root constraint (ledger S4).** an LLM cannot reliably make SET-LEVEL judgments —
> what partitions a collection, what is relevant, what emerged, whether its own output is
> good — and cannot police itself on them. asked anyway, it produces the APPEARANCE of
> the judgment. this skill is shaped so it is never asked.

---

## 0 · the governing line — span vs set

    span-level    a claim resolvable to a SPAN in frozen material: transcribe · select
                  quote+link · count · pattern-flag · arrange · render.
                  checkable by machine or by the user cheaply.  → the AGENT's territory.
    set-level     a property of the whole collection: partition · relevance · relation ·
                  emergence · quality. no span resolves it; its producer cannot check it.
                  → the USER's territory. the agent only EXHIBITS, PROPOSES, RECORDS.

    three modes   batch    phases 1-4 · agent alone · span-level ONLY · machine-checked
                  session  phase 5    · together · every set-level judgment RULED by the user
                  render   phases 6-7 · mechanical compile from rulings · user sample-audit

read `references/checks.md` FIRST — the batch is written to pass countable checks, so
know them before producing anything. check output is an EXHIBIT shown to the user,
never a gate that silently passes.

---

## 1 · the contract

    in            a list of github links · plus an optional contextual prompt
    query         ONE standing query, given by the user
    scale         ~100 typical · ~300 maximum. the batch scales flat; the SESSION cost
                  grows with the collection — that is the accepted price of the user's
                  sovereignty, and still orders cheaper than reading raw repos. chunk it.
    out           `INDEX.md` — the deliverable · `EMERGE.md` — the spoken companion
    pre-curation  the user's own act. it stays manual. seed ORDER is the user's own
                  signal — preserved through the whole batch.

### the run tree

    runs/<run-id>/                   run-id = <date>-<slug> · each run standalone
        seeds.md                     the list as given + the classification pass
        dossiers/<owner>__<repo>.md  raw · FROZEN · carries `status:`
        gists/<owner>__<repo>.md     selected spans · recompilable · working material
        workbench.md                 the exhibits + the check-report — session input
        rulings.md                   the user's judgments, verbatim-faithful — OUTRANKS
                                     everything inferred · the session's resume-state
        INDEX.md                     compiled from rulings + gists · standalone
        EMERGE.md                    compiled from ACCEPTED observations only

### four layers, decreasing fixity

    raw       dossiers            FROZEN — a wrong one is re-fetched as a NEW record
    inferred  gists · harvest · exhibits · proposals     recompilable
    ruled     rulings.md          the USER's — outranks all inferred content
    rendered  INDEX · EMERGE      mechanical re-renders of ruled + inferred

---

## 2 · invariants — stated once, held everywhere

    capture-over-judge      fetch wide, decide nothing while gathering; every filter is
                            a LATER act. capture wide, STORE lean.
    claims-resolve-to-spans every claim carries `← "quote" (link)` into frozen material,
                            or it IS `#void`. a paraphrase without a span is authorship,
                            not evidence — forbidden. machine-checked (C1).
    void-over-hallucination `#void` is an OUTCOME. never pad a slot. the void tally is
                            REPORTED as an exhibit, never judged into a score.
    you-do-the-reading      no sub-LLM delegation, ever. and the same guard runs UPWARD:
                            you read and select — you do not conclude on the set. the
                            set is the user's. exporting their judgment to yourself is
                            the same exportation one level up.
    failures-stay-visible   blocked/private/rate-limited → flagged with reason, link
                            preserved, IN the final index. silent skipping cannot be
                            audited.
    signal-over-saturation  the user's attention is the scarce resource. atomic lines,
                            chunked exhibits, one focus per message at the session.
    display-not-comparison  counts (stars, forks, issues) appear ONLY in glance lines.
                            never in prose, never compared, never even to deny comparing.
                            machine-checked (C4).

---

## 3 · the run — seven phases

### batch — agent alone, span-level only

**phase 1 · seeds**
    do        classify every link BEFORE fetching. flag+skip accidental index-repos
              (awesome-lists) — never rabbithole into members. a seed that IS an
              index-repo and is itself the artifact → flag and ASK.
    out       `seeds.md` — every link, its classification, seed order preserved

**phase 2 · fetch** — load `references/fetch.md`
    do        one frozen dossier per repo. thread 1 by 1, SEQUENTIALLY. never recurse
              into codebase subdirectories — tree-shape for language ROLES only.
    ladder    plain → stealth → alternative → flag · 2 attempts per rung · record the
              rung that worked
    gate      evidence, not interpretation. missing → `#void`/`unknown`, never invented.
    pause     **fetch complete → report, AWAIT the user's proceed. DO NOT TERMINATE.**

**phase 3 · gist** — load `references/gist.md`
    do        one repo at a time, from its dossier alone. spine FIXED (what / why / how →
              technology · technicality) · leaves EARNED. every line
              `claim ← "quote" (link)` or `#void — reason`.
    harvest   relation-quotes into a `#graph-harvest` block, verbatim + link. do NOT
              resolve, do NOT relate — that is exhibit material.
    flags     impartially, each WITH its quote: hype · seo/ai filler · abandonment ·
              fake/weak contribution · paywall-sabotage (`unfree?`) · contradictions.
              RECORD; the user weighs.

**phase 4 · workbench** — load `references/workbench.md`
    do        compile the exhibits, in seed order: whole-view one-liners · grounded tag
              candidates · name-resolved relation candidates · the flag roster · an
              order-proposal marked [proposal] · the check-report (C1-C8).
    gate      run every check. violations are fixed or listed — never waved through.
    commit    the batch ends checkpointed. everything after this line is co-work.

### session — together, where every set-level judgment lives

**phase 5 · session** — load `references/session.md`
    do        walk the exhibits with the user, ONE family per message, chunked.
              everything you offer is [proposal] with grounding attached — recommend
              when unsure, never a bare menu. the user rules: accept · edit · reject ·
              add. record every ruling verbatim in `rulings.md`.
    ruled     the ≤12 tags and each repo's ≤4 · every relation edge (2 types — a third
              is proposed to the user, never coined) · the index order (default: seed
              order) · which emerge-observations are true enough to speak.
    caps      4/12 discipline the PROPOSALS. the user may break a cap — record that
              they did. the cap is theirs.
    pace      the user's. multiple sittings are normal — `rulings.md` is resume-state.

### render — mechanical, then audited

**phase 6 · render** — load `references/render.md`
    do        compile INDEX.md from rulings + gists: flat list · ruled order · each repo
              once · glance (facts only) · always-visible tag line · #git / #gist /
              #graph unfolds · blocked repos in. compile EMERGE.md from ACCEPTED
              observations only — TTS prose, atomic paragraphs, says LESS if little
              was accepted.
    gate      standalone — zero pointers to run files (C5). re-run all checks.

**phase 7 · audit**
    do        the user picks the sample — never the agent. re-resolve every claim in
              those entries against the frozen dossiers. report misses with the failing
              line, fix, re-count. then close: commit, deliver INDEX + EMERGE.

---

## 4 · discipline

    checks    countable properties only (references/checks.md). run at each phase exit.
              output is shown, never self-graded. NO self-judgment of artifact quality —
              that ritual always passes; it did (ledger S4.1).
    commit    git-checkpoint every phase boundary + every ~10 repos inside a long phase.
              if `runs/` sits under no git repo, `git init` it.
    resume    mark before work, mark after outcome, save atomically. `status: ok` → skip ·
              `partial`/`rate-limited` → redo that one, overwrite in place. never wipe
              intermediate work. `rulings.md` resumes the session.
    on failure  fix in place or revert that unit under git and retry. the failure AND
                its resolution stay visible.

---

## 5 · when this skill is wrong — seeds, evolvable

    - a claim genuinely needs a span from OUTSIDE the frozen dossier → re-fetch into a
      new record first; never cite unfrozen material.
    - the session overwhelms the user at scale → chunk harder, spread sittings, or
      shrink the run. never absorb their rulings to "help".
    - a check becomes satisfiable by gaming its count → the check is rewritten WITH the
      user, and the gaming is recorded.
    - the 2-type relation set misses a real, evidenced kind → propose the third, with
      its quotes. the user widens the vocabulary or refuses.
    - provenance, not dependency: this skill was derived from `spec.md` + `ledger.md`
      in its home repo (anselmetbrl/skill-construction). it RUNS without them. this
      section carries its own seeds so the skill travels whole.
