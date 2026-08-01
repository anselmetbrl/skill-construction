# gist — letta-ai/letta · seed 08

    source · dossiers/letta-ai__letta.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    by its own first note, the LEGACY server of a platform that has moved on
      ← "> [!NOTE] > This repository contains the legacy Letta server (the API server
         behind the Letta V1 API and SDKs). Active development has moved to the [Letta
         Agent repo](https://github.com/letta-ai/letta-code), and self-hosting an API
         server is now done via the [App Server]"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    the platform itself is stated as agents with persistent, self-revising memory
      ← "Build AI with advanced memory that can learn and self-improve over time."
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)

## why-it-is

    #void — the readme states WHAT is built and where development moved, never the need
      it answers. no span argues why stateful memory was required or what failed without
      it. the closest is the About field's assertion, which is a description, not a why.

## how-it-is · technology (internal)

    #void — this repo's readme describes almost no internals of its own. it routes to
      other repos and to docs. the one structural statement it makes about itself is its
      legacy status, already recorded under what-it-is.

## how-it-is · technicality (external)

    the documented entry point is a different repo's npm package
      ← "1. Install the [Letta Code](https://github.com/letta-ai/letta-code) CLI tool:
         `npm install -g @letta-ai/letta-code`"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    the SDK targets three placements — hosted cloud, local, or self-hosted server
      ← "The SDK can run agents on [Constellation] (Letta's agent cloud), fully locally on
         your machine, or against a self-hosted [App Server]."
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    running locally means spawning the successor repo as a subprocess
      ← "To run the same agent fully locally (the SDK spawns [Letta Code]
         (https://github.com/letta-ai/letta-code) on your machine as a subprocess), swap
         out the client"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    model choice is stated as open, with a recommendation attached
      ← "Letta is fully model-agnostic, though we recommend the latest Anthropic, OpenAI,
         and zAI models for best performance"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)

## leaves — earned, not padded

    the previous-generation SDKs are named as still available but no longer advised
      ← "The previous-generation [V1 SDKs] (`@letta-ai/letta-client` for TypeScript,
         `letta-client` for Python) target the Letta API directly and are still available
         … We recommend the Agent SDK for new projects."
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    the hosted path requires a key before the first example runs
      ← "Below is a quick example of creating a stateful agent and streaming a
         conversation with it (requires a [Letta API key](https://app.letta.com/api-keys))."
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)

#graph-harvest

    "Active development has moved to the [Letta Agent repo]
      (https://github.com/letta-ai/letta-code)"
      (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
      → names `letta-ai/letta-code` by explicit URL — a repo IN this collection, seed 09
    "This repository contains the legacy Letta server"
      (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
      → names THIS repo as legacy relative to that one; the span carries the direction
    "the SDK spawns [Letta Code](https://github.com/letta-ai/letta-code) on your machine
      as a subprocess"
      (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
      → names `letta-ai/letta-code` again, as a runtime dependency
    "# Letta (formerly MemGPT)"
      (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
      → names `MemGPT` — a former name of this same project, not a separate thing

## flags

    hype · the shipped example sets an agent persona and a user profile that both assert
      superintelligence, inside runnable sample code
      ← "human: \"Name: Timber. Status: dog. Occupation: building Letta, infrastructure to
         democratize self-improving superintelligence\", persona: \"I am a self-improving
         superintelligence.\""
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    abandonment · a self-declared handover, with a direction and NO date
      ← "> [!NOTE] > This repository contains the legacy Letta server … Active development
         has moved to the [Letta Agent repo]"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    contribution · a contributor-scale claim made by the project about itself, unsourced
      ← "Letta is an open source project built by over a hundred contributors from around
         the world."
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    filler · the readme embeds a remote analytics beacon that fires on render
      ← "src=\"https://static.scarf.sh/a.png?x-pxid=0486b269-51d8-4a28-b1ec-2d9bad999839
         &page=README.md\""
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    unfree?
      #void — none stated in THIS readme. the repo is Apache-2.0 and a self-hosted App
      Server path is named; whether the successor repo gates features is that repo's
      material, not this one's
    contradiction
      #void — none found in the frozen material
