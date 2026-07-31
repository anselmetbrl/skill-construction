status: ok
# denful/den
url          https://github.com/denful/den
description  "Aspect-oriented, context-driven Nix configurations."
## #git
stars 530 · forks 49 · license Apache-2.0 · open-issues 20 · release #void
lang-roles  Nix
## readme (verbatim signal)
- "den — Aspect-oriented, Context-driven Nix. Write a feature once. Run it on every host, user, and platform you have"
- "Den turns Nix configuration into composable features instead of per-host piles of modules. A Den aspect is a plain function: give it context... returns configuration for every Nix class it touches — nixos, darwin, homeManager, hjem, or a class you invent"
- "No mkIf / enable clutter. The shape of the context is the condition"
- "Den embraces your Nix. With or without flakes... Zero dependencies. Every part is optional and replaceable — Den works with the setup you already have, and gets out of the way"
## #graph (harvested, unresolved)
- Nix-configuration cluster: devenv 01 (dev envs), vpsadminos 10 (NixOS host), stereOS 11, yo 15 — RESOLVE phase 6 (alternative-to devenv? different layer: den=config composition, devenv=dev shells)
