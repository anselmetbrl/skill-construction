---
status: ok
seed: 18
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# ExtensityAI/symbolicai

    url          https://github.com/ExtensityAI/symbolicai
    description  "A neurosymbolic perspective on LLMs"   ← About field, verbatim (R4)
    site         https://extensity.ai/ · docs https://extensityai.gitbook.io/symbolicai

## #git

    stars          1.7k                    (R4)
    forks          91                      (R4)
    watchers       30                      (R4)
    license        BSD-3-Clause            (R4) — confirmed by readme S24
    open-issues    0                       (R4)
    open-prs       0                       (R4)
                   → BOTH ZERO on a 1.7k-star repo. recorded as a fact, not read as
                     health in either direction; the cause is #void here.
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     python ← pyproject.toml at root (R1); "pip install symbolicai" (S13)
                   NOTE the readme's banner/preview images are served from the `dev`
                        branch, not the default branch (R1 observation).
    deep-links     readme    https://raw.githubusercontent.com/ExtensityAI/symbolicai/HEAD/README.md
                   docs      https://extensityai.gitbook.io/symbolicai
                   primitives https://extensityai.gitbook.io/symbolicai/features/primitives
                   contracts https://extensityai.gitbook.io/symbolicai/features/contracts
                   custom-engine https://extensityai.gitbook.io/symbolicai/engines/custom_engine
                   local-engine https://extensityai.gitbook.io/symbolicai/engines/local_engine
                   paper     https://arxiv.org/abs/2402.00854
                   deepwiki  https://deepwiki.com/ExtensityAI/symbolicai

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "# **SymbolicAI: A neuro-symbolic perspective on LLMs**"
    S2  "SymbolicAI is a **neuro-symbolic** framework, combining classical Python
         programming with the differentiable, programmable nature of LLMs in a way that
         actually feels natural in Python."
    S3  "It's built to not stand in the way of your ambitions. It's easily extensible and
         customizable to your needs by virtue of its modular design."
    S4  "> ❗️**NOTE**❗️ The framework's name is intended to credit the foundational work of
         Allen Newell and Herbert Simon that inspired this project."
    S5  "At the core of SymbolicAI are `Symbol` objects—each one comes with a set of tiny,
         composable operations that feel like native Python."
    S6  "`Symbol` comes in **two flavours**: 1. **Syntactic** – behaves like a normal
         Python value (string, list, int ‐ whatever you passed in). 2. **Semantic** – is
         wired to the neuro-symbolic engine and therefore *understands* meaning and
         context."
    S7  "Why is syntactic the default? Because Python operators (`==`, `~`, `&`, …) are
         overloaded in `symai`. If we would immediately fire the engine for *every*
         bitshift or comparison, code would be slow and could produce surprising
         side-effects. Starting syntactic keeps things safe and fast; you opt-in to
         semantics only where you need them."
    S8  "S = Symbol(\"Cats are adorable\") # default = syntactic / print(\"feline\" in
         S.sem) # => True / print(\"feline\" in S)     # => False"
    S9  "Because the projections return the *same underlying object* with just a different
         behavioural coat, you can weave complex chains of syntactic and semantic
         operations on a single symbol."
    S10 "| `==` | Comparison | ✓ | ✓ | Tests for equality. Syntactic: literal match.
         Semantic: fuzzy/conceptual equivalence (e.g. 'Hi' == 'Hello'). |"
    S11 "They say LLMs hallucinate—but your code can't afford to. That's why SymbolicAI
         brings **Design by Contract** principles into the world of LLMs. Instead of
         relying solely on post-hoc testing, contracts help build correctness directly
         into your design"
    S12 "@contract( pre_remedy=True,  # Try to fix bad inputs automatically /
         post_remedy=True, # Try to fix bad LLM outputs automatically /
         accumulate_errors=True, # Feed history of errors to each retry …)"
    S13 "To get started with SymbolicAI, you can install it using pip: pip install
         symbolicai"
    S14 "SymbolicAI uses multiple engines to process text, speech and images. We also
         include search engine access to retrieve information from the web."
    S15 "> ❗️**NOTE**❗️Please note that some of these optional dependencies may require
         additional installation steps. Additionally, some are only experimentally
         supported now and may not work as expected."
    S16 "SymbolicAI now features a configuration management system with priority-based
         loading. The configuration system looks for settings in three different
         locations, in order of priority"
    S17 "A neurosymbolic engine is **required** to use the `symai` package."
    S18 "\"NEUROSYMBOLIC_ENGINE_MODEL\": \"anthropic:claude-sonnet-4-6\", \"SYMBOLIC_ENGINE\":
         \"wolframalpha\", \"FORMAL_ENGINE\": \"axiom\", \"EMBEDDING_ENGINE_MODEL\":
         \"text-embedding-3-small\", \"SEARCH_ENGINE_MODEL\": \"parallel\", \"INDEXING_ENGINE\":
         \"qdrant\", \"DRAWING_ENGINE_MODEL\": \"flux-pro-1.1\", \"OCR_ENGINE_MODEL\":
         \"mistral-ocr-latest\""                        ← the full-config example
    S19 "> ❗️**NOTE**❗️Model names are provider-prefixed (`openai:gpt-5.4`,
         `anthropic:claude-sonnet-4-6`, `gemini:gemini-3.5-flash`)—the prefix selects the
         provider. All engines talk raw REST through a shared `httpx` transport—no
         provider SDKs required."
    S20 "Engine tests run against a mock transport by default—no API keys needed: pytest
         tests --engine-api=mock"
    S21 "Read SymbolicAI's DeepWiki [page](…) for a generated code tour, and check out our
         [paper](https://arxiv.org/abs/2402.00854) for the framework design."
    S22 "@article{dinu2024symbolicai, title={Symbolicai: A framework for logic-based
         approaches combining generative models and solvers}, author={Dinu,
         Marius-Constantin and Leoveanu-Condrei, Claudiu and Holzleitner, Markus and
         Zellinger, Werner and Hochreiter, Sepp}, journal={arXiv preprint
         arXiv:2402.00854}, year={2024}}"
    S23 "If you appreciate this project, please leave a star ⭐️ and share it with friends
         and colleagues. To support the ongoing development of this project even further,
         consider donating."
    S24 "This project is licensed under the BSD-3-Clause License."
    S25 "We are also seeking contributors or investors to help grow and support this
         project. If you are interested, please reach out to us."
    S26 "`.cluster(**clustering_kwargs?)` | Data Clustering | | ✓ | Cluster data into
         groups semantically. Uses scikit-learn's HDBSCAN via `symbolicai[cluster]`."

