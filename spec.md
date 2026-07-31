# spec — holistic-meta-index, v1

> **the name.** `holistic-meta-indexing_of_multi-project-research_as_dataset-graph_for_human-attention`
> four modules — ACT · OBJECT · FORM · PURPOSE. `-` binds a compound, `_` marks a module
> boundary. invocation handle: `holistic-meta-index`.

> **what this is.** a declarative v1 spec for a pipeline that turns a hand-curated list of
> github repos into a navigable meta-index giving BIRD'S-EYE orientation. one file.
> syntax-agnostic. the WHAT; `CLAUDE.md` holds the HOW-to-work-with-the-user.

> **how to read it.** one node per claim, named by what it does. keys are aligned, atomic,
> foldable. each node folds into a **falsification**:
> - `moderation(~invalidation)` — when this decision becomes mistaken.
> - `modification(~verification)` — how to re-read, what nuance recontextualises it then.
> - written short as `moderation` / `modification` in the nodes below.
> - `[evolve]` = an evolvable seed, not law. `[open]` = unresolved, resolve WITH the user.
> - nodes **cross-link by name** (`links`), not by id. hierarchy is a reading-view; the real
>   shape is a graph. section 0 nodes are wide-scope — they live ONCE and are referenced,
>   never restated inside the chain.

> **audit before trusting.** a blueprint to BUILD FROM and to DISTRUST. source-refs
> (`A7`, `R9`, `S2.8`, `v0.1 L177`) point back to `ledger.md` and the original mess —
> trace them, don't take them. the map is not the territory.

---

## 0 · root — orientation, not substitution

> the purpose every node below serves. the index gives POSITION and ACCESS. the user still
> reads the repos themselves.

    why           the bottleneck is attention and access, not storage         (R9 R10)
                  reading repo-by-repo yields only depth, never position —
                  position exists only in the collection
    moderation    [evolve] an index so thin it gives no orientation at all
    modification  [evolve] deepen the gist; never let it stand IN FOR the repo
    governs       all nodes below

---

## 0.1 · wide-scope nodes — each lives once, referenced by name

### capture-over-judge — gather wide, decide nothing while gathering
    why           judgment at fetch-time silently discards what a later pass would need
    practice      fetch everything plausibly relevant; every filter is a LATER act
    moderation    [evolve] over-capture buries the signal or blows the context budget
    modification  [evolve] capture wide, STORE lean — trim at store-time, never at fetch-time
    links         fetch · gist

### evidence-over-verdict — describe what IS, quote-grounded; refuse the verdict
    why           the index orients; it never ranks or judges on the user's behalf   (A22 A35)
    practice      every claim carries the quote (with link) that shows it
    moderation    [evolve] refusing all judgment leaves the user with undigested noise
    modification  [evolve] surface the SIGNAL with its quote; the user weighs it
    links         gist · relate · index · void-over-hallucination

### void-over-hallucination — `#void` when the material does not say
    why           an empty field is an OUTCOME; a fabricated one is damage           (A17)
    practice      `#void` for unknown/absent · never pad a slot to look complete
    moderation    [evolve] so much `#void` that the entry conveys nothing
    modification  [evolve] say plainly that the repo is uninformative — that IS the finding
    links         gist · tag · relate · emerge

### what-can-be-rewritten — three layers, decreasing fixity
    raw           dossiers, fetched fact          FROZEN — never rewritten     (v0.1 L45)
    inferred      gists · tags · relations        recompilable — writeback is legitimate
    rendered      the index layout                re-renderable at will
    why           later layers COMPILE from earlier ones rather than rewriting history
    moderation    [evolve] a raw dossier is provably wrong or corrupt
    modification  [evolve] re-fetch into a NEW record; annotate, never edit in place
    links         fetch · gist · relate · index

### the-agent-does-the-reading — no sub-LLM delegation
    why           "send readme to model X, write response to disk" produces a different
                  artifact than the agent ITSELF reading                        (v0.1 L79-80)
    practice      the agent reads and writes gists directly — beware exporting responsibility
    moderation    [evolve] volume genuinely exceeds one agent's reach
    modification  [evolve] split by BATCH, not by delegation — same agent, more passes
    links         gist · tag · relate · emerge

