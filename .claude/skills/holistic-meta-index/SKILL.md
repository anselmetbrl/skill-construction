---
name: holistic-meta-index
description: Turn a hand-curated list of GitHub repos into ONE navigable meta-index giving bird's-eye orientation across a collection — quote-grounded per-repo gists, a small tag set that partitions, evidence-gated relations, and a spoken digest companion. Invoked explicitly by name. Full name — holistic-meta-indexing_of_multi-project-research_as_dataset-graph_for_human-attention.
---

# holistic-meta-index

> **orientation, not substitution.** the index gives POSITION and ACCESS.
> the user still reads the repos. a gist NEVER stands in for a repo.
> the bottleneck is attention and access, not storage.

> **the build is not the run.** a perfect pipeline that never crawled a real repo
> is worth nothing. the map is not the territory.

---

## 0 · before anything — load the gate

read `references/self-check.md` FIRST. it is one gate with two objects: your own
prose, and every artifact this pipeline emits. this pipeline demands impartiality
of repos — run it on yourself first.

---

## 1 · the contract

    in            a list of github links · plus an optional contextual prompt
    query         ONE standing query, given by the user or already known
    scale         ~100 typical · ~300 maximum
    out           `INDEX.md`  the deliverable
                  `EMERGE.md` the spoken companion
    pre-curation  the user's own act. it stays manual. you start at the list.

### the run tree

    runs/<run-id>/                   run-id = <date>-<slug>  [build-note]
        seeds.md                     the list as given + the classification pass
        dossiers/<owner>__<repo>.md  raw · FROZEN · carries `status:`
        gists/<owner>__<repo>.md     inferred · recompilable · working material
        gists/_whole.md              one line per repo — the resident whole-view
                                     [build-note] a scaling concretion, see phase 4
        graph.md                     relations compiled once, then mirrored
        INDEX.md                     the deliverable
        EMERGE.md                    the companion

each run stands alone — no memory across runs, no staleness tracking, no refresh.
blocked repos get NO separate report: they stay IN the index, flagged, links preserved.

`[build-note]` marks a concretion made at build-time, not carried from the spec.
it is a guess until the run confirms it. keep the seam visible; do not silently firm it.

---

## 2 · invariants — stated once, held at every phase

    capture-over-judge      fetch everything plausibly relevant. judgment at fetch-time
                            silently discards what a later pass needs. every filter is
                            a LATER act. capture wide, STORE lean.
    evidence-over-verdict   describe what IS, carrying the quote (with link) that shows
                            it. refuse the verdict. the user weighs it.
    void-over-hallucination `#void` when the material does not say. an empty field is an
                            OUTCOME; a fabricated one is damage. never pad a slot to
                            look complete.
    three layers            raw dossiers FROZEN · gists/tags/relations recompilable ·
                            the index freely re-renderable. later layers COMPILE from
                            earlier ones, never rewrite them. a wrong dossier is
                            re-fetched into a NEW record, annotated, never edited.
    you do the reading      no sub-LLM delegation. "send the readme to a model, write
                            the response to disk" produces a different artifact than
                            YOU reading. when volume exceeds reach, split by BATCH —
                            same agent, more passes. never export responsibility.
    failures-stay-visible   private/deleted/blocked/rate-limited → flagged with the
                            reason, link preserved, present in the final index. silent
                            skipping is the one failure that cannot be audited.
    signal-over-saturation  the user's attention is the scarce resource. digestion over
                            congestion. atomic lines over walls. caps protect signal;
                            they are never a number to hit.

---

## 3 · the run — eight phases

each phase: **do** what it says · pass its **gate** · **load** its reference when it
needs the detail · **checkpoint** before moving on.

### phase 1 · seeds
    load      —
    do        classify every link BEFORE fetching anything.
              flag+skip accidental index-repos (awesome-lists, curated collections).
              never rabbithole into their members.
    gate      a seed that IS an index-repo and is itself the artifact → flag and ASK.
              never expand it into members unasked.
    out       `seeds.md` — every link, its classification, its verdict

### phase 2 · fetch
    load      `references/fetch.md`
    do        one dossier per repo. thread 1 by 1, SEQUENTIALLY.
              never recurse into codebase subdirectories — tree-SHAPE only, for
              language ROLES; you are not reading the source.
              over-capture, then store lean: markdown, no html noise.
    ladder    plain → stealth → alternative → flag · 2 attempts per rung
    gate      evidence, not interpretation. a missing value is empty or `unknown`,
              never invented. do not summarise or infer here.
    out       `dossiers/<owner>__<repo>.md`, each with `status:`
    pause     **phase 2 completes → report, then AWAIT the user's proceed.**
              offer: proceed · retry-blocked. DO NOT TERMINATE.

### phase 3 · gist — uni pass
    load      `references/gist.md`
    do        one repo at a time, from the repo ALONE. augment from its own material.
              spine FIXED: what-it-is (notion) · why-it-is (question) · how-it-is
              (mediation → technology internal / technicality external).
              leaves EARNED: as many quote-grounded nodes as the repo actually yields.
    harvest   while reading, record any relation-quote in the gist's `#graph` block
              ("an X alternative", "unlike X", "incompatible with X"). do NOT resolve
              names yet — phase 6 does that.
              [build-note] harvest-then-resolve is a build-time concretion. the spec
              says only "no quote → no relation"; harvesting at read-time is what
              makes that gate scale past a handful of repos. unconfirmed until run.
    gate      `#void` over padding. a thin repo is a FINDING, not a failure to hide.
    micro     self-check after EACH repo.
    out       `gists/<owner>__<repo>.md`

