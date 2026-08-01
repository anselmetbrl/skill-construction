# gist — vpsfreecz/vpsadminos · seed 10

    source · dossiers/vpsfreecz__vpsadminos.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a small host OS whose entire job is running unprivileged system containers
      ← "vpsAdminOS is a small OS serving as a host for unprivileged Linux system
         containers."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)

## why-it-is

    the goal is stated as a felt property — containers that pass for virtual machines
      ← "It is designed to run full distributions inside unprivileged containers which
         look and feel as much as a virtual machine as possible."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    and the need is grounded in a named operator running it in production
      ← "vpsAdminOS is developed and used in production by [vpsFree.cz](https://vpsfree.cz),
         a non-profit organization which provides virtual servers to its members."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)

## how-it-is · technology (internal)

    the base is named honestly, and it is two projects rather than one
      ← "It is based on [NixOS](https://nixos.org) and [not-os](https://github.com/
         cleverca22/not-os/)."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    the kernel is patched rather than taken as-is, specifically for containers
      ← "vpsAdminOS uses: - [LTS kernel with a mix of out-of-tree patches]
         (https://github.com/vpsfreecz/linux) to improve container experience,"
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    the stack is named component by component, with no layer left implied
      ← "- runit as an init system, - ZFS for storage," · "- LXC is used to run the
         containers, - BIRD for network routing."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    container management is its own tool, written for this purpose
      ← "- our own tools for system container management called [osctl]
         (https://man.vpsadminos.org/man8/osctl.8.html),"
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)

## how-it-is · technicality (external)

    it pins its own nixpkgs, so the host does not depend on ambient Nix state
      ← "vpsAdminOS is developed on top of the latest NixOS release and pins nixpkgs in
         `flake.lock`, so you do not need to set `NIX_PATH`."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    building the whole OS is two make targets, one of them a VM
      ← "# Build the OS / make / # Run under qemu / make qemu"
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    a project-run binary cache exists specifically to avoid rebuilding the kernel
      ← "vpsAdminOS has its own binary cache which contains builds of vpsAdminOS with the
         current NixOS stable branch. Using it can save a lot of time building the
         kernel."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)

## leaves — earned, not padded

    the container lifecycle is a small verb set on one command
      ← "osctl ct new --distribution alpine myct01" · "osctl ct start myct01" · "osctl ct
         attach myct01"
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    networking offers two explicit models, bridged and routed
      ← "# Bridged veth / osctl ct netif new bridge --link lxcbr0 myct01 eth0 / # Routed
         veth / osctl ct netif new routed myct01 eth1"
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    the heaviest storage test suite is opt-in, not part of CI
      ← "OpenZFS full-suite execution is available as an explicit `test-runner` tag and is
         not part of default `-t ci` runs."
         (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)

#graph-harvest

    "It is based on [NixOS](https://nixos.org) and [not-os](https://github.com/
      cleverca22/not-os/)."
      (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
      → names `NixOS` · names `cleverca22/not-os`

## flags

    hype
      #void — none found. the readme calls itself "a small OS", names its base rather
      than claiming novelty, and makes no comparative or superlative claim anywhere
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material