### failures-stay-visible — a blocked repo is an outcome, not an omission
    why           silent skipping is the one failure that cannot be audited      (v0.1 L64 L102)
    practice      private/deleted/blocked/rate-limited → flagged with the reason, link
                  preserved, and still present in the final index
    moderation    [evolve] flag-noise crowds out the working entries
    modification  [evolve] keep the flag, demote the detail into the fold
    links         seeds · fetch · index

### checkpoint-and-resume — mark before work, mark after outcome, save atomically
    why           the run is long and interruptible; nothing already earned is re-earned
    practice      per-repo state · `status: ok` → skip · `partial`/`rate-limited` → redo that
                  one, overwrite in place · never wipe intermediate work on a state change
    practice      process each facet MODULARLY, checkpointed under git — so a defect is
                  isolated, diffable, self-healable rather than a whole-run rebuild
    moderation    [evolve] resume skips work that a changed upstream has invalidated
    modification  [evolve] invalidate the dependent layer explicitly; raw stays frozen
    links         fetch · what-can-be-rewritten

### signal-over-saturation — the user's attention is the scarce resource
    why           more output is not more value; congestion is the failure mode    (A35)
    practice      digestion over congestion · atomic lines over walls · caps exist to
                  protect signal, never to hit a number
    moderation    [evolve] compression drops a distinction the user actually needed
    modification  [evolve] keep the distinction, move the detail into the fold
    links         tag · index · emerge

---

## 1 · the chain

    seeds → dossiers → gists → tags → relations → index    (+ emerge companion)

### seeds — a pre-curated list, entering as-is
    in            a list of github links + an optional contextual prompt        (A3)
    query         ONE standing query for now; per-run queries deliberately deferred (R4 R5)
    scale         ~100 typical, ~300 maximum                                    (R2)
    do            classify each link first · flag+skip accidental index-repos
                  (awesome-lists) — never rabbithole into their members         (A5)
    gate          pre-curation is the user's own act and stays manual           (R8)
    moderation    [evolve] a seed IS an index-repo and is itself the relevant artifact
    modification  [evolve] flag it and ask; never expand it into members unasked
    links         failures-stay-visible

### fetch — over-capture into one frozen dossier per repo
    in            seeds                             out    one raw dossier per repo
    source        github api for structured data · scrape website/wiki/docs for the rest (A1)
    capture       readme · manifests · tree-shape (for language ROLES, not just %) · langs ·
                  license · issues open/resolved · activity · contributors · dates
                  [evolve] the exact field-shape stays loose; v0.1's 2.1 block is a sketch
    store         markdown, no html noise · full FETCH, minimal STORE               (O7)
    ladder        plain → stealth → alternative → flag · 2 attempts per rung        (O6)
    normalise     self-heal into cohesive llm-readable markdown before gisting      (A2)
    gate          evidence, not interpretation · missing value → empty or `unknown`,
                  never invented · do not summarise or infer here              (v0.1 L74)
    moderation    [evolve] a source needs a fetch route none of the rungs cover
    modification  [evolve] add the rung, record which one worked; never silently skip
    links         capture-over-judge · what-can-be-rewritten · checkpoint-and-resume ·
                  failures-stay-visible

