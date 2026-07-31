# fetch — over-capture into one frozen dossier per repo

> span-level, fully the agent's. this phase HELD in the test run — the ladder degraded
> honestly and recorded its rung. carried forward with its measured facts.

## the ladder — plain → stealth → alternative → flag · 2 attempts per rung

    plain         the direct, cheapest route for the source
    stealth       a different client/header/path when plain is blocked
    alternative   a different SOURCE for the same fact (api ⇄ raw ⇄ page ⇄ manifest)
    flag          nothing reached it → record the reason, preserve the link, keep the
                  repo IN the index with the field `#void`. never silently skip.
    record        which rung worked, per repo, in the dossier.

## measured routes  [this was measured in a Claude-remote container, 2026-07-31 —
                     REMEASURE in any new environment before trusting it]

    raw.githubusercontent.com/<o>/<r>/HEAD/<path>   200 — readme · manifests · license,
                                                    any public repo, no setup
    api.github.com/repos/<o>/<r>                    403 unless the repo is in session
                                                    scope · rate limit 15000/hr when it is
    add_repo (cross-owner)                          REFUSED in that environment → the
                                                    authenticated api unreachable for
                                                    most seeds there
    github.com/<o>/<r> via WebFetch                 200 — PARTIAL #git: description ·
                                                    stars · forks · license · open-issues ·
                                                    release. DROPS (js-rendered):
                                                    contributors · lang% · commit-date
    non-github sites (docs · wikis)                 200

## the per-repo routine

    #git facts    api when reachable, else WebFetch of the public page. what neither
                  yields → `#void — reason`, link preserved.
    lang ROLES    inferred from manifests (Cargo.toml=rust · flake.nix=nix ·
                  package.json=js/ts · pyproject.toml=python · go.mod=go …) — roles
                  over raw % is what the spec wanted anyway.
    update cue    releases/tags · non-bot commits · maintainer response, as FACTS with
                  dates. naive last-commit is a trap (bot bumps, merges). the cue is
                  evidence; alive/dead verdicts belong to no one but the user.
    #gist feed    the readme fetched raw (HEAD, fall back master/main), read by YOU.
                  key spans captured VERBATIM into the dossier with their link — the
                  gist phase cites only what is frozen here.
    manifests     fetched when the readme is thin on stack/deps. deps are #git FACTS,
                  never relation edges.
    docs/wiki     consulted only when the readme is genuinely unclear.

## dossier shape — lean, frozen, carries `status:`

    status        ok | partial | rate-limited | blocked   (frontmatter, drives resume)
    identity      owner/repo · url · official description (verbatim)
    #git          stars · forks · license · open-issues · release · lang-roles · dates ·
                  voids flagged with reasons · deep links (readme anchors · docs · site)
    spans         the verbatim quote bank for gisting — over-capture the signal,
                  store lean: no full-html, no badge noise, no whole-readme dump
    flags-raw     anything fetch itself revealed (moved · archived · thin · index-repo?)

## discipline

    sequential    1 by 1. never recurse into codebase subdirectories — tree-SHAPE only,
                  for language roles. you are not reading the source.
    evidence      not interpretation. missing → `#void`/`unknown`, never invented.
                  no summarising here — that is the gist's selection work.
    frozen        a wrong dossier is re-fetched into a NEW record, annotated, never
                  edited in place.
    pause         when the last dossier lands: report coverage + voids + blocked,
                  commit, AWAIT the user's proceed. do not terminate.
