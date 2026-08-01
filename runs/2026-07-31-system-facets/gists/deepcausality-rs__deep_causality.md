# gist — deepcausality-rs/deep_causality · seed 16

    source · dossiers/deepcausality-rs__deep_causality.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    the reference implementation of a named theory, not a library that grew a theory
      ← "DeepCausality is the reference implementation of the **Effect Propagation Process
         (EPP)**, a single axiomatic foundation for dynamic causality based on Whitehead's
         process metaphysics"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    the whole system rests on one stated axiom
      ← "The EPP rests on a single axiom: **`m₂ = m₁ >>= f`**. Effect propagation becomes
         a monadic dependency, with no assumption of any background spacetime."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

## why-it-is

    stated as a specific limitation in the existing frameworks, then what it adds
      ← "Classical computational causality frameworks (Pearl's SCM, Granger causality,
         DBNs) assume fixed background spacetime and static causal structure and thus
         cannot handle dynamic causal structures; DeepCausality contributes **dynamic,
         adaptive, and emergent** causality as first-class modalities, with a programmable
         deontic layer for verifiable safety."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    and, for the mathematics, as the cost of crossing between silos
      ← "Most scientific-computing stacks force you to bridge silos: one library for
         tensors, another for geometric algebra, a third for topology, with glue code in
         between."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

## how-it-is · technology (internal)

    three primitives operationalise the axiom, plus an optional fourth for safety
      ← "| **One axiom, three primitives** | Causaloid, Context, and Causal State Machine
         derived from a single functional-dependency axiom |"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    structure and sequencing are two isomorphic expressions of the same thing
      ← "- **Causaloid.** A polymorphic container for the causal function `f` (after
         Hardy). It carries causal *structure* … - **CausalMonad.** The bind side of the
         axiom, carrying causal *sequencing* through Kleisli composition."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    the environment is a queryable hypergraph, which is what detaches it from spacetime
      ← "An explicit hypergraph carrying the operational environment: sensor data,
         temporal structures (linear and non-linear), spatial locations (Euclidean and
         non-Euclidean). Detaching causality from a fixed background spacetime requires
         the Context to be queryable and dynamic."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    a deontic layer gates proposed actions before they execute
      ← "An optional, programmable deontic layer that uses a **defeasible deontic
         calculus** to resolve normative conflicts and decide whether a CSM-proposed
         action is permissible under an immutable ethos."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

## how-it-is · technicality (external)

    every mathematical layer shares one categorical interface, in stable Rust
      ← "| **Uniform mathematics** | Tensors, MultiVectors, Manifolds, and
         `PropagatingEffect` share one categorical interface (Functor / Monad / Comonad)
         via arity-5 HKT in stable Rust |"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    the crate boundary is the entry point, and it is one line
      ← "cargo add deep_causality_core"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    it sits under a foundation rather than a company
      ← "DeepCausality is hosted as a sandbox project at the [Linux Foundation for Data &
         AI](https://landscape.lfai.foundation/)."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    two build systems are documented, make and Bazel
      ← "make install   # Install dependencies / make build     # Build incrementally" ·
         "The repository also supports Bazel builds."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

## leaves — earned, not padded

    the interventional API walks a named academic ladder, and the example shows all three
      ← "This walks **Pearl's Ladder of Causation**: 1. **Association** (Rung 1) … 2.
         **Intervention** (Rung 2): `intervene(3.0)` forces a value mid-chain. 3.
         **Counterfactual** (Rung 3): Same chain, different outcome under the
         intervention."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    the audit log accumulates through the chain rather than being bolted on
      ← "`bind` short-circuits on error, accumulates the audit log, and supports
         counterfactual `intervene` operations."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    six of its crates carry the papers they implement, in-tree
      ← "**deep_causality_ethos** * [\"A Defeasible Deontic Calculus for Resolving Norm
         Conflicts\"](deep_causality_ethos/papers/ddic.pdf), Olson & Forbus"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    it ships guidance for LLM-assisted use of itself
      ← "For LLM-assisted project-building guidance, see [SKILLS.md](./SKILLS.md)."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)

#graph-harvest

    #void — this readme argues against a named intellectual position (Pearl's SCM,
      Granger causality, DBNs) and against a category of scientific-computing stack. it
      never names a competing software project, so nothing resolves against the
      collection.

## flags

    hype · two bare comparative performance claims, neither carrying a measurement
      ← "| **Float106 precision** | 106-bit float (~32 decimal digits) on stable Rust,
         several × faster than IEEE binary128 |" · "which cuts the scalar count from six
         to four (~50% compute reduction)"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    hype · a strong theoretical property asserted as a consequence, in the first sentence
      ← "with the consequence that the resulting framework is
         general-relativistic-native and quantum-native"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    filler · a broken URL ships in the badge block, the repository name misspelled
      ← "[codefactor-url]: https://www.codefactor.io/repository/github/deepcausality-rs/
         deep_causalityl"
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    unfree? · a backing entity is named for commercial support, alongside an MIT licence
      and no stated feature gating
      ← "if you need more support for a larger or commercial project, please feel free to
         reach out to the [Center of Dynamic Causality](https://www.causalcenter.com/
         contact/) that backs the Deep Causality project."
         (https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md)
    contradiction
      #void — none found in the frozen material

## finding — the register is academic, not promotional

    the strong claims here are theoretical positioning backed by cited papers, a Zenodo
      DOI and a CITATION.cff, rather than benchmark marketing. the two unmeasured speed
      claims above are the exception and are flagged as such
      #void — an observation about the source, carrying no claim about the project