### gist — the inferred layer, written by the agent reading
    in            dossiers                          out    one gist per repo
    pass uni      augment from the repo ALONE                                       (A7)
    pass multi    after ALL uni is done, re-read each from the evolved whole        (A7)
                  synthesis from the holistic holons, not reductionism              (A9)
    spine         FIXED — what-it-is (notion) · why-it-is (question) · how-it-is (mediation)
                    how-it-is splits   technology   internal: what it is built of
                                       technicality external: dependencies, stack-fit  (A20)
    leaves        EARNED — as many quote-grounded nodes as the repo actually yields;
                  `#void` when absent, never padded to fill the shape             (S2.6)
    flag          impartially: marketing-hype (a superlative asserted as established fact,
                  in the project's own promotional register) · seo/ai filler · abandonment ·
                  fake or weak contribution · paywall-sabotage (cloud hosting fine,
                  crippled self-hosting is not → `unfree?`) · contradictions across the
                  repo — RECORD the conflict, the user resolves            (v0.1 L86-103, A14)
    trust         subtractive — eroded by accumulated red flags. never a computed score (A21)
    fallback      docs/wiki consulted only when the readme is genuinely unclear
    beware        readmes use their OWN headings — do not assume `## Features` exists ·
                  do not reuse one phrase across what/why/how; each angle is distinct
    moderation    [evolve] a repo yields so little that every leaf is `#void`
    modification  [evolve] say so plainly — a thin repo is a finding, not a failure to hide
    links         the-agent-does-the-reading · evidence-over-verdict ·
                  void-over-hallucination · capture-over-judge

### tag — few, distinctive, derived from the whole
    in            all gists                         out    4 per repo · ≤12 across the collection
    order         derive per repo FIRST, then distil the 12 AFTER every repo is tagged —
                  do not reduce to 4 before the tags have converged             (A16 A23)
    why the caps  more tags saturate signal, and llms generate synonymous slop      (A16)
    quality       NON-REDUNDANCY against the whole system                          (S2.11)
                    fails  redundant with an existing field   `rust`  — lang% carries it
                           a systemic given                   `local` — assumed anyway
                           too broad to partition             `ai` · `memory`
                    passes a distinctive function that PARTITIONS the collection —
                           vectorisation · conversion · transcription · visualisation
                  discrimination is a property of the SET, not of the repo
    format        lowercase_underscore                                        (v0.1 L146)
    empty         `#void` — never force a tag                                       (A17)
    vocabulary    the user's latin-root vocabulary is INSPIRATION, not a whitelist ·
                  guard against deriving synonyms instead of distinct high-signal tags (A15 A18)
    moderation    [evolve] 4 cannot carry a repo, or 12 cannot carry the collection
    modification  [evolve] surface the pressure to the user — the cap is a signal-discipline,
                  not a law to conform to at the cost of meaning
    links         signal-over-saturation · void-over-hallucination

### relate — cross-repo edges, only where evidence shows them
    in            all gists read together (the multi pass)   out   a decoupled `#graph` module
    types         alternative-to   A positions itself as a substitute for B
                  conflicts-with   contradictory claims, or stated incompatibility
    gate          no quote → NO relation · "no relation" is valid and common      (S2.13)
                  never invented to fill a slot — the `#void` discipline, applied to edges
    compare       QUALITIES not quantities — claims, features, dependencies,
                  technologies. never stars, dates or counts                        (A20)
    deps          not an edge — origin-truth, listed as a `#git` fact
    home          the `#graph` module, mirrored per-gist so the index reads standalone
    moderation    [evolve] the fixed 2-type set misses a real, evidenced relation
    modification  [evolve] widen the vocabulary WITH the user; the agent never coins
                  relation-types alone                                              (A19)
    links         evidence-over-verdict · what-can-be-rewritten · index

### index — one flat list, unfolding per repo
    out           ONE artifact — the index IS the shortlist; no second leaderboard  (S2.8)
    form          a flat, relevance-ordered LIST · each repo appears exactly ONCE ·
                  no category-parent nesting, so no repo needs a single "primary" home
    tree          only INTRA-repo: glance → unfold
    glance        lang% · stars · contributors · significant-update cue ·
                  the official description (github's top-right field)
    tags          a dedicated line directly under the glance — always visible,
                  never folded, so IDE text-search reaches it                      (S2.10)
    unfold        `#git`    origin-truth: metadata in nuance, shortcut-links into
                            readme/website/wiki
                  `#gist`   what-it-is · why-it-is · how-it-is
                  `#graph`  relations
    navigate      a TOC/legend of the categories + IDE text-search on the tag line —
                  regroup a category on DEMAND, without unfolding nests            (S2.9)
    rank          relevance-to-query orders attention. DISPLAY ≠ COMPARISON: counts are
                  shown for first-glance, never ranked or compared by         (S2.2, v0.1 L170)
    standalone    reading only the index must suffice to grasp each repo — never force
                  opening a separate gist file                                (v0.1 L177)
    render        markdown, ide-native fold, no html noise · indentation for visual
                  nesting · a header per depth
    layout        re-renders the same compiled material; it never reprocesses fields or
                  relations. further layouts are a later re-render               [deferred]
    moderation    [evolve] the flat list scatters a category so badly that search
                  cannot re-gather it
    modification  [evolve] add a GROUPED re-render alongside — the material is untouched,
                  the layout is free
    links         orientation-not-substitution · signal-over-saturation ·
                  what-can-be-rewritten · failures-stay-visible

### emerge — a spoken companion that helps digest the index
    out           a post-scriptum beside the index. NOT a second index, NOT a self-audit (A27)
    form          TTS prose — linear and speakable · no tables, no nesting that does not
                  read aloud
    glance        **bold** fields · atomic paragraph-modules · never walls —
                  legible to the eye AND to the ear                               (S2.14)
    content       ONLY what EMERGED from the whole and cannot sit in a per-repo cell:
                  cross-cutting epistemological signals, the shape of the collection,
                  warnings worth carrying into the reading
    gate          non-redundant with the index · non-padded — if little emerged, say LESS
    moderation    [evolve] nothing emerged that the index does not already carry
    modification  [evolve] say the little there is, and stop
    links         signal-over-saturation · void-over-hallucination ·
                  orientation-not-substitution

---

## 2 · self-audit — enforced against the finished work, not as a phase

    what          did this run slop, flatten, hype, or pretend to understand?    (A35 A22)
    when          inward quality control over the output — distinct from `emerge`,
                  which faces outward to the user
    how           [open] this overlaps `CLAUDE.md`'s root `practice` (the pre-ship gate:
                  concrete-referent · live-once · provenance · cadence-suspicion).
                  ONE gate serving both, or two with different objects — the agent's
                  own prose vs the pipeline's artifacts? resolve with the user.
    moderation    [evolve] the audit becomes a ritual that always passes
    modification  [evolve] audit against a SAMPLE the user picks, not one the agent picks

---

## 3 · scope

    in v1         everything in section 1 above
    deferred      a designed relation ontology                                      (A19)
                  the root-vocabulary as a tag WHITELIST                            (A18)
                  memory across runs — each run stands alone                   (A30 A31)
                  staleness and refresh                                             (A32)
                  persisted contradiction-resolutions — these live in the user's pkm (A33)
                  multiple index layouts — enabled by `index.layout`, not built
    removal       a repo leaves an index only by the user's hand                    (A34)

---

## · openended — this file is unfinished, by design

    - every `moderation`/`modification` is an evolvable seed. prototype output is the
      real falsification: they prove out or break in practice, never on paper.
    - `[open]` significant-update heuristics: releases/tags · non-bot commit filtering ·
      maintainer responsiveness. naive last-commit is a trap (bot bumps, merges).    (S2.7)
    - `[open]` does the 2-type relation set hold at 300 repos?
    - `[open]` self-audit vs the stance file's pre-ship gate — one or two.
    - `[open]` enforcement grain: before / during / after each pass. during might be irrealistic for how an agentic llm workds, micro self-reflection after each pass (macro before and after each phase) is crucial  for per-pass self-evaluation and self-healing debug git try-again resolution             (L2.3)
    - `[open]` a glossary of the user's idiolect — deferred.
    - `[open]` BIG THREAD: the latin-root vocabulary is deferred as TAGS, yet it keeps
      re-entering as the META-language (moderation/modification here; the tags that
      "pass" in `tag.quality`). alive as language while dead as taxonomy — unresolved.
    - do not settle for this file as a summary: re-ingest the conversation and the
      six source files holistically.
