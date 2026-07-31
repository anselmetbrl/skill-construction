# seeds — 2026-07-31-system-facets

    run-id      2026-07-31-system-facets
    date        2026-07-31
    phase       1 · seeds — COMPLETE, awaiting the user's proceed
    seeds       25
    fetched     0 — nothing in this file is fetched evidence

## the standing query — as given, verbatim

> "the query is meta, im testing the skill with many projects that are at diverse
>  facets of my system potentially"

    given-at    the invocation turn, in reply to the agent's request for the query
    status      RECORDED VERBATIM · not yet resolved into an index-facing query

### what the agent reads in it — [guess], unconfirmed

    purpose     a SKILL TEST. the run exercises the pipeline; the check-report and
                the failure modes are first-class output, not decoration.
    collection  "diverse facets of my system, POTENTIALLY" — the hedge is signal.
                sparse partitions · many partition-of-one tags · "no relation" as the
                expected common outcome are HONEST FINDINGS here, not shortfalls.
    open        the index-facing standing query — the question the INDEX answers
                ABOUT THE REPOS — is NOT yet given. it is not needed until phase 3
                (gist selection). asked at the phase 1 → 2 boundary, not authored here.

## the seeds — seed order PRESERVED, exactly as given

    NN  owner/repo                          classification      note
    01  cachix/devenv                       project?            —
    02  bevyengine/bevy                     project?            —
    03  chaosprint/glicol                   project?            —
    04  dakra/ghostel                       project?            —
    05  lasantosr/intelli-shell             project?            —
    06  trueagi-io/hyperon-experimental     project?            name carries "experimental"
    07  h4ckf0r0day/obscura                 project?            —
    08  letta-ai/letta                      project?            owner-pair with 09
    09  letta-ai/letta-code                 project?            owner-pair with 08
    10  vpsfreecz/vpsadminos                project?            —
    11  papercomputeco/stereOS              project?            —
    12  denful/den                          project?            —
    13  jlevy/kash                          project?            —
    14  typedb/typedb                       project?            owner==repo
    15  QuackHack-McBlindy/yo               project?            —
    16  deepcausality-rs/deep_causality     project?            owner≈repo
    17  anselmetbrl/skill-construction      project? · SELF     the run's own home repo
    18  ExtensityAI/symbolicai              project?            —
    19  opencog/atomspace                   project?            —
    20  onestardao/WFGY                     project?            —
    21  stanfordnlp/dspy                    project?            —
    22  boundaryml/baml                     project?            —
    23  cheat-engine/cheat-engine           project?            owner==repo
    24  dynobo/normcap                      project?            —
    25  screenpipe/screenpipe               project?            owner==repo

    urls        https://github.com/<owner>/<repo> for all 25, as given.
    duplicates  none. every owner/repo pair distinct.
    order       the user's pre-curation signal. carried unchanged through the batch.

### classification legend

    project?        presumed an ordinary project repo. the `?` is load-bearing:
                    UNCONFIRMED. no evidence has been fetched.
    index-repo?     suspected list/aggregator/awesome-list. would be flagged+skipped,
                    never recursed into.  → 0 seeds carry this. see the finding below.
    SELF            the seed is this run's own home repo.

### notes are STRUCTURAL only

    every note above derives from the LINK STRING alone — owner==repo, shared owner,
    a word inside the repo name. no note describes what any project IS.
    descriptions are fetched evidence and belong to phase 2. none appear here.

## flags raised at phase 1

### F1 · seed 17 is the run's own home — flag and ASK

    anselmetbrl/skill-construction is the repo this run executes inside, and the home
    of the skill executing it. it is NOT an index-repo, so the skill's index-repo rule
    does not fire. but the self-reference is real: its dossier and gist would be built
    from material this run is simultaneously writing.
    → carried IN, unchanged, pending the user's ruling. the agent decides nothing.

### F2 · seeds 08 + 09 share an owner

    letta-ai/letta and letta-ai/letta-code. a shared owner is NOT an edge and is not
    treated as one. if a relation exists it will arrive as a #graph-harvest span from
    the material, name-resolved mechanically at the workbench — or not at all.

### F3 · PHASE 1 CANNOT DO WHAT SKILL.md ASKS — skill finding, recorded

    SKILL.md phase 1 says: "classify every link BEFORE fetching."
    before fetching, the only evidence in hand is the URL STRING. that yields the
    structural notes above and nothing more.

    to classify a seed as index-repo / project / docs-collection from the link alone,
    the agent must reach for TRAINED MEMORY of the named repo. that is unfrozen
    material — forbidden by claims-resolve-to-spans, and precisely the authorship the
    S4 inversion was built to stop.

    so the phase resolves one of two ways, both honest, neither free:
      a) structural-only classification — what this file does. cheap, order preserved,
         and the index-repo guard is DEFERRED to fetch rather than performed.
      b) a light evidence touch before full fetch — one cheap request per seed to
         classify on real spans. this is fetching, and the phase boundary moves.

    taken     (a), because it invents nothing.
    cost      the awesome-list guard did not run at phase 1. it now runs at fetch:
              any dossier revealing an index-repo is flagged there and NOT recursed
              into. the guard holds; it holds one phase later than written.
    status    OPEN — a skill defect for the ledger, not a run failure. the test found it.

## exit

    phase 1 complete. 25 seeds classified structurally, order preserved, 0 fetched.
    3 flags raised, 0 resolved by the agent.
    → AWAIT the user's proceed before phase 2 · fetch.
