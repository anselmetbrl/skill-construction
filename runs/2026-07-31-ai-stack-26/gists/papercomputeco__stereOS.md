# papercomputeco/stereOS
what-it-is   a hardened, minimal Linux OS purpose-built to host AI agents
why-it-is    AI agents need a locked-down, controlled host with a lifecycle/control plane, not a general desktop
how-it-is
  technology   NixOS-style build (`system.build.raw/qcow2`); orchestration daemons `stereosd` + `agentd`
  technicality ships "mixtapes" — machine images bundling an agent harness (e.g. opencode); raw EFI / QCOW2 images; restricted `agent` user PATH
leaves       "mixtapes that bundle a hardened, minimal Linux system with specific AI agent harnesses" · control plane for agent operators
flags        none
trust        whole
#graph       AI-agent infra theme: obscura (07), screenpipe (25), letta-code (09) · Nix cluster: devenv, den, vpsadminos, yo
