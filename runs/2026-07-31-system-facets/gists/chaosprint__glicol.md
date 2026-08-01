# gist — chaosprint/glicol · seed 03

    source · dossiers/chaosprint__glicol.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a music language whose name IS its paradigm — graph-oriented live coding
      ← "Glicol (an acronym for \"graph-oriented live coding language\") is a computer
         music language with both its language and audio engine written in [Rust
         programming language]"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    you connect nodes; the whole syntax is two connectors
      ← "The basic idea of Glicol is to connect different nodes like synth modules." ·
         "Two ways for connecting: `>>` and `~reference`"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)

## why-it-is

    stated outright, and as a two-sided goal rather than one audience
      ← "The motivation of Glicol is: - to help people with zero knowledge of coding and
         music production to get started with live coding - to offer experienced music
         coders a tool for quick prototyping and hacking"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    the design principle is borrowed from a research community and named
      ← "In [NIME community](https://nime.org/), it is known as: > low entry fee and high
         ceilings" (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)

## how-it-is · technology (internal)

    the hard path was chosen deliberately — parser and engine written rather than bound
      ← "- write the parser in Rust - write the audio engine in Rust that works seamlessly
         with the AST processing - port it to browsers using `WebAssembly`,
         `AudioWorklet` and `SharedArrayBuffer`"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    that choice is what makes an in-language DSP escape hatch possible
      ← "To write everything from low-level also opens the door for `meta` node."
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    graph updates are diffed rather than rebuilt
      ← "no need to select anything, just change the code and update, Glicol engine will
         use `LCS` algorithm to handle adding, updating and removing"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)

## how-it-is · technicality (external)

    the low-level base is what buys the platform range
      ← "Given this low-level nature, Glicol can run on many different platforms such as
         browsers, VST plugins and Bela board."
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    the engine is extractable as a library, not only usable as an app
      ← "The reward is that we now have an Rust audio lib called `glicol_synth`: / It can
         run on Web, Desktop, DAW, Bela board, etc."
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    collaboration is a stated architectural concern, not an add-on
      ← "- Decentralised collaboration using `yjs` and a unique `be-ready` mechanism"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)

## leaves — earned, not padded

    errors are designed to not stop the music — an unusual runtime stance
      ← "- Robust error handling: error reported in console, but previous music will
         continue!" (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    teaching is a design constraint, tied to the graph being audible node by node
      ← "When Glicol is used in education, we can let students see and hear each node,
         even including 'envelope'."
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    the roadmap is checked through 0.12.0 and the remaining items are open-ended
      ← "- [ ] better music expressions, more variation for `seq` nodes - [ ] exploring
         new forms of musical interactions"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)

#graph-harvest

    "For the audio engine, instead of mapping it to existing audio lib like
      `SuperCollider`, I decide to do it the hard way"
      (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
      → names `SuperCollider`

## flags

    hype · promotional adjectives applied to its own engine and library
      ← "Glicol's synth-like syntax and powerful audio engine…" · "Safe, performant,
         light-weight and ergonomic audio lib for web apps"
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    abandonment · inverted — a self-issued STABILITY warning, undated
      ← "> Note that Glicol is still highly experimental, so it can be risky for live
         performances. > The API may also change before version 1.0.0."
         (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    filler
      #void — none found in the frozen material
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material
