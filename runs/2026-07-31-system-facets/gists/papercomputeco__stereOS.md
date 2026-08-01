# gist — papercomputeco/stereOS · seed 11

    source · dossiers/papercomputeco__stereOS.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    an OS built for one occupant — an AI agent — rather than for a user
      ← "A Linux based operating system hardened and purpose-built for AI agents."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    what it actually emits is images that pair a minimal system with one agent harness
      ← "stereOS produces machine images - called **mixtapes** - that bundle a hardened,
         minimal Linux system with specific AI agent harnesses."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)

## why-it-is

    #void — the readme never states the need. "hardened" is asserted twice without a
      span saying what threat is being hardened against, or what happens when an agent
      runs on an ordinary system instead. the why is absent, not merely brief.

## how-it-is · technology (internal)

    the agent is confined by a restricted PATH that each image extends deliberately
      ← "Each mixtape appends its agent package to `stereos.agent.extraPackages`, which
         adds the binary to the agent user's restricted PATH."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    privilege is split into two accounts with separate homes
      ← "* `admin` user and group for administrative operations: `/home/admin` * `agent`
         user and group for agent to assume: `/home/agent/workspace`"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    two daemons hold the lifecycle, and they live in separate repositories
      ← "* [`stereosd`](https://github.com/papercomputeco/stereosd) - stereOS system daemon
         * [`agentd`](https://github.com/papercomputeco/agentd) - agent management daemon"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    the whole configuration surface it adds is two NixOS options
      ← "stereOS declares two custom options: | `stereos.ssh.authorizedKeys` … |
         `stereos.agent.extraPackages` | `listOf package` | `[]` | Packages added to the
         agent's restricted PATH |"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)

## how-it-is · technicality (external)

    one raw disk image is canonical and the other formats derive from it
      ← "| Raw EFI | `system.build.raw` | `stereos.img` | Canonical artifact. Apple Virt
         Framework bootable |"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    distribution ships checksums and sizes for every artifact, as a manifest
      ← "`lib/dist.nix:mkDist` assembles all formats into a publish-ready directory with
         zstd-compressed variants (`-19 -T0`) and a `mixtape.toml` manifest containing
         SHA-256 checksums and file sizes for every artifact"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    one target is explicitly NOT a stereOS image, and the readme says why
      ← "The Lambda MicroVM source bundle is not a full stereOS VM image. It packages
         stereOS userspace into a Dockerfile-based rootfs bundle because AWS Lambda
         MicroVM images are created from Dockerfile application sources, not custom kernel
         or disk artifacts."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)

## leaves — earned, not padded

    the development variant is separated from the shipping one by SSH key injection
      ← "The `-dev` variant of each mixtape includes `profiles/dev.nix` for local SSH key
         injection."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    the licence disclaims governing the images it produces, and says how to check
      ← "System images built from stereOS are aggregates of independently licensed
         components. No single license governs the image as a whole. Consult each
         package's license metadata (available via `nix-store --query --references` or the
         image SBOM) to determine obligation."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/LICENSE)

#graph-harvest

    #void — no span positions stereOS against a named alternative. every name in the
      readme is a dependency, a same-owner daemon, or a bundled agent binary; none is a
      rival, and none resolves into this collection.

## flags

    hype · "hardened" is asserted twice as the defining property with no span defining
      what hardening it means
      ← "A Linux based operating system hardened and purpose-built for AI agents." ·
         "images … that bundle a hardened, minimal Linux system"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    contradiction · the licence file opens by reserving all rights and then grants AGPL
      ← "Copyright (c) 2026 Paper Compute Co. All rights reserved." · "The stereOS NixOS
         configurations are licensed under the GNU Affero General Public License v3.0
         (AGPL-3.0)."
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/LICENSE)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated

## finding — the shape of this readme

    the material is almost entirely build-artifact reference: image formats, distribution
      layout, NixOS options, dependency table. the why-it-is void above is a property of
      the source, not of the reading
      #void — an observation about the source, carrying no claim about the project

## finding — a plural advertised, one instance shipped

    the Mixtapes table announces a category and lists a single row
      ← "| Mixtape | Agent binary | API key | |---------|-------------|---------| |
         `opencode-mixtape` | `opencode` | `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` |"
         (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
