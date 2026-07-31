---
status: ok
seed: 11
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests, LICENSE) · R4 WebFetch (page facts)
---

# papercomputeco/stereOS

    url          https://github.com/papercomputeco/stereOS
    description  "A Linux based operating system hardened and purpose built for AI
                 agents"   ← About field, verbatim (R4)
    site         https://stereos.ai/

## #git

    stars          486                     (R4)
    forks          30                      (R4)
    watchers       4                       (R4)
    license        GitHub reports "Not visible" (R4) — the auto-detector did not
                   classify it. FETCHED DIRECTLY (R1, LICENSE at root, 200):
                   "The stereOS NixOS configurations are licensed under the GNU Affero
                    General Public License v3.0 (AGPL-3.0)."
                   → AGPL-3.0, stated in the file, behind a custom preamble that
                     evidently defeats GitHub's classifier. the discrepancy is the
                     finding; both sources recorded.
    open-issues    5                       (R4)
    open-prs       2                       (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     nix   ← flake.nix at root (R1); the readme is written in NixOS-module
                         terms throughout (S8, S9, S12)
                   make  ← Makefile at root (R1). purpose not stated in readme → #void.
    deep-links     readme   https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md
                   license  https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/LICENSE
                   site     https://stereos.ai/
                   stereosd https://github.com/papercomputeco/stereosd
                   agentd   https://github.com/papercomputeco/agentd
                   dist-lib lib/dist.nix
                   dev-prof profiles/dev.nix

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "A Linux based operating system hardened and purpose-built for AI agents."
    S2  "stereOS produces machine images - called **mixtapes** - that bundle a hardened,
         minimal Linux system with specific AI agent harnesses."
    S3  "| `opencode-mixtape` | `opencode` | `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` |"
                                                        ← the Mixtapes table, ONE row
    S4  "Each mixtape appends its agent package to `stereos.agent.extraPackages`, which
         adds the binary to the agent user's restricted PATH."
    S5  "The `-dev` variant of each mixtape includes `profiles/dev.nix` for local SSH key
         injection."
    S6  "The stereOS system is minimal in nature with several orchestration daemons
         handling agent lifecycle and acting as a control plane for agent operators:"
    S7  "* `admin` user and group for administrative operations: `/home/admin` * `agent`
         user and group for agent to assume: `/home/agent/workspace`"
    S8  "* [`stereosd`](https://github.com/papercomputeco/stereosd) - stereOS system
         daemon * [`agentd`](https://github.com/papercomputeco/agentd) - agent management
         daemon"
    S9  "| Raw EFI | `system.build.raw` | `stereos.img` | Canonical artifact. Apple Virt
         Framework bootable |"                          ← Image formats table
    S10 "The Lambda MicroVM source bundle is not a full stereOS VM image. It packages
         stereOS userspace into a Dockerfile-based rootfs bundle because AWS Lambda
         MicroVM images are created from Dockerfile application sources, not custom
         kernel or disk artifacts."
    S11 "`lib/dist.nix:mkDist` assembles all formats into a publish-ready directory with
         zstd-compressed variants (`-19 -T0`) and a `mixtape.toml` manifest containing
         SHA-256 checksums and file sizes for every artifact"
    S12 "stereOS declares two custom options: | `stereos.ssh.authorizedKeys` | `listOf
         str` | `[]` | SSH public keys for admin and agent users. Useful for development
         purposes. | | `stereos.agent.extraPackages` | `listOf package` | `[]` | Packages
         added to the agent's restricted PATH |"
    S13 "| `nixpkgs` | `nixos-26.05` | Base packages |"  ← External dependencies table
    S14 "| `dagger` | `github:dagger/nix` | CI engine |" ← External dependencies table
    S15 "Copyright (c) 2026 Paper Compute Co. All rights reserved."      ← LICENSE (R1)
    S16 "System images built from stereOS are aggregates of independently licensed
         components. No single license governs the image as a whole."   ← LICENSE (R1)
    S17 "Consult each package's license metadata (available via `nix-store --query
         --references` or the image SBOM) to determine obligation."     ← LICENSE (R1)

## potential-relation spans — collected, NOT resolved

    "| `nixpkgs` | `nixos-26.05` | Base packages |" (readme, S13)
       → names `nixpkgs` — a dependency. #git fact, not an edge.
    "| `agentd` | `github:papercomputeco/agentd` |" · "| `stereosd` |
     `github:papercomputeco/stereosd` |" (readme, External dependencies table)
       → names two SAME-OWNER repos, neither a seed of this run.
    "| `dagger` | `github:dagger/nix` | CI engine |" (readme, S14)
       → names `dagger/nix` — a dependency, out of collection.
    "| `opencode-mixtape` | `opencode` |" (readme, S3)
       → names `opencode` — a bundled agent harness, out of collection.
    "`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`" (readme, S3)
       → names model VENDORS by env-var. not projects in this collection.

## flags-raw — what fetch itself revealed

    thin?          the readme is 3.8 KB and is almost entirely BUILD-ARTIFACT reference:
                   image formats, distribution layout, NixOS options, dependency table.
                   the why-it-is content is one line (S1). recorded as a fact — a gist
                   leaf beyond what/how will likely be #void, and that is a FINDING.
    index-repo?    no.
    archived/moved no notice.
    licence-flag   the About panel reports no license while the repo DOES carry an
                   AGPL-3.0 LICENSE with an "All rights reserved." copyright line above
                   it (S15). the two lines sit in the same file. recorded verbatim,
                   both of them, unresolved — the reading is the user's.
    note-for-gist  the Mixtapes table advertises a plural ("mixtapes") and lists ONE
                   row (S3). recorded as a count of the material, not a judgment.
    note-for-gist  no promotional superlatives found. "hardened" (S1, S2) is asserted
                   twice without a span defining what hardening it means → the CLAIM is
                   recorded; its substantiation in this readme is #void.
