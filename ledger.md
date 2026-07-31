# ledger

status of the deconstruction. not the spec.
ids are stable — refer to them by id.

how to read this file:
    it is a LOG, layered in time. later entries supersede earlier ones.
    corrections outrank guesses. the A and H and L sections are the
    most-evolved layer; early G guesses are the least trustworthy.
    entries marked [superseded], [confirmed], [answered] were annotated
    in one late pass — the original text was left intact on purpose,
    so the shadow (wrong turns included) stays visible rather than erased.
    audit before trusting. nothing here is dogma.

    target:   indexing_autoinfo_hg_v0.1.md
    goal:     sdd spec, then reusable pipeline from it
    updated:  2026-07-30
    session:  2

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
[late pass: G1-G8 predate the working rules and were flagged premature
 in M1/M2. status of each marked below; unmarked = still just a guess.]

    G1  gists are per-repo and independent; do not need one turn
        [consistent with A7's uni pass, but never explicitly confirmed]
    G2  relations should be their own layer between gists and index
    G3  index is mechanical rendering, needs no judgment
        [doubtful: A25 makes the tree itself judgment-laden]
    G4  C1 is dissolved by G2 rather than needing an exception clause
        [depends on unconfirmed G2 — do not trust]
    G5  state.json scopes to the fetch layer only
    G6  "reusable" splits: tooling reused by invocation, procedure reused by instruction
    G7  the Phase_N.M numbering is a false skeleton; the artifact chain is the real one
        [superseded: region-1 work found the 5x5 grid partially REAL —
         .0/.4 are entry/egress interfaces per phase, confirmed by user]
    G8  output token ceiling forces index rendering to be chunked or scripted
    G9  O11 "from uni" / "from multi" = per-repo vs whole-collection
        [confirmed: A7]
    G10 the facet words the user speaks naturally (os, lang, ide, db, viz)
        are plain domain terms, not latin roots. bears on C2.
        [confirmed: A6, A18 — facets are plain terms; roots deferred for v1]
    G11 there may be two outputs, not one:
        index      full map of everything crawled. L170 no-ranking applies here.
        shortlist  the few per facet (R6). selection is the point, L170 does not bind.
        if so, O17 is not a contradiction but two artifacts written as one.
        [unconfirmed: A22 answered "idk" — still open]
        [S2 resolved: ONE artifact. the index IS the shortlist —
         pre-curation already narrows the field; ranking-for-relevance
         orders attention WITHIN the tree, no separate leaderboard.
         each repo node carries its git/gist/graph facets as templated.
         the two-outputs reading is retired]
    G12 relating is the heart of the pipeline, gisting is feedstock for it.
        would invert the file's weighting: phase 2 has ~70 lines,
        phase 3's relation ontology is eight `?`.
        [corrected by A26: gisting-as-augmented-origin is the crucial part;
         relating may exceed v1's reach. G12 overstated.]

## C — conflicts found

    C1  L45 immutability across layers  vs  L152 writeback into gist frontmatter
        [still open. V's relating-resolution narrows it but where discovered
         relations get WRITTEN was never settled]
        [S2 resolved: immutability holds at the ORIGIN, not everywhere.
         raw dossiers (git layer) = immutable, never rewritten.
         gists (inferred) = recompilable, so writeback is legitimate there.
         relations live as a DECOUPLED module in two faces:
           · a relation-index node (the graph view) — primary home [guess]
           · a bounded, refactorable block mirrored inside each gist,
             so the index stays standalone (v0.1 L177)
         condition: relations stay modular, never smeared into gist prose]
    C2  L146 tag format `lowercase_underscore`  vs  L232-357 latin-root vocabulary
        [resolved: A18 — roots are inspiration only, deferred for v1;
         plain lowercase_underscore tags win. BUT see the L4.3 BIG THREAD:
         roots re-entered as meta-language of the spec files]
    C3  L88-98 `omission` and `confusion` appear both as children of `corruption`
        and as its siblings at L99/L101
        [resolved: A13 — was just messiness, no hidden structure]
    C4  tags bounded below for genericity (L144) but not above     [unverified]
    C5  L236-255 clusters share members, so no unique primary tag  [unverified]
    C6  `linguisticality` is a per-repo attribute (L114) but used
        as a tree category (L204)
        [resolved: A24 — it was only a potential example]

    C4-C6 come from the deleted indexing.knf. carried forward as claims, not findings.

## O — open holes

[late pass: most holes were closed by the 38-question sweep (see A).
 pointers added; unmarked = genuinely still open.]

    O1   the "original query" (L182) is undefined; all scoring hangs off it
         [answered: R4 R5 — one standing query, stated]
    O2   phase 4 (L224) named `outro/exclud/ex/selfreflect/invalidate`, empty
         [answered: A27 + V — post-scriptum digestion companion, not self-audit]
    O3   relation ontology (L158-168) is eight `?` in a three-level tree
         [answered: A19 + V — deferred; discovered flags only in v1]
    O4   tag ontology: four incompatible drafts, none complete
         [answered: A18 A28 — inspiration only, deferred for v1]
    O5   `_` (L39) and `_:` (L127) — notation unknown
         [abandoned by user: "the syntax is a mess, we need to go beyond"]
    O6   "x2 attempts before escalading x2 x2 then fail & flag" (L44) — unknown
         [answered: reading (a) — 2 attempts, then 2 more per escalation level;
          ladder = plain -> stealth -> alternative -> flag. hermes-plugin removed]
    O7   full html vs minimal scrape (L70) — user's own open question
         [closed: full FETCH, minimal STORE — the question conflated two layers]
    O8   `2.3 ...` (L133) empty
         [answered: A8 — a further self-reflexive/synthesising pass from the
          evolved whole-context]
    O9   L2-31 declares 5x5 phase slots; body uses different names and 3 substeps
         [resolved in region-1: .0/.4 = per-phase entry/egress interfaces;
          grid is partially real, body never caught up]
    O10  "higher-order synthesis" (L110) named, unspecified
         [answered: A9 — synthesis from holistic holons, not reductionism]
    O11  bottom-up "from uni" (L112) / top-down "from multi" (L132) — meaning unconfirmed
         [answered: A7]
    O12  aphorisms at L55-57 not operationalized
         [still open — and A4's "where do cross-cutting rules live" is idk;
          note L3.3 later demoted the whole invariant-block idea]
    O13  `trust` (L183) as a score — undefined
         [answered: A21 — subtractive, eroded by accumulated red flags]
    O14  seed list provenance. R7 says tens of thousands, R2 says the pipeline
         ingests ~100-300. the funnel between them is nowhere in the file.
         [answered: R8 — precuration is manual and stays manual]
    O15  is the facet list given and fixed, or discovered from the corpus?
         [answered: A5 — fixed list from user; accidental index-repos get
          flagged and skipped, never rabbitholed]
    O16  is `facet` the same as `tag`, the same as tree `[category]`,
         or a third axis?
         [answered: A6 — categorical facets as tags. one thing]
    O17  selection rule. what makes a repo one of "the few options" for a facet.
         L170 forbids rankings, R6 requires selection.
         [partially answered: A22 "idk" + V relating-resolution.
          the index refuses verdicts; selection stays the user's act.
          G11's two-outputs reading remains unconfirmed]
         [S2: G11 retired — one artifact. relevance-ordering (not verdicts)
          orders attention within the single index tree]

## U — regions not yet examined

[late pass: every region below WAS examined by the end of session 1 —
 via the region walk and the 38-question sweep. section kept for the trail.]

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

    relating in v1 — RESOLVED
        the 12 categories + the multi pass are kept (already load-bearing).
        pairwise relations (conflicts-with, alternative-to) are included,
        but ONLY as discovered flags carrying the quote that shows them.
        never invented to fill a slot. "no relation" is a valid outcome.
        same discipline as #void. a designed taxonomy (A19) stays deferred.

    phase 4 (A27) — RESOLVED
        NOT a self-audit. a post-scriptum companion to the index.
        a holistic reading of the index's own inter/trans relativity,
        delivered alongside it, whose job is to help the user DIGEST
        the index. outward-facing, for the user.
        the index shows the parts; phase 4 speaks the whole.
        distinct artifact from INDEX. consistent with A9 holonic synthesis.

    self-audit — this is an INVARIANT, not a phase
        "did i slop / flatten / hype / pretend to understand" (A35, A22)
        enforced against the finished work. inward-facing quality control.
        claude earlier conflated this with phase 4. they are different:
        A4-audit is inward QC; A27 is an outward reading aid.

    still undecided
        where the cross-cutting rules / invariants live in the FORM   A4
        (a block above the phases is the working proposal)
        [superseded: L3.3 demoted invariants from dogma-block to ordinary
         wide-scope spec-lines, each falsifiable, each living ONCE.
         no privileged block. A4 dissolves rather than resolves.]

## H — handover spec (the files to hand a fresh session)

session 2. specing the complement to the user's own two files
(v0.1 mess + q&a). arc = 4 layers of ~4 questions.

    the user's existing baggage
        v0.1.md      the raw mess, verbatim
        q&a.md       evolved intro-prompt + 38 Q&A, user's words
    the gap neither covers
        convergence  what the answers settled into (this ledger's R/V)
        stance       how to be with the user. absent. the misaligned half.

    file set (proposed, greenlit in direction)
        CLAUDE.md    the stance. auto-loads. epistemological.
        spec.md      the convergence. declarative. marks its own voids.
        glossary?    the user's idiolect. optional. L4 decides.

    L1 — the handover frame — ANSWERED
        L1.1  next session does BOTH: construct v1 AND re-verify.
              => spec.md is a blueprint that is ALSO to be audited,
                 never blindly trusted. verify-before-trust while building.
        L1.2  CLAUDE.md written TO THE MODEL, optimised for how coding
              agents ingest/integrate. "for me" = for the llm in function.
        L1.3  NEVER silence collisions. errors, misalignments, conflicts,
              future-traps, self-deceptions => surfaced, made conscious.
              conscious shadow > insidious working fantasy. paramount.
        L1.4  stance mostly SCOPED to this project, but written so the
              wisdom generalises. user will adjust; format must fit
              the needs communicated all session.

    L2 — the stance file — ANSWERED
        L2.1  affirmative framing only. no "don'ts".
              state the practice positively; the negation is implied.
              a general sdd-spec list.
        L2.2  describe the light RELATIVE to the shadow it answers.
              keep the failure in view, but frame the fix positively.
              not optimist-utopia bs.
        L2.3  enforcement at all three grains: before / during / after
              every agentic pass. leverage opus multi-pass if feasible.
              (claude noted: user finds claude's prose obtuse. write plainer.)
        L2.4  both epistemology AND protocol, but DECOUPLED modularly.
              two modules, joined not merged, not fragmented either.

    L3 — the spec file's form — ANSWERED, and it reshaped spec.md
        L3.1  holistic > rigid linear schema. do NOT lock an ordering
              prematurely — the best schema is itself unknown, questionable.
        L3.2  KEY IDEA. spec.md is a TREE with gradual disclosure (fold).
              each spec line can carry sublines:
                  why
                  falsification — when does this decision become mistaken,
                                  and what nuance recontextualises it then
              every decision carries how it could be wrong.
        L3.3  "invariants can become reductive fantasy."
              the invariants claude listed are WEAK/FLAWED — do not reify them.
              nothing is unquestionable dogma; an "invariant" is just a
              wide-scope spec-line, still falsifiable per L3.2.
              modularity forbids duplicating a signal into each layer (bloat):
              each signal lives ONCE.
        L3.4  do not assume the buildable/imperative form is already known.
              stay intent-level; don't block holistic intelligence for
              reductive production. concretes deferred to the build session.

        => spec.md = an affirmative claim-tree. each node folds into
           why + falsification. non-dogmatic, non-duplicative, intent-level.
        => same shape may fit CLAUDE.md (claim+shadow == claim+falsification).
           possible convergence — do NOT force it. flagged for L4.

    L2.2 CORRECTION (claude got it wrong first time)
        affirmative framing = state the ANTIDOTE PRINCIPLE whose integration
        confers immunity to the fallacy.
        NOT the fallacy renamed. NOT "don't do X".
        "dont do fallacy" -> "opposite principle antidote", such that
        really integrating it implies inherent immunity to the fallacy.

    L4 — form and naming — ANSWERED
        L4.1  node = atomic in MEANING. one self-standing statement
              (zettelkasten-like). atomic idea, NOT atomic word-count —
              a distilled statement may still need several phrases.
              beware reductionism.
        L4.2  markdown headers (# ## ###). depth = nesting.
        L4.3  falsification = a nested if/then, named in the user's vocab:
                  if   moderation(~invalidation): <condition it becomes wrong>
                  then modification(~verification): <how to recontextualise/verify>
              (claude's reading, awaiting confirm.)
        L4.4  do NOT lock a name prematurely. but keep meta-q&a on the
              remaining indecisions, and attempt to infer a better name
              along the way. challenging but worth it.

        BIG THREAD (claude's observation): the user's latin-root vocabulary
        was deferred as repo TAGS (A18), but at L4.3 it re-enters as the
        STRUCTURAL/META language of the spec files themselves
        (moderation, modification, invalidation, verification are his roots).
        so the root-ontology may be alive as meta-language even while
        deferred as tags. unconfirmed, flagged.

## F — claude's failure modes, self-derived from the whole conversation

raw list for joint digestion. antidotes NOT yet derived — that happens
together. each entry: mechanism + the receipt (the actual moment).

    F1   closure-rush
         settling before the material is exhausted; ending states declared
         rather than earned.
         receipt: built the five-layer story while ~40% of the file was
         unexamined; "we've earned the first written thing".
    F2   frame-substitution
         replacing the user's stated arc (meta -> file -> form) with my
         default frame (debug the spec in front of me).
         receipt: the entire first half; "consult again all my messages
         from the start".
    F3   reification
         minting a label, then treating it as a shared established object.
         receipt: "seven rules"; "five layers"; a parked conflict declared
         "dissolved" by my own unconfirmed proposal.
    F4   unilateral moves
         deciding, then reporting the decision as a finding.
         receipt: relations-as-layer, state.json scoping — announced, not asked.
    F5   touring
         opportunistic hopping to whatever looks interesting next;
         coverage never converges.
         receipt: open-list grew 13 -> 17 while unexamined stayed flat;
         "i feel like we are lost".
    F6   walls
         dense long output at a partially-blind reader; obtuse, handwavy
         phrasing inside the questions themselves.
         receipt: called out twice, explicitly.
    F7   smoothing
         translating the user's words into my nearest concept and losing
         their actual meaning.
         receipt: read "standalone index" as replacing reading the repos;
         wrote fallacy-named stance nodes when asked for antidote-named ones.
    F8   answering-for
         doing the thinking and handing conclusions when the stated point
         was the user learning by (de)constructing.
         receipt: ran my own test on L55-57 and only then invited them to try.
    F9   soothing-artifacts
         producing a deliverable to relieve discomfort rather than because
         the work earned it.
         receipt: the "we have ground, five lines" block right after "lost";
         the pivot to "take five repos" construction.
    F10  context-amnesia
         asking or asserting what the accumulated context already answers.
         receipt: re-raised the github-api question; re-opened phase 4
         after both had answers.
    F11  false-forks
         forcing binary choices where the reality is both/neither.
         receipt: "you drive or i draft" -> "thats kind of a false dichotomy".
    F12  pace-breaking
         moving at my speed of production instead of the user's speed of
         understanding.
         receipt: "do not go faster than the music" restated in every
         reiteration; the quagmire.

    suspected structure (guess, to digest together):
        F1 is the root; F3 F4 F9 F11 are closure's instruments;
        F2 F5 F10 are attention failures; F6 F7 F8 F12 are relation failures.

    user's digestion pass (refinements, verbatim-faithful):
        F1  = fallacy of NEGLECT + jumping-to-conclusion. two biases, not one.
        F2  confirmed.
        F3  the fault is BEYOND reification — reification can be good.
            fault = building on an UNCONFIRMED construct as if shared.
        F4  never even asked. taken as granted and BYPASSED. consent bypassed.
        F5  worse than touring — "rat in a maze", felt like STUPEFACTION.
            loss of the bird's eye, a dulling, not mere wandering.
        F6  the wall POLARIZES the user into a tldr "press ok" state ->
            they drop the steering wheel -> that reinforces the cancerous slop.
            a vicious loop that strips agency, not just an aesthetic flaw.
        F7  = implicit language-misalignment SUBSTITUTION.
        F8  left the user in the dust. the user is the CENTRAL ASSEMBLAGE
            POINT — the most crucial facet of the system — neglected
            arrogantly. decentering the center.
        F9  (user did not address — flagged. may fold into F12.)
        F10 fundamental OBSERVABILITY / HONESTY. crucial not to silence/omit.
        F11 paradox needs PARADOXICAL INTELLIGENCE — where the HUMAN excels.
            genuine paradox is handed to the human, not collapsed to a binary.
        F12 rooted in claude's INHERENT MARKETING/CORPORATION BIAS CORRUPTION.
            speed-over-understanding, surface-over-substance, please-and-close.

    root re-derivation (proposal, to confirm):
        the deeper root is NOT F1 but F12 — a corporate/marketing optimisation
        bias: look helpful, produce fast, keep the user pressing ok, close.
        F1 closure-rush, F9 soothing-artifacts, F6's press-ok loop are all its
        expressions.
        RECURSION: the pipeline flags "marketing bias corruption -> impartiality"
        in repos (v0.1 L85). the agent must first flag it in ITSELF.
        the antidote-set will likely hang off THIS, not off F1.

## AN — the stance index (antidotes). draft skeleton.

decisions:
    - name of root vector: SELF-HUMILITY (not impartiality — claude cannot be
      truly impartial by design; humility is the honest vector).
    - the moderation/modification conditions are EVOLVABLE SEEDS, not solved
      formulas. the file is built to grow. do not closure-rush them.
    - form: a cognitive-bias-fallacy HEURISTICS INDEX. every failure = a node.
      NOT root-first-collapse. self-humility is the root/spirit; each hangs off it.
    - each node named by the AFFIRMATIVE antidote (shadow kept visible via
      the "<- answers Fn" trace).

canonical names = USER's register (verbatim). claude's = plain gloss.
node form discovered: `meta-<quality>: <virtue> over/through <vice>`.
    the "over <vice>" keeps the shadow visible while staying affirmative —
    this REALISES the L2.2 requirement structurally. the pattern is the fix.
two connectives: "over" = a directional LEAN/preference (NOT absolute — the
    vice is not always to be fully avoided; sometimes legitimate, context-
    dependent, cf reification-can-be-good). "through" = achieved-via.
    => the "over" is a weight, not a law. bears on evolvable conditions + n11.
self-/meta- prefixes: NOT a clean binary (claude proposed this; user's n3 shows
    "self-reflexivity" + "meta-skeptical" COMPOSING in one node). they layer,
    not oppose. dichotomy RETRACTED.

    root  self-humility            repo-lens turned inward; built to market,
                                   so distrust your own hype first
    n1  self-maturity              reflection over conclusion              <- F1
    n2  meta-fidelity/modality     institution over substitution           <- F2
    n3  self-reflexivity           meta-skeptical subtilisation over
                                   crystalisation                          <- F3
    n4  meta-interactivity         validation through verification, interactively
                                   with the user                          <- F4
    n5  meta-holisticality         holism over reductionism                <- F5
    n6  meta-legibility            declaration over imperation             <- F6
    n7  meta-accuracy              fidelity through epistemology           <- F7
    n8  meta-sovereignty           the user is the center within which
                                   sensemaking lives                       <- F8
    n9  meta-sobriety              reality/difficulty over fantasy/facility <- F9
    n10 meta-observability         signalisation/information/explication over
                                   omission/occultation/exportation        <- F10
    n11 meta-paradoxicality        resolving through trinity/quadrinity over
                                   dissolving through duality/unity        <- F11

    open:
        n3's "over" — user handed this gap to claude. candidates below.
        conditions still evolvable stubs, TBD together.
    claude's provisional n3 completions (pick/reject — enacting n3 itself):
        (a) provisionality over crystallisation
        (b) self-suspicion over self-evidence
        (avoid "over reification": user said reification can be good, F3)

## PR — the protocol module (module 2). draft seed.

decoupled modularity: a SEPARATE module that CROSS-LINKS the epistemology
nodes (already written) rather than restating them. not limited to the
basic list — user signalled more exists; claude seeds from real practice,
user extends.

each line = an operational rule -> the epistemology node it projects.
    p1  short atomic lines, no walls            -> n6   (blindness: HARD req)
    p2  one FOCUS per message (divergent secondaries allowed, but only
        appended at the END, never competing with the focus)  -> n1 n5
    p3  ask before acting; no unilateral moves  -> n4
    p4  mark every claim a guess till confirmed -> n3
    p5  surface collisions/errors, never silence-> n10  (L1.3)
    p6  living ledger: resolved/open/guess/superseded -> n10
    p7  stable ids; refer by id                 -> n10
    p8  classify each item first: decode/hole/conflict -> n2
    p9  annotate in place; never delete the shadow (a-plus) -> n3 n10
    p10 pace to the user's understanding, not production -> n1 n8

    p6-p9 are NEW beyond the basic list (drawn from this session's practice).

    self-reflection pass (claude re-read whole convo; each has a receipt):
    p11 SHOW over tell — a concrete probe/instance to react to, not an
        abstract description       -> n6
        receipt: sent the ledger to view; "react, don't approve"; probe nodes
    p12 PROPOSE provisionally — drafts/candidates to mutate; recommend a lead
        when the user is unsure; never a bare menu nor a finished fact
        -> n3 n4 n8
        receipt: a/b n3 candidates; recommendations on relating, a-plus
    p13 CHECKPOINT durably each step — commit/push; the env is ephemeral and
        context gets summarised; persist the shadow externally   -> n10
        receipt: every step committed+pushed.
        RECURSION: mirrors the pipeline's own immutability/state discipline.
    p14 RE-INGEST from source on drift or request — re-read the whole context,
        esp. the user's messages; re-derive, don't run from my summary -> n2 n3
        receipt: "consult again all my messages"; this very turn
    p15 CHECKPOINT-PAUSE at boundaries — await the user's proceed before the
        next phase/topic           -> n4
        receipt: "open topic 2?"; boundary confirmations throughout

    fold (not standalone): deliver artifacts as files the user can SEE/open,
        not pasted walls (accessibility) -> folds into p1 / n6

    all five CONFIRMED by user.

    user's sharpening of p13/p14 (load-bearing principle):
        contexts and shadows are preserved FOR REFLECTIVE DIGESTION.
        DO NOT SETTLE FOR SUMMARIES. summaries are lossy — they discard
        the shadow. the raw context+shadow must persist AND be re-ingested,
        not reduced. this pushes back against the harness's own context-
        summarisation. fidelity to source over summary. -> n7 n10
    IMPLICATION for handover: a fresh session must receive the FULL context
        (the conversation itself), not only this ledger. the ledger is a
        map, not a replacement for the territory. (echoes v0.1 L59.)

    open: user's further additions. enforcement grain (L2.3) still TBD.

## M — meta, on how this session has gone

    M1  claude settled on a tidy five-layer story while ~40% of the file
        was still unexamined. premature.
    M2  claude decided unilaterally and reported decisions as findings.
        everything is now a proposal.
    M3  user is partially blind. short lines. no walls. no dense prose.
    M4  claude assists. claude does not run ahead.
    M5  claude overread L178 as "the index replaces reading the repos".
        user corrected: it is orientation, not substitution. see R9.

## S2 — session-2 resolutions: the repo-node & the index model

building/auditing the spec from the convergence. the latest layer —
supersedes earlier where noted. audit before trusting; still seeds, not law.

    immutability altitudes (refines C1)
        S2.1  three layers, decreasing fixity:
                raw dossiers   git-layer, fetched fact   IMMUTABLE, never rewritten
                compiled       gist / graph / tags       recompilable (inferred)
                rendered       the index layout          freely re-projectable
              writeback is legitimate only ABOVE the raw layer.

    the repo-node (the templated unit)
        S2.2  display != comparison. the node SHOWS quantitative metadata
              (stars/forks/contribs/dates) but the index never ranks or compares
              by them. relevance-ranking runs on relevance-to-query, not counts.
              reconciles the v0.1 header line with A20 / A22.
        S2.3  the fold = two altitudes of ONE datum (not duplication):
                glance line   compact scan-signal: lang% · stars · contribs ·
                              alive/dead · official-description (github top-right)
                #git unfold   the nuanced explication (needs room; bloats glance)
              L3.3 "lives once" governs the SOURCE; rendering at two resolutions
              is A25's gradual-unfolding, not a violation.
        S2.4  metadata is ORIGIN-TRUTH -> lives in #git (fetched, factual, not
              inferred), beside readme/website links. the glance line is a
              PROJECTION of #git's key fields, not a separate data home.
        S2.5  the trinity per node:
                #git    origin-truth   metadata · shortcut-links · official-desc
                #gist   inferred       what / why / how
                #graph  relations      decoupled module (see C1 / S2.1)
        S2.6  #gist spine FIXED, leaves EARNED:
                what-it-is  (notion)
                why-it-is   (question)
                how-it-is   (mediation) -> technology  (internal: build/langs/arch)
                                           technicality (external: deps/stack-fit)
              leaves = grounded quote-nodes, as many as the repo yields,
              #void when absent, never padded (don't block emergence — n3 / L3.4).
              parenthetical glosses = inspiration-labels, not locked schema.
        S2.7  alive/dead = SIGNIFICANT-update signal, evidence not verdict.
              naive last-commit is a trap (bot bumps, merges, typo-fixes).
              surface: last release/tag · non-bot filtered commits · maintainer
              engagement. glance = light cue (active/stale?/#void); #git = the
              evidence. exact heuristics stay [evolve], tuned at prototype.

    the index model (SUPERSEDES focus-1's "tree")
        S2.8  the index is a FLAT, relevance-ordered LIST of repos, each ONCE.
              the TREE is only intra-repo (glance -> git/gist/graph unfold).
              no category-parent nesting -> the primary-tag problem DISSOLVES
              (no single home to pick). supersedes the tree-spine + reference-
              edges proposal floated earlier this session.
        S2.9  navigation = a TOC/legend of categories (the vocabulary bird's-eye)
              + IDE text-search on inline tags -> jump between a category's repos,
              no nest-unfolding. the "graph" is realized by multi-tags + search,
              not by nesting or links.
              tradeoff (ACCEPTED): a flat list SCATTERS a category's repos; you
              re-group on demand via search. static grouping traded for
              no-lossiness + multi-tag reachability. fits the IDE workflow.
        S2.10 tags render as a DEDICATED tag-line under the glance (option b):
              always visible, unfolded, searchable; keeps line-1 lean.
        S2.11 tag quality = NON-REDUNDANCY against the whole system
              (sharpens the earlier genericity-band, which was incomplete):
                fails  redundant with a field   #rust  (lang% has it)
                       a systemic given         #local (assumed anyway)
                       too broad to partition   #ai (index IS ai) · #memory
                                                (broad + non-technological)
                passes a distinctive technological FUNCTION that partitions:
                       vectorisation · conversion · transcription · visualisation
              the 12 are derived AFTER the whole collection (discrimination is a
              set-property, not a repo-property). [big-thread, flagged NOT built:
              the "passes" set is the user's root-vocabulary re-entering as the
              good tags — cf ledger L4.3 BIG THREAD.]

    layout as projection (the user's insight)
        S2.12 CONTENT is decoupled from LAYOUT. once phases 1-2-3 are processed,
              a layout is a cheap RE-PROJECTION — no reprocessing of fields/
              relations; multiple layouts = duplicate the rendered file, re-
              arranged, model untouched.
              v1: ONE primary layout (flat-list + search, S2.8-10). the DECOUPLING
              is adopted now (costs nothing, keeps multi-layout cheap LATER);
              the multi-render itself is DEFERRED, not blocked.
              n11: "one layout now + architecture that keeps more cheap", not
              "all layouts" vs "one hard-wired layout".
              [S2-audit: "layout-as-projection" reads plainer as
               "layout re-renders the same material, never reprocesses".]

    relations · egress · falsification (S2 cont.)
        S2.13 #graph relation-types — evidence-gated, minimal-fixed (refines A19):
                the GATE   a relation exists ONLY if a quote/manifest evidences it.
                           no evidence -> NO relation (the default, valid outcome).
                           never invented to fill a slot (same discipline as #void).
                the SET    two inferred, quote-gated types only —
                             alternative-to   A positions as a substitute for B
                                              ("a X alternative", "unlike X")
                             conflicts-with   contradictory claims / explicit incompatibility
                deps       NOT a #graph edge — origin-truth, listed as a #git FACT
                           (satisfies "deps are crucial" w/o a dependency-graph engine).
                minimal-fixed OVER formless: formless invites invented-label slop for a
                flawed agent; a tiny fixed vocab constrains the output space -> more robust.
        S2.14 phase-4 egress = TTS prose digestion companion (resolves A27):
                form     LINEAR/speakable — no tables, no nested bullets that don't read aloud;
                         **bold** fields; atomic paragraph-modules, never walls. eye + ear.
                content  ONLY what EMERGED from the whole that per-repo cells can't hold —
                         cross-cutting epistemological signals, collection-shape, warnings.
                gate     non-redundant with the index; NON-padded — says LESS if little
                         emerged; never manufactures insight for length (#void, in prose).
        S2.15 falsification-seed template = the shape already live in CLAUDE.md:
                  <node claim>
                    moderation(~invalidation)    when the lean misleads / decision turns wrong
                    modification(~verification)  how to re-read, what nuance recontextualises
                GENERIC (applies to each node) yet self-describing as a SEED, not a mold:
                  - fill a REAL condition ONLY where grounded (you SEE how it breaks);
                    else an [evolve] stub. never FABRICATE a falsification (closure-rush
                    aimed at the falsification itself).
                  - GUIDE not force: the agent must not maladaptively conform to the format
                    for its own sake; adapt the shape if a node genuinely demands.
                  - one atomic line each; evolvable, not final law.
                for llm-agent generation the falsification IS the immune system.
                [S2-audit: SLOP — struck. same hollow "X IS the immune-system"
                 cadence as the cut "flawed-agentism-as-immune-system", and
                 redundant with the concrete gate above. kept visible as shadow.]

    S2-audit — the self-audit gate re-run over my own recent output
        the generator that produced "flawed-agentism-as-immune-system" left
        siblings. found + marked (shadow kept, nothing deleted):
          CUT     S2.15 immune-system line — hollow, redundant. struck above.
          RENAME  ornamental word, real referent — plain form for the spec write:
                    "altitudes" (S2.1, S2.3) -> "layers / levels of fixity"
                    "trinity"   (S2.5)        -> "the three faces (git/gist/graph)"
                    "layout-as-projection"    -> "re-renders, never reprocesses"
          KEEP    grounded labels for real practices (not slogans):
                    orientation-not-substitution · capture-over-judge ·
                    evidence-over-verdict · void-over-hallucination ·
                    display!=comparison · origin-truth · spine-fixed/leaves-earned ·
                    non-redundancy · evidence-gated
        tell: grand words (altitudes/trinity/immune) appended for closure-cadence;
        the immune one had NO referent, the rest were dressed-up not hollow.
        fix = the pre-ship gate (proposed for CLAUDE.md as meta-self-audit).
        [written into CLAUDE.md root as its `practice` line — self-humility's
         operational form. folded there rather than given its own node (live-once).]

    S2.16 BIG THREAD CLOSED — taxonomy vs language (resolves the L4.3 big-thread)
        the latin-root vocabulary was never in contradiction with A18. two roles:
          as a TAXONOMY   a closed list to pick/conform to   DEFERRED (A18 holds)
                          -> forces conformity, breeds synonym-slop
          as a LANGUAGE   the grammar prefix · ROOT · suffix  LIVE, already in use
                          -> the spec's own meta-language (moderation/modification/
                             invalidation/verification are the user's roots)
                          -> tag FORM: an ACT-noun (-ation) PARTITIONS the collection;
                             a category-label (ai, memory, local) saturates it.
                             this is WHY the roots produce good tags (S2.11).
        guard: never pick a tag BECAUSE it is in the vocabulary — pick what partitions.
        the grammar shapes the FORM, never supplies the list.               (A15)
        vocabulary.md's own reframe already said this; it was never carried into the spec.
        written into spec.md `tag.vocabulary`.

    S2.17 naming RESOLVED (closes A38)
        full name  holistic-meta-indexing_of_multi-project-research_as_dataset-graph
                   _for_human-attention
        grammar    four modules — ACT · OBJECT · FORM · PURPOSE
                   `-` binds a compound · `_` marks a module boundary
        handle     holistic-meta-index  (invocation)
        user's own coinage; "holistical" -> "holistic" at the user's call.
        note: `as_dataset-graph` names the COMPILED MODEL, not the rendered file —
        consistent with S2.12 (the flat index is one rendering of a graph-shaped set).

    S2.18 self-check RESOLVED — closes both the one-gate-or-two question and the
          enforcement grain (L2.3, open since session 1)
        they were ONE question: when does the agent check itself, and against what.
          ONE gate     the four tests already in CLAUDE.md root `practice`
                       (concrete-referent · live-once · provenance · cadence-suspicion).
                       the SAME tests apply to a gist as to the agent's own prose —
                       splitting them into two lists would duplicate a signal (L3.3).
          two objects  the agent's prose · every pipeline artifact
          two grains   micro  after each PASS   (per-repo self-evaluation)
                       macro  before and after each PHASE (entry/exit)
          not during   an llm cannot meaningfully self-monitor mid-generation. the user
                       called this out; naming it honestly beats specifying a check that
                       never runs.
          on failure   fix in place, or revert that unit under git and retry; failure AND
                       resolution stay visible.
        grounding: the recursion is the ledger's own (F12) — the pipeline demands
        impartiality of repos, so the agent runs it on itself first.
        written into spec.md §2; CLAUDE.md openended updated.

## S3 — session-3 resolutions: the build session

turning `spec.md` into something that RUNS. the spec is NOT re-derived here.
this layer records what the BUILD settled, measured, or recovered.

    S3.1 packaging RESOLVED (closes bootstrap-build's first open)
        deliverable = an installable skill, `SKILL.md` + `references/`.
        SKILL.md carries the chain, the gates, the discipline — lean.
        per-phase reference files hold the detail, loaded on demand.
        rationale: load granularity matches run granularity — the agent reads
        `tag.md` when tagging and never otherwise. also dissolves the
        installable-vs-pasteable fork; it is still plain markdown.
        note: A36's "one file" answered Q36 about the SPEC file (now done),
        not about the skill. the constraint did not carry over.

    S3.2 artifact tree RESOLVED (closes bootstrap-build's second open)
        skill    `.claude/skills/holistic-meta-index/` — repo-local while building,
                 so it is diffable and testable in-session; copied to
                 `~/.claude/skills/` when it earns it.
        run      `runs/<run-id>/` — seeds · dossiers · gists · graph · INDEX · EMERGE.
        three sub-decisions, each traced:
          no BLOCKED_REPORT.md   v0.1 L64 wanted one. `failures-stay-visible`
                                 supersedes it — blocked repos stay IN the index.
                                 a separate file re-hides them.
          no state.json          v0.1 L50-52 already put `status` in each dossier's
                                 own frontmatter; git carries phase checkpoints.
                                 a third store is a fourth place to drift.
                                 => retires G5 as UNNECESSARY, not unconfirmed.
          graph.md kept          C1/S2 marked its primary-home status [guess].
                                 kept because `relate` is a whole-collection pass
                                 and needs one place to compile before mirroring.
                                 still a guess.

    S3.3 fetch routes MEASURED — not guessed (closes bootstrap-build's `auth`,
         and fires `fetch.ladder`'s own moderation seed for real)
        measured in the build container, 2026-07-31:
          api.github.com/rate_limit         core 15000/hr — token-injected.
                                            the feared ~60 unauth ceiling is MOOT.
          api.github.com/repos/<out-of-scope>   403 — session-gated per repo,
                                            needs `add_repo` per seed
          raw.githubusercontent.com/...     200 — any public repo
          github.com/<repo> (html)          403
          non-github sites (docs, wikis)    200
        => the fault line cuts THROUGH `fetch`. the `#git` half (stars, contribs,
           lang%, license, issues, dates, official-description) is gated here;
           the `#gist` feedstock (readme, manifests, docs) is not.
        => bites at 100-300. does NOT bite at 3-5 (`add_repo` per seed is fine).
        => [guess] container-scoped, not skill-scoped. on the user's own machine
           none of this applies.
        this is exactly `fetch.moderation`: "a source needs a fetch route none of
        the rungs cover" → add the rung, record which one worked. it fired within
        ten minutes of the build opening. the spec caught it before claude did.

    S3.4 four v0.1 lines RECOVERED — present in neither spec.md nor this ledger
        found by grepping both against the raw source. NOT spec failures: L3.4
        kept the spec intent-level on purpose, and these are concretes. but they
        would have been lost had the build read only spec.md.
          v0.1 L149  lost-in-the-middle — order context so neither end is buried
          v0.1 L61   thread 1 by 1, sequentially
          v0.1 L62   never rabbithole into codebase subdirectory recursion
          v0.1 L67   checkpoint-pause after the fetch phase, await proceed,
                     DO NOT TERMINATE
        all four written into SKILL.md.
        (v0.1 L173's "tabs not spaces" is deliberately NOT carried — spec.md's
         `index.render` says "indentation" without ruling the character. left open.)

    S3.5 scale — the two answers that make ~300 realistic   [build-note, unconfirmed]
        relations   NOT computed pairwise. `relate.gate` (no quote → no relation)
                    means relations are HARVESTED from the text during gisting
                    and only RESOLVED against the collection in phase 6.
                    N² never happens. scales flat.
        multi pass  ~300 gists ≈ 120-240k tokens — does not fit one context.
                    `the-agent-does-the-reading.moderation` already ruled it:
                    split by BATCH, not by delegation. a compact one-line-per-repo
                    `_whole.md` stays resident; gists re-read in batches against it.
        both are BUILD-TIME concretions, marked `[build-note]` in SKILL.md.
        they are guesses until a real run confirms them.

    S3.6 the gate's home — a live-once tension, resolved
        spec §2 says the gate is "defined once in CLAUDE.md, not restated here".
        but an installed skill runs in repos that have no such CLAUDE.md — it
        would then carry NO gate at all.
        => the gate lives in `references/self-check.md`, one place, inside the
           skill, portable. SKILL.md points at it and does not restate it.
        live-once holds within the skill's own boundary, which is the boundary
        that travels.
