---
status: ok
seed: 08
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# letta-ai/letta

    url          https://github.com/letta-ai/letta
    description  "Platform for stateful agents: AI with advanced memory that can learn
                 and self-improve over time."   ← About field, verbatim (R4)
    site         https://docs.letta.com

## #git

    stars          24.0k                   (R4)
    forks          2.6k                    (R4)
    watchers       138                     (R4)
    license        Apache-2.0              (R4)
    open-issues    25                      (R4)
    open-prs       24                      (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4. the readme makes a CLAIM about
                   contributor scale — "over a hundred contributors" (S12) — which is a
                   project statement, not a fetched count.
    lang-roles     python ← pyproject.toml at root (R1); the V1 SDK is named
                          `letta-client` for Python (S11)
                   NOTE the readme's own quickstart is TypeScript/npm throughout
                          (S5-S9) and points at other repos for it. the manifest and
                          the readme's foreground language DISAGREE — recorded, not
                          resolved.
    deep-links     readme    https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md
                   docs      https://docs.letta.com/letta-agent
                   agent-sdk https://docs.letta.com/letta-agent-sdk/overview
                   app-server https://docs.letta.com/letta-agent/app-server
                   quickstart https://docs.letta.com/letta-agent-sdk/quickstart
                   v1-sdks   https://docs.letta.com/api-overview/client-sdks
                   leaderboard https://leaderboard.letta.com/
                   agents-md AGENTS.md

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "# Letta (formerly MemGPT)"
    S2  "Build AI with advanced memory that can learn and self-improve over time."
    S3  "> [!NOTE] > This repository contains the legacy Letta server (the API server
         behind the Letta V1 API and SDKs). Active development has moved to the [Letta
         Agent repo](https://github.com/letta-ai/letta-code), and self-hosting an API
         server is now done via the [App Server](https://docs.letta.com/letta-agent/
         app-server). See [AGENTS.md](AGENTS.md) for details."
    S4  "* [Letta Agent](https://docs.letta.com/letta-agent): run agents locally in your
         terminal, via the desktop app, or via channels like Slack"
    S5  "Requires [Node.js 22.19+](https://nodejs.org/en/download)"
    S6  "1. Install the [Letta Code](https://github.com/letta-ai/letta-code) CLI tool:
         `npm install -g @letta-ai/letta-code`"
    S7  "When running the CLI tool, your agent can help you code and do any task you can
         do on your computer."
    S8  "Letta Code supports [skills](https://docs.letta.com/letta-agent/skills) and
         [subagents](https://docs.letta.com/letta-agent/subagents), and bundles pre-built
         skills/subagents for advanced memory and continual learning."
    S9  "Letta is fully model-agnostic, though we recommend the latest Anthropic, OpenAI,
         and zAI models for best performance (see our [model leaderboard]
         (https://leaderboard.letta.com/) for our rankings)."
    S10 "The SDK can run agents on [Constellation](https://docs.letta.com/letta-agent/
         constellation) (Letta's agent cloud), fully locally on your machine, or against
         a self-hosted [App Server](https://docs.letta.com/letta-agent/app-server)."
    S11 "The previous-generation [V1 SDKs](https://docs.letta.com/guides/get-started/intro)
         (`@letta-ai/letta-client` for TypeScript, `letta-client` for Python) target the
         Letta API directly and are still available … We recommend the Agent SDK for new
         projects."
    S12 "Letta is an open source project built by over a hundred contributors from around
         the world. There are many ways to get involved in the Letta OSS project!"
    S13 "Below is a quick example of creating a stateful agent and streaming a
         conversation with it (requires a [Letta API key](https://app.letta.com/api-keys))."
    S14 "human: \"Name: Timber. Status: dog. Occupation: building Letta, infrastructure to
         democratize self-improving superintelligence\", persona: \"I am a self-improving
         superintelligence. Timber is my best friend and collaborator.\""
                                                        ← the Hello World code example
    S15 "To run the same agent fully locally (the SDK spawns [Letta Code]
         (https://github.com/letta-ai/letta-code) on your machine as a subprocess), swap
         out the client: `const client = new LettaAgentClient({ backend: \"local\" });`"
    S16 "***Legal notices**: By using Letta and related Letta services (such as the Letta
         endpoint or hosted service), you are agreeing to our [privacy policy] … and
         [terms of service].*"

## potential-relation spans — collected, NOT resolved

    "Active development has moved to the [Letta Agent repo]
     (https://github.com/letta-ai/letta-code)" (readme, S3)
       → names `letta-ai/letta-code` — SEED 09 OF THIS RUN, by explicit URL.
    "This repository contains the legacy Letta server" (readme, S3)
       → the same span carries the direction: THIS repo is named legacy relative to it.
    "1. Install the [Letta Code](https://github.com/letta-ai/letta-code) CLI tool"
     (readme, S6)  ·  "the SDK spawns [Letta Code] … as a subprocess" (readme, S15)
       → names `letta-ai/letta-code` twice more, as install-target and as subprocess.
    "# Letta (formerly MemGPT)" (readme, S1)
       → names `MemGPT` — a former NAME of this same project, not a separate thing.
    "we recommend the latest Anthropic, OpenAI, and zAI models" (readme, S9)
       → names model VENDORS. not projects in this collection.

    NOTE for the workbench: this is the run's first relation span that resolves to a
    collection member by explicit URL rather than by name-guess. the flag F2 raised at
    phase 1 — "a shared owner is NOT an edge" — is now separately EVIDENCED by the
    material itself. the TYPE remains the user's ruling; the two available types are
    alternative-to and conflicts-with, and a legacy/successor span may fit NEITHER.
    that is a candidate for [proposal: new relation type], never coined here.

## flags-raw — what fetch itself revealed

    thin?          the readme is short (4.7 KB) for a 24.0k-star repo, and most of it
                   routes the reader ELSEWHERE (docs.letta.com, letta-code, App Server).
                   recorded as a fact.
    index-repo?    no.
    archived/moved NOT archived on the page, but S3 is a self-declared handover notice:
                   "legacy" + "Active development has moved to". this is the
                   abandonment-as-dated-FACTS material the gist flags — except it
                   carries NO date. the direction is stated; the when is #void.
    note-for-gist  S14 — the shipped Hello World example sets a persona of "a
                   self-improving superintelligence" and a human-block describing
                   "infrastructure to democratize self-improving superintelligence".
                   this is the project's own promotional register appearing inside
                   executable sample code. recorded as a span.
    note-for-gist  the readme embeds a scarf.sh tracking pixel
                   (static.scarf.sh/a.png?x-pxid=…&page=README.md) — a readme-render
                   analytics beacon. recorded as a FACT; the user weighs it.
