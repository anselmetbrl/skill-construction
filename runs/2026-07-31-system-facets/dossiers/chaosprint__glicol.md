---
status: ok
seed: 03
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# chaosprint/glicol

    url          https://github.com/chaosprint/glicol
    description  "Graph-oriented live coding language and music/audio DSP library
                 written in Rust"   ← About field, verbatim (R4)
    site         https://glicol.org

## #git

    stars          3,000                   (R4)
    forks          99                      (R4)
    watchers       34                      (R4)
    license        MIT                     (R4)
    open-issues    45                      (R4)
    open-prs       3                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme's roadmap marks
                   `0.12.0` as the last checked item; that is a ROADMAP mark, not a
                   release record. see S20.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     NO root manifest. probed one level (R1):
                   rust ← rs/Cargo.toml 200 · rs/wasm/Cargo.toml 200
                   js   ← js/package.json 200
                   readme confirms both roles in prose: S1, S16.
    deep-links     readme    https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md
                   site      https://glicol.org
                   npm-docs  https://glicol.js.org
                   npm       https://npmjs.com/glicol
                   rust-lib  https://github.com/chaosprint/glicol/tree/main/rs/synth
                   bela      https://github.com/chaosprint/glicol/tree/main/rs/bela
                   vst       https://github.com/chaosprint/glicol/tree/main/rs/vst

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "Glicol (an acronym for \"graph-oriented live coding language\") is a computer
         music language with both its language and audio engine written in [Rust
         programming language](https://www.rust-lang.org/), a modern alternative to
         C/C++."
    S2  "Given this low-level nature, Glicol can run on many different platforms such as
         browsers, VST plugins and Bela board."
    S3  "Glicol's synth-like syntax and powerful audio engine also make it possible to
         combine high-level synth or sequencer control with low-level sample-accurate
         audio synthesis, all in real-time."
    S4  "The motivation of Glicol is: - to help people with zero knowledge of coding and
         music production to get started with live coding - to offer experienced music
         coders a tool for quick prototyping and hacking"
    S5  "In [NIME community](https://nime.org/), it is known as: > low entry fee and high
         ceilings"
    S6  "This is Glicol's philosophy to approach these goals: - design the language from
         a new instrument design perspective - embrace the spirit of the internet for a
         better experience"
    S7  "Reflected in the implementation: - Glicol adopts a graph-oriented paradigm -
         Glicol can be used in browsers with zero-installation"
    S8  "The basic idea of Glicol is to connect different nodes like synth modules. / All
         you need to know is the audio input/output behaviour of each node."
    S9  "Two ways for connecting: `>>` and `~reference`"
    S10 "This is actually analogous to how hardware module pass signals. / It is very
         easy to remember and to get started."
    S11 "When Glicol is used in education, we can let students see and hear each node,
         even including 'envelope'."
    S12 "For the audio engine, instead of mapping it to existing audio lib like
         `SuperCollider`, I decide to do it the hard way:"
    S13 "- write the parser in Rust - write the audio engine in Rust that works
         seamlessly with the AST processing - port it to browsers using `WebAssembly`,
         `AudioWorklet` and `SharedArrayBuffer`"
    S14 "The main reason is to explore performant audio in browsers for easy access and
         live coding collaboration."
    S15 "The reward is that we now have an Rust audio lib called `glicol_synth`: / It can
         run on Web, Desktop, DAW, Bela board, etc."
    S16 "To write everything from low-level also opens the door for `meta` node."
    S17 "- Near-native, garbage-collection-free and memory-safe real-time audio in web
         browsers"                                              ← Features <details>
    S18 "- Robust error handling: error reported in console, but previous music will
         continue!"                                             ← Features <details>
    S19 "- Decentralised collaboration using `yjs` and a unique `be-ready` mechanism"
                                                                ← Features <details>
    S20 "> Note that Glicol is still highly experimental, so it can be risky for live
         performances. > The API may also change before version 1.0.0."
    S21 "- [x] `0.8.0` embed `Rhai` in glicol 🎉"                ← Roadmap
    S22 "- [x] `0.10.0` run as a VST plugin  - [x] `0.11.0` run on Bela  - [x] `0.12.0`
         distribute as a `npm` package"                         ← Roadmap
    S23 "- [ ] better music expressions, more variation for `seq` nodes  - [ ] exploring
         new forms of musical interactions"                     ← Roadmap, UNchecked
    S24 "| [NPM Docs](https://glicol.js.org) | Safe, performant, light-weight and
         ergonomic audio lib for web apps |"
    S25 "- What you see is what you get, i.e. declarative programmering for both code
         writing and executing … Glicol engine will use `LCS` algorithm to handle adding,
         updating and removing"                                 ← Features <details>

## potential-relation spans — collected, NOT resolved

    "instead of mapping it to existing audio lib like `SuperCollider`, I decide to do it
     the hard way" (readme, S12) → names `SuperCollider`
    "written in [Rust programming language], a modern alternative to C/C++" (readme, S1)
     → names `C/C++` — a language comparison, not a project one. listed for the
     workbench to resolve mechanically and almost certainly discard.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no. monorepo — rs/ and js/ subtrees are its own components, not
                   third-party members. NOT recursed into beyond the manifest probe
                   needed for lang-roles.
    archived/moved no notice.
    note-for-gist  S20 is a self-issued stability warning ("still highly experimental …
                   can be risky for live performances"). S3 ("powerful audio engine"),
                   S17 ("Near-native"), S24 ("Safe, performant, light-weight and
                   ergonomic") are promotional register in the same readme. both
                   directions recorded; the gist flags, the user weighs.
    note-for-gist  a large "Glicol can be used for:" block is HTML-COMMENTED OUT in the
                   readme source. commented-out text is not shown to a reader; it is NOT
                   quoted as a claim here. recorded as a fetch observation only.
