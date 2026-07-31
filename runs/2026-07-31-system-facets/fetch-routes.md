# fetch-routes — the ladder, REMEASURED in this container

    when        2026-07-31 · Claude-remote container, agent-proxy egress
    why         fetch.md carries measured routes with the instruction "REMEASURE in any
                new environment before trusting it". this is that remeasurement.
    verdict     the prior table HOLDS in substance. two corrections, one addition.

## measured, this container

    R1  raw.githubusercontent.com/<o>/<r>/HEAD/<path>   200 · via curl · RAW BYTES
        swept across all 25 seeds: 24 × 200 on README.md, 1 × 404 (seed 17, no README).
        manifests probed the same way, 16 filenames × 25 repos, all resolving.
        → the #gist feed and the manifest/lang-role route. no sub-LLM in the path.

    R2  api.github.com/repos/<o>/<r>                    403 for 24 of 25 seeds
        body: "GitHub access to this repository is not enabled for this session."
        api.github.com/rate_limit answers 200 with limit 15000 — the token is live,
        the PROXY gates per-repo on session scope. seed 17 (anselmetbrl/skill-
        construction, in scope) answers 200.
        → authenticated #git facts are reachable for exactly ONE seed.

    R3  add_repo, cross-owner                           REFUSED
        "cross-tier adds are not supported in v1: requested cachix/devenv but session
        already has repos from owner(s) [anselmetbrl]".
        → matches the prior measurement. R2 cannot be widened from inside this session.

    R4  github.com/<o>/<r> via WebFetch                 200 · PARTIAL #git
        yields: About description · stars · forks · watchers · license · open issues ·
        open PRs. DROPS: release tag/date · languages+% · contributors · "used by".
        → matches the prior measurement exactly.

## corrections to the prior table

    C-a  github.com/<o>/<r> by direct curl is 403, not 200 — the same per-repo proxy
         gate as R2. only WebFetch reaches the public page, because it egresses through
         the harness rather than the container proxy. the prior table listed the page
         under WebFetch and never claimed curl; recording the distinction so the next
         remeasure does not retry curl and read the 403 as "repo blocked".

    C-b  github.com atom feeds (releases.atom · commits/HEAD.atom) are 403 — same gate.
         the prior table did not mention them. they are NOT a route here.
         → release tags/dates and commit dates have no cheap reliable source in this
           container for 24 of 25 seeds. expect `#void — no reachable source` on those
           fields rather than invention. this is the honest outcome, and the void tally
           will report it (C6).

## addition — the sub-LLM boundary, held explicitly

    WebFetch answers a prompt "using a small fast model". the invariant
    you-do-the-reading forbids sub-LLM delegation. these are reconciled by SPLIT, and
    the split is already the skill's own:

        WebFetch  is used ONLY to TRANSCRIBE displayed numeric/label facts for the
                  glance line — stars, forks, license, issues, the About string.
                  transcription of a rendered number is not reading.
        curl+me   the README arrives as raw bytes and I read every one myself.
                  every #gist span is selected by me from that raw text.

    fetch.md already says it: "#gist feed — the readme fetched raw ... read by YOU."
    no gist span will ever originate from a WebFetch result.

## consequences for this run

    lang-roles     from manifests (R1). the sweep is already complete for all 25.
                   3 seeds carry NO root manifest — chaosprint/glicol · onestardao/WFGY ·
                   cheat-engine/cheat-engine — plus seed 17. probed deeper per repo.
    stars/forks/   R4, one WebFetch per seed.
    license/issues
    release/dates  mostly `#void — no reachable source (R2 gated, C-b feeds gated)`.
    contributors   `#void — js-rendered, dropped by R4` unless the README states it.
    seed 17        the only seed with full authenticated #git via R2. it also has NO
                   README (R1 404) — its #gist feed must come from its other files.
