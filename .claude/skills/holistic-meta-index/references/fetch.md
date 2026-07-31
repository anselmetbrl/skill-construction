# fetch — over-capture into one frozen dossier per repo

> phase 2 of the chain. one raw dossier per repo. FROZEN once written (never rewritten;
> a wrong one is re-fetched into a NEW record). evidence, not interpretation — no gisting
> here. `capture-over-judge`, `what-can-be-rewritten`, `checkpoint-and-resume`,
> `failures-stay-visible` all live in `spec.md §0.1`; this file is the operational detail.

---

## the ladder — plain → stealth → alternative → flag · 2 attempts per rung

    plain         the direct, cheapest route for the source
    stealth       a different client/header/path when plain is blocked
    alternative   a different SOURCE for the same fact (page ⇄ api ⇄ raw ⇄ manifest)
    flag          none of the rungs reached it → record the reason, preserve the link,
                  keep the repo IN the index with the field `#void` (never silently skip)

---

## measured routes — this environment, 2026-07-31   [build-measured, records reality]

> the spec says record which rung worked. measured live, not guessed (ledger S3.3 confirmed):

    raw.githubusercontent.com/<o>/<r>/HEAD/<path>   200  — readme, manifests, license, any public repo. NO add_repo.
    api.github.com/repos/<owner>/<repo>             403  — session-gated. needs the repo in scope.
    api.github.com/rate_limit                       200  — core 15000/hr (token-injected). ample.
    add_repo <cross-owner>                          REFUSED — v1 blocks adding a repo whose owner
                                                    differs from the session's existing owner(s).
                                                    → the authenticated #git API is UNREACHABLE this
                                                      session for any repo not owned by anselmetbrl.
    github.com/<owner>/<repo> (WebFetch)            200  — recovers PARTIAL #git: official description ·
                                                    stars · forks · license · open-issues · latest release.
                                                    DROPS (js-rendered): contributors · lang% · commit-date.

## the resulting per-repo routine (out-of-owner repos, 24 of 25)

    #git facts    WebFetch github.com/<o>/<r>  → description · stars · forks · license · open-issues · release
                  lang ROLES  ← inferred from manifests (Cargo.toml=rust · package.json=js/ts ·
                                flake.nix=nix · pyproject.toml=python · go.mod=go · CMakeLists=c/cpp)
                                — the spec PREFERS roles over raw % anyway (fetch.capture)
                  contributors · exact lang% · commit-date  → `#void`, reason: session-scope-gated,
                                link preserved (failures-stay-visible)
    #gist feed    curl raw README (HEAD; fall back master/main) — the AGENT reads it, no sub-LLM gist.
                  key verbatim quotes captured into the dossier so phase 3 gists from the dossier.
    manifests     fetched selectively when the readme is thin on stack/deps.
    in-scope repo anselmetbrl/skill-construction (17) — full #git available; but it is a markdown
                  project (this skill's own home), not a typical software repo.

## dossier shape — lean, frozen, carries `status:`

    status:       ok | partial | rate-limited | blocked   (frontmatter, drives resume)
    identity      owner/repo · url · official-description
    #git facts    stars · forks · license · open-issues · release · lang-roles · (voids flagged)
    readme        the what-it-is claim + key feature/quote lines, VERBATIM, with the readme link.
                  over-capture the signal, store lean — no full-readme dump, no html noise.
    flags         anything the fetch itself revealed (moved/renamed/archived/thin/index-repo?)

## gate

    evidence, not interpretation. a missing value → `#void` or `unknown`, NEVER invented.
    do not summarise or infer here — that is phase 3. capture wide, store lean.
