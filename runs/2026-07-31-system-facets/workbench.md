# workbench — the exhibits, compiled for your judgment

> everything here is EXHIBIT or [proposal]. nothing in this file is decided.
> order everywhere is SEED ORDER — your own pre-curation signal, preserved.
> you never need to open a gist or dossier to rule; the grounding is attached here.

---

# E1 · whole-view

    NN · owner/repo · "official description, verbatim" · flags:n voids:n · spine-voids

    01 · cachix/devenv · "Fast, Declarative, Reproducible, and Composable Developer
         Environments using Nix" · flags:2 voids:10 · why
    02 · bevyengine/bevy · "A refreshingly simple data-driven game engine built in Rust"
         · flags:2 voids:7 · —
    03 · chaosprint/glicol · "Graph-oriented live coding language and music/audio DSP
         library written in Rust" · flags:2 voids:5 · —
    04 · dakra/ghostel · "Terminal emulator powered by libghostty" · flags:0 voids:9 · why
    05 · lasantosr/intelli-shell · "Like IntelliSense, but for shells" · flags:2 voids:6 · —
    06 · trueagi-io/hyperon-experimental · "MeTTa programming language implementation" ·
         flags:2 voids:6 · —
    07 · h4ckf0r0day/obscura · "The headless browser for AI agents and web scraping" ·
         flags:4 voids:5 · —
    08 · letta-ai/letta · "Platform for stateful agents: AI with advanced memory that can
         learn and self-improve over time." · flags:4 voids:5 · why · how-technology
    09 · letta-ai/letta-code · "Stateful agents that are like people, with memory,
         identity, and the ability to learn and adapt" · flags:3 voids:6 · why
    10 · vpsfreecz/vpsadminos · "Host for Linux system containers based on NixOS, ZFS and
         LXC" · flags:0 voids:8 · —
    11 · papercomputeco/stereOS · "A Linux based operating system hardened and purpose
         built for AI agents" · flags:2 voids:9 · why
    12 · denful/den · "Aspect-oriented, context-driven Nix configurations." · flags:3
         voids:7 · —
    13 · jlevy/kash · "The knowledge agent shell" · flags:3 voids:5 · —
    14 · typedb/typedb · "TypeDB: Built for systems, not records" · flags:3 voids:8 · —
    15 · QuackHack-McBlindy/yo · "Yo is a compie-time grammar compiler (Nix) and a runtime
         deterministic interpretor (Rust)…" · flags:3 voids:7 · —
    16 · deepcausality-rs/deep_causality · "Dynamic Causality in Rust" · flags:4 voids:7 · —
    17 · anselmetbrl/skill-construction · #void — no About field · flags:0 voids:11 · —
    18 · ExtensityAI/symbolicai · "A neurosymbolic perspective on LLMs" · flags:3 voids:4 · —
    19 · opencog/atomspace · "The OpenCog (hyper-)graph database and graph rewriting
         system" · flags:3 voids:5 · —
    20 · onestardao/WFGY · "WFGY is heading toward WFGY 5.0 Polaris Protocol, a major
         open-source release for AI reasoning, RAG, agents, and real-world workflows." ·
         flags:5 voids:7 · —
    21 · stanfordnlp/dspy · "DSPy: The framework for programming—not prompting—language
         models" · flags:1 voids:10 · how-technology
    22 · boundaryml/baml · "The programming language for agents" · flags:3 voids:9 · why
    23 · cheat-engine/cheat-engine · "Cheat Engine. A development environment focused on
         modding" · flags:1 voids:10 · why
    24 · dynobo/normcap · "OCR powered screen-capture tool to capture information instead
         of images" · flags:1 voids:7 · —
    25 · screenpipe/screenpipe · "YC (S26) | Record your screen 24/7 and plug into your
         agents. Local, private, secure. Connect to OpenClaw, Hermes agent and 100+ apps"
         · flags:6 voids:4 · —

    status      25 ok · 0 blocked · 0 skipped
    spine-voids 6 repos never state their why · 2 never state their internals

---

# E2 · tag candidates

