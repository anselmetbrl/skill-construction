# _whole — the resident whole-view (multi pass)

    query   the most relevant repos for every facet of AI, where AI spans the whole
            computing stack (facets: os · lang · env · ide · research · agent · db · viz · ...)
    method  one compact line per repo. relevance = centrality to the AI-stack query,
            NOT a quality verdict (evidence-over-verdict). it orders ATTENTION only.

## the shape — clusters that emerged (thematic, realised as tags not forced edges)

    C1 llm-programming     dspy · baml · symbolicai            — program/typed LLMs, not prompt them
    C2 neurosymbolic/AGI   hyperon · atomspace · deep_causality · symbolicai
    C3 agent-memory/harness letta · letta-code · kash · skill-construction
    C4 agent-infra/capture obscura · stereOS · screenpipe · normcap
    C5 nix-stack           devenv · den · vpsadminos · yo · stereOS
    C6 shells              intelli-shell · kash · yo
    C7 knowledge-db        typedb · atomspace
    C8 creative/engine     bevy · glicol
    C9 editor-tooling      ghostel
    outlier                cheat-engine (reverse-engineering / memory-editing)

    note  clusters OVERLAP (symbolicai ∈ C1∩C2; stereOS ∈ C4∩C5; kash ∈ C3∩C6;
          atomspace ∈ C2∩C7) — which is WHY a flat multi-tag list beats a single-home tree.

## one line per repo   (facet · relevance-tier · one-phrase notion · flag?)

    hyperon          research/agent   HIGH   MeTTa, OpenCog-Hyperon AGI language
    letta            agent            HIGH   stateful-agent platform (ex-MemGPT); legacy→letta-code
    letta-code       agent            HIGH   stateful agent harness w/ memory, skills, subagents
    dspy             research/lang    HIGH   program—not prompt—LMs (Stanford, research-grounded)
    baml             lang/agent       HIGH   typed programming language for agents
    symbolicai       research/agent   HIGH   neurosymbolic Python × LLM, Design-by-Contract
    atomspace        db/research      HIGH   OpenCog in-RAM hypergraph KR for AGI
    deep_causality   research         HIGH   dynamic causality in Rust (EPP)
    stereOS          os/agent         MED-HI Linux OS hardened for AI agents (nix "mixtapes")
    obscura          agent            MED-HI Rust headless browser for AI agents      · HYPE
    screenpipe       agent/capture    MED-HI local 24/7 screen memory + MCP           · HYPE·UNFREE
    devenv           env              MED    declarative Nix dev environments
    intelli-shell    env/shell        MED    command manager, optional LLM
    kash             agent/shell      MED    knowledge-agent shell (Python, MCP)
    typedb           db               MED    strongly-typed DB / TypeQL               · HYPE
    skill-construction agent/meta     MED    THIS skill's home repo (self-referential)
    yo               agent/voice      MED    Nix+Rust voice assistant, explicitly NON-LLM
    normcap          viz/capture      MED-LO OCR screen-capture (text, not images)
    den              env/config       MED-LO aspect-oriented Nix configuration
    vpsadminos       os               LO     NixOS-based container host OS
    glicol           lang/audio       LO     graph-oriented live-coding audio language (Rust)
    ghostel          ide/terminal     LO     Emacs terminal emulator (libghostty)
    bevy             lang/engine      LO     data-driven ECS game engine (Rust)
    WFGY             research?         LO?    claimed AI-reasoning ecosystem           · SEO/FILLER (substance #void)
    cheat-engine     tooling          LO     memory scanner / game-modding (OUTLIER)

## evidenced cross-repo edges (for phase 6 — the ONLY hard relations)

    letta  → letta-code    superseded-by   self-stated "development has moved to letta-code"
    hyperon → atomspace    succeeds        "successor to the OpenCog Classic Atomese language"
    everything else        = thematic (shared tags + search), NOT an evidenced edge
