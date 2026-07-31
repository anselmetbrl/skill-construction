---
status: ok
seed: 21
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# stanfordnlp/dspy

    url          https://github.com/stanfordnlp/dspy
    description  "DSPy: The framework for programming—not prompting—language models"
                 ← About field, verbatim (R4)
    site         https://dspy.ai/

## #git

    stars          36.5k                   (R4)
    forks          3.1k                    (R4) — the page also renders 3.2k in
                   navigation; both readings recorded, neither picked.
    watchers       203                     (R4)
    license        MIT                     (R4)
    open-issues    307                     (R4)
    open-prs       319                     (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     python ← pyproject.toml at root (R1); "pip install dspy" (S6);
                          "DSPy stands for Declarative Self-improving Python" (S3)
    deep-links     readme    https://raw.githubusercontent.com/stanfordnlp/dspy/HEAD/README.md
                   docs      https://dspy.ai/
                   pypi      https://pepy.tech/projects/dspy
                   paper-2023 https://arxiv.org/abs/2310.03714
                   paper-gepa https://arxiv.org/abs/2507.19457
                   paper-mipro https://arxiv.org/abs/2406.11695
                   paper-dsp https://arxiv.org/abs/2212.14024

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "## DSPy: _Programming_—not prompting—Foundation Models"
    S2  "DSPy is the framework for _programming—rather than prompting—language models_.
         It allows you to iterate fast on **building modular AI systems** and offers
         algorithms for **optimizing their prompts and weights**, whether you're building
         simple classifiers, sophisticated RAG pipelines, or Agent loops."
    S3  "DSPy stands for Declarative Self-improving Python. Instead of brittle prompts,
         you write compositional _Python code_ and use DSPy to **teach your LM to deliver
         high-quality outputs**."
    S4  "Learn more via our [official documentation site](https://dspy.ai/) or meet the
         community, seek help, or start contributing via this GitHub repo and our
         [Discord server]"
    S5  "**Please go to the [DSPy Docs at dspy.ai](https://dspy.ai)**"
    S6  "pip install dspy"
    S7  "To install the very latest from `main`: pip install
         git+https://github.com/stanfordnlp/dspy.git"
    S8  "If you're looking to understand the framework, please go to the [DSPy Docs at
         dspy.ai](https://dspy.ai). / If you're looking to understand the underlying
         research, this is a set of our papers:"
    S9  "**[Jul'25] [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement
         Learning](https://arxiv.org/abs/2507.19457)**"
    S10 "**[Oct'23] [DSPy: Compiling Declarative Language Model Calls into Self-Improving
         Pipelines](https://arxiv.org/abs/2310.03714)**"
    S11 "**[Jun'24] [Optimizing Instructions and Demonstrations for Multi-Stage Language
         Model Programs](https://arxiv.org/abs/2406.11695)**"
    S12 "[Dec'23] [DSPy Assertions: Computational Constraints for Self-Refining Language
         Model Pipelines](https://arxiv.org/abs/2312.13382)"
    S13 "[Dec'22] [Demonstrate-Search-Predict: Composing Retrieval & Language Models for
         Knowledge-Intensive NLP](https://arxiv.org/abs/2212.14024.pdf)"
    S14 "If you use DSPy or DSP in a research paper, please cite our work as follows:
         @inproceedings{khattab2024dspy, title={DSPy: Compiling Declarative Language
         Model Calls into Self-Improving Pipelines}, … journal={The Twelfth International
         Conference on Learning Representations}, year={2024}}"
    S15 "The **DSPy** logo is designed by **Chuyi Zhang**."

## potential-relation spans — collected, NOT resolved

    "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning" (readme, S9)
       → names `Reinforcement Learning` — a METHOD, not a project. no resolvable target.
    "Instead of brittle prompts, you write compositional _Python code_" (readme, S3) ·
     "_Programming_—not prompting—" (readme, S1)
       → positions against PROMPTING as a practice, not against any named project.
    no span in this readme names another software project at all — the outbound links
    are its own docs, its own PyPI page, its own arXiv papers, and its own social
    accounts.
    → 0 edge candidates from this seed.

    NOTE for the workbench: seed 22 (boundaryml/baml) occupies visibly adjacent
    territory — structured, typed authoring of LLM calls — and NEITHER readme names the
    other. the absence is recorded so the workbench discards the temptation explicitly.

## flags-raw — what fetch itself revealed

    thin?          YES, in an unusual direction. the readme is 4.8 KB for a 36.5k-star
                   repo, and it functions almost entirely as a ROUTER: three separate
                   times it tells the reader to go to dspy.ai instead (S5, S8, and the
                   standalone "## Documentation: [dspy.ai]" heading). the what/why
                   content is two paragraphs (S2, S3); everything else is install,
                   citations, and papers. this is a FINDING about the material, and the
                   gist's leaves beyond what/why will be correspondingly bare.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  the register is ACADEMIC — nine papers listed with dates and arXiv
                   links, two BibTeX entries, a named conference. the strongest
                   promotional phrase is "teach your LM to deliver high-quality outputs"
                   (S3). the em-dash slogan (S1) is positioning, not a benchmark claim.
                   NO self-benchmark tables, NO comparison rows, NO superlatives about
                   rivals. recorded as a fact about the material.
    note-for-gist  a large block listing the framework's evolution (twitter threads,
                   earlier papers) is HTML-COMMENTED OUT in the readme source. commented
                   text is not shown to a reader and is NOT quoted as a claim here.
                   recorded as a fetch observation only.
    note-for-gist  license is MIT per the page (R4); the readme itself never states a
                   license. recorded as a single-source fact.
