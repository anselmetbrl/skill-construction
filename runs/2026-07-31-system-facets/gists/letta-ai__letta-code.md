# gist — letta-ai/letta-code · seed 09

    source · dossiers/letta-ai__letta-code.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    an agent harness whose stated aim is agents resembling people rather than tools
      ← "Letta Code is a stateful agent harness for creating agents that are more like
         people than tools. Letta Code agents have memory, identity, and a sense of
         experience over time."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    what it claims is distinctive is self-modification reaching the harness itself
      ← "They learn and evolve over long horizons through rewriting their own memory,
         skills, prompts, and even the harness itself (through mods)."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)

## why-it-is

    #void — the readme never states the need. it opens on what the agents ARE and moves
      to a feature table. no span says what failed in stateless harnesses or for whom.

## how-it-is · technology (internal)

    memory is version-controlled with git and can be synced to a repository
      ← "All context (including memory blocks) is tracked via git. Sync context to a
         custom GitHub repository by setting `/memory-repository set git@github.com:...`"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    skills load from three scopes — global, project, and per-agent
      ← "Loads global skills (`~/.letta`), project-scoped skills (`.agents/skills`), and
         agent-scoped skills (stored in MemFS)."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    agents can invoke agents, including themselves
      ← "Call built-in subagents (general-purpose, forked, recall, history-analyzer) async
         or sync. Agents can call any other agent (including themselves) as subagents"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    context revision is scheduled, not only reactive
      ← "Configure periodic dreaming with `/sleeptime`, audit memory quality with
         `/doctor`, and view memory with `/palace`"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)

## how-it-is · technicality (external)

    installed from npm, with a Nix flake documented as a first-class alternative
      ← "npm install -g @letta-ai/letta-code" · "Nix users can run or install Letta Code
         through the repository flake: `nix run github:letta-ai/letta-code` … See
         [docs/nix.md](docs/nix.md) for Home Manager and NixOS service examples."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    the harness runs anywhere while agent state lives in the vendor's cloud
      ← "Agents stored in Letta Cloud keep their memory, identity, and conversations there
         while the Letta Code harness can run on any connected computer: your laptop,
         [GitHub Actions], a managed cloud sandbox, a remote VM, or a Mac Mini."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    model keys are the user's own, swappable at runtime
      ← "Run `/connect` to configure your own LLM API keys (OpenAI / ChatGPT, Anthropic,
         Z.ai coding plan, etc.), and use `/model` to swap models."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    skills can be installed from third-party hubs, not only from this project
      ← "| GitHub | `letta skills install https://github.com/owner/repo` … | [ClawHub]
         (https://clawhub.ai/) | `openclaw skills install <skill-slug>` → `letta skills
         install <skill-slug>` |"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)

## leaves — earned, not padded

    configuration is delegated to the agent rather than documented for the user
      ← "> [!TIP] > Letta Code agents are designed to be self-configuring. If you want to
         configure something (e.g. skills, behavior, hooks, permissions), try asking your
         agent to do it for you."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    any machine can be enrolled as a named execution environment
      ← "Any machine can be made into an available environment by running: `letta server`
         / `letta server --env-name \"work-laptop\"`"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    the research lineage is named with papers rather than asserted
      ← "Letta Code is developed by the creators of [MemGPT](https://arxiv.org/abs/
         2310.08560) and [sleep-time compute](https://arxiv.org/abs/2504.13171) (now
         called \"dreaming\")"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)

#graph-harvest

    "Letta Code is developed by the creators of [MemGPT](https://arxiv.org/abs/2310.08560)"
      (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
      → names `MemGPT` — which seed 08's readme states is that project's former name
    "| [ClawHub](https://clawhub.ai/) | `openclaw skills install <skill-slug>` → `letta
      skills install <skill-slug>` |"
      (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
      → names `ClawHub` · names `openclaw`
    "| [Hermes Skills Hub](https://hermes-agent.nousresearch.com/docs/skills/) | `hermes
      skills install <skill-path>` → `letta skills install <skill-path>` |"
      (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
      → names `Hermes Skills Hub`

## flags

    hype · anthropomorphic properties asserted as description, in the opening two lines
      ← "creating agents that are more like people than tools. Letta Code agents have
         memory, identity, and a sense of experience over time."
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    unfree? · two feature-table rows are account-gated, stated plainly in the table
      ← "[Remote & Multi-Env](https://docs.letta.com/letta-code/client-server-architecture)
         (requires signing in with Letta)" · "[Secrets](https://docs.letta.com/letta-code/
         secrets) (requires signing in with Letta)"
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    filler · the readme embeds a remote analytics beacon that fires on render
      ← "src=\"https://static.scarf.sh/a.png?x-pxid=76801c33-8e75-4055-8eea-2c8092519a90
         &page=README.md\""
         (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    abandonment
      #void — none. this is the repo seed 08 declares development moved TO
    contribution
      #void — none found in the frozen material
    contradiction
      #void — none found in the frozen material

## finding — the naming is one-directional

    seed 08's readme names this repo three times, including its handover notice. this
      readme names seed 08 nowhere. the asymmetry is evidence the user may want when
      ruling the edge, and it is recorded rather than smoothed
      #void — an observation about the sources, carrying no claim about either project
