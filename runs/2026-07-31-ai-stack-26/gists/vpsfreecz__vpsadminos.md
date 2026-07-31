# vpsfreecz/vpsadminos
what-it-is   a small host OS for unprivileged Linux system containers, based on NixOS
why-it-is    run full distributions inside unprivileged containers that "look and feel as much as a virtual machine as possible"
how-it-is
  technology   NixOS + not-os; LTS kernel with out-of-tree patches; runit init; ZFS storage; LXC
  technicality production-used by the non-profit vpsFree.cz; container management via its own `osctl` tool
leaves       unprivileged system containers · ZFS-backed · runit + LXC · in real production use
flags        none
trust        whole
#graph       "based on NixOS and not-os" (dep-fact) · Nix cluster: devenv (01), den (12), stereOS (11), yo (15)
