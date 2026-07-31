# denful/den
what-it-is   aspect-oriented, context-driven Nix configuration — a feature as a composable function
why-it-is    Nix configs scatter one concern across per-host module piles; make a feature reusable across hosts/users/platforms
how-it-is
  technology   Nix; "an aspect is a plain function: give it context (hosts, users) and it returns configuration for every Nix class it touches — nixos, darwin, homeManager..."
  technicality works with or without flakes/home-manager; "Zero dependencies... gets out of the way"
leaves       "Write a feature once. Run it on every host, user, and platform" · "No mkIf / enable clutter" · bring-your-own Nix classes
flags        none
trust        whole
#graph       Nix cluster — a DIFFERENT layer from devenv (01): den = config composition, devenv = dev shells · vpsadminos (10), stereOS (11), yo (15)
