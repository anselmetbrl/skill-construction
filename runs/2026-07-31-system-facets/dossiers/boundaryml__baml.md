---
status: ok
seed: 22
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# boundaryml/baml

    url          https://github.com/boundaryml/baml
    description  "The programming language for agents"   ← About field, verbatim (R4)
    site         https://www.boundaryml.com/

## #git

    stars          8.7k                    (R4)
    forks          463                     (R4)
    watchers       32                      (R4)
    license        Apache-2.0              (R4) — the readme itself never states it
    open-issues    199                     (R4)
    open-prs       100                     (R4)
    release-tag    #void — R2 gated, atom feeds gated. readme carries a PyPI version
                   BADGE whose rendered value is absent from raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     THREE manifests at root (R1) — an unusually mixed set:
                   nix   ← flake.nix
                   js/ts ← package.json
                   go    ← go.mod
                   rust  ← NOT at root, but the readme states the implementation
                         language directly: "We're hiring software engineers who love
                         Rust." (S13) and "It has a type system like Rust" (S3).
                         the ROLE is readme-evidenced; a root Cargo.toml is absent.
                   baml  ← the project's own language, distributed via PyPI as `baml-py`
    deep-links     readme    https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md
                   site      https://www.boundaryml.com/
                   explore   https://www.boundaryml.com/explore
                   quickstart https://boundaryml.com/quickstart
                   pypi      https://pypi.org/project/baml-py/
                   contributing /CONTRIBUTING.md

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "# BAML: Basically A Made-up Language"
    S2  "BAML is the programming language for agents."
    S3  "BAML looks like TypeScript, but every feature is built so agents make fewer
         mistakes: - It has a type system like Rust, but compiles even faster than Go."
    S4  "- Types persist at runtime. There is no `any` nor casting dangerously to any
         type."
    S5  "- Errors are typed and statically analyzed."
    S6  "- The filesystem describes the modules/namespaces."
    S7  "- Has green threads, and colorless concurrency like Go"
    S8  "- Built-in tests / eval framework"
    S9  "- Built-in stdlib for agents"
    S10 "- Every baml tool is natively designed for agents, with no garbage outputs, etc."
    S11 "- Can be run standalone or adopt incrementally (you can call a BAML function
         from TS, Py, Go, C#, Java, etc)."
    S12 "brew install boundaryml/tap/baml / baml agent install / baml init / baml ide
         install --code"
    S13 "Made with ❤️ by Boundary. HQ in Seattle, WA. / We're hiring software engineers
         who love Rust. [Email us](mailto:founders@boundaryml.com) or reach out on
         [Discord]"
    S14 "[Explore the website and examples](https://www.boundaryml.com/explore)."
    S15 "See our [guide on getting started](/CONTRIBUTING.md)."

## potential-relation spans — collected, NOT resolved

    "BAML looks like TypeScript, but … It has a type system like Rust, but compiles even
     faster than Go." (readme, S3)
       → names `TypeScript` · `Rust` · `Go` — LANGUAGES, not projects in this collection.
         resolvable to nothing here.
    "Has green threads, and colorless concurrency like Go" (readme, S7)
       → names `Go` again, as a design comparison. same outcome.
    "you can call a BAML function from TS, Py, Go, C#, Java, etc" (readme, S11)
       → names host LANGUAGES. interop targets, not edges.
    no span names another software PROJECT.
    → 0 edge candidates from this seed.

    NOTE for the workbench: seed 21 (stanfordnlp/dspy) is the nearest neighbour in
    subject matter — both replace hand-written prompts with a typed/compositional
    authoring layer — and NEITHER readme names the other. recorded from both sides so
    the workbench discards the pairing explicitly rather than by omission.

## flags-raw — what fetch itself revealed

    thin?          YES — 1.9 KB, the SMALLEST readme in the run by a wide margin, for a
                   8.7k-star repo. it is a feature bullet-list plus four install lines
                   and a hiring note. there is no why-it-is paragraph at all: the readme
                   never states what problem BAML answers, only what it resembles and
                   what it has. the gist's `why` leaf will be #void, and that void is
                   the finding.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  UNVERIFIED COMPARATIVE CLAIMS, stacked in one sentence: "a type
                   system like Rust, but compiles even faster than Go" (S3). a compile-
                   speed comparison against a named language with no measurement, no
                   benchmark link, and no methodology anywhere in the readme. recorded
                   verbatim as a claim.
    note-for-gist  "every feature is built so agents make fewer mistakes" (S3) and "with
                   no garbage outputs, etc." (S10) are efficacy claims with no evidence
                   in the readme. the trailing "etc." on a correctness claim is recorded
                   as written.
    note-for-gist  the name is self-deprecating by construction — "Basically A Made-up
                   Language" (S1) — while the tagline is maximal — "THE programming
                   language for agents" (S2). both registers in four lines. recorded.
    note-for-gist  the readme is a COMMERCIAL surface as much as a technical one: a
                   company, an HQ, a hiring pitch and a founders@ email in its closing
                   lines (S13), with the substance routed to boundaryml.com (S14). no
                   feature gating is stated anywhere; the repo is Apache-2.0 per the
                   page. recorded as facts on both sides.
