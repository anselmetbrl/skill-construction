
Phase_0
    Phase_0.0
    Phase_0.1
    Phase_0.2
    Phase_0.3
    Phase_0.4
Phase_1
    Phase_1.0
    Phase_1.1
    Phase_1.2
    Phase_1.3
    Phase_1.4
Phase_2
    Phase_2.0
    Phase_2.1
    Phase_2.2
    Phase_2.3
    Phase_2.4
Phase_3
    Phase_3.0
    Phase_3.1
    Phase_3.2
    Phase_3.3
    Phase_3.4
Phase_4
    Phase_4.0
    Phase_4.1
    Phase_4.2
    Phase_4.3
    Phase_4.4





{
instruction:
    _ 
    phase-0_intro/includ/in: 
        automate a preprocessing pipeline (crawling/scraping/augmenting/relating/indexing), from a list of github projects, for holistically assisting a human's research, by (de)constructing a meta index/graph/tree  
        ----
        the system augments user judgment rather than replacing it
        x2 attempts before escalading x2 x2 then fail & flag
        preservation of : **Immutability across layers.** Raw dossiers persist; later layers compile from them rather than rewriting history. statefulness
            'state.json persists per-repo (or per-batch minimum) completion so resume skips finished work after crash'
            'state.json logs/tracks per-repo completion and supports resume after crash, skipping finished repos and reprocessing only incomplete ones without wiping intermediate folders
            Never delete prior artifacts as part of state transitions. If you checkpoint progress to a `state.json`, the rule is: mark before work, mark after outcome, save atomically
            the mechanism behind "checkpointable" : **Resume rule (check before every (crawl/scrape/...) call):** 
                if `<owner>__<repo>.md` already exists, read its `status` field. 
                    `status: ok` → skip, it's a completed evidence record, dont re-fetch it.    
                    `status: rate-limited` or `partial` → re-crawl just that one repo and overwrite in place. 
        reflect/introspect backward as you go to selfheal inccrementally, dont rush blindly looking only forward
        ---
        simplicity but not simplistic
        complexity but not complicated
        decoupled modularity 
        ---
        /!\ **Confusing code generation with real execution.** A perfect pipeline implementation means nothing if the agent never crawled real repos. Run the actual CRAWL against the seed file. Inspect raw dossiers. The build is not the run. The map is not the territory.
    phase-1_git/import/download:
        thread carefully 1 by 1 sequentially
        dont get lost in codebase subdirectory recursion
        ---
        flag private/deleted/blocked repos in BLOCKED_REPORT.md rather than being dropped, then skip to the next one
        'Rate-limited/anti-bot blocks must NOT be silently skipped: aggressive retry with stealth (alternate user agents, Hermes obscura plugin, etc) then alternative approaches, then flag failure&why if exhausted'
        ---
        'Phase 1 completes then checkpoint pause awaiting CLI input (proceed or retry-blocked); do not terminate'
        1.1
        1.2 
            scrape full html? or minimal version modularly for now
                extract the complete readme.md file
        1.3 
            markdown, NO HTML noise
            Do not summarize, paraphrase, or infer anything. The dossier is **evidence, not interpretation**. - Do not invent fields. 
                If a value is missing, leave it empty or use `"unknown"`.
    phase-2_gist:
        agentically analyse
            /!\ **Mechanical gist mistaken for understanding.** Regex section extraction + LLM-as-templater produces fields that look semantic but don't actually summarize. 
            /!\ Generating gists via "send README to model X, write response to disk" with no agent oversight produces a different artifact than the agent *itself* reading and summarizing.
            Resist potential urges to add/export responsability to a sub-LLM stage.
        holistically **read all in one llm turn**
        grounding with essential quotes rather than ungrounded fabulation
        ---
        carefully warn/flag:
            corruption marketing bias -> impartiality
                The actual check is a pattern: does any body sentence assert a superlative or self-praise as established fact, in the project's own promotional register, rather than describing what it does? 
                SEO
                AI
                abandon
                `contradictions`: claims that conflict across the repository. Record the conflict; let the user resolve.
                omission
                confusion
                slop
                hype
                    "the best/first/only/most/fastest/..."
                fakeness
                paywall
                    Self-hosted completeness is essential; cloud-only or paid-tier-sabotaged projects get a needs-verification flag "unfree?" 
            confusion ambiguity -> clarity
                describe rough projects as rough
            omission neglect silence absence -> declarativity
                A blocked repo is an **outcome**, no omission.
            misapplication failure error mistake -> validity
        ---
        /!\ Custom README headings and duplicated facets.** READMEs use their own headings ("Three primitives", "Benchmarks", "What X is not"). 
            Don't assume literal `## Features` exists. 
            Don't reuse the same phrase in `What this is`, `Approach`, `Features`, and `Why` — pick genuinely different angles for each.
        Docs/wiki are consulted only as fallback when README is genuinely unclear to understand the project
        ---
        higher-order synthesis
        ---
        2.1 bottom-up augmentation (from uni)
            {
                linguisticality:
                    lang: rust%lisp%nix% (language stats should sum to ~100% else some is missing/unkown)
                    what: rust=x/y/z lisp=x/y/z nix=x/y/z 
                        (List all languages present, not just the top one — a project can have a real Rust core hidden under 8% Python scripting)
                        Every language percentage in INDEX is paired with a role
                    why: description
                popularity:
                    star:
                    contribution/participation:
                    forks:
                chronology:
                    first_creation-date: YYYY/MM/DD
                    last_commit-type: x ago (D/M/Y)
                _:
                    liscence
                    unresolved_issue: n
                    resolved_issue: n
            }
        2.2 top-down augmentation (from multi)
        2.3 
            ...
            first derivation then distillation (dont limit/reduce to 4 before having converged the tags to the 4 essential ones)
            tagging:
                {
                tag/flag/attribution_ontology/terminology:
                           see the end of the page
                }
                1. **Variety**: Aim the tagging process for a mix of broad categories, specific keywords, and sub-genres
                2. **Count**: Generate 4 tags per resource
                    'Tag hard caps: max 4 distinct tags per repo, max 12 distinct tags across the entire collection'
                3. **Genericity Threshold**: Only include tags sufficiently generic to appear across multiple resources; avoid one-off specificity
                4. **Emptiness**: If no suitable tags emerge, use the #void tag, do not force tags
                5. **Format Consistency**: All tags must be lowercase with underscores between words (e.g., `machine_learning`, `knowledge_graph`, `api_bridging`)
    phase-3_graph/relate:
        holistically **read all in one llm turn**
            for context-window, append primary-scored repositories at the top and multi-synthesis field at the bottom of the pipeline so llm doest neglect it in the middle fallacy
        compare qualities not quantities (never compare starts/contributors/...)
        `contradictions`: claims that conflict across the repositories. Record the conflict; let the user resolve.
            Cross-repo flagging writes back into relevant gists frontmatter
                Cross-references are rendered as : 
                conflicts-with:
                x-link-with:
                y
                z (my relational ontology)
        {
        link/relation_ontology:
                ?
                ?   
                    ?
                    ?
                ?
                    ?
                    ?
                ?
        }
        ---
        INDEX has NO numbered rankings; it is a navigable map, not a leaderboard
        'Each repo appears ONCE under its primary tag; supplementary tags folded as inline metadata'
        markdown (IDE-native fold), NO HTML noise
        Tab indentation (not spaces) creates visual nesting that headers alone can't.
            Each facet on its own tab-indented line for clear naviguation
            each facet also starting with a header relative to its position in the tree (# ## ### #### ...)
        **Completeness over cleanliness.** Failed or blocked repos remain visible with preserved links.
        The INDEX is **standalone** — someone reading only the INDEX should understand each repo's gist. 
            /!\ Do not make me depend on opening individual `.gist.md` files.
        ---
        {
        ranking/scoring:
            relativity_with_my-original-query
            trust
        }
        ---
        {
        nested-tree =
            #
                # [category]
                    # [repo-link](aliased as author-name/repo-name) | [lang(n%)] [star(n*)] [contributors(n@)] | [official-description-section]
                        #git 
                            tldr-relevant-descriptive-subsections_shortcut-links(from official readme/website/wiki sources) : []
                        #gist
                            # what it is (notion)
                                # description : []
                                # ? 
                            # why it is (question)
                                # ?
                                # ?
                            # how it is (mediation)
                                # technology(structurality/construction)(internality) : []
                                # technicality(systemicality/constitution)(externality) : []
        imperfect-example =
                # [linguisticality]
                    # [.../rust-lang/rust] | [Rust90.3% HTML6.5% Shell0.8% C0.8% JavaScript0.5% Python0.3% Other0.8%] [115000*] [6700@] | [Empowering everyone to build reliable and efficient software.] 
                        #
                            https://github.com/rust-lang/rust#why-rust
                            https://doc.rust-lang.org/book/ch00-00-introduction.html
                            https://blog.rust-lang.org/2025/12/19/what-do-people-love-about-rust/
                        #
                            # it is a programming language that ... 
                                [quote-link(s)]
                            # it is especially for ... 
                                [quote-link(s)]
                            # it is by/with/through ... 
                                [quote-link(s)]
                        #
                            # beware of significant unresolved-issues about ... 
                                [quote-link(s)]
                            # beware of significant contradictions about ... 
                                [quote-link(s)]     
        }

    phase-4_outro/exclud/ex/selfreflect/invalidate: 

   
}


---

{
tags (its a mess yet) :

< self-~auto-~meta~ memory~~~versality/variety~~~flexivity~~~modality~~~methodology~~~mechanicity~materiality modalisation~~version~~memorisation~~methodologisation
    <
        <
        <
        <
        <
    < 
        <
        <
        <
        <
    < 
        <
        <
        <
        <
    < 
        <
        <
        <
        <


struct!
        ?form!
        ?soci!
        plex
        sign
        pos
    serv!
    script!
    modl!
    duct!
        caus
    port!
        ?vers!
        ?clud!
        cept
        ject
    val!
    ?dimensionalis!
        ?spatialis!
        ?temporalis!
        ?visualis!

---

modalisation~~modelisation~moderation~~modulation~modularisation~~modification
re-in-trans-inter-cross-di-con-VERS-ion-alisation
pre-re-ob-con-SERV-ation   ~ re-pre-de-in-a-TENT-ion
pre-re-de-con-in-a-SIGN-ation
re-trans-in-de-con-FORM-ation
trans-de-con-in-SCRIPT-ion
re-pro-trans-de-con-in-DUCT-ion
QUEST-ion
re-multi-du-com-si-in-ap-ex-PLIC-ation
re-de-con-in-ob-STRUCT-ion-uration    re-pro-trans-inter-de-com-in-POS-ition   
re-de-con-in-STIT-ution   re-trans-de-con-im-ex-PORT-ation-alisation   re-con-in-ex-CLUS-ion   dis-as-SOCI-ation   re-dis-con-a-TRIB-ution
DIMENS-ion
    SPATIALIS-ation
    TEMPORALIS-ation
~ VISUALIS-ation 
~ (labo/ope/impe/fede/ite/mode/abst)RAT-ion
~ re-pro-in-e-JECT-ion
re-de-con-inter-intra-extra-in-ex-CEPT-ion
e-VALUAT-ion
    QUALIFI-cation
    QUANTIFI-cation
CAUS-ation
~ re-in-de-e-VOLUT-ion

---

    ~~gnition~solution
    ~~manifestation
    ~~modalisation~version

    ~~memorisation
    ~~servation~archivation
    ~~indexation
    ~~condensation
    ~~notion
    ~~modularisation~symbolisation~signation~segmentation

    ~~symbolisation
    ~~formation
    ~~scription
    ~~vocation~duction~rection~methodisation~question
    ~~pression
    ~~plication
    ~~modelisation
    
    ~~struction/structuration~position~conexion~categorisation~tribution
    ~~stitution/systemisation~portation~clusion~sociation~organisation~fluctuation
    ~~dimension~vectorisation~spatialisation~temporalisation
    ~~figuration~spectralisation~imagination~visualisation
    ~~constellation~orbitation~gravitation~radiation
    ~~modelisation/modularisation
    
    ~~(labo/ope/impe/fede/ite/mode)ration
    ~~organisation~gestion
    ~~ordination~plication~synchronisation
    ~~mediation~portation~jection~duction~ception~interaction
    ~~manifestation
    ~~modification
    
    ~~observation
    ~~evaluation~qualification~quantisation
    ~~resolution
    ~~notification~signalisation
    ~~vision~visualisation
    ~~causation~chronologisation
    ~~detection
    ~~modelisation
    
    ~~modification~integration~normalisation~compatibilisation
    ~~volution~version
    ~~ception~transaction
    ~~vulnerabilisation/validation/securisation/protection~clusion
    ~~servation~tension
    ~~modulation

}






