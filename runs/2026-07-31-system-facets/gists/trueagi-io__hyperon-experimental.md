# gist — trueagi-io/hyperon-experimental · seed 06

    source · dossiers/trueagi-io__hyperon-experimental.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    an implementation of a language called MeTTa, positioned as a successor language
      ← "One of the focuses in the Hyperon design is a successor to the OpenCog Classic
         Atomese language with clear semantics supporting meta-language features,
         different types of inference, etc. What we have landed on is an \"Atomese 2\"
         language called MeTTa (Meta Type Talk)."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    and the revision of a whole prior system, self-declared pre-alpha
      ← "OpenCog Hyperon is a substantially revised, novel version of OpenCog - which is
         currently at an active pre-alpha stage of development and experimentation."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)

## why-it-is

    the need is named in one clause and not elaborated — clearer semantics than the
    language it succeeds
      ← "a successor to the OpenCog Classic Atomese language with clear semantics
         supporting meta-language features, different types of inference, etc."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)

## how-it-is · technology (internal)

    a Rust core, split across three crates, with the interpreter in one of them
      ← "Main library `libhyperon.rlib` is written in Rust language … Source code of the
         library is divided on three crates located under [./hyperon-common],
         [./hyperon-atom] and [./lib] directories."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    the atomspace and interpreter live together in the same crate
      ← "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    a C API is the widening layer, generated rather than hand-written
      ← "In order to provide API for platforms and languages other than Rust there is a C
         API export library `libhyperonc`. … Native library is compiled using Cargo, C
         headers are generated using cbindgen tool."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)

## how-it-is · technicality (external)

    Python is reached through that C layer, in two hops
      ← "First part is a native Python library `libhyperonpy` which is written using
         [pybind11], it converts Python API calls into C API calls and vice versa. Second
         part is a Python library `hyperon` which uses `libhyperonpy` as a proxy"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    the cheapest entry is a pip install, not a build
      ← "It is the most simple way of getting MeTTa interpreter especially if you are a
         Python developer. / The following command installs the latest release version
         from PyPi package repository: / python3 -m pip install hyperon"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    a third-party extension point is declared at the crate boundary
      ← "[./hyperon-atom](./hyperon-atom) crate contains core API which can be imported by
         third-party built-in modules providers."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)

## leaves — earned, not padded

    two REPLs exist, one per language surface
      ← "After installing package or starting Docker container run MeTTa Python based
         interpreter: / metta-py" · "Using Docker you can also run Rust REPL: / metta-repl"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    experimental features are gated behind cargo features, edited before compiling
      ← "The experimental features can be enabled by editing [Cargo.toml](./lib/Cargo.toml)
         file before compilation or by using `--features` [command line option]"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    a distributed-atomspace integration is on by default and pulls a build dependency
      ← "To support DAS integration (enabled by default): * Protobuf compiler"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)

#graph-harvest

    "OpenCog Hyperon is a substantially revised, novel version of OpenCog"
      (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
      → names `OpenCog`
    "a successor to the OpenCog Classic Atomese language"
      (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
      → names `OpenCog Classic` · names `Atomese`
    "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
      (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
      → names `atomspace`
    "To support DAS integration (enabled by default): * Protobuf compiler"
      (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
      → names `DAS` · resolves in-tree to `singnet/das` via the dependency transcript

## flags

    hype · promotional register applied to its own succession claim
      ← "OpenCog Hyperon is a substantially revised, novel version of OpenCog"
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    abandonment · inverted — a self-declared pre-alpha status, matching the repo name
      ← "which is currently at an active pre-alpha stage of development and
         experimentation."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    filler
      #void — none found in the frozen material
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material

## finding — the shape of this readme

    the what and why are concentrated in one short Overview; the remaining ~90% is
    build, install and troubleshooting. leaves beyond the three above are thin because
    the material is thin on them, not because they were skipped.
      #void — an observation about the source, carrying no claim about the project
