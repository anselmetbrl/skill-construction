status: ok
# vpsfreecz/vpsadminos
url          https://github.com/vpsfreecz/vpsadminos
description  "Host for Linux system containers based on NixOS, ZFS and LXC"
## #git
stars 185 · forks 30 · license MIT · open-issues 10 · release #void(not shown)
lang-roles  Nix (NixOS-based) · Ruby/C (osctl tooling — inferred, unconfirmed) 
## readme (verbatim signal)
- "vpsAdminOS is a small OS serving as a host for unprivileged Linux system containers. It is based on NixOS and not-os"
- "designed to run full distributions inside unprivileged containers which look and feel as much as a virtual machine as possible"
- "developed and used in production by vpsFree.cz, a non-profit... provides virtual servers to its members"
- components: LTS kernel + out-of-tree patches, runit init, ZFS storage, osctl (own container mgmt tool), LXC
## #graph (harvested, unresolved)
- "based on NixOS and not-os" → dep-fact (Nix ecosystem: devenv 01, den 12, stereOS?) — not an edge; hold thematic