### phase 4 · gist — multi pass
    load      `references/gist.md`
    do        after ALL uni is done: build `gists/_whole.md` — one compact line per
              repo. keep it resident. re-read each gist against the evolved whole,
              in batches. synthesis from the holistic holons, not reductionism.
    order     highest relevance FIRST, the whole-view synthesis LAST — the middle of
              a long context is where attention is neglected. never bury either end.
    gate      the multi pass ADDS relative position. it does not rewrite the uni gist
              into a summary of the collection.
    micro     self-check after each batch.

### phase 5 · tag
    load      `references/tag.md`
    do        derive per repo FIRST. only AFTER every repo is tagged, distil the ≤12
              collection-wide set. never reduce to 4 before the tags have converged.
    caps      4 per repo · ≤12 across the collection · `lowercase_underscore`
    quality   NON-REDUNDANCY against the whole system. discrimination is a property
              of the SET, not of the repo.
              fails   redundant with a field (`rust` — lang% carries it) ·
                      a systemic given (`local`) · too broad to partition (`ai`)
              passes  a distinctive function that PARTITIONS the collection
    gate      never force a tag → `#void`. never pick a tag BECAUSE it is in the
              user's vocabulary — pick what partitions.
    caution   the caps are a signal-discipline. if 4 cannot carry a repo or 12 cannot
              carry the collection, SURFACE the pressure to the user. do not conform
              at the cost of meaning.

### phase 6 · relate
    load      `references/relate.md`
    do        collect the relation-quotes harvested in phase 3. resolve their targets
              against the collection. compile `graph.md`, then mirror each repo's
              edges into its gist so the index reads standalone.
    types     `alternative-to` · `conflicts-with` — these two only
    gate      no quote → NO relation. "no relation" is valid and common. never
              invented to fill a slot. never coin a new relation-type alone — a
              genuine third type is surfaced to the user, not minted.
    compare   QUALITIES: claims, features, dependencies, technologies.
              never stars, dates or counts.
    deps      not an edge. origin-truth, listed as a `#git` fact.

### phase 7 · index
    load      `references/index.md`
    do        ONE artifact. the index IS the shortlist; there is no second leaderboard.
              a flat, relevance-ordered list. each repo exactly ONCE. no category-parent
              nesting — so no repo needs a "primary" home.
    tree      only INTRA-repo: glance → unfold
    glance    lang% · stars · contributors · significant-update cue · the official
              github description
    tags      a dedicated line under the glance — ALWAYS visible, never folded, so
              text-search reaches it
    unfold    `#git` origin-truth · `#gist` what/why/how · `#graph` relations
    gate      DISPLAY ≠ COMPARISON. counts are shown for first-glance and never ranked
              or compared by. relevance-to-query orders attention; nothing else does.
    gate      standalone — reading only the index must suffice to grasp each repo.

### phase 8 · emerge
    load      `references/emerge.md`
    do        a post-scriptum beside the index. NOT a second index. NOT a self-audit.
              TTS prose — linear and speakable. **bold** fields, atomic paragraph
              modules, never walls. legible to the eye AND the ear.
    content   ONLY what emerged from the whole and cannot sit in a per-repo cell:
              cross-cutting signals, the shape of the collection, warnings worth
              carrying into the reading.
    gate      non-redundant with the index. NON-padded. if little emerged, say LESS.
              never manufacture insight for length.

---

## 4 · discipline — how a phase actually runs

    macro     self-check BEFORE and AFTER each phase — entry check, exit check
    micro     self-check after each PASS — per-repo, per-batch
    not during  an llm cannot meaningfully self-monitor mid-generation. naming that
                honestly beats specifying a check that never runs.
    commit    git-checkpoint at every phase boundary, and every ~10 repos within a
              long phase. a defect must be diffable and revertable, never a whole-run
              rebuild. if `runs/` sits under no git repo, `git init` it — the
              checkpoint discipline is not optional.
    resume    mark before work, mark after outcome, save atomically.
              `status: ok` → skip, it is a completed record. `partial` /
              `rate-limited` → redo THAT one, overwrite in place.
              never wipe intermediate work on a state change.
    pause     checkpoint-pause at each phase boundary: report what the phase produced,
              name what broke, await the user's proceed.
    on failure  self-heal: fix in place, or revert that unit under git and retry.
                the failure AND its resolution stay visible.

---

## 5 · when this spec is wrong

every rule above carries a condition under which it misleads. the source spec records
them as evolvable seeds, not law. when one fires:

    surface it   name the collision to the user. never silence, never route around it.
    record it    which rung worked, which cap broke, which repo defeated the shape.
    never        smooth the mess away to keep the run looking clean.

the falsification seeds live in `spec.md` beside each node. prototype output is the
real falsification — they prove out or break in practice, never on paper.
