# gist — cachix/devenv · seed 01

    source · dossiers/cachix__devenv.md, frozen 2026-07-31
      #void — provenance line, not a claim
    query · "what/why/how each project really is"
      #void — provenance line, not a claim

## what-it-is

    developer environments declared as a Nix file, entered as a shell
      ← "# [devenv.sh](https://devenv.sh) - Fast, Declarative, Reproducible, and
         Composable Developer Environments"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    the whole surface is two commands — one scaffolds, one activates
      ← "Running ``devenv init`` generates ``devenv.nix``" · "And ``devenv shell``
         activates the environment."
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)

## why-it-is

    #void — the readme never states the need it answers. it opens on a feature list
      and never argues for its own existence; the four adjectives in the title are
      asserted as properties, not as an answer to a stated problem.

## how-it-is · technology (internal)

    rust, for the process manager
      ← "**[Native process manager](https://devenv.sh/processes/)** written in Rust with
         dependency ordering, restart policies, readiness probes (exec, HTTP, systemd
         notify), socket activation, watchdog heartbeats, and file watching"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    nix as the evaluation layer, with caching between evaluations
      ← "**[Instant environments]…** with incremental Nix evaluation caching (sub 100ms
         when nothing changed)"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    the hermeticity escape hatch is named and typed rather than hidden
      ← "-i, --impure / Relax the hermeticity of the environment."
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)

## how-it-is · technicality (external)

    the package set is nixpkgs, not its own
      ← "**[100,000+ packages](https://devenv.sh/packages/)** from Nixpkgs for Linux,
         macOS, x64, and ARM64 (including WSL2)"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    it attaches to a shell you already enter, through direnv
      ← "**[direnv integration](https://devenv.sh/integrations/direnv/)** for automatic
         shell activation when entering a directory"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    it emits containers without the usual container tooling
      ← "**[OCI containers](https://devenv.sh/containers/)** built from your environment
         without Docker"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)

## leaves — earned, not padded

    composition is the unit: environments import environments
      ← "**[Composable via imports](https://devenv.sh/composing-using-imports/)** to
         share and reuse environments across projects"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    an environment can exist with no config file at all
      ← "**[Ad hoc environments](https://devenv.sh/ad-hoc-developer-environments/)** from
         the CLI without any config files"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    two AI surfaces ship as stated features — a tool server and a config generator
      ← "**[MCP server](https://devenv.sh/mcp/)** for AI assistant integration (package
         and option search)" · "generate    Generate devenv.yaml and devenv.nix using AI"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    secrets are declared against a provider, not stored in the environment
      ← "**[SecretSpec](https://devenv.sh/integrations/secretspec/)** for declarative,
         provider agnostic secrets management (keyring, 1Password, dotenv)"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)

#graph-harvest

    #void — no span positions devenv against a named alternative. the nearest,
      "built from your environment without Docker", names an absent dependency rather
      than a rival, and is not harvested as a relation.

## flags

    hype · a self-measured latency figure asserted in a feature bullet, no methodology
      ← "(sub 100ms when nothing changed)"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    hype · scale figures used as feature claims, three consecutively
      ← "**[50+ languages](https://devenv.sh/languages/)**" · "**[100,000+ packages]
         (https://devenv.sh/packages/)**" · "**[40+ services](https://devenv.sh/services/)**"
         (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate is
      stated anywhere in the readme
    contradiction
      #void — none found in the frozen material
