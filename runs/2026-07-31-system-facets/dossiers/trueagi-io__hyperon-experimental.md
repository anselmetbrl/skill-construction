---
status: ok
seed: 06
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# trueagi-io/hyperon-experimental

    url          https://github.com/trueagi-io/hyperon-experimental
    description  "MeTTa programming language implementation"   ← About field, verbatim (R4)
    site         https://metta-lang.dev

## #git

    stars          266                     (R4)
    forks          98                      (R4)
    watchers       16                      (R4)
    license        MIT                     (R4)
    open-issues    93                      (R4)
    open-prs       2                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme's own troubleshooting
                   output quotes an in-tree version string: "hyperon v0.2.6" (S20) —
                   that is a Cargo error transcript, NOT a release record.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust   ← Cargo.toml at root (R1); "Main library `libhyperon.rlib` is
                          written in Rust language" (S12)
                   cmake  ← CMakeLists.txt at root (R1); "All components which depend on
                          `libhyperonc` are built using [CMake]" (S15)
                   c      ← "there is a C API export library `libhyperonc`" (S13)
                   python ← "Source code of the Python integration library is located
                          under [./python]" (S14); PyPi package `hyperon`
    deep-links     readme    https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md
                   api-docs  https://trueagi-io.github.io/hyperon-experimental
                   metta     https://metta-lang.dev
                   spec      https://wiki.opencog.org/w/File:MeTTa_Specification.pdf
                   wiki      https://wiki.opencog.org/w/Hyperon
                   examples  https://github.com/trueagi-io/metta-examples
                   contrib   ./docs/CONTRIBUTING.md
                   dev-guide ./docs/DEVELOPMENT.md
                   scripts   ./python/tests/scripts
                   structure ./docs/assets/structure.svg

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "OpenCog Hyperon is a substantially revised, novel version of OpenCog - which is
         currently at an active pre-alpha stage of development and experimentation."
    S2  "One of the focuses in the Hyperon design is a successor to the OpenCog Classic
         Atomese language with clear semantics supporting meta-language features,
         different types of inference, etc."
    S3  "What we have landed on is an \"Atomese 2\" language called MeTTa (Meta Type
         Talk)."
    S4  "In order to get familiar with MeTTa one can visit [MeTTa website]
         (https://metta-lang.dev)"
    S5  "The examples of MeTTa programs can be found in [./python/tests/scripts]
         directory."
    S6  "More complex usage scenarios are located at [MeTTa examples repo]
         (https://github.com/trueagi-io/metta-examples)."
    S7  "It is the most simple way of getting MeTTa interpreter especially if you are a
         Python developer. / The following command installs the latest release version
         from PyPi package repository: / python3 -m pip install hyperon"
    S8  "Another way is using released Docker image: / docker run -ti trueagi/hyperon:latest"
    S9  "After installing package or starting Docker container run MeTTa Python based
         interpreter: / metta-py"
    S10 "Using Docker you can also run Rust REPL: / metta-repl"
    S11 "A docker image can be used as a ready to run stable and predictable development
         environment."
    S12 "Main library `libhyperon.rlib` is written in Rust language, it contains core API
         which can be used from other Rust projects. Source code of the library is
         divided on three crates located under [./hyperon-common], [./hyperon-atom] and
         [./lib] directories."
    S13 "In order to provide API for platforms and languages other than Rust there is a C
         API export library `libhyperonc`. … Native library is compiled using Cargo, C
         headers are generated using cbindgen tool."
    S14 "Source code of the Python integration library is located under [./python]
         directory. … First part is a native Python library `libhyperonpy` which is
         written using [pybind11], it converts Python API calls into C API calls and vice
         versa."
    S15 "All components which depend on `libhyperonc` are built using [CMake]
         (https://cmake.org/) build tool in order to manage dependencies automatically."
    S16 "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
    S17 "[./hyperon-atom](./hyperon-atom) crate contains core API which can be imported by
         third-party built-in modules providers."
    S18 "To support DAS integration (enabled by default): * Protobuf compiler"
    S19 "The experimental features can be enabled by editing [Cargo.toml](./lib/Cargo.toml)
         file before compilation or by using `--features` [command line option]"
    S20 "… which satisfies dependency `tokio = \"^1.43.0\"` of package `metta-bus-client
         v0.3.0 (https://github.com/singnet/das?tag=0.11.1#aeafbddf)` … which satisfies
         git dependency `metta-bus-client` of package `hyperon v0.2.6`"
                                                        ← troubleshooting transcript
    S21 "Requirements for building C and Python API: * Python3 and Python3-dev (3.8 or
         later) * Pip (23.1.2 or later) * GCC (7.5 or later) * CMake (3.24 or later)"
    S22 "To support Git based modules (enabled by default): * OpenSSL library * Zlib
         library"
    S23 "Running benchmarks requires nightly toolchain so they can be run using: cargo
         +nightly bench --features benchmark"
    S24 "The REPL needs a path to the libpython library in the current environment."
    S25 "The language servers which we use for development are: - [rust-analyzer] -
         [clangd] - [Python LSP server]"

## potential-relation spans — collected, NOT resolved

    "OpenCog Hyperon is a substantially revised, novel version of OpenCog" (readme, S1)
       → names `OpenCog`
    "a successor to the OpenCog Classic Atomese language" (readme, S2)
       → names `OpenCog Classic` · names `Atomese`
    "What we have landed on is an \"Atomese 2\" language called MeTTa" (readme, S3)
       → names `Atomese 2`
    "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
     (readme, S16)                                       → names `atomspace`
    "A lot of different materials can be found on [OpenCog wiki server]
     (https://wiki.opencog.org/w/Hyperon)." (readme)     → names `OpenCog wiki`
    "[MeTTa specification](https://wiki.opencog.org/w/File:MeTTa_Specification.pdf)"
     (readme)                                            → names the OpenCog wiki again
    "`metta-bus-client v0.3.0 (https://github.com/singnet/das?tag=0.11.1#aeafbddf)`"
     (readme, S20)  ·  "To support DAS integration (enabled by default)" (readme, S18)
       → names `singnet/das` / `DAS`

    NOTE for the workbench: seed 19 of this run is `opencog/atomspace`, under the
    `opencog` owner. FOUR of the spans above name OpenCog, OpenCog Classic, Atomese, or
    atomspace. name-resolution against the collection is the workbench's mechanical job
    and the TYPE is the user's ruling — nothing is decided here.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  "experimental" is in the repo NAME and S1 states "active pre-alpha
                   stage of development and experimentation" — a self-declared maturity
                   level, in the project's own words.
    note-for-gist  the readme is dominated by build/install/troubleshooting material.
                   the what/why content is concentrated in its short Overview. a gist
                   leaf beyond that will be thin — that thinness is a FINDING.
    note-for-gist  S1's "substantially revised, novel version" is promotional register
                   applied to its own predecessor relationship. recorded as a span.
