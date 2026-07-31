status: ok
# papercomputeco/stereOS
url          https://github.com/papercomputeco/stereOS
description  "A Linux based operating system hardened and purpose built for AI agents"
## #git
stars 486 · forks 30 · license #void(not shown) · open-issues 5 · release #void
lang-roles  Nix (NixOS-style build attrs: system.build.raw/qcow2, stereos.agent.extraPackages)
## readme (verbatim signal)
- "A Linux based operating system hardened and purpose-built for AI agents"
- "produces machine images - called mixtapes - that bundle a hardened, minimal Linux system with specific AI agent harnesses" (e.g. opencode-mixtape → opencode binary)
- "orchestration daemons handling agent lifecycle and acting as a control plane for agent operators": stereosd, agentd; restricted `agent` user PATH
- image formats: Raw EFI (Apple Virt), QCOW2 (QEMU/KVM)
## #graph (harvested, unresolved)
- thematic: AI-agent sandbox/infra (obscura 07, screenpipe 25, letta-code 09) · Nix cluster (devenv 01, den 12, vpsadminos 10, yo 15)
