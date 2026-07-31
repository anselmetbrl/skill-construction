# cachix/devenv
what-it-is   declarative, composable per-project developer environments built on Nix
why-it-is    closes the "works on my machine" gap — reproducible tooling without global installs or Docker-heavy setups
how-it-is
  technology   Nix evaluation + a Rust-written native process manager; terminal UI; bundled nixd LSP
  technicality Nixpkgs (100,000+ packages); composable via imports; OCI containers built without Docker; adopted as a `devenv.nix`
leaves       "50+ languages with built in tooling" · "40+ services like PostgreSQL, Redis..." · tasks with DAG execution · profiles for variants
flags        none — feature-forward but claims are enumerable/verifiable
trust        whole
#graph       built ON Nix (dep-fact) · den (12) is a DIFFERENT Nix layer (config composition, not dev shells)

## position (multi-pass)
C5 nix-stack · env · MED. the mature dev-shell node; sibling den (config layer). infra-enabling to the AI query, not core-AI.
