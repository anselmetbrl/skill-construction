---
status: ok
seed: 02
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# bevyengine/bevy

    url          https://github.com/bevyengine/bevy
    description  "A refreshingly simple data-driven game engine built in Rust"
                 ← About field, verbatim (R4)
    site         https://bevy.org

## #git

    stars          47.4k                   (R4)
    forks          4.7k                    (R4)
    watchers       314                     (R4)
    license        Apache-2.0, MIT         (R4) — dual, confirmed by readme S14
    open-issues    2.8k                    (R4)
    open-prs       547                     (R4)
    release-tag    #void — R2 gated, atom feeds gated (see fetch-routes C-b)
    release-date   #void — no reachable source. the readme states a CADENCE, not a
                   date: see S4.
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust  ← Cargo.toml present at root (R1); readme names Rust throughout
    deep-links     readme    https://raw.githubusercontent.com/bevyengine/bevy/HEAD/README.md
                   quickstart https://bevy.org/learn/quick-start/introduction
                   api-docs  https://docs.rs/bevy/latest/bevy/
                   examples  https://github.com/bevyengine/bevy/tree/latest/examples
                   news      https://bevy.org/news/
                   migration https://bevy.org/learn/migration-guides/
                   cargo-features docs/cargo_features.md

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "## What is Bevy? / Bevy is a refreshingly simple data-driven game engine built
         in Rust. It is free and open-source forever!"
    S2  "## WARNING / Bevy is still in the early stages of development. Important
         features are missing. Documentation is sparse."
    S3  "A new version of Bevy containing breaking changes to the API is released
         [approximately once every 3 months]"
    S4  "We provide [migration guides](https://bevy.org/learn/migration-guides/), but we
         can't guarantee migrations will always be easy. Use only if you are willing to
         work in this environment."
    S5  "**MSRV:** Bevy relies heavily on improvements in the Rust language and compiler.
         As a result, the Minimum Supported Rust Version (MSRV) is generally close to
         \"the latest stable release\" of Rust."
    S6  "## Design Goals" — the six, verbatim:
         "* **Capable**: Offer a complete 2D and 3D feature set"
         "* **Simple**: Easy for newbies to pick up, but infinitely flexible for power
            users"
         "* **Data Focused**: Data-oriented architecture using the Entity Component
            System paradigm"
         "* **Modular**: Use only what you need. Replace what you don't like"
         "* **Fast**: App logic should run quickly, and when possible, in parallel"
         "* **Productive**: Changes should compile quickly ... waiting isn't fun"
    S7  "Bevy can be built just fine using default configuration on stable Rust. However
         for really fast iterative compiles, you should enable the \"fast compiles\"
         setup"
    S8  "This [list][cargo_features] outlines the different cargo features supported by
         Bevy. These allow you to customize the Bevy feature set for your use-case."
    S9  "Bevy is the result of the hard work of many people. A huge thanks to all Bevy
         contributors, the many open source projects that have come before us, the
         [Rust gamedev ecosystem](https://arewegameyet.rs/), and the many libraries we
         build on."
    S10 "Bevy will always be free and open source, but it isn't free to make. Please
         consider [sponsoring our work](https://bevy.org/donate/) if you like what we're
         building."
    S11 "Before contributing or participating in discussions with the community, you
         should familiarize yourself with our [**Code of Conduct**]"
    S12 "For more complex architecture decisions and experimental mad science, please
         open a [GitHub Discussion](https://github.com/bevyengine/bevy/discussions) so we
         can brainstorm together effectively!"
    S13 "**[Bevy Assets](https://bevy.org/assets/):** A collection of awesome Bevy
         projects, tools, plugins and learning materials."
    S14 "all code in this repository is dual-licensed under either: * MIT License … *
         Apache License, Version 2.0 … at your option."
    S15 "This dual-licensing approach is the de-facto standard in the Rust ecosystem"
    S16 "The [assets](assets) included in this repository (for our [examples]) typically
         fall under different open licenses."
    S17 "<!-- This next line need to stay exactly as is. It is required for BrowserStack
         sponsorship. --> / This project is tested with BrowserStack."

## potential-relation spans — collected, NOT resolved

    none found. no span positions bevy against a named alternative engine. S9 names the
    "Rust gamedev ecosystem" collectively and S13 points at a Bevy-asset collection —
    neither names a rival project.

## flags-raw — what fetch itself revealed

    thin?          no. readme substantial.
    index-repo?    no. S13 points OUT to an asset collection hosted on bevy.org; the
                   repo itself is the engine. no recursion warranted.
    archived/moved no notice.
    note-for-gist  S2+S4 are a self-issued maturity WARNING in the project's own words —
                   the inverse of hype, and unusually explicit. S1's "free and
                   open-source forever" and "refreshingly simple" are promotional
                   register in the same readme. both directions recorded as spans; the
                   gist flags, the user weighs.
    note-for-gist  S17 is a sponsorship-mandated line whose text is contractually fixed
                   ("need to stay exactly as is"). recorded as a fact, not judged.
