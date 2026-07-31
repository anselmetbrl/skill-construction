# tags — run 2026-07-31-ai-stack-26

## the collection-wide set — 12 (derived AFTER per-repo tagging)

these 12 are the FUNCTIONS that partition this collection. each names an act, not a
category. lang (rust/nix/python) is NOT a tag — lang-roles carries it (non-redundancy).

    llm_programming       program/typed LLMs instead of prompting them
    neurosymbolic         symbolic reasoning fused with / over neural models
    knowledge_graph       (hyper)graph / typed knowledge stores + query
    agent_memory          persistent, self-improving memory for agents
    agent_runtime         where agents run or act — harness, host, web-hands
    shell_augmentation    command/notation layers over the shell
    nix_configuration     Nix as the config/build/OS substrate
    screen_capture        turning the screen into text / searchable memory
    browser_automation    headless/scriptable browser as a tool
    voice_interface       spoken / natural-language command surface
    creative_coding       code as a medium for games / audio / art
    reverse_engineering   inspecting & modifying running program memory

## per-repo tags (≤4 each · #void where none of the 12 honestly fit)

    hyperon          neurosymbolic · knowledge_graph
    letta            agent_memory · agent_runtime
    letta-code       agent_memory · agent_runtime
    dspy             llm_programming
    baml             llm_programming
    symbolicai       llm_programming · neurosymbolic
    atomspace        knowledge_graph · neurosymbolic
    deep_causality   neurosymbolic
    stereOS          agent_runtime · nix_configuration
    obscura          browser_automation · agent_runtime
    screenpipe       screen_capture · agent_memory
    devenv           nix_configuration
    intelli-shell    shell_augmentation
    kash             shell_augmentation · agent_memory
    typedb           knowledge_graph
    skill-construction agent_runtime
    yo               shell_augmentation · voice_interface · nix_configuration
    normcap          screen_capture
    den              nix_configuration
    vpsadminos       nix_configuration
    glicol           creative_coding
    bevy             creative_coding
    ghostel          #void  (terminal-emulation — no partitioning slot; OUTLIER on the tag axis)
    WFGY             #void  (substance is #void — tagging on its CLAIMS would hallucinate)
    cheat-engine     reverse_engineering

## PRESSURE surfaced (spec: tag.moderation — do not conform at the cost of meaning)

    the collection is HETEROGENEOUS: a dense AI-core (neurosymbolic / agent / llm ≈ 13
    repos) plus a scattered long-tail of enablers and singletons (nix, shells, capture)
    and true outliers (ghostel, cheat-engine, bevy, glicol).

    a 12-tag budget partitions the AI-core well but leaves the tail THIN: 8 repos carry a
    single tag; 2 (ghostel, WFGY) carry #void. that is honest — but you should know it.

    candidate 13th–16th tags (if you want the tail to partition too, greenlight any):
        terminal_emulation   → ghostel            (removes a #void)
        audio_synthesis      → glicol             (splits it from bevy under creative_coding)
        containerization     → vpsadminos · stereOS · devenv
        local_first          → screenpipe · normcap · yo · kash   (privacy axis; spec warns
                               `local` can read as a systemic-given — here it is NOT universal)

    decision left to you: keep the disciplined 12 (AI-core-first), or widen for the tail.
