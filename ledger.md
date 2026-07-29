# ledger

status of the deconstruction. not the spec.
ids are stable — refer to them by id.

    target:   indexing_autoinfo_hg_v0.1.md
    goal:     sdd spec, then reusable pipeline from it
    updated:  2026-07-29
    session:  1

## method

    work-kinds:
        decode      user knows, claude guesses, user confirms
        hole        nobody knows, derive from first principles
        conflict    both known, incompatible, user chooses

    rules:
        claude marks every reading as a guess until confirmed
        one topic per exchange
        no files written unless asked
        short lines, no walls

    order:
        1  purpose        <- current
        2  frame
        3  ontologies
        4  artifacts + mechanics

## R — resolved

    R1  deliverable is an sdd spec; pipeline is built from it, not instead of it
    R2  scale: ~100 repos typical, ~300 max
    R3  gists are written by an agent reading, not by a program calling an api
        confidence: soft ("i guess 2"), revisitable
    R4  query is ONE STANDING query for now
        per-run queries are a stated long-term goal, deliberately deferred
        reason: usable sooner, no premature generality
    R5  the standing query:
        curate, across github, the most relevant repos for every facet of ai,
        where ai is taken to span the whole computing stack
        facets named so far: os lang env ide research agent vcs db viz ...
    R6  the goal is a SHORTLIST — a few options per facet — not only a map
    R7  user is screening on the order of tens of thousands of repos
    R8  precuration is manual and stays manual. the pipeline starts at the
        already-curated seed list.
    R9  the index does NOT replace reading the projects. user still analyses
        each one directly. the index gives orientation and access, not substitution.
    R10 the bottleneck is attention and access, not storage.
        "rat in a maze" = reading repo-by-repo never yields position,
        only depth. position exists only in the collection.
    R11 O14's "digest randomly" = attention gives out, sampling turns haphazard.
        not "order is irrelevant".

## G — guesses awaiting confirmation

claude's, made before the working rules existed. none are earned yet.

    G1  gists are per-repo and independent; do not need one turn
    G2  relations should be their own layer between gists and index
    G3  index is mechanical rendering, needs no judgment
    G4  C1 is dissolved by G2 rather than needing an exception clause
    G5  state.json scopes to the fetch layer only
    G6  "reusable" splits: tooling reused by invocation, procedure reused by instruction
    G7  the Phase_N.M numbering is a false skeleton; the artifact chain is the real one
    G8  output token ceiling forces index rendering to be chunked or scripted
    G9  O11 "from uni" / "from multi" = per-repo vs whole-collection
    G10 the facet words the user speaks naturally (os, lang, ide, db, viz)
        are plain domain terms, not latin roots. bears on C2.
    G11 there may be two outputs, not one:
        index      full map of everything crawled. L170 no-ranking applies here.
        shortlist  the few per facet (R6). selection is the point, L170 does not bind.
        if so, O17 is not a contradiction but two artifacts written as one.
    G12 relating is the heart of the pipeline, gisting is feedstock for it.
        would invert the file's weighting: phase 2 has ~70 lines,
        phase 3's relation ontology is eight `?`.

## C — conflicts found

    C1  L45 immutability across layers  vs  L152 writeback into gist frontmatter
    C2  L146 tag format `lowercase_underscore`  vs  L232-357 latin-root vocabulary
    C3  L88-98 `omission` and `confusion` appear both as children of `corruption`
        and as its siblings at L99/L101
    C4  tags bounded below for genericity (L144) but not above     [unverified]
    C5  L236-255 clusters share members, so no unique primary tag  [unverified]
    C6  `linguisticality` is a per-repo attribute (L114) but used
        as a tree category (L204)                                  [unverified]

    C4-C6 come from the deleted indexing.knf. carried forward as claims, not findings.

## O — open holes

    O1   the "original query" (L182) is undefined; all scoring hangs off it
    O2   phase 4 (L224) named `outro/exclud/ex/selfreflect/invalidate`, empty
    O3   relation ontology (L158-168) is eight `?` in a three-level tree
    O4   tag ontology: four incompatible drafts, none complete
    O5   `_` (L39) and `_:` (L127) — notation unknown
    O6   "x2 attempts before escalading x2 x2 then fail & flag" (L44) — unknown
    O7   full html vs minimal scrape (L70) — user's own open question
    O8   `2.3 ...` (L133) empty
    O9   L2-31 declares 5x5 phase slots; body uses different names and 3 substeps
    O10  "higher-order synthesis" (L110) named, unspecified
    O11  bottom-up "from uni" (L112) / top-down "from multi" (L132) — meaning unconfirmed
    O12  aphorisms at L55-57 not operationalized
    O13  `trust` (L183) as a score — undefined
    O14  seed list provenance. R7 says tens of thousands, R2 says the pipeline
         ingests ~100-300. the funnel between them is nowhere in the file.
    O15  is the facet list given and fixed, or discovered from the corpus?
    O16  is `facet` the same as `tag`, the same as tree `[category]`,
         or a third axis?
    O17  selection rule. what makes a repo one of "the few options" for a facet.
         L170 forbids rankings, R6 requires selection.

## U — regions not yet examined

    U1   L84-103   vice -> virtue four-fold
    U2   L40/L224  in/ex polarity across phase 0 and phase 4
    U3   L236-255  4x4 tree of empty `<` markers
    U4   L258-278  roots with `!` and `?` markers
    U5   L282-304  prefix x ROOT x suffix morphology
    U6   L308-356  six `~~` groups
    U7   L113-131  metadata schema        (read, not interrogated)
    U8   L137-146  tagging rules          (read, not interrogated)
    U9   L170-178  index rendering rules  (read, not interrogated)
    U10  L186-222  nested-tree format and example

## M — meta, on how this session has gone

    M1  claude settled on a tidy five-layer story while ~40% of the file
        was still unexamined. premature.
    M2  claude decided unilaterally and reported decisions as findings.
        everything is now a proposal.
    M3  user is partially blind. short lines. no walls. no dense prose.
    M4  claude assists. claude does not run ahead.
    M5  claude overread L178 as "the index replaces reading the repos".
        user corrected: it is orientation, not substitution. see R9.