## potential-relation spans — collected, NOT resolved

    "\"SYMBOLIC_ENGINE\": \"wolframalpha\", \"FORMAL_ENGINE\": \"axiom\", … \"INDEXING_ENGINE\":
     \"qdrant\"" (readme, S18)
       → names `wolframalpha` · `axiom` · `qdrant` — PLUGGABLE ENGINES, i.e. optional
         dependencies. out of collection.
    "Uses scikit-learn's HDBSCAN via `symbolicai[cluster]`" (readme, S26)
       → names `scikit-learn`. dependency, out of collection.
    "All engines talk raw REST through a shared `httpx` transport—no provider SDKs
     required." (readme, S19)
       → names `httpx` and, negatively, provider SDKs. dependency-level, no edge.
    "provider-prefixed (`openai:gpt-5.4`, `anthropic:claude-sonnet-4-6`,
     `gemini:gemini-3.5-flash`)" (readme, S19) · "`pip install \"symbolicai[hf]\"`",
     "`[whisper]`", "`[lean]`" (readme, optional extras)
       → names model VENDORS and ecosystem tools (`hf`, `whisper`, `lean`). out of
         collection.
    "The framework's name is intended to credit the foundational work of Allen Newell and
     Herbert Simon" (readme, S4)  → names RESEARCHERS. not projects.
    "[DeepWiki](https://deepwiki.com/ExtensityAI/symbolicai)" (readme, S21)
       → names `DeepWiki`, a third-party doc-generation service. NOTE seed 12 (den) also
         carries a DeepWiki badge — a shared third-party service, NOT an edge between the
         two seeds. recorded so the workbench discards it explicitly.

    → 0 in-collection edge candidates.

    NOTE for the workbench: this seed occupies the same broad territory as seeds 06
    (hyperon-experimental), 16 (deep_causality), 19 (atomspace), 21 (dspy) and 22 (baml)
    — symbolic/neuro-symbolic reasoning and structured LLM programming — and names NONE
    of them. the collection's densest thematic neighbourhood produces, so far, no
    material-grounded edges at all. that is the finding, and it is stated rather than
    filled.

## flags-raw — what fetch itself revealed

    thin?          no — 16.8 KB, and unusually substantive on MECHANISM: the syntactic/
                   semantic split is explained with its rationale (S7) and demonstrated
                   with contrasting output (S8).
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  ZERO open issues and ZERO open PRs at 1.7k stars (R4). recorded as a
                   bare fact. it admits opposite readings — a tended tracker or a closed
                   one — and the material supports neither, so no verdict is entered.
    note-for-gist  PROMOTIONAL REGISTER, mild and mostly self-aware: "in a way that
                   actually feels natural in Python" and "It's built to not stand in the
                   way of your ambitions" (S2, S3). against that, an explicit maturity
                   caveat in the project's own voice: "some are only experimentally
                   supported now and may not work as expected" (S15). both recorded.
    note-for-gist  S11 opens the contracts section with a claim about LLM behaviour
                   ("They say LLMs hallucinate—but your code can't afford to") used to
                   motivate the feature. recorded as the readme's own framing.
    note-for-gist  FUNDING/INVESTMENT APPARATUS — a donation button plus an explicit
                   solicitation of "contributors or investors" (S23, S25), alongside a
                   company site and a contact email. the code is BSD-3-Clause (S24) with
                   no feature gating stated. recorded as facts on both sides.
    note-for-gist  the readme's images are pinned to the `dev` branch rather than the
                   default branch. a readme rendered from a release tag would show
                   development-branch assets. recorded as a fetch observation.
