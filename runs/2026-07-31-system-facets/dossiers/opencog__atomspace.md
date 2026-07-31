---
status: ok
seed: 19
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests, LICENSE) · R4 WebFetch (page facts)
capture: readme (39.4 KB) read in three passes — head, body, tail — because a single
         capture exceeded the tool's inline limit. the full file was read.
---

# opencog/atomspace

    url          https://github.com/opencog/atomspace
    description  "The OpenCog (hyper-)graph database and graph rewriting system"
                 ← About field, verbatim (R4)
    site         https://opencog.org

## #git

    stars          986                     (R4)
    forks          255                     (R4)
    watchers       83                      (R4)
    license        GitHub reports "Not visible" (R4) — the auto-detector did not
                   classify it. FETCHED DIRECTLY (R1, LICENSE at root, 200):
                   "Unless indicated otherwise (a license reference in file headers, or
                    a LICENSE file in a directory), all OpenCog source files use the AGPL
                    with additional permissions to link OpenCog libraries with non-AGPL
                    works; the text of the OpenCog linking exception is located at the
                    end of this file."
                   → AGPL-3.0 WITH a custom linking exception. the non-standard preamble
                     is what defeats the classifier. recorded verbatim rather than
                     flattened to "AGPL".
    open-issues    68                      (R4)
    open-prs       0                       (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     c++    ← CMakeLists.txt at root (R1); "many (not all) Atom types do
                          have a corresponding C++ class" (S14)
                   cmake  ← CMakeLists.txt at root (R1); the documented build is
                          `cmake .. && make -j` (S25)
                   python ← pyproject.toml at root (R1); Cython listed as an optional
                          prerequisite (S27)
                   scheme/guile ← "guile · Embedded scheme REPL; version 3.0 or newer
                          required" (S26); "The simplest, most complete and extensive
                          interface … is via scheme" (S28)
                   atomese ← the project's own in-graph language (S6)
    deep-links     readme    https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md
                   license   https://raw.githubusercontent.com/opencog/atomspace/HEAD/LICENSE
                   wiki-atomspace https://wiki.opencog.org/w/AtomSpace
                   wiki-atomese https://wiki.opencog.org/w/Atomese
                   wiki-pattern https://wiki.opencog.org/w/Pattern_matching
                   blog      https://blog.opencog.org/
                   metagraph-paper opencog/sheaf/docs/ram-cpu.pdf
                   examples  examples/atomspace · examples/pattern-matcher

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "The OpenCog AtomSpace is an in-RAM knowledge representation (KR) database with
         an associated query engine and graph-re-writing system. It is a kind of in-RAM
         generalized hypergraph (metagraph) database."
    S2  "Metagraphs offer more efficient, more flexible and more powerful ways of
         representing graphs: [a metagraph store is literally just-plain better than a
         graph store.](…/opencog/sheaf/docs/ram-cpu.pdf) On top of this, the Atomspace
         provides a large variety of advanced features not available anywhere else."
    S3  "The AtomSpace is a platform for building Artificial General Intelligence (AGI)
         systems. It provides the central knowledge representation component for OpenCog.
         As such, it is a fairly mature component, on which a lot of other systems are
         built, and which depend on it for stable, correct operation in a day-to-day
         production environment."
    S4  "It is now commonplace to represent data as graphs; there are more graph databases
         than you can shake a stick at. What makes the AtomSpace different? A dozen
         features that no other graph DB does, or has even dreamed of doing."
    S5  "A key difference: the AtomSpace is a metagraph store, not a graph store.
         Metagraphs can efficiently represent graphs, but not the other way around."
    S6  "**Graphs are executable.** Graph vertex types include \"plus\", \"times\",
         \"greater than\" and many other programming constructs. The resulting graphs
         encode [\"abstract syntax trees\"] and the resulting language is called
         [Atomese](https://wiki.opencog.org/w/Atomese)."
    S7  "**Search queries are graphs.** … every query, every search is also a graph. That
         means one can store a collection of searches in the database, and access them
         later. This allows a graph rule engine to be built up."
    S8  "**Inverted searches.** ([DualLink].) … one \"has an answer\" and is looking for
         all \"questions\" for which its a solution. This is pattern recognition, as
         opposed to pattern search."
    S9  "**Graph nodes carry vectors** [Values] are mutable vectors of data. Each graph
         element (vertex or edge, node or link) can host an arbitrary collection of
         Values. This is, each graph element is also a key-value database."
    S10 "**Graphs specify flows** Values can be static or dynamic. For the dynamic case, a
         given graph can be thought of as \"pipes\" or \"plumbing\"; the Values can
         \"flow\" along that graph."
    S11 "**Frames (ChangeSets)** Store a sequence of graph rewrites, changes of values as
         a single changeset. … Very roughly, a changeset resembles a git commit, but for
         the graph database. … By storing frames, it is possible to revert to earlier
         graph state."
    S12 "### What it Isn't / Newcomers often struggle with the AtomSpace, because they
         bring preconceived notions of what they think it should be, and its not that."
    S13 "* **It's not JSON.** … * **It's not SQL. It's also not noSQL**. … * **It's not a
         vertex+edge store**."
    S14 "**What is it, then?** Most simply, the AtomSpace stores immutable, globally
         unique, [typed] [s-expressions.] … Each s-expression is called \"an Atom\". Each
         Atom is globally unique: there is only one copy, ever, of any given s-expression
         (Atom)."
    S15 "The AtomSpace is meant to allow general knowledge representation, in any format."
    S16 "All this means that the AtomSpace is different and unusual. It might be a bit
         outside of the comfort zone for most programmers. It doesn't have API's that are
         instantly recognizable to users of these other systems. There is a challenging
         learning curve involved. We're sorry about that"
    S17 "As it turns out, knowledge representation is hard, and so the AtomSpace has been
         (and continues to be) a platform for active scientific research on knowledge
         representation, knowledge discovery and knowledge manipulation. If you are
         comfortable with extremely complex mathematical theory, and just also happen to
         be extremely comfortable writing code, you are invited -- encouraged -- to join
         the project."
    S18 "Atomese originally arose as an attempt by Ben Goertzel and company to combine
         symbolic AI methods with probability theory, resulting in the definition of PLN,
         Probabilistic Logic Networks, articulated in several books devoted to the topic."
    S19 "This brings Atomese to it's present-day state: an infrastructure for symbolic AI,
         together with a (hyper-)graph database, offering dynamic sensori-motor processing
         primitives. The hope is that this is an appropriate toolset for agentic systems
         that can reify, transform and transmute their own content. It remains a research
         platform to figure out how this is possible, or, perhaps being more honest, if
         this is possible."
    S20 "Atoms are: * Used to represent graphs, networks, and long-term stable graphical
         relations. * Indexed … * Globally unique … * Immutable … * Large, bulky,
         heavy-weight (because indexes are necessarily bulky)."
    S21 "By contrast, Values, and valuations in general, are: * A way of holding on to
         rapidly-changing data, including streaming data. … * Are not indexed, and are
         accessible only by direct reference. * Small, fast, fleeting (no indexes!)"
    S22 "The AtomSpace is a relatively mature system, and thus fairly complex. Because
         other users depend on it, it is not very \"hackable\"; it needs to stay
         relatively stable."
    S23 "These innards are best left to committed systems programmers and research
         scientists; there is no easy way for junior programmers to participate, at
         least, not without a lot of hard work and study."
    S24 "Experience in any of the following areas will make things easier for you; in
         fact, if you are good at any of these ... we want you. Bad. * Database
         internals; query optimization. * Logic programming; Prolog. * SAT-solving;
         Answer Set programming; Satisfiability Modulo Theories. …"
    S25 "cd to project root dir / mkdir build / cd build / cmake .. / make -j / sudo make
         install / make -j check ARGS=-j"
    S26 "###### guile / * Embedded scheme REPL; version 3.0 or newer required."
    S27 "###### Cython / * C bindings for Python. (Cython version 0.23 or newer) *
         Recommended, as many users enjoy using python."
    S28 "The simplest, most complete and extensive interface to Atoms and the Atomspace is
         via scheme, and specifically, the GNU Guile scheme implementation."
    S29 "Python is more familiar than scheme to most programmers … Unfortunately, it is
         not as easy and simple to use as scheme; it also has various technical issues.
         Thus, it is significantly less-used than scheme in the OpenCog project."
    S30 "Unless indicated otherwise …, all OpenCog source files use the AGPL with
         additional permissions to link OpenCog libraries with non-AGPL works"  ← LICENSE

## potential-relation spans — collected, NOT resolved

    ── the run's largest single harvest, and the ONE place a collection-adjacent name
       appears. resolution is the workbench's mechanical job; nothing is typed here. ──

    "It provides the central knowledge representation component for OpenCog." (readme, S3)
       → names `OpenCog`
    "Atomese originally arose as an attempt by Ben Goertzel and company to combine
     symbolic AI methods with probability theory, resulting in the definition of PLN"
     (readme, S18)  → names `Atomese` · `PLN`
    "Dead projects: these are no longer maintained. They used to work, but have been
     abandoned for various theoretical and political reasons: * [Natural language chat,
     robot control](https://github.com/opencog/opencog) (the opencog repo)" (readme)
       → names `opencog/opencog` AS A DEAD PROJECT, by explicit URL, in this repo's own
         words.
       → NOTE seed 06 (trueagi-io/hyperon-experimental) states: "OpenCog Hyperon is a
         substantially revised, novel version of OpenCog" and "a successor to the OpenCog
         Classic Atomese language". THIS repo is `opencog/atomspace`; the repo seed 06's
         span calls dead is `opencog/opencog`. THEY ARE DIFFERENT REPOSITORIES under the
         same owner, and `opencog/opencog` is NOT a seed of this run.
       → resolving whether seed 06 and seed 19 are related — and if so how — requires
         judgment about what "OpenCog" denotes across two readmes. that is set-level.
         it goes to the workbench as a CANDIDATE with both spans attached, and the type
         is the user's ruling. it may also be the run's first case where neither
         available type (alternative-to · conflicts-with) fits, in which case it becomes
         a [proposal: new relation type] and is never coined by the agent.
    "Zombie projects: these are half-dead; no one is currently working on them, but they
     should still work … * [Genomic, proteomic data analysis](…/opencog/agi-bio) * [Port
     of the MOSES machine learning to Atomese](…/opencog/as-moses) * [Unified Rule
     Engine](…/opencog/ure) * [OpenAI Gym and Minecraft agents](…/opencog/rocca)" (readme)
       → names FOUR same-owner repos, self-classified half-dead. none a seed of this run.
    "* [Store AtomSpaces to disk](…/opencog/atomspace-rocks) * [Network-distributed
     AtomSpace storage](…/opencog/atomspace-cog) * [Network shell to AtomSpaces …]
     (…/opencog/cogserver) * [Sparse Vector/Matrix embeddings …](…/opencog/matrix) *
     [Sensori-motor research](…/opencog/sensory) * [Language learning](…/opencog/learn)"
     (readme)  → names SIX same-owner modules. none a seed of this run.
    "[Carnegie Mellon Binary Analysis Platform (BAP)](…) … Thus, similar to the AtomSpace,
     but very highly specialized for binaries, and nothing else." · "[Modelica](…) …
     Not suitable for general graph structures." (readme, Related ideas)
       → names `BAP` · `Modelica` as explicitly COMPARED systems. both out of collection.
    "Seems that the AtomSpace is no longer alone in the hypergraph world! As of 2022, one
     can find a python library called [HyperNetX](…). Their documentation is even eerily
     similar to our own! Gee, how could that happen?" (readme, Interesting Reading)
       → names `HyperNetX` — out of collection, and the span carries an insinuation of
         copying. recorded verbatim; the reading is the user's.
    "[NetworkX](https://networkx.org/) is a python package for analyzing complex networks."
     (readme)  → names `NetworkX`, out of collection.
    "cogutil · Common OpenCog C++ utilities · https://github.com/opencog/cogutil" ·
     "[ocpkg repo](…/opencog/ocpkg)" · "[opencog Docker containers](…/opencog/docker)"
     (readme, Prerequisites)  → same-owner build dependencies. none a seed of this run.

## flags-raw — what fetch itself revealed

    thin?          NO — 39.4 KB, the largest readme in the run, and dense with mechanism,
                   theory and history rather than install boilerplate.
    index-repo?    no. it names ~15 sibling repos, but as components and downstream
                   systems of ITSELF, not as an aggregation. NOT recursed into.
    archived/moved this repo carries no notice. it DOES classify sibling projects as
                   "Zombie projects: these are half-dead" and "Dead projects: these are
                   no longer maintained … abandoned for various theoretical and political
                   reasons". recorded verbatim: an unusually candid self-report of an
                   ecosystem's decay, made by the surviving component about its siblings.
                   NO DATES accompany it → the abandonment cue has a direction and no
                   when. the `when` is #void.
    note-for-gist  SUPERLATIVE CLAIMS, unusually direct: "a metagraph store is literally
                   just-plain better than a graph store" (S2, as LINK TEXT to a PDF the
                   project itself hosts), "advanced features not available anywhere else"
                   (S2), "A dozen features that no other graph DB does, or has even
                   dreamed of doing" (S4). the supporting PDF was NOT fetched — a claim
                   needing it must re-fetch into a new record first. recorded as claims.
    note-for-gist  AGAINST that, an equally direct counter-register in the same readme:
                   "There is a challenging learning curve involved. We're sorry about
                   that" (S16), "it is not very \"hackable\"" (S22), "there is no easy way
                   for junior programmers to participate" (S23), and the closing honesty
                   of S19 — "to figure out how this is possible, or, perhaps being more
                   honest, if this is possible." both directions recorded; the user
                   weighs.
    note-for-gist  the "Interesting Reading" section insinuates that a third-party
                   library's documentation copied its own ("eerily similar to our own!
                   Gee, how could that happen?"). recorded verbatim as a span. it is an
                   unsubstantiated implication about an outside project, and it is the
                   user's to weigh, not the agent's to characterise.
    note-for-gist  a TODO section ships in the readme naming an open bug by number
                   ("bug 2995") for Android porting. recorded as a fact.
