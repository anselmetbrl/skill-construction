---
status: ok
seed: 09
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# letta-ai/letta-code

    url          https://github.com/letta-ai/letta-code
    description  "Stateful agents that are like people, with memory, identity, and the
                 ability to learn and adapt"   ← About field, verbatim (R4)
    site         https://docs.letta.com/letta-code/cli

## #git

    stars          2.9k                    (R4)
    forks          342                     (R4)
    watchers       9                       (R4)
    license        Apache-2.0              (R4)
    open-issues    90                      (R4)
    open-prs       104                     (R4)
    release-tag    #void — R2 gated, atom feeds gated. readme carries an npm version
                   BADGE whose rendered value is absent from raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     js/ts ← package.json at root (R1); distributed via npm as
                          `@letta-ai/letta-code` (S13)
                   nix   ← flake.nix at root (R1); readme documents it: "Nix users can
                          run or install Letta Code through the repository flake" (S22)
    deep-links     readme    https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md
                   docs      https://docs.letta.com/letta-code/cli
                   memory    https://docs.letta.com/letta-code/memory
                   memfs     https://docs.letta.com/letta-code/memfs
                   skills    https://docs.letta.com/letta-code/skills
                   subagents https://docs.letta.com/letta-code/subagents
                   hooks     https://docs.letta.com/letta-code/hooks
                   channels  https://github.com/letta-ai/letta-code/blob/main/src/channels/README.md
                   nix-doc   docs/nix.md
                   research  https://www.letta.com/research

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "Letta Code is a stateful agent harness for creating agents that are more like
         people than tools."
    S2  "Letta Code agents have memory, identity, and a sense of experience over time."
    S3  "They learn and evolve over long horizons through rewriting their own memory,
         skills, prompts, and even the harness itself (through mods)."
    S4  "Letta Code can be used interactively, or to power always-on agents that work
         proactively."
    S5  "> [!TIP] > Letta Code agents are designed to be self-configuring. If you want to
         configure something (e.g. skills, behavior, hooks, permissions), try asking your
         agent to do it for you."
    S6  "Agents programmatically rewrite their context to improve and adapt over time,
         including system prompt learning (through [memory blocks]) and [skill learning].
         Configure periodic dreaming with `/sleeptime`, audit memory quality with
         `/doctor`, and view memory with `/palace`"          ← feature table
    S7  "All context (including memory blocks) is tracked via git. Sync context to a
         custom GitHub repository by setting `/memory-repository set git@github.com:...`"
                                                             ← feature table, MemFS
    S8  "Loads global skills (`~/.letta`), project-scoped skills (`.agents/skills`), and
         agent-scoped skills (stored in MemFS). View skills with `/skills` and create
         with `/skill-creator`"                              ← feature table, Skills
    S9  "Call built-in subagents (general-purpose, forked, recall, history-analyzer) async
         or sync. Agents can call any other agent (including themselves) as subagents"
                                                             ← feature table
    S10 "Run custom scripts at key points of agent execution to automate workflows"
                                                             ← feature table, Hooks
    S11 "Configure heartbeats and crons, and let agents work across time with
         self-managed schedules"                             ← feature table
    S12 "Make secrets available as environment variables (across machines) while
         obfuscating their values from context"              ← feature table, Secrets
    S13 "Install the package via [npm] … `npm install -g @letta-ai/letta-code`"
    S14 "Run `/connect` to configure your own LLM API keys (OpenAI / ChatGPT, Anthropic,
         Z.ai coding plan, etc.), and use `/model` to swap models."
    S15 "Agents stored in Letta Cloud keep their memory, identity, and conversations there
         while the Letta Code harness can run on any connected computer: your laptop,
         [GitHub Actions], a managed cloud sandbox, a remote VM, or a Mac Mini."
    S16 "Run `/login` from the CLI or sign in through the desktop app to access agents in
         your Letta account."
    S17 "Any machine can be made into an available environment by running: `letta server`
         / `letta server --env-name \"work-laptop\"`"
    S18 "[Remote & Multi-Env](…) (requires signing in with Letta)"   ← feature table
    S19 "[Secrets](…) (requires signing in with Letta)"              ← feature table
    S20 "Install skills into a specific agent's memory with `letta skills install
         <skill>`"
    S21 "Letta Code is developed by the creators of [MemGPT](https://arxiv.org/abs/
         2310.08560) and [sleep-time compute](https://arxiv.org/abs/2504.13171) (now
         called \"dreaming\"), and driven by our [research](https://www.letta.com/research)
         in AI memory and continual learning."
    S22 "Nix users can run or install Letta Code through the repository flake: `nix run
         github:letta-ai/letta-code` / `nix profile install github:letta-ai/letta-code`
         / See [docs/nix.md](docs/nix.md) for Home Manager and NixOS service examples."
    S23 "Community maintained packages are available for Arch Linux users on the [AUR]"
    S24 "Made with 💜 in San Francisco"

## potential-relation spans — collected, NOT resolved

    "Letta Code is developed by the creators of [MemGPT](https://arxiv.org/abs/2310.08560)"
     (readme, S21)   → names `MemGPT` — which seed 08's readme states is this same
                       organisation's FORMER name ("# Letta (formerly MemGPT)").
                       resolution is the workbench's mechanical job.
    "[ClawHub](https://clawhub.ai/) | `openclaw skills install <skill-slug>` →
     `letta skills install <skill-slug>`" (readme, skills table)
       → names `ClawHub` / `openclaw` — a skill SOURCE, out of collection.
    "[Hermes Skills Hub](https://hermes-agent.nousresearch.com/docs/skills/) |
     `hermes skills install <skill-path>` → `letta skills install <skill-path>`"
     (readme, skills table)
       → names `Hermes Skills Hub` — a skill SOURCE, out of collection.
    "Run `/connect` to configure your own LLM API keys (OpenAI / ChatGPT, Anthropic,
     Z.ai coding plan, etc.)" (readme, S14)
       → names model VENDORS. not projects in this collection.
    "[GitHub Actions](https://github.com/letta-ai/letta-code-action)" (readme, S15)
       → names `letta-ai/letta-code-action` — same owner, NOT a seed of this run.

    NOTE for the workbench: seed 08's readme names THIS repo by explicit URL three
    times, including the handover span "Active development has moved to". this repo's
    own readme does NOT name seed 08 anywhere. the naming is ONE-DIRECTIONAL, and that
    asymmetry is itself evidence the user may want when ruling the edge.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice. this is the repo seed 08 declares active development
                   moved TO.
    note-for-gist  S1-S3 are anthropomorphic register asserted as description — "more
                   like people than tools", "identity", "a sense of experience over
                   time". recorded as spans, in the project's own words.
    note-for-gist  paywall/unfree? — TWO feature-table rows carry "(requires signing in
                   with Letta)": Remote & Multi-Env (S18) and Secrets (S19). the package
                   is Apache-2.0 and npm-installable, and cloud hosting being paid is
                   not itself the flag; whether account-gating these two features
                   crosses into crippled self-hosting is the USER's subtraction. both
                   spans recorded verbatim so the judgment has its evidence.
    note-for-gist  the readme embeds a scarf.sh tracking pixel, as seed 08's does.
                   recorded as a FACT.
    note-for-gist  this repo's subject matter — skills, subagents, hooks, memory,
                   permissions — overlaps the machinery of the run executing it. no
                   observation is drawn from that here; cross-repo statements are
                   session material and statements about the USER are forbidden outright.
