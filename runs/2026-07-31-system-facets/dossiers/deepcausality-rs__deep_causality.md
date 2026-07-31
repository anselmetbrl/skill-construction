---
status: ok
seed: 16
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# deepcausality-rs/deep_causality

    url          https://github.com/deepcausality-rs/deep_causality
    description  "Dynamic Causality in Rust"   ← About field, verbatim (R4)
    site         https://deepcausality.com

## #git

    stars          269                     (R4)
    forks          22                      (R4)
    watchers       4                       (R4)
    license        MIT                     (R4) — confirmed by readme S26
    open-issues    1                       (R4)
    open-prs       2                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. the crates.io badge is a static
                   "Latest" label, not a version string.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust  ← Cargo.toml at root (R1); "in stable Rust" (S10); crates.io
                   bazel ← "The repository also supports Bazel builds." (S24)
                   make  ← "make install / make build / make test …" (S23)
                   NOTE a workspace of ~17 named crates (S18-S22), each with its own
                        README linked from the root readme.
    deep-links     readme    https://raw.githubusercontent.com/deepcausality-rs/deep_causality/HEAD/README.md
                   site      https://deepcausality.com
                   getting-started https://www.deepcausality.com/docs/getting-started/install/
                   docs.rs   https://docs.rs/deep_causality/latest/deep_causality/
                   crates.io https://crates.io/crates/deep_causality
                   examples  examples/README.md
                   skills    ./SKILLS.md
                   citation  CITATION.cff
                   doi       https://doi.org/10.5281/zenodo.20195214
                   security  SECURITY.md
                   ossf      https://bestpractices.coreinfrastructure.org/projects/7568

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "DeepCausality is the reference implementation of the **Effect Propagation
         Process (EPP)**, a single axiomatic foundation for dynamic causality based on
         Whitehead's process metaphysics, with the consequence that the resulting
         framework is general-relativistic-native and quantum-native."
    S2  "Classical computational causality frameworks (Pearl's SCM, Granger causality,
         DBNs) assume fixed background spacetime and static causal structure and thus
         cannot handle dynamic causal structures; DeepCausality contributes **dynamic,
         adaptive, and emergent** causality as first-class modalities, with a
         programmable deontic layer for verifiable safety."
    S3  "DeepCausality is hosted as a sandbox project at the [Linux Foundation for Data &
         AI](https://landscape.lfai.foundation/)."
    S4  "Dynamic causality can be daunting at first, and if you need more support for a
         larger or commercial project, please feel free to reach out to the [Center of
         Dynamic Causality](https://www.causalcenter.com/contact/) that backs the Deep
         Causality project."
    S5  "For LLM-assisted project-building guidance, see [SKILLS.md](./SKILLS.md)."
    S6  "This walks **Pearl's Ladder of Causation**: 1. **Association** (Rung 1) … 2.
         **Intervention** (Rung 2): `intervene(3.0)` forces a value mid-chain. 3.
         **Counterfactual** (Rung 3): Same chain, different outcome under the
         intervention."
    S7  "| **One axiom, three primitives** | Causaloid, Context, and Causal State Machine
         derived from a single functional-dependency axiom |"
    S8  "| **Effect Ethos** | Defeasible deontic calculus (after Forbus) that verifies
         actions against an immutable ethos before execution |"
    S9  "| **Geometric Algebra** | Clifford algebras (Pauli, spacetime, conformal,
         projective, Dixon, Spin(10) GUA) with shared metric conventions |"
    S10 "| **Uniform mathematics** | Tensors, MultiVectors, Manifolds, and
         `PropagatingEffect` share one categorical interface (Functor / Monad / Comonad)
         via arity-5 HKT in stable Rust |"
    S11 "| **Float106 precision** | 106-bit float (~32 decimal digits) on stable Rust,
         several × faster than IEEE binary128 |"
    S12 "| **Differential Topology** | Manifolds, simplicial complexes, lattice gauge
         theory verified against 24 reference results from Creutz |"
    S13 "The EPP rests on a single axiom: **`m₂ = m₁ >>= f`**. Effect propagation becomes
         a monadic dependency, with no assumption of any background spacetime."
    S14 "- **Causaloid.** A polymorphic container for the causal function `f` (after
         Hardy). It carries causal *structure* and is isomorphic across three forms
         (**Singleton**, **Collection**, **Graph**)"
    S15 "- **CausalMonad.** The bind side of the axiom, carrying causal *sequencing*
         through Kleisli composition. `bind` short-circuits on error, accumulates the
         audit log, and supports counterfactual `intervene` operations."
    S16 "An explicit hypergraph carrying the operational environment: sensor data,
         temporal structures (linear and non-linear), spatial locations (Euclidean and
         non-Euclidean). Detaching causality from a fixed background spacetime requires
         the Context to be queryable and dynamic."
    S17 "An optional, programmable deontic layer that uses a **defeasible deontic
         calculus** to resolve normative conflicts and decide whether a CSM-proposed
         action is permissible under an immutable ethos. Required wherever emergent
         causality is in play, since static verifiability is no longer possible there."
    S18 "Most scientific-computing stacks force you to bridge silos: one library for
         tensors, another for geometric algebra, a third for topology, with glue code in
         between. The DeepCausality stack lifts every mathematical layer into the same
         categorical interface"
    S19 "The [Maxwell example](examples/physics_examples/maxwell/) derives `E` and `B` as
         bivector grades of a single electromagnetic field `F = ∇A`, which cuts the
         scalar count from six to four (~50% compute reduction) and is directly
         applicable to 5G/6G phased-array antenna design."
    S20 "| [`ultragraph`](ultragraph/README.md) | Two-phase hypergraph backend for
         CausaloidGraph and Context |"
    S21 "| [`deep_causality_discovery`] | Causal Discovery Language (typestate DSL:
         load → clean → select → discover → analyse) |"
    S22 "| [`deep_causality_haft`] | Arity-5 higher-kinded types via witness pattern;
         Effect / Functor / Applicative / Monad / CoMonad |"
    S23 "make install   # Install dependencies / make build     # Build incrementally /
         make test      # Run all tests / make check     # Security audit"
    S24 "The repository also supports Bazel builds. Install [bazelisk] and run: `bazel
         build //...`"
    S25 "Contributions are welcome! Please read: * [AI Coding Assistants]
         (AiCodingAssistants.md) * [Contributing Guide](CONTRIBUTING.md) * [Code of
         Conduct](CODE_OF_CONDUCT.md)"
    S26 "This project is licensed under the [MIT license](LICENSE)."
    S27 "[JetBrains](https://www.jetbrains.com/) provides the project with an all-product
         license."
    S28 "The [Center for Dynamic Causality](https://www.causalcenter.com) contributes
         ongoing research and resources to the DeepCausality project."
    S29 "> Hansen, M. (2026). *DeepCausality* [Computer software]. Zenodo.
         https://doi.org/10.5281/zenodo.20195214"
    S30 "Inspired by research from: * [Judea Pearl]: Structural Causal Models * [Lucien
         Hardy]: Causaloid framework * [Elias Bareinboim]: Transportability and data
         fusion"

