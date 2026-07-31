# QuackHack-McBlindy/yo
what-it-is   a full-stack voice assistant — half Nix compile-time grammar compiler, half Rust runtime interpreter
why-it-is    fast, offline, rule-based plain-language → shell-command execution, deliberately WITHOUT an LLM
how-it-is
  technology   Nix grammar compiler (expands sentence templates into optimized regex) + Rust deterministic runtime (exact + fuzzy matching)
  technicality NixOS module or standalone Rust (TOML scripts); ESP32 clients; runs on one port; containerizable
leaves       "translating plain-language commands into system shell actions" · Offline (no internet after setup) · Safe (rule-based, user defines rules)
flags        none
trust        whole
#graph       DISTINCTIVE anti-LLM stance — "yo is NOT: an LLM with shell access!" — a philosophical contrast to the LLM-agent shells kash (13) and intelli-shell (05, AI mode) · Nix+Rust cluster

## position (multi-pass)
C5∩C6 · agent/voice · MED. the deliberate ANTI-LLM counterpoint — the collection's philosophical foil to the LLM-agent cluster.
