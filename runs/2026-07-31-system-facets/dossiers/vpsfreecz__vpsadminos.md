---
status: ok
seed: 10
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# vpsfreecz/vpsadminos

    url          https://github.com/vpsfreecz/vpsadminos
    description  "Host for Linux system containers based on NixOS, ZFS and LXC"
                 ← About field, verbatim (R4)
    site         https://vpsadminos.org/

## #git

    stars          185                     (R4)
    forks          30                      (R4)
    watchers       9                       (R4)
    license        MIT                     (R4)
    open-issues    10                      (R4)
    open-prs       0                       (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     nix    ← flake.nix at root (R1); "pins nixpkgs in `flake.lock`" (S10)
                   ruby   ← Gemfile at root (R1). the readme does NOT name Ruby →
                            the ROLE is manifest-evidenced, its purpose is #void.
                   make   ← Makefile at root (R1); "# Build the OS / make" (S11)
    deep-links     readme    https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md
                   docs      https://vpsadminos.org/
                   man       https://man.vpsadminos.org/
                   ref       https://ref.vpsadminos.org/
                   iso       https://iso.vpsadminos.org/
                   osctl-man https://man.vpsadminos.org/man8/osctl.8.html
                   example-cfg https://github.com/vpsfreecz/vpsfree-cz-configuration
                   kernel    https://github.com/vpsfreecz/linux
                   cache     https://cache.vpsadminos.org

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "vpsAdminOS is a small OS serving as a host for unprivileged Linux system
         containers."
    S2  "It is based on [NixOS](https://nixos.org) and [not-os](https://github.com/
         cleverca22/not-os/)."
    S3  "It is designed to run full distributions inside unprivileged containers which
         look and feel as much as a virtual machine as possible."
    S4  "vpsAdminOS is developed and used in production by [vpsFree.cz](https://vpsfree.cz),
         a non-profit organization which provides virtual servers to its members."
    S5  "See [vpsfree-cz-configuration](https://github.com/vpsfreecz/vpsfree-cz-configuration)
         for example cluster configuration."
    S6  "vpsAdminOS uses: - [LTS kernel with a mix of out-of-tree patches]
         (https://github.com/vpsfreecz/linux) to improve container experience,"
    S7  "- runit as an init system, - ZFS for storage,"
    S8  "- our own tools for system container management called [osctl]
         (https://man.vpsadminos.org/man8/osctl.8.html),"
    S9  "- LXC is used to run the containers, - BIRD for network routing."
    S10 "vpsAdminOS is developed on top of the latest NixOS release and pins nixpkgs in
         `flake.lock`, so you do not need to set `NIX_PATH`. Ensure flakes are enabled
         (Nix >= 2.4 or `experimental-features = nix-command flakes` in `nix.conf`)."
    S11 "vpsAdminOS can now be built and run: / # Build the OS / make / # Run under qemu
         / make qemu"
    S12 "Our kernel live-patch facility requires [ccache](https://wiki.nixos.org/wiki/
         CCache) to build the OS."
    S13 "The QEMU runner creates two disk images - `sda.img` and `sdb.img` which are added
         as QEMU ATA drives and can be used to create a mirrored ZFS pool that persists
         across reboots."
    S14 "OpenZFS full-suite execution is available as an explicit `test-runner` tag and is
         not part of default `-t ci` runs."
    S15 "# Configure osctld: / osctl pool install tank / # Create a container: / osctl ct
         new --distribution alpine myct01"
    S16 "# Bridged veth / osctl ct netif new bridge --link lxcbr0 myct01 eth0 / # Routed
         veth / osctl ct netif new routed myct01 eth1"
    S17 "vpsAdminOS has its own binary cache which contains builds of vpsAdminOS with the
         current NixOS stable branch. Using it can save a lot of time building the
         kernel."
    S18 "substituters = [ \"https://cache.vpsadminos.org\" ]; trusted-public-keys =
         [ \"cache.vpsadminos.org:wpIJlNZQIhS+0gFf1U3MC9sLZdLW3sh5qakOWGDoDrE=\" ];"
    S19 "* IRC: #vpsadminos @ irc.libera.chat"

## potential-relation spans — collected, NOT resolved

    "It is based on [NixOS](https://nixos.org) and [not-os](https://github.com/
     cleverca22/not-os/)." (readme, S2)
       → names `NixOS` · names `cleverca22/not-os`
    "vpsAdminOS uses: … runit as an init system, ZFS for storage, … LXC is used to run
     the containers, BIRD for network routing." (readme, S7+S9)
       → names `runit` · `ZFS` · `LXC` · `BIRD` — COMPONENTS. #git facts, not edges.
    "[LTS kernel with a mix of out-of-tree patches](https://github.com/vpsfreecz/linux)"
     (readme, S6)   → names `vpsfreecz/linux` — same owner, NOT a seed of this run.
    "https://linuxcontainers.org/" (readme, Docs list)
       → names `linuxcontainers.org` — a doc pointer, out of collection.

    NOTE for the workbench: several seeds of this run carry `flake.nix` and name NixOS.
    a SHARED DEPENDENCY is not a relation edge and will not be proposed as one. only a
    span that positions one seed AGAINST or ALONGSIDE another named seed can become an
    edge, and its type is the user's ruling.

## flags-raw — what fetch itself revealed

    thin?          the readme is short (3.8 KB) and is structured as an install/usage
                   guide. the what/why content is its first paragraph. recorded.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  no promotional register found. the readme states scope plainly
                   ("a small OS"), names its base honestly (S2), and names its operator
                   and funding context (S4). the ABSENCE of hype is recorded as an
                   observation about the material, not as praise.
    note-for-gist  S4 is a production-use claim with a named non-profit operator behind
                   it — an unusually checkable provenance statement. recorded as a span
                   for the user to weigh; not verified by this run.
