# gist — opencog/atomspace · seed 19

    source · dossiers/opencog__atomspace.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    an in-memory knowledge store that is a metagraph rather than a graph
      ← "The OpenCog AtomSpace is an in-RAM knowledge representation (KR) database with an
         associated query engine and graph-re-writing system. It is a kind of in-RAM
         generalized hypergraph (metagraph) database."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    what it actually stores, stripped to the simplest statement it makes about itself
      ← "**What is it, then?** Most simply, the AtomSpace stores immutable, globally
         unique, [typed] [s-expressions.] … Each s-expression is called \"an Atom\". Each
         Atom is globally unique: there is only one copy, ever, of any given s-expression"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    its stated role is infrastructural, a component others are built on
      ← "The AtomSpace is a platform for building Artificial General Intelligence (AGI)
         systems. It provides the central knowledge representation component for OpenCog."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)

## why-it-is

    the need is stated as a representational goal — generality across data shapes
      ← "The goal of the AtomSpace is to be general: to allow you to work with whatever
         style of data you want: structured or unstructured. As graphs, as tables, as
         objects. As lambda expressions, as abstract syntax trees, as prolog-like logical
         statements."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    and as an unsolved research problem, stated as such
      ← "As it turns out, knowledge representation is hard, and so the AtomSpace has been
         (and continues to be) a platform for active scientific research on knowledge
         representation, knowledge discovery and knowledge manipulation."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)

## how-it-is · technology (internal)

    queries are themselves graphs, which is what lets rules be stored and searched
      ← "**Search queries are graphs.** … every query, every search is also a graph. That
         means one can store a collection of searches in the database, and access them
         later. This allows a graph rule engine to be built up."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    graphs are executable, and the resulting language has a name
      ← "**Graphs are executable.** Graph vertex types include \"plus\", \"times\",
         \"greater than\" and many other programming constructs. The resulting graphs
         encode [\"abstract syntax trees\"] and the resulting language is called
         [Atomese](https://wiki.opencog.org/w/Atomese)."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    the central split is immutable structure carrying mutable values
      ← "**Graph nodes carry vectors** [Values] are mutable vectors of data. Each graph
         element (vertex or edge, node or link) can host an arbitrary collection of
         Values. This is, each graph element is also a key-value database."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    and that split makes the graph a pipeline rather than only a store
      ← "**Graphs specify flows** Values can be static or dynamic. For the dynamic case, a
         given graph can be thought of as \"pipes\" or \"plumbing\"; the Values can
         \"flow\" along that graph."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    state is versioned in changesets, explicitly on the git analogy
      ← "**Frames (ChangeSets)** Store a sequence of graph rewrites, changes of values as
         a single changeset. … Very roughly, a changeset resembles a git commit, but for
         the graph database. … By storing frames, it is possible to revert to earlier
         graph state."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    searching runs in reverse too — answers looking for their questions
      ← "**Inverted searches.** ([DualLink].) … one \"has an answer\" and is looking for
         all \"questions\" for which its a solution. This is pattern recognition, as
         opposed to pattern search."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)

## how-it-is · technicality (external)

    the primary interface is Scheme, and the readme says the Python one is worse
      ← "The simplest, most complete and extensive interface to Atoms and the Atomspace is
         via scheme, and specifically, the GNU Guile scheme implementation." · "Python is
         more familiar than scheme to most programmers … Unfortunately, it is not as easy
         and simple to use as scheme; it also has various technical issues."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    the build is CMake with a small set of required packages
      ← "cd to project root dir / mkdir build / cd build / cmake .. / make -j / sudo make
         install / make -j check ARGS=-j"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    the licence carries a hand-written exception for linking non-AGPL work
      ← "all OpenCog source files use the AGPL with additional permissions to link OpenCog
         libraries with non-AGPL works"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/LICENSE)

## leaves — earned, not padded

    the readme spends a whole section on what it is NOT, because newcomers assume wrong
      ← "### What it Isn't / Newcomers often struggle with the AtomSpace, because they
         bring preconceived notions of what they think it should be, and its not that."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    and names the three wrong mental models exactly
      ← "* **It's not JSON.** … * **It's not SQL. It's also not noSQL**. … * **It's not a
         vertex+edge store**."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    Atoms and Values are separated for stated performance reasons, not only conceptual
      ← "Atoms are: … * Large, bulky, heavy-weight (because indexes are necessarily
         bulky)." · "By contrast, Values … * Are not indexed, and are accessible only by
         direct reference. * Small, fast, fleeting (no indexes!)"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    the project states its own difficulty and apologises for it
      ← "There is a challenging learning curve involved. We're sorry about that: if you
         have ideas for better API's … then contact us!"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    stability is stated as a constraint that costs hackability
      ← "The AtomSpace is a relatively mature system, and thus fairly complex. Because
         other users depend on it, it is not very \"hackable\"; it needs to stay
         relatively stable."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)

#graph-harvest

    "It provides the central knowledge representation component for OpenCog."
      (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
      → names `OpenCog`
    "Dead projects: these are no longer maintained. They used to work, but have been
      abandoned for various theoretical and political reasons: * [Natural language chat,
      robot control](https://github.com/opencog/opencog) (the opencog repo)"
      (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
      → names `opencog/opencog` by explicit URL, as DEAD. note it is a DIFFERENT repo
        from this one, and is not a seed of this run
    "Atomese originally arose as an attempt by Ben Goertzel and company to combine
      symbolic AI methods with probability theory, resulting in the definition of PLN"
      (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
      → names `Atomese` · names `PLN`
    "[Carnegie Mellon Binary Analysis Platforrm (BAP)](https://github.com/
      BinaryAnalysisPlatform/bap) … Thus, similar to the AtomSpace, but very highly
      specialized for binaries, and nothing else."
      (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
      → names `BAP` as an explicitly compared system
    "Seems that the AtomSpace is no longer alone in the hypergraph world! As of 2022, one
      can find a python library called [HyperNetX](https://hypernetx.readthedocs.io/en/
      latest/). Their documentation is even eerily similar to our own! Gee, how could that
      happen?"
      (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
      → names `HyperNetX`

## flags

    hype · superlative claims of uniqueness, including one used as link text to a PDF the
      project itself hosts
      ← "[a metagraph store is literally just-plain better than a graph store.]" · "the
         Atomspace provides a large variety of advanced features not available anywhere
         else." · "A dozen features that no other graph DB does, or has even dreamed of
         doing."
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    abandonment · this repo classifies its own sibling ecosystem as half-dead and dead,
      with a direction and NO dates
      ← "Zombie projects: these are half-dead; no one is currently working on them, but
         they should still work" · "Dead projects: these are no longer maintained. They
         used to work, but have been abandoned for various theoretical and political
         reasons"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    contribution · an unsubstantiated insinuation that a third party copied its docs
      ← "Their documentation is even eerily similar to our own! Gee, how could that
         happen?"
         (https://raw.githubusercontent.com/opencog/atomspace/HEAD/README.md)
    filler
      #void — none found in the frozen material
    unfree?
      #void — none found. AGPL with a linking exception, no edition tiering, no paywalled
      feature, no account gate stated
    contradiction
      #void — the readme's uniqueness claims and its self-critical passages sit in tension
      of REGISTER but do not contradict as claims; both directions are recorded above

## finding — the counter-register

    unusually, the same readme that claims no one else has dreamed of its features also
      says its learning curve is challenging, that it is not hackable, that juniors cannot
      participate, and closes its history with "to figure out how this is possible, or,
      perhaps being more honest, if this is possible." both directions are recorded and
      neither is averaged into a verdict
      #void — an observation about the source, carrying no claim about the project
