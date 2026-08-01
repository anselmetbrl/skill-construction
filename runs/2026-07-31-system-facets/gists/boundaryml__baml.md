# gist — boundaryml/baml · seed 22

    source · dossiers/boundaryml__baml.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a programming language whose stated addressee is agents rather than people
      ← "BAML is the programming language for agents."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    and the name says what the authors think of that claim
      ← "# BAML: Basically A Made-up Language"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## why-it-is

    #void — the readme never states a problem. it says what BAML resembles and what it
      has, and asserts a purpose for every feature, but no span says what goes wrong
      without it, for whom, or what it replaces. the why is absent from the source.

## how-it-is · technology (internal)

    the design brief is stated as one criterion applied to every feature
      ← "BAML looks like TypeScript, but every feature is built so agents make fewer
         mistakes"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    types survive into runtime, and the usual escape hatches are removed
      ← "- Types persist at runtime. There is no `any` nor casting dangerously to any
         type."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    errors are part of the type system rather than a convention
      ← "- Errors are typed and statically analyzed."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    module structure is taken from the filesystem rather than declared
      ← "- The filesystem describes the modules/namespaces."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    testing and an agent standard library are in the language, not beside it
      ← "- Built-in tests / eval framework" · "- Built-in stdlib for agents"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## how-it-is · technicality (external)

    it is designed to be adopted piecemeal, callable from six host languages
      ← "- Can be run standalone or adopt incrementally (you can call a BAML function from
         TS, Py, Go, C#, Java, etc)."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    the install is a package manager line and three commands, including an editor plugin
      ← "brew install boundaryml/tap/baml / baml agent install / baml init / baml ide
         install --code"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## leaves — earned, not padded

    concurrency is borrowed from a named language's model, explicitly
      ← "- Has green threads, and colorless concurrency like Go"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    the substance is on a website, and the readme routes there twice
      ← "[Explore the website and examples](https://www.boundaryml.com/explore)."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

#graph-harvest

    #void — no span names another software project. the readme names LANGUAGES —
      TypeScript, Rust, Go, and six interop hosts — and languages do not resolve against
      this collection.

## flags

    hype · a compile-speed comparison against a named language with no measurement,
      no benchmark link, and no methodology anywhere in the readme
      ← "It has a type system like Rust, but compiles even faster than Go."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    hype · efficacy claims about correctness, one of them trailing an "etc."
      ← "every feature is built so agents make fewer mistakes" · "- Every baml tool is
         natively designed for agents, with no garbage outputs, etc."
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    contribution · the readme closes as a commercial and hiring surface
      ← "Made with ❤️ by Boundary. HQ in Seattle, WA. / We're hiring software engineers who
         love Rust. [Email us](mailto:founders@boundaryml.com)"
         (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material

## finding — the smallest readme in the run

    1.9 KB: a bullet list, four install lines, and a hiring note. the why-it-is void above
      is the finding — the front page of a widely starred language project states no
      problem it solves. the register is also split in four lines, between a
      self-deprecating name and a maximal tagline
      #void — an observation about the source, carrying no claim about the project