> derived PER REPO from grounded material first, then unioned. lowercase_underscore.
> form guard applied: an ACT-noun that partitions beats a category-label that absorbs.
> `ai`, `memory`, `local`, `rust`, `nix` were REJECTED as candidates for exactly that
> reason — they absorb rather than cut, and several would hold half the collection.
> the ≤12 cap and the ≤4-per-repo cap discipline the PROPOSAL below. the SET is yours.

## T1 · declaration — a system described as data, then evaluated into being

    partitions  01 devenv · 10 vpsadminos · 11 stereOS · 12 den · 15 yo
    01  "Fast, Declarative, Reproducible, and Composable Developer Environments"
        (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    10  "vpsAdminOS is developed on top of the latest NixOS release and pins nixpkgs in
        `flake.lock`" (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    11  "stereOS declares two custom options: | `stereos.ssh.authorizedKeys` … |
        `stereos.agent.extraPackages` |"
        (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    12  "Den turns Nix configuration into composable **features** instead of per-host piles
        of modules." (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    15  "It takes declarative sentence templates with optional parameters and entity lists,
        expands them into all possible variants"
        (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

## T2 · composition — smaller units combining into larger ones as the core mechanic

    partitions  01 devenv · 03 glicol · 12 den · 13 kash · 16 deep_causality
    01  "**[Composable via imports](https://devenv.sh/composing-using-imports/)** to share
        and reuse environments across projects"
        (https://raw.githubusercontent.com/cachix/devenv/HEAD/README.md)
    03  "The basic idea of Glicol is to connect different nodes like synth modules."
        (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    12  "includes = [ den.aspects.performance ];   # aspects compose"
        (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    13  "An action is composable with other actions simply as a Python function"
        (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    16  "Because both consume and produce the same carrier, they compose freely."
        (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

## T3 · interpretation — a language parsed and executed by this project

    partitions  03 glicol · 06 hyperon · 14 typedb · 15 yo · 19 atomspace · 22 baml
    03  "- write the parser in Rust - write the audio engine in Rust that works seamlessly
        with the AST processing"
        (https://raw.githubusercontent.com/chaosprint/glicol/HEAD/README.md)
    06  "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
        (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    14  "The query language of TypeDB is [TypeQL]. The syntax of TypeQL is fully
        variablizable" (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    15  "*50%* **Rust: run-time deterministic interpreter with some fuzziness on top**"
        (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    19  "**Graphs are executable.** … the resulting language is called [Atomese]"
        (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    22  "BAML is the programming language for agents."
        (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## T4 · typing — a type system as the organising claim, not an implementation detail

    partitions  06 hyperon · 14 typedb · 19 atomspace · 22 baml
    06  "an \"Atomese 2\" language called MeTTa (Meta Type Talk)."
        (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
    14  "TypeDB schemas are based on a modern type system that natively supports
        inheritance and interfaces"
        (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    19  "the AtomSpace stores immutable, globally unique, [typed] [s-expressions.]"
        (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    22  "It has a type system like Rust, but compiles even faster than Go." · "Types
        persist at runtime. There is no `any`"
        (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## T5 · verification — checking a claim or an output before it is accepted

    partitions  16 deep_causality · 18 symbolicai · 20 WFGY · 25 screenpipe
    16  "a **defeasible deontic calculus** to resolve normative conflicts and decide
        whether a CSM-proposed action is permissible under an immutable ethos"
        (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    18  "contracts help build correctness directly into your design"
        (https://raw.githubusercontent.com/ExtensityAI/symbolicai/HEAD/README.md)
    20  "6. verifying before unlock"
        (https://raw.githubusercontent.com/onestardao/WFGY/HEAD/README.md)
    25  "Enforced at three layers … Not prompt-based. Deterministic."
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T6 · capture — taking in what is on a screen or a wire and making it data

    partitions  07 obscura · 24 normcap · 25 screenpipe
    07  "obscura fetch https://example.com --dump html"
        (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    24  "OCR powered screen-capture tool to capture information instead of images."
        (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    25  "captures a screenshot only when something actually changes"
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T7 · transcription — a signal turned into text by a model

    partitions  15 yo · 24 normcap · 25 screenpipe
    15  "**GGML-based bin models from the Whisper family is used for speech-to-text.**"
        (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    24  "- [tesseract](https://github.com/tesseract-ocr/tesseract) - _OCR engine_"
        (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    25  "Real-time speech-to-text using Whisper (Large-V3-Turbo) running locally"
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T8 · containment — an occupant deliberately confined by the host

    partitions  10 vpsadminos · 11 stereOS · 25 screenpipe
    10  "vpsAdminOS is a small OS serving as a host for unprivileged Linux system
        containers." (https://raw.githubusercontent.com/vpsfreecz/vpsadminos/HEAD/README.md)
    11  "adds the binary to the agent user's restricted PATH"
        (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/README.md)
    25  "- **Endpoint gating**: `allow-raw-sql: false`, `allow-frames: false`"
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T9 · persistence — state deliberately outliving the session that made it

    partitions  08 letta · 09 letta-code · 13 kash · 19 atomspace · 25 screenpipe
    08  "Build AI with advanced memory that can learn and self-improve over time."
        (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
    09  "All context (including memory blocks) is tracked via git."
        (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    13  "A workspace is just a directory of files that have a few conventions to make it
        easier to maintain context" (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    19  "By storing frames, it is possible to revert to earlier graph state."
        (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    25  "All data stored on your device in a local SQLite database."
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T10 · retrieval — a searchable structure built over accumulated material

    partitions  05 intelli-shell · 13 kash · 14 typedb · 19 atomspace · 25 screenpipe
    05  "transforming your terminal into a structured, searchable, and intelligent library
        of your commands"
        (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    13  "Kash auto-detects and uses `ripgrep` (for search)"
        (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    14  "Perform [graphical database queries], returning results that satisfy a provided
        search pattern." (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    19  "**Search queries are graphs.**"
        (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    25  "Full-text keyword search (SQLite FTS5) under the hood."
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T11 · self-modification — the system rewriting its own definition at run time

    partitions  09 letta-code · 13 kash · 21 dspy
    09  "They learn and evolve over long horizons through rewriting their own memory,
        skills, prompts, and even the harness itself (through mods)."
        (https://raw.githubusercontent.com/letta-ai/letta-code/HEAD/README.md)
    13  "kash can read its own functionality and enhance itself by writing new actions."
        (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    21  "DSPy stands for Declarative Self-improving Python."
        (https://raw.githubusercontent.com/stanfordnlp/dspy/HEAD/README.md)

## T12 · prompt-displacement — hand-written prompts replaced by a structured artifact

    partitions  18 symbolicai · 20 WFGY · 21 dspy · 22 baml
    18  "brings **Design by Contract** principles into the world of LLMs"
        (https://raw.githubusercontent.com/ExtensityAI/symbolicai/HEAD/README.md)
    20  "It helps AI systems avoid treating raw natural language as if it were already an
        executable task." (https://raw.githubusercontent.com/onestardao/WFGY/HEAD/README.md)
    21  "Instead of brittle prompts, you write compositional _Python code_"
        (https://raw.githubusercontent.com/stanfordnlp/dspy/HEAD/README.md)
    22  "every feature is built so agents make fewer mistakes"
        (https://raw.githubusercontent.com/boundaryml/baml/HEAD/README.md)

## T13 · substitution — standing in for an incumbent while keeping its interface

    partitions  04 ghostel · 07 obscura
    04  "**Ghostel** is a terminal emulator for Emacs powered by [libghostty-vt], the VT
        engine behind the [Ghostty] terminal."
        (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    07  "acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright"
        (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

## T14 · inspection — reading the internals of a system while it runs

    partitions  07 obscura · 23 cheat-engine · 25 screenpipe
    07  "Obscura implements the Chrome DevTools Protocol"
        (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    23  "monodatacollector.sln: … to get Mono features to inspect the .NET environment of
        the process"
        (https://raw.githubusercontent.com/cheat-engine/cheat-engine/HEAD/README.md)
    25  "Each capture pairs a screenshot with the accessibility tree"
        (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## T15 · causation — cause modelled as a first-class object   [PARTITION-OF-ONE]

    partitions  16 deep_causality
    16  "DeepCausality is the reference implementation of the **Effect Propagation Process
        (EPP)**, a single axiomatic foundation for dynamic causality"
        (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    note        allowed as a PROPOSAL only. never silently minted into the set.

## T16 · falsification — recording the conditions under which a claim becomes wrong
                          [PARTITION-OF-ONE]

    partitions  17 skill-construction
    17  "each node folds into a **falsification**: / - `moderation(~invalidation)` — when
        this decision becomes mistaken."
        (https://raw.githubusercontent.com/anselmetbrl/skill-construction/6c1763a3/spec.md)
    note        allowed as a PROPOSAL only. never silently minted into the set.

## [proposal] the ≤12, and what each choice costs

    proposed set, 12:
      declaration · composition · interpretation · typing · verification · capture ·
      transcription · containment · persistence · retrieval · self-modification ·
      prompt-displacement

    dropped, and the cost of dropping each:
      substitution   — T13 holds only 2 repos, and both are already carried by other
                       tags. cost: ghostel loses the one tag that names what it IS
                       relative to its ecosystem, and ghostel is otherwise thinly tagged.
      inspection     — T14's three repos are each carried by capture or containment.
                       cost: cheat-engine drops to ONE tag total. it is the least
                       well-tagged repo in the set under this proposal.
      causation      — partition-of-one. cost: deep_causality's most distinctive property
                       becomes invisible to a tag search.
      falsification  — partition-of-one. cost: same, for skill-construction.

    coverage under the proposed 12:
      every repo gets ≥1 tag EXCEPT 02 bevy and 17 skill-construction.
      02 bevy carries composition only weakly and no other proposed tag fits its
         grounded spans — it is a game engine in a collection that is not about games.
      17 skill-construction's grounded spans support falsification and declaration; the
         first is dropped as a partition-of-one and the second is a stretch.
      → BOTH would render `#void` on their tag line. that is an honest outcome and it is
        put to you rather than fixed by inventing a tag to cover them.

    the ≤4 per repo, under the proposed 12:
      25 screenpipe hits SEVEN — verification, capture, transcription, containment,
         persistence, retrieval, inspection. it exceeds the cap by three under any
         reading. which four is a judgment the material cannot make.
      19 atomspace hits four exactly — interpretation, typing, persistence, retrieval.
      13 kash hits four exactly — composition, persistence, retrieval, self-modification.

---

# E3 · relation candidates

> every harvest span, name-resolved MECHANICALLY against the collection by script.
> 64 named targets across 41 harvest entries. types carry `?` — the type is YOURS.

## resolved INTO the collection

    R1  08 letta → 09 letta-code                            [alternative-to?] [conflicts-with?]
        "Active development has moved to the [Letta Agent repo](https://github.com/
         letta-ai/letta-code)"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
        "This repository contains the legacy Letta server"
         (https://raw.githubusercontent.com/letta-ai/letta/HEAD/README.md)
        resolved by  EXPLICIT URL. unambiguous.
        direction    one-way. seed 08 names seed 09 three times; seed 09 names seed 08
                     nowhere.
        NOTE         NEITHER available type fits. this is a legacy→successor relation,
                     not an alternative and not a conflict. see [proposal: new type].

    R2  06 hyperon → 19 atomspace                           SUSPECT — see below
        "[./lib](./lib) crate contains MeTTa atomspace and interpreter implementations."
         (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
        resolved by  BARE NAME `atomspace` matching seed 19's repo name.
        ⚠ FALSE POSITIVE, probably. the span refers to hyperon's OWN in-tree atomspace
          implementation, not to the `opencog/atomspace` repository. mechanical name
          resolution cannot tell a concept from a repo that shares its name.
          → surfaced rather than silently dropped OR silently kept. your ruling.

## the indirect case — no direct edge, and worth your eye anyway

    R3  06 hyperon ↔ 19 atomspace, via a third repo that is NOT in this collection
        seed 06: "OpenCog Hyperon is a substantially revised, novel version of OpenCog"
                 · "a successor to the OpenCog Classic Atomese language"
                 (https://raw.githubusercontent.com/trueagi-io/hyperon-experimental/HEAD/README.md)
        seed 19: "It provides the central knowledge representation component for OpenCog."
                 · "Dead projects: … * [Natural language chat, robot control](https://
                 github.com/opencog/opencog) (the opencog repo)"
                 (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
        the shape  seed 06 declares itself the successor to "OpenCog". seed 19 declares
                   itself a component OF "OpenCog" and separately declares the repo
                   NAMED opencog/opencog dead. `opencog/opencog` is not a seed here.
        the question whether "OpenCog" denotes the same thing in both readmes is a
                   judgment about meaning across two documents. no span resolves it.
                   → set-level. yours, with both sides quoted above.

## resolved OUT of collection — context, not edges

    55 distinct names. listed once, in seed order of the repo that named them:
      03 SuperCollider · 04 vterm · eat · eat.el · comint · 05 Atuin · tldr-pages/tldr ·
      06 OpenCog · OpenCog Classic · Atomese · DAS · singnet/das · 07 headless Chrome ·
      Puppeteer · Playwright · NousResearch/hermes-agent · 08 MemGPT · 09 ClawHub ·
      openclaw · Hermes Skills Hub · 10 NixOS · cleverca22/not-os · 12 Dendritic · Unify ·
      flake-parts · home-manager · 13 xonsh · Terminal · Warp · iTerm2 · Kitty · WezTerm ·
      Hyper · 15 Home Assistant · 18 wolframalpha · axiom · qdrant · DeepWiki ·
      19 opencog/opencog · PLN · BAP · HyperNetX · 20 LangChain · AutoGPT ·
      24 TextSnatcher · GreenShot · TextShot · gImageReader · Capture2Text · Frog ·
      Textinator · Text-Grab · dpScreenOCR · PowerToys Text Extractor · uv ·
      25 Rewind.ai · Limitless · Microsoft Recall · Granola · Otter.ai

    three names appear in TWO seeds each, and NONE of them makes an edge between those
    seeds — they are shared third parties:
      `tldr-pages/tldr` — 05 and 13 · `uv` — 13 and 24 · `DeepWiki` — 12 and 18

## [proposal: new relation type]

    the two sanctioned types are alternative-to and conflicts-with. R1 fits neither:
    seed 08 does not offer itself as an alternative to seed 09, and does not conflict
    with it — it declares itself SUPERSEDED BY it, and names the successor.

    proposed  `succeeded-by` — one repo names another as where its development moved,
              in its own words. the inverse reading, `supersedes`, is the same edge
              read from the other end.
    evidence  R1's two spans above, both from seed 08's readme.
    NOT COINED. this edge does not exist unless you adopt the type. if you refuse it,
    R1 is recorded as [deferred] and renders `#void`, and the letta pair simply sits
    adjacent in the index with no edge between them.

## the count, plainly

    edges resolving into the collection ....... 1 unambiguous (R1), 1 suspect (R2)
    edges NOT proposed .......................... 24 of 25 repos have no in-collection edge
    "no relation" is the expected common outcome here, and it is what the material shows.

---

# E4 · flag roster

> every flag from every gist, grouped by repo, each with its quote in the gist.
> 63 flags fired across 25 repos. no totals, no severity ordering — accumulation is
> visible here; SUBTRACTION is yours.

    01 devenv           hype ×2 (self-measured latency · scale figures as claims)
    02 bevy             hype (permanence claim) · contribution (sponsor-mandated line)
    03 glicol           hype (promotional adjectives) · abandonment-inverted (self-issued
                        stability warning)
    04 ghostel          — none fired. all six flag classes #void.
    05 intelli-shell    hype (promotional opening) · contribution (curl-to-shell install)
    06 hyperon          hype (succession claim) · abandonment-inverted (self-declared
                        pre-alpha)
    07 obscura          hype (two self-benchmark tables) · contribution (six proxy vendors
                        with affiliate codes) · contradiction (cloud tier beside a
                        no-gating pledge) · filler (stale headline count)
    08 letta            hype (superintelligence persona in sample code) · abandonment
                        (self-declared handover, NO date) · contribution (unsourced
                        contributor-scale claim) · filler (analytics beacon)
    09 letta-code       hype (anthropomorphic assertion) · unfree? (two account-gated
                        features) · filler (analytics beacon)
    10 vpsadminos       — none fired. all six flag classes #void.
    11 stereOS          hype ("hardened" asserted, never defined) · contradiction
                        ("All rights reserved." above an AGPL grant)
    12 den              contribution ×2 (four testimonials + adopter list · uncited
                        European Commission claim) · hype (AI-authorship slogan)
    13 kash             hype (first-person promotional) · unfree? (closed adjacent product
                        solicited twice) · filler (duplicated paragraph)
    14 typedb           hype ×2 (four superlatives in four sentences · vendor superlative
                        in its own voice) · unfree? (three editions, one contact-only)
    15 yo               hype ×2 (superlative doubled · two pasted timings as evidence) ·
                        contribution (funding apparatus ×2 + wallet)
    16 deep_causality   hype ×2 (two unmeasured comparatives · quantum-native claim) ·
                        filler (broken badge URL) · unfree? (commercial support entity)
    17 skill-construct  — none fired. all six flag classes #void.
    18 symbolicai       hype (ergonomics framing) · abandonment-inverted (experimental
                        caveat) · contribution (investor solicitation)
    19 atomspace        hype (uniqueness superlatives) · abandonment (sibling ecosystem
                        self-classified dead/half-dead, NO dates) · contribution
                        (insinuation that a third party copied its docs)
    20 WFGY             filler ×3 (fabricated FAQ link paths · hidden AI routing block ·
                        print-this-exactly instruction) · contradiction (asserts MIT and
                        declines to name a licence, same file) · hype (proof routing
                        inward)
    21 dspy             filler (routes the reader away three times)
    22 baml             hype ×2 (unmeasured compile-speed comparison · correctness claims
                        with a trailing "etc.") · contribution (hiring surface)
    23 cheat-engine     abandonment (toolchain pinned to old versions, NO date)
    24 normcap          filler (TODO marker inside a user-facing install block)
    25 screenpipe       contradiction (privacy section vs FAQ on network traffic) ·
                        unfree? ×2 (non-OSI licence, 7-day commercial evaluation ·
                        undated licence change) · filler (keyword-stuffed LLM block) ·
                        hype (uncited benchmark vs three vendors) · contribution
                        (AI-generated PRs welcomed)

    three repos fired NOTHING: 04 ghostel · 10 vpsadminos · 17 skill-construction.
    that is a fact about their readmes, not a ranking of the projects.

---

# E5 · order proposal

    [proposal] KEEP SEED ORDER — the order you gave.

    reason      it is your own pre-curation signal and the only ordering in this run that
                carries information the agent did not manufacture. every alternative
                ordering I could offer would be built from exhibits above, which means
                the index would then encode MY arrangement of your collection.
    alternatives considered and NOT offered:
                by flag count — would read as a ranking. forbidden by the invariant that
                  the index never ranks.
                by tag cluster — presupposes the tag set, which you have not ruled yet.
                by any count — forbidden outright (C4).
    cost        seed order puts thematically adjacent repos far apart (06 hyperon and 19
                atomspace sit thirteen apart; 07 obscura and 25 screenpipe eighteen).
                the always-visible tag line is the compensating mechanism: text-search a
                tag, get its cluster, regardless of order.
    "keep my order" costs you one word. any reorder you name is recorded verbatim.

---

# E6 · check-report

    run at phase 3 exit · re-runnable: `python3 checks.py`

    C1 grounding        543 claim heads · violations = 0
    C2 graph-types      coined types = 0
    C3 graph-fill       41 harvest entries · malformed = 0 · 9 gists render #void
    C4 counts-in-prose  violations = 0 · counts inside quoted evidence = 1 [OPEN, D1]
    C6 voids-reported   177 across 25 gists · range 4 (symbolicai, screenpipe) to 11
                        (skill-construction). this is an HONESTY RATE, not a score.
    C7 flag-grounding   63 flags fired · ungrounded = 0
    C9 coverage         dossiers without gist = 0 · orphan gists = 0

    violations found and REPAIRED during the phase, kept visible:
      · C1 initially read 14 violations — my own wrapped claim heads broke the four-space
        convention, and harvest entries were being scanned as claims. both fixed; C3 was
        strengthened to validate harvest entries properly.
      · TWO grounding errors of my own, same shape: a licence ABSENCE given a quote that
        did not evidence it, in seed 17 and seed 23. both now stand as voids with their
        probe. an absence has no span.
      · C4 fired once on quoted evidence. NOT silently exempted — recorded as decision D1,
        open for your ruling, with the gaming risk written down.

---

# E7 · emerge candidates

> observations only the whole collection shows. subject = the REPOS, never you.
> few is normal. none is valid. these are candidates; NONE is spoken unless you accept it.

    [candidate] E7a · six of twenty-five readmes never state the need they answer
      the projects are devenv, ghostel, letta, letta-code, stereOS, baml, cheat-engine.
      each states what it IS and how it works, and no span says what fails without it.
      spans: "#void — the readme never states the need it answers" (gists/cachix__devenv.md)
             "#void — the readme never states a problem" (gists/boundaryml__baml.md)

    [candidate] E7b · the collection's densest theme produces no mutual naming at all
      six repos occupy symbolic reasoning and structured LLM authoring — hyperon,
      deep_causality, atomspace, symbolicai, dspy, baml — and not one names another.
      spans: "no span in this readme names another software project"
             (gists/stanfordnlp__dspy.md)
             "this readme argues against a named intellectual position … it never names a
              competing software project"
             (gists/deepcausality-rs__deep_causality.md)

    [candidate] E7c · two readmes address a machine rather than a reader
      one hides its instructions in an HTML comment; the other puts keyword-stuffed prose
      in a collapsed block labelled for LLMs. the hidden one instructs the model to emit
      a fixed string.
      spans: "AI ROUTING NOTE (Homepage) … If user asks: - \"what is WFGY?\" -> explain"
             (https://raw.githubusercontent.com/onestardao/WFGY/HEAD/README.md)
             "If you're looking for a rewind alternative, recall alternative, or a private
              local screen recorder with AI, screenpipe is the most popular option"
             (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

    [candidate] E7d · four licences could not be read from GitHub's panel
      stereOS, atomspace and WFGY each carry a non-standard preamble that defeats the
      classifier; cheat-engine has no licence file at any probed path. all four were
      resolved by fetching the file, or recorded as an absence.
      spans: "all OpenCog source files use the AGPL with additional permissions to link
              OpenCog libraries with non-AGPL works"
             (https://raw.githubusercontent.com/opencog/atomspace/HEAD/LICENSE)
             "Copyright (c) 2026 Paper Compute Co. All rights reserved."
             (https://raw.githubusercontent.com/papercomputeco/stereOS/HEAD/LICENSE)

    [candidate] E7e · the collection is almost entirely non-self-referential
      nine of twenty-five readmes name no outside project at all, and of sixty-four names
      harvested across the rest, exactly one resolves unambiguously to another seed.
      spans: "#void — no span in this repo names any other project"
             (gists/anselmetbrl__skill-construction.md)
             "→ names `letta-ai/letta-code` by explicit URL — a repo IN this collection"
             (gists/letta-ai__letta.md)

    NOT offered, and why:
      any observation about your curation, your taste, or what the selection reveals
      about you. forbidden outright — the subject must be the repos (C8).

---

# exit

    phase 4 complete. every exhibit compiled, every check re-run and reported.
    nothing above is decided. next is the SESSION, where you rule:
    tags · relations · order · which emerge-candidates are true enough to speak.
