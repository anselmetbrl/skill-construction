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

    order given by user:
        1  meta      how an llm consumes an instruction file
        2  file      what this pipeline is
        3  form      notation, one file, key-value        <- not yet opened

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

## A — answers to Q1-Q38

user's own words, compressed. not interpreted.

    fetch
    A1   github api for structured data; scraping for website / wiki / the rest
    A2   `1.1` = crawl+scrape, then normalise / selfheal / prepare llm-readability
         cohesively, before phase 2 begins
    A3   input = a list of links, plus an optional contextual prompt when pertinent
    A5   facets are a FIXED list the user gives.
         some seeds will mistakenly be indexes (awesome-lists etc) —
         flag and skip. never rabbithole into them.

    naming
    A6   facets ARE tags. categorical facets as tags. one thing, not three.
    A15  the tag list is INSPIRATION, not a whitelist.
         guard against the llm deriving synonyms instead of distinct high-signal tags.
    A16  4 per repo / 12 collection-wide because more tags saturate signal
         and llms generate synonymous slop.
         the 12 are derived AFTER every repo is individually tagged.
    A17  `#void` = placeholder for unknown/empty, so the llm doesn't hallucinate
         when a repo isn't informative enough.
    A18  the latin-root vocabulary is the user's own etymological sense-making.
         a mess to convey to an llm. inspiration only. PREMATURE FOR V1.
    A23  the 12 max categories are inferred after individual tagging.
         avoid duplicate placement or 300 links become a 900-line index.
    A28  which draft is which:
            L258-278   most refined. possibly too distilled even for the user.
            L282-304   previous refinement. comprehensive, not llm-legible.
            L308-356   earlier distillation from a much bigger haystack.
                       saturated with not-so-relevant terms.
    A29  the goal was isolating each word's essential unique etymological meaning
         beneath prefixes/suffixes.
         `~` = a soft separator. connections deliberately flaky, intuitive, not fixed.

    gist
    A7   uni  = augment from the repo alone.
         multi = after ALL uni is done, augment each again from the evolved
                 context of the whole, relatively.
    A8   `2.3` = a further complementary pass from the evolved context.
         more self-reflexive / synthesising.
    A9   "higher-order synthesis" = synthesis from holistic holons,
         not reductionism.
    A10  "contribution/participation" = contributors, and whether they are
         fake / abandoned / weak / active. same suspicion as hype stars.
    A11  the vice→virtue table is a mess. intent was to flag vices;
         naming the virtues may deter from actually flagging the vices.
    A12  the ten items under `corruption` came from experience + braindump.
    A13  C3 was simply messiness.
    A14  unfree = paywall sabotage. cloud hosting is fine;
         artificial limits on self-hosting are not.
    A20  qualities to compare = what a project claims to be, its features,
         dependencies, technologies/technicalities.
         NOT stars, dates or counts.

    relate
    A19  the relation ontology is PREMATURE. for v1 either
         standard types (similarity/alternativity, conflictuality, synergy)
         or possibly left formless. open.
    A21  `trust` is subtractive — gradually invalidated by accumulation of
         red flags and deceptions.
    A22  the fear behind L170: an index that misleads, or that claims to
         understand on the user's behalf. impartial relevance, no verdicts.
    A24  `linguisticality` as a tree category was probably just an example.
    A25  the nested tree matters — gradual hierarchical continuity unfolding.
         the drawn version is an imperfect sketch.
    A26  gisting as augmented git/origin is crucial.
         relating may be too much to ask of an llm agent for v1. undecided.

    egress
    A27  phase 4 is not a second index. it complements the index's
         digestibility and navigability — conveying what emerged
         self-reflexively from the holonic analysis.
         possibly adversarial. undecided.

    operation
    A30  each run produces a STANDALONE index.
    A31  tens of thousands already screened. thousands remain,
         over many runs of tens to hundreds.
         long-term meta memory in the skill = premature.
    A32  staleness / refresh = premature for v1.
    A33  contradiction resolutions live in the user's head and pkm.
         out of scope for v1.
    A34  removal from an index, if ever, only by the user.
    A35  success = a non-sloppy index tree that delivers birdseye view,
         non-slop augmentation, and digestion rather than congestion.
         explicitly not: verbose wordiness, corner-cutting that optimises
         the task's surface instead of the user's experience.

    form
    A36  one file for v1. declarative. it doubles as the high-quality
         blueprint signal for later imperative construction.
    A37  syntax-agnostic. coding-principled (lisp/nix/rust).
         modular key-value-like strings.
         density target: a line of poetry — rich in signal.
         NOT verbose paragraphs. NOT reductionist minimal mashups.
    A38  the skill is invoked explicitly by name. the user names it at the end.
         a long modular working name may be inferred meanwhile.

    unanswered
    A4   where the cross-cutting rules live — "idk". still open.

## V — v1 scope, derived from the answers

proposal. confirm or correct.

    in v1
        fixed facet list, given by the user           A5 A6
        index-is-an-index detection, flag and skip    A5
        github api + targeted scraping                A1
        normalise/selfheal before gisting             A2
        per-repo gist from the repo alone             A7 uni
        second pass over each repo from the whole     A7 multi
        tagging: 4 per repo, 12 collection-wide       A16 A23
        `#void` instead of hallucinating              A17
        red-flag accumulation as subtractive trust    A21
        nested-tree index, standalone                 A25
        each run standalone                           A30

    deferred by the user, explicitly
        latin-root tag vocabulary as a whitelist      A18
        a designed relation ontology                  A19
        long-term memory across runs                  A31
        staleness and refresh                         A32
        persisted contradiction resolutions           A33

    still undecided
        how much relating v1 attempts                 A19 A26
        what phase 4 actually does                    A27
        where the cross-cutting rules live            A4

## M — meta, on how this session has gone

    M1  claude settled on a tidy five-layer story while ~40% of the file
        was still unexamined. premature.
    M2  claude decided unilaterally and reported decisions as findings.
        everything is now a proposal.
    M3  user is partially blind. short lines. no walls. no dense prose.
    M4  claude assists. claude does not run ahead.
    M5  claude overread L178 as "the index replaces reading the repos".
        user corrected: it is orientation, not substitution. see R9.
