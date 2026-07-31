# graph — run 2026-07-31-ai-stack-26

relations compiled once from the harvested quotes, then mirrored into each repo's gist.
types: `alternative-to` · `conflicts-with` only. compare QUALITIES, never counts.

## resolved edges — IN-collection, evidence-gated (2)

    letta-code  --alternative-to-->  letta
        evidence   letta README (self-stated): "This repository contains the legacy Letta
                   server... Active development has moved to the Letta Agent repo [letta-code]"
        reading    a succession — letta-code is the active substitute for the legacy letta.
                   both by letta-ai. deps/lineage ("formerly MemGPT") are #git facts, not edges.

    hyperon  --alternative-to-->  atomspace
        evidence   hyperon README: MeTTa is "a successor to the OpenCog Classic Atomese
                   language"; atomspace README: "the central knowledge representation
                   component for OpenCog" (i.e. OpenCog Classic's KR store).
        reading    hyperon (OpenCog Hyperon) positions as successor to the OpenCog-Classic
                   stack that atomspace anchors. TARGET-RESOLUTION NUANCE [flagged]: "Atomese
                   language" ≈ the atomspace store — same lineage, not a verbatim repo-name
                   match. kept because both are OpenCog-Classic KR and the succession is explicit.

## recorded NON-edges — a quote exists, but no IN-collection target (honest voids)

    glicol      "instead of ... SuperCollider"        → SuperCollider not in collection
    ghostel     "compares to vterm / eat"             → vterm, eat not in collection
    obscura     "drop-in replacement for ... Chrome / Puppeteer / Playwright"  → not in collection
    screenpipe  "leading ... alternative to Rewind.ai / Recall / Granola / Otter.ai" → not in collection
    deep_causality "cannot handle ... Pearl's SCM / Granger / DBNs"  → not in collection
    typedb      "unifies relational / document / graph ... without their shortcomings" → generic categories
    dspy        "Instead of brittle prompts"          → prompting is a practice, not a repo

## a claim that negates a CATEGORY, not a repo — carried to EMERGE, not forced as an edge

    yo   "yo is NOT: an LLM with shell access!"  — a philosophical contrast to the LLM-agent
         shells (kash, intelli-shell-AI, letta). it names no in-collection repo, so the gate
         yields NO edge. the tension is real and collection-shaped → surfaced in EMERGE.md.

## everything else = thematic (shared tags + text-search), NOT an evidenced edge

    the clusters (llm-programming, neurosymbolic, agent-*, nix, shells, capture) are realised
    by the tag line + IDE search, exactly as the spec intends — not by forced graph edges.
    for a 25-repo hand-curated set, TWO hard edges is the honest, gate-respecting outcome.