## potential-relation spans — collected, NOT resolved

    "Classical computational causality frameworks (Pearl's SCM, Granger causality, DBNs)
     assume fixed background spacetime and static causal structure and thus cannot handle
     dynamic causal structures" (readme, S2)
       → names `Pearl's SCM` · `Granger causality` · `DBNs` — academic FRAMEWORKS, not
         software projects. no target resolves against this collection.
    "Most scientific-computing stacks force you to bridge silos: one library for tensors,
     another for geometric algebra, a third for topology" (readme, S18)
       → names CATEGORIES of library, no project. no resolvable target.
    "DeepCausality can express all [major frameworks of classical computation causality]"
     (readme, linking examples/classical_causality_examples)
       → an in-repo directory, not an external project.
    "Inspired by research from: * [Judea Pearl] … * [Lucien Hardy] … * [Elias
     Bareinboim]" (readme, S30)  → names RESEARCHERS. not projects.
    "[bazelisk](https://github.com/bazelbuild/bazelisk)" (readme, S24)
       → names a build tool. dependency, out of collection.

    NOTE for the workbench: this readme argues hard against a named intellectual
    position (S2) and never against a named software project. seeds 06
    (hyperon-experimental) and 19 (opencog/atomspace) also occupy reasoning /
    knowledge-representation territory, and NONE of the three names either of the
    others. absence of an edge is the finding, and it is stated rather than filled.

## flags-raw — what fetch itself revealed

    thin?          no — 22.9 KB.
    index-repo?    no. it is a monorepo cataloguing its OWN ~17 crates; the crate tables
                   point in-tree, not at third parties. NOT recursed into.
    archived/moved no notice.
    note-for-gist  UNVERIFIED PERFORMANCE CLAIMS, two of them, each a bare comparative
                   with no cited measurement in the readme: "several × faster than IEEE
                   binary128" (S11) and "(~50% compute reduction)" (S19). recorded
                   verbatim as claims; nothing here verifies them.
    note-for-gist  the register is ACADEMIC rather than promotional — "reference
                   implementation", "single axiomatic foundation", papers linked in-tree
                   for six separate crates, a Zenodo DOI and a CITATION.cff (S29). the
                   strong claims that do appear ("general-relativistic-native and
                   quantum-native", S1) are theoretical positioning, not benchmark
                   marketing. recorded with spans; the user weighs.
    note-for-gist  COMMERCIAL ADJACENCY, stated openly: a backing entity is named for
                   "larger or commercial project" support (S4) and again as a
                   contributor of "research and resources" (S28). the code itself is MIT
                   (S26) with no feature gating stated anywhere in the readme. recorded
                   as facts on both sides.
    note-for-gist  S5 — the project ships a `SKILLS.md` for "LLM-assisted
                   project-building guidance", and S25 links an `AiCodingAssistants.md`
                   contributor doc. recorded as facts about the repo's own contents.
    note-for-gist  a broken link is present in the badge block: the CodeFactor URL ends
                   "deep_causalityl" with a trailing L. recorded as a fetch observation.
