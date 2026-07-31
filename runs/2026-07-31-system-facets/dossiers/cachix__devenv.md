---
status: ok
seed: 01
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# cachix/devenv

    url          https://github.com/cachix/devenv
    description  "Fast, Declarative, Reproducible, and Composable Developer Environments
                 using Nix"   ← About field, verbatim (R4)
    site         https://devenv.sh

## #git

    stars          7.2k                    (R4)
    forks          528                     (R4)
    watchers       25                      (R4)
    license        Apache-2.0              (R4)
    open-issues    305                     (R4)
    open-prs       44                      (R4)
    release-tag    #void — R2 gated, atom feeds gated (see fetch-routes C-b).
                   readme shows the running version in its own CLI output: "2.0.0"
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust  ← Cargo.toml present at root (R1)
                   nix   ← flake.nix present at root (R1)
                   note: the readme names Rust explicitly for the process manager.
    deep-links     readme  https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md
                   docs    https://devenv.sh/getting-started/
                   options https://devenv.sh/reference/options/
                   roadmap https://devenv.sh/roadmap/
                   blog    https://devenv.sh/blog/

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "# [devenv.sh](https://devenv.sh) - Fast, Declarative, Reproducible, and
         Composable Developer Environments"
    S2  "Running ``devenv init`` generates ``devenv.nix``"
    S3  "And ``devenv shell`` activates the environment."
    S4  "https://devenv.sh 2.0.0: Fast, Declarative, Reproducible, and Composable
         Developer Environments"
    S5  "**[Instant environments]…** with incremental Nix evaluation caching (sub 100ms
         when nothing changed)"
    S6  "**[Native process manager](https://devenv.sh/processes/)** written in Rust with
         dependency ordering, restart policies, readiness probes (exec, HTTP, systemd
         notify), socket activation, watchdog heartbeats, and file watching"
    S7  "**[50+ languages](https://devenv.sh/languages/)** with built in tooling:
         compilers, LSP servers, formatters, linters, and version selection"
    S8  "**[100,000+ packages](https://devenv.sh/packages/)** from Nixpkgs for Linux,
         macOS, x64, and ARM64 (including WSL2)"
    S9  "**[40+ services](https://devenv.sh/services/)** like PostgreSQL, Redis, MySQL,
         MongoDB, Elasticsearch, Caddy, and more"
    S10 "**[Composable via imports](https://devenv.sh/composing-using-imports/)** to
         share and reuse environments across projects"
    S11 "**[Profiles](https://devenv.sh/profiles/)** for environment variants"
    S12 "**[OCI containers](https://devenv.sh/containers/)** built from your environment
         without Docker"
    S13 "**[direnv integration](https://devenv.sh/integrations/direnv/)** for automatic
         shell activation when entering a directory"
    S14 "**[MCP server](https://devenv.sh/mcp/)** for AI assistant integration (package
         and option search)"
    S15 "**[AI generation](https://devenv.new)** to scaffold environments from a natural
         language description"
    S16 "**[LSP for devenv.nix](https://devenv.sh/lsp/)** with autocomplete, hover docs,
         and go to definition via bundled nixd"
    S17 "**[Ad hoc environments](https://devenv.sh/ad-hoc-developer-environments/)** from
         the CLI without any config files"
    S18 "**[Terminal UI]…** with live build progress, task hierarchy, and error details"
    S19 "**[Native shell reloading]…** that rebuilds in the background while your shell
         stays interactive"
    S20 "**[SecretSpec](https://devenv.sh/integrations/secretspec/)** for declarative,
         provider agnostic secrets management (keyring, 1Password, dotenv)"
    S21 "**[Tasks](https://devenv.sh/tasks/)** with DAG based execution, caching,
         parallel runs, and namespace support"
    S22 "generate    Generate devenv.yaml and devenv.nix using AI"   ← CLI help output
    S23 "-i, --impure / Relax the hermeticity of the environment."   ← CLI help output

## potential-relation spans — collected, NOT resolved

    none found. the readme names Nix, Nixpkgs, direnv, Docker, PostgreSQL, Redis,
    1Password, nixd, crate2nix, uv2nix — all as components, integrations, or things
    built WITHOUT. no span positions devenv AGAINST a named alternative.
    "built from your environment without Docker" (S12) is the closest; it names an
    absence of a dependency, not a rivalry. left for the gist to judge as harvest-or-not.

## flags-raw — what fetch itself revealed

    none. repo reachable, readme substantial, no archive/move notice, not an index-repo.
    the readme's promotional register (superlative feature framing, the "sub 100ms"
    self-measurement in S5, the "50+/100,000+/40+" counts) is GIST territory — recorded
    as spans above, flagged there, not judged here.
