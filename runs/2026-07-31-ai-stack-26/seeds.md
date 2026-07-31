# seeds — run 2026-07-31-ai-stack-26

    query    curate, across github, the most relevant repos for every facet of ai,
             where ai is taken to span the whole computing stack
             facets: os · lang · env · ide · research · agent · vcs · db · viz · ...   (R5)
    given    25 github links (recounted — the invocation text said 26; letta + letta-code
             are two distinct repos, total is 25). listed verbatim below.
    prompt   none supplied beyond the standing query.

---

## classification — index-repo detection (phase-1 gate)

> the ONLY phase-1 verdict that blocks: is a seed an accidental index-repo
> (awesome-list / curated collection)? → flag + ask, never rabbithole (A5).
> the `notion?` column is a PRE-FETCH guess, to be confirmed or overwritten by the
> dossier. `#unknown` = i do not know this repo; i will NOT invent it (void-over-hallucination).

    #   owner/repo                            class     notion? (pre-fetch guess — unconfirmed)
    01  cachix/devenv                         project   dev environments via nix
    02  bevyengine/bevy                       project   rust game engine / ecs
    03  chaosprint/glicol                     project   rust audio live-coding language
    04  dakra/ghostel                         project   #unknown — resolve at fetch
    05  lasantosr/intelli-shell               project   shell command manager / assist
    06  trueagi-io/hyperon-experimental       project   hyperon / metta agi runtime (opencog lineage)
    07  h4ckf0r0day/obscura                   project   #unknown — resolve at fetch
    08  letta-ai/letta                        project   agent memory framework (ex-memgpt)
    09  letta-ai/letta-code                   project   letta coding agent
    10  vpsfreecz/vpsadminos                  project   nixos-based container hypervisor os
    11  papercomputeco/stereOS                project   #unknown — "os", resolve at fetch
    12  denful/den                            project   #unknown — resolve at fetch
    13  jlevy/kash                            project   shell / ai command toolkit
    14  typedb/typedb                         project   strongly-typed knowledge-graph database
    15  QuackHack-McBlindy/yo                 project   #unknown — resolve at fetch
    16  deepcausality-rs/deep_causality       project   rust causal-reasoning / hypergeometry
    17  anselmetbrl/skill-construction        project   the user's OWN repo — this skill's home (in session scope)
    18  ExtensityAI/symbolicai                project   neurosymbolic ai framework
    19  opencog/atomspace                     project   opencog knowledge-representation store
    20  onestardao/WFGY                       project   #unknown — llm reasoning framework?, resolve at fetch
    21  stanfordnlp/dspy                      project   declarative llm programming framework
    22  boundaryml/baml                       project   language for llm functions / prompts
    23  cheat-engine/cheat-engine             project   memory scanner / debugger
    24  dynobo/normcap                        project   ocr screen-capture tool
    25  screenpipe/screenpipe                 project   continuous screen/context recording

## verdict

    index-repos found    NONE flagged pre-fetch. no name matches the awesome-list /
                         curated-collection shape. nothing to flag-and-ask at phase 1.
    caveat               6 repos are `#unknown` to me (04 ghostel · 07 obscura · 11 stereOS ·
                         12 den · 15 yo · 20 WFGY). IF a fetch reveals one is actually an
                         index-repo, it gets flagged THEN and surfaced to the user — the
                         gate re-fires at fetch, it is not closed here.
    scope note           only 17 (anselmetbrl/skill-construction) is in session GitHub scope.
                         the other 24 need `add_repo` for #git api metadata (ledger S3.3).
                         raw readme/docs via raw.githubusercontent + WebFetch need no add.
    proceed              all 25 advance to phase 2 · fetch, threaded 1-by-1, sequentially.
