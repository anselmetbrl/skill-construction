# INDEX — AI across the whole computing stack

    run     2026-07-31-ai-stack-26 · 25 repos, hand-curated by the user
    query   the most relevant repos for every facet of AI, where AI spans the whole
            computing stack (os · lang · env · ide · research · agent · db · viz · ...)
    order   by RELEVANCE-TO-QUERY — it orders ATTENTION only. counts are shown for
            first-glance and are NEVER ranked or compared by (display ≠ comparison).
            note: dspy 36.5k★ and bevy 47.4k★ sit MID/LOW here — stars did not lift them.
    read    each repo appears ONCE. glance + tags are always visible; #git/#gist/#graph
            fold under each repo's heading. reading only this file should suffice.
    voids   contributors · exact lang% · commit-date are `#void` for 24/25 repos — the
            GitHub API was unreachable this session (cross-owner add_repo refused). the
            public page gave stars/forks/license/issues/description; lang-roles inferred
            from manifests. this is a session limit, not the repos' — flagged, not hidden.

## tag legend — the 12 functions that partition this collection
    llm_programming · neurosymbolic · knowledge_graph · agent_memory · agent_runtime ·
    shell_augmentation · nix_configuration · screen_capture · browser_automation ·
    voice_interface · creative_coding · reverse_engineering
    (search a tag to regroup its cluster · 8 repos carry one tag, 2 carry #void — see tags.md)

## flag legend
    HYPE = promotional superlatives in the repo's own register · UNFREE = license stepped
    away from open · FILLER = README written to route crawlers, thin on substance.
    flags are EVIDENCE, not verdicts — you weigh them.

---

## 01 · trueagi-io/hyperon-experimental — OpenCog-Hyperon's MeTTa language (AGI)
    glance   Rust+Python · ★266 · contribs #void · pre-alpha, PyPi `hyperon` · "MeTTa programming language implementation"
    tags     `neurosymbolic` `knowledge_graph`
    #git     MIT · forks 98 · open-issues 93 · metta-lang.dev · [readme](https://github.com/trueagi-io/hyperon-experimental)
    #gist    what: reference implementation of MeTTa ("Meta Type Talk"), Hyperon's "Atomese 2" language
             why:  OpenCog Classic's Atomese needed clearer semantics + meta-language for varied AGI inference
             how:  Rust interpreter core + Python bindings · `pip install hyperon` · pre-alpha
    #graph   alternative-to → atomspace (02) — "a successor to the OpenCog Classic Atomese language"

## 02 · opencog/atomspace — in-RAM hypergraph knowledge store for AGI
    glance   C++ (scheme/py) · ★986 · contribs #void · mature · "The OpenCog (hyper-)graph database and graph rewriting system"
    tags     `knowledge_graph` `neurosymbolic`
    #git     license #void(not shown) · forks 255 · open-issues 68 · [readme](https://github.com/opencog/atomspace)
    #gist    what: OpenCog's in-RAM (hyper)graph KR database with query engine + graph rewriting
             why:  a KR substrate for AGI — a metagraph, "literally just-plain better than a graph store" (pdf-backed)
             how:  C++ core; ecosystem modules (atomspace-rocks disk, atomspace-cog network, cogserver, matrix)
    #graph   succeeded-by ← hyperon (01) · graph-data theme w/ typedb (13) — share-tag

## 03 · ExtensityAI/symbolicai — neurosymbolic Python × LLM
    glance   Python · ★1.7k · contribs #void · BSD-3 · "A neurosymbolic perspective on LLMs"
    tags     `llm_programming` `neurosymbolic`
    #git     BSD-3-Clause · forks 91 · open-issues 0 · [readme](https://github.com/ExtensityAI/symbolicai)
    #gist    what: a neuro-symbolic framework fusing Python programming with LLMs
             why:  make LLM behavior composable AND correct within ordinary Python
             how:  `Symbol` primitives (Syntactic/Semantic); "Design by Contract" over LLMs; local/custom engines
    #graph   the HINGE of C1∩C2 — llm-programming (dspy 05, baml 06) ∩ neurosymbolic (01,02,04); share-tag, no edge

## 04 · deepcausality-rs/deep_causality — dynamic causality in Rust
    glance   Rust · ★269 · contribs #void · crates.io, Miri-tested · "Dynamic Causality in Rust"
    tags     `neurosymbolic`
    #git     MIT · forks 22 · open-issues 1 · Linux Foundation (Data & AI) sandbox · [readme](https://github.com/deepcausality-rs/deep_causality)
    #gist    what: reference implementation of the Effect Propagation Process (EPP) — dynamic computational causality
             why:  classical frameworks (Pearl SCM, Granger, DBNs) assume static structure; this models dynamic/emergent causality
             how:  Rust crate; axiomatic EPP grounded in Whitehead's process metaphysics; programmable deontic layer
    #graph   contrasts Pearl SCM/Granger/DBNs (out-of-collection) · causal pole of neurosymbolic cluster

## 05 · stanfordnlp/dspy — program, don't prompt, language models
    glance   Python · ★36.5k · contribs #void · pip `dspy`, 307 open · "DSPy: The framework for programming—not prompting—language models"
    tags     `llm_programming`
    #git     MIT · forks 3.1k · Stanford NLP · research-grounded (papers) · [readme](https://github.com/stanfordnlp/dspy)
    #gist    what: a framework for programming — not prompting — LMs (Declarative Self-improving Python)
             why:  brittle hand-written prompts don't scale; write code, optimize prompts + weights
             how:  Python modules + optimizer algorithms; for classifiers / RAG / agent loops
    #graph   alternative-to manual prompting (out-of-collection) · C1 w/ baml (06), symbolicai (03) — share-tag

## 06 · boundaryml/baml — a typed programming language for agents
    glance   Rust (multi-target) · ★8.7k · contribs #void · brew/CLI, 199 open · "The programming language for agents"
    tags     `llm_programming`
    #git     Apache-2.0 · forks 463 · callable from TS/Py/Go/C#/Java · [readme](https://github.com/boundaryml/baml)
    #gist    what: a purpose-built language for LLM agents ("Basically A Made-up Language")
             why:  general code lets agents make mistakes; a typed, agent-first language reduces them
             how:  TS-like syntax, Rust-like types, runtime-persistent types, static analysis; built-in eval framework
    #graph   C1 llm-programming w/ dspy (05), symbolicai (03) — share-tag, no evidenced edge (neither names the other)

## 07 · letta-ai/letta-code — stateful agent harness (memory, skills, subagents)
    glance   TypeScript/Node · ★2.9k · contribs #void · npm `@letta-ai/letta-code`, 90 open · "Stateful agents that are like people, with memory, identity, and the ability to learn and adapt"
    tags     `agent_memory` `agent_runtime`
    #git     Apache-2.0 · forks 342 · CLI + desktop + browser/mobile + Slack/Telegram/Discord · [readme](https://github.com/letta-ai/letta-code)
    #gist    what: a stateful agent harness — agents "more like people than tools" with memory + identity
             why:  tool-like agents don't persist experience; let them learn and self-modify (memory, skills, prompts, harness)
             how:  Node CLI; MemFS ("all context tracked via git"); skill-learning, /sleeptime, subagents, hooks, crons
    #graph   alternative-to → letta (08): the ACTIVE successor · shape parallels skill-construction (16), this run's own harness

## 08 · letta-ai/letta — stateful-agent platform (formerly MemGPT) · LEGACY
    glance   #void lang · ★24.0k · contribs #void · 25 open · "Platform for stateful agents: AI with advanced memory that can learn and self-improve over time"
    tags     `agent_memory` `agent_runtime`
    #git     Apache-2.0 · forks 2.6k · TS Agent SDK; Constellation cloud / local / self-hosted · [readme](https://github.com/letta-ai/letta)
    #gist    what: the platform/server for stateful agents with long-term memory (ex-MemGPT)
             why:  LLM agents are stateless; give them memory that learns/self-improves
             how:  legacy API server + TS SDK; model-agnostic — NOTE self-stated "development has moved to letta-code"
    #graph   superseded-by ← letta-code (07) — read letta-code first · lineage "formerly MemGPT"

## 09 · papercomputeco/stereOS — a Linux OS hardened for AI agents
    glance   Nix · ★486 · contribs #void · license #void · "A Linux based operating system hardened and purpose built for AI agents"
    tags     `agent_runtime` `nix_configuration`
    #git     license #void(not shown) · forks 30 · open-issues 5 · [readme](https://github.com/papercomputeco/stereOS)
    #gist    what: a hardened, minimal Linux OS purpose-built to host AI agents
             why:  agents need a locked-down host with a lifecycle/control plane, not a general desktop
             how:  NixOS-style build; ships "mixtapes" (images bundling an agent harness); daemons stereosd/agentd
    #graph   the BRIDGE — agent-runtime ∩ nix-stack; theme w/ obscura (10), screenpipe (11), and devenv/den/yo/vpsadminos

## 10 · h4ckf0r0day/obscura — Rust headless browser for AI agents   [HYPE]
    glance   Rust · ★19.9k · contribs #void · Apache-2.0, 23 open · "The open-source headless browser for AI agents and web scraping. Lightweight, stealthy, and built in Rust."
    tags     `browser_automation` `agent_runtime`
    #git     Apache-2.0 · forks 1.4k · runs JS via V8, Chrome DevTools Protocol · [readme](https://github.com/h4ckf0r0day/obscura)
    #gist    what: a Rust headless-browser engine for scraping + AI-agent automation
             why:  headless Chrome is heavy and detectable at scale; target low-footprint, stealthy automation
             how:  Rust + V8; "drop-in replacement for headless Chrome with Puppeteer and Playwright"; single binary
    flag     HYPE — self-benchmark table w/ bolded wins; "Obscura Cloud" waitlist; sponsor "7M+ residential IPs"; "10,000 stars" banner. claims plausible but self-measured.
    #graph   alternative-to headless Chrome/Puppeteer/Playwright (out-of-collection)

## 11 · screenpipe/screenpipe — local 24/7 screen memory for agents   [HYPE · UNFREE]
    glance   Rust + desktop · ★20.6k · contribs #void · 74 open · "YC (S26) | Record your screen 24/7 and plug into your agents. Local, private, secure."
    tags     `screen_capture` `agent_memory`
    #git     "Screenpipe Commercial License (source-available)" · forks 2.0k · SQLite FTS5 · [readme](https://github.com/screenpipe/screenpipe)
    #gist    what: a local-first tool recording screen+audio into a searchable, AI-queryable memory
             why:  give you (and agents) private recall of everything on your computer, kept local
             how:  Rust + desktop; event-driven capture + accessibility tree, OCR fallback; MCP (Claude Desktop, Cursor, VS Code)
    flag     HYPE — "YC S26", "outperforming Google/Microsoft/OpenAI", "the leading... most popular" ·
             UNFREE — license moved AWAY from open ("we updated our license to keep screenpipe sustainable"); source-available, not OSI
    #graph   alternative-to Rewind.ai/Recall/Granola/Otter.ai (out-of-collection) · capture theme w/ normcap (18)

## 12 · jlevy/kash — the knowledge agent shell (Python, MCP)
    glance   Python (xonsh) · ★25 · contribs #void · AGPL-3.0, 1 open · "The knowledge agent shell"
    tags     `shell_augmentation` `agent_memory`
    #git     AGPL-3.0 · forks 5 · uv-managed · [readme](https://github.com/jlevy/kash)
    #gist    what: "Knowledge Agent SHell" — a Python+AI shell (and library) turning functions into composable "actions"
             why:  make knowledge tasks modular, exploratory, AI-native — Unix-pipe-style over files/URLs/notes
             how:  xonsh-based shell OR pure Python library; each action is also an MCP tool (Anthropic Desktop / Cursor)
    #graph   small/early (25★ — a finding, not a fault) · shell cluster w/ intelli-shell (14), yo (17)

## 13 · typedb/typedb — a strongly-typed database (TypeQL)   [HYPE]
    glance   Rust (inferred) · ★4.4k · contribs #void · MPL-2.0, 280 open · "Built for systems, not records"
    tags     `knowledge_graph`
    #git     MPL-2.0 · forks 369 · TypeDB Cloud / Community Edition + Studio GUI · [readme](https://github.com/typedb/typedb)
    #gist    what: a strongly-typed database with query language TypeQL, unifying relational/document/graph models
             why:  each classical DB model has shortcomings; a type-system-first model for complex interconnected data
             how:  TypeQL (declarative, functional, typed); schema of entities/relations/attributes + inheritance/interfaces
    flag     HYPE — "next-gen", "groundbreaking query language", "we've reinvented the database". typed model is substantive; register oversells.
    #graph   knowledge-data theme w/ atomspace (02) — share-tag

## 14 · lasantosr/intelli-shell — IntelliSense for your shell
    glance   Rust · ★1.3k · contribs #void · Apache-2.0, 4 open · "Like IntelliSense, but for shells"
    tags     `shell_augmentation`
    #git     Apache-2.0 · forks 23 · Bash/Zsh/Fish/Nushell/PowerShell · [readme](https://github.com/lasantosr/intelli-shell)
    #gist    what: a command-template + snippet manager for the shell
             why:  flat shell history loses reusable, parameterized commands; make them a searchable library
             how:  Rust binaries; ctrl+space search; `{{variables}}`; optional local/remote LLMs; TLDR import
    #graph   self-distinguishes from shell history ("complementary, not competitors") · shell cluster w/ kash (12), yo (17)

## 15 · cachix/devenv — declarative Nix developer environments
    glance   Nix + Rust · ★7.2k · contribs #void · Apache-2.0, 304 open, release 2.0.0 · "Fast, Declarative, Reproducible, and Composable Developer Environments using Nix"
    tags     `nix_configuration`
    #git     Apache-2.0 · forks 528 · devenv.sh · [readme](https://github.com/cachix/devenv)
    #gist    what: declarative, composable per-project developer environments built on Nix
             why:  close the "works on my machine" gap — reproducible tooling without global installs or Docker
             how:  Nix eval + a Rust process manager; 100k+ Nixpkgs, 40+ services; OCI containers without Docker
    #graph   nix-stack (a DIFFERENT layer from den 19: dev-shells vs config-composition)

## 16 · anselmetbrl/skill-construction — THIS skill's home repo (self-referential)
    glance   Markdown · ★0 · contribs #void · description #void · (the user's own working repo)
    tags     `agent_runtime`
    #git     license #void · forks 0 · 0 open · in session scope · [repo](https://github.com/anselmetbrl/skill-construction)
    #gist    what: the meta-project in which THIS skill (holistic-meta-index) is co-constructed with the user
             why:  build a reusable natural-language pipeline that turns curated repo lists into a navigable meta-index
             how:  Markdown only — declarative SDD spec (spec.md) + stance (CLAUDE.md) + design log (ledger.md); no code
    #graph   SELF-REFERENTIAL — produced the pipeline running now · agent-skill theme w/ letta-code (07), thematic only

## 17 · QuackHack-McBlindy/yo — Nix+Rust voice assistant, explicitly NON-LLM
    glance   Nix + Rust · ★23 · contribs #void · MIT, 0 open · "compile-time grammar compiler (Nix) and runtime deterministic interpreter (Rust)... a full-stack voice assistant"
    tags     `shell_augmentation` `voice_interface` `nix_configuration`
    #git     MIT · forks 0 · NixOS module or standalone Rust; ESP32 clients · [readme](https://github.com/QuackHack-McBlindy/yo)
    #gist    what: a full-stack voice assistant — half Nix grammar-compiler, half Rust deterministic interpreter
             why:  fast, offline, rule-based plain-language → shell command, deliberately WITHOUT an LLM
             how:  Nix compiles sentence templates → regex; Rust runtime does exact+fuzzy matching; runs offline, one port
    #graph   the deliberate ANTI-LLM counterpoint — "yo is NOT an LLM with shell access" (see EMERGE) · Nix+Rust cluster

## 18 · dynobo/normcap — OCR screen-capture (grab text, not images)
    glance   Python/Qt (inferred) · ★2.7k · contribs #void · release v0.6.0, 73 open · "OCR powered screen-capture tool to capture information instead of images. For Linux, macOS and Windows."
    tags     `screen_capture`
    #git     license #void(not shown) · forks 124 · Flathub flatpak + prebuilt installers · [readme](https://github.com/dynobo/normcap)
    #gist    what: an OCR-powered screen-capture tool that grabs the TEXT on screen
             why:  often you want the text shown on screen, not a screenshot image of it
             how:  desktop OCR tool; cross-platform prebuilt releases; README candidly lists its own alternatives
    #graph   screen_capture w/ screenpipe (11) but DIFFERENT function (point OCR grab vs continuous recording) — share-tag

## 19 · denful/den — aspect-oriented, context-driven Nix
    glance   Nix · ★530 · contribs #void · Apache-2.0, 20 open · "Aspect-oriented, context-driven Nix configurations."
    tags     `nix_configuration`
    #git     Apache-2.0 · forks 49 · works with/without flakes; zero deps · [readme](https://github.com/denful/den)
    #gist    what: aspect-oriented, context-driven Nix config — a feature as a composable function
             why:  Nix configs scatter one concern across per-host module piles; make a feature reusable
             how:  "an aspect is a plain function of context returning config for nixos/darwin/homeManager..."; "No mkIf/enable clutter"
    #graph   nix-stack — config-composition layer (vs devenv 15 dev-shells); w/ vpsadminos (20), stereOS (09), yo (17)

## 20 · vpsfreecz/vpsadminos — NixOS-based container host OS
    glance   Nix (+Ruby/C) · ★185 · contribs #void · MIT, 10 open · "Host for Linux system containers based on NixOS, ZFS and LXC"
    tags     `nix_configuration`
    #git     MIT · forks 30 · production at vpsFree.cz · [readme](https://github.com/vpsfreecz/vpsadminos)
    #gist    what: a small host OS for unprivileged Linux system containers, based on NixOS
             why:  run full distributions in unprivileged containers that "feel as much like a VM as possible"
             how:  NixOS + not-os; LTS kernel + patches, runit, ZFS, LXC; its own `osctl` container tooling
    #graph   nix-stack — the infra-OS end · "based on NixOS and not-os" (dep-fact)

## 21 · chaosprint/glicol — graph-oriented live-coding audio language
    glance   Rust + WASM · ★3.0k · contribs #void · MIT, 45 open · "Graph-oriented live coding language and music/audio DSP library written in Rust"
    tags     `creative_coding`
    #git     MIT · forks 99 · glicol.org · runs web/VST/Bela · [readme](https://github.com/chaosprint/glicol)
    #gist    what: a graph-oriented live-coding language with its own Rust audio-DSP engine
             why:  real-time, memory-safe audio synthesis across browser/VST/embedded, without C/C++ hazards
             how:  Rust (language + engine) → WASM; a purpose-built engine (not mapped onto an existing lib)
    #graph   alternative-to SuperCollider (out-of-collection) · creative_coding w/ bevy (22)

## 22 · bevyengine/bevy — data-driven ECS game engine in Rust
    glance   Rust · ★47.4k · contribs #void · Apache-2.0 OR MIT, 2.8k open · "A refreshingly simple data-driven game engine built in Rust"
    tags     `creative_coding`
    #git     Apache-2.0/MIT dual · forks 4.7k · bevy.org · [readme](https://github.com/bevyengine/bevy)
    #gist    what: a data-driven ECS game engine in Rust, "free and open-source forever"
             why:  a game engine simple for newcomers yet flexible for power users, native to Rust
             how:  Rust; ECS/data-oriented; modular crates ("use only what you need"). HONEST early-stage warning (not hype)
    #graph   domain-isolated (highest ★ in the set — but relevance-ordered LOW: a game engine, not AI) · creative_coding w/ glicol (21)

## 23 · dakra/ghostel — Emacs terminal emulator (libghostty)
    glance   Emacs Lisp + native · ★804 · contribs #void · GPL-3.0-or-later, 11 open · "Terminal emulator powered by libghostty"
    tags     `#void`  (terminal-emulation — no partitioning slot in the 12; OUTLIER on the tag axis)
    #git     GPL-3.0-or-later · forks 47 · MELPA; prebuilt binary auto-downloads · [readme](https://github.com/dakra/ghostel)
    #gist    what: a terminal emulator for Emacs powered by libghostty-vt (Ghostty's VT engine)
             why:  a fast, correct, featureful terminal INSIDE Emacs, beyond older Emacs terminals
             how:  Emacs Lisp + native module; Kitty keyboard+graphics protocols, true color; bash/zsh/fish/nushell integration
    #graph   alternative-to vterm/eat (out-of-collection) · tag #void — see tags.md pressure note

## 24 · cheat-engine/cheat-engine — memory scanner / game-modding   [OUTLIER]
    glance   Pascal (Lazarus/FPC) · ★18.8k · contribs #void · license #void, 1.3k open · "A development environment focused on modding"
    tags     `reverse_engineering`
    #git     license #void(not shown) · forks 2.7k · cheatengine.org · [readme](https://github.com/cheat-engine/cheat-engine)
    #gist    what: a memory scanner / debugger / "development environment focused on modding games and applications"
             why:  inspect and modify a running program's memory — for game modding and reverse-engineering
             how:  Pascal (Lazarus 2.2.2 / FPC); Windows-centric; assembly-level tooling; large mature community
    #graph   THEMATIC OUTLIER — reverse-engineering, unrelated to the AI/agent/nix/knowledge clusters; a partition-of-one

## 25 · onestardao/WFGY — claimed AI-reasoning "ecosystem"   [FILLER]
    glance   #void lang · ★1.8k · contribs #void · license #void, 10 open · "WFGY is heading toward WFGY 5.0 Polaris Protocol, a major open-source release for AI reasoning, RAG, agents, and real-world workflows."
    tags     `#void`  (substance is #void — tagging on its CLAIMS would hallucinate)
    #git     license #void(not shown) · forks 162 · [readme](https://github.com/onestardao/WFGY)
    #gist    what: a self-described "ecosystem"/protocol for AI reasoning/RAG/agents ("5.0 Polaris Protocol")
             why:  claims to be a "gate" for "broken AI workflows" — but the README asserts POSITIONING, not a mechanism
             how:  #void — the README does not describe a codebase; it describes versions and crawler-routing
    flag     FILLER — README opens as an "AI ROUTING NOTE (Homepage)... flagship public route"; repeated "fastest practical
             gate"; from the README a reader cannot tell what the code does. the #void in what/why/how IS the finding.
    #graph   a self-referential ecosystem index (its OWN versions), NOT an awesome-list → stays IN, flagged, never skipped
