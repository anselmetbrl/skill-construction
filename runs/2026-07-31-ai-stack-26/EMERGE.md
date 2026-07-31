# EMERGE — the whole, spoken

*A companion to the index. Not a second list — the things that only show up when you hold all
twenty-five repos at once. Read it aloud if you like; it's built for the ear.*

---

**The spine of your collection is a wager about HOW to build AI, not a pile of chatbots.**
Almost nothing here is a finished assistant. It is method and infrastructure. Two camps
answer the same question — how do you make a machine reason reliably. One camp says *program
it*: **dspy**, **baml**, and **symbolicai** turn LLM calls into typed, testable code instead
of brittle prompts. The other says *reason symbolically*: **hyperon**, **atomspace**, and
**deep_causality** build explicit knowledge and causal structure. **symbolicai** is the hinge
that touches both.

**You curated a dissenter, and that's a signal.** In the middle of an AI-stack collection,
**yo** states flatly that it is *NOT an LLM with shell access* — a fast, offline, rule-based
voice assistant that refuses the whole premise its neighbours are built on. It sits right next
to **kash** and **intelli-shell**, which lean INTO AI in the shell. Holding them together is
the point: you kept a foil, not just believers.

**Nix is the quiet substrate under a third of the list.** **devenv**, **den**, **vpsadminos**,
**stereOS**, and **yo** are all Nix — and they are not redundant, they are different layers:
dev-shells, config-composition, a container host OS, an agent host OS, a voice grammar. This is
your stack showing through the curation. Notably, **stereOS** is where two of your worlds meet
— a Nix OS built specifically to sandbox AI agents.

**There's a privacy-and-local thread worth naming.** **screenpipe**, **normcap**, **kash**, and
**yo** all keep data on your machine. But carry one warning into the reading: **screenpipe's
license just stepped AWAY from open** — now "source-available", not OSI-open, in its own words
*"to keep screenpipe sustainable."* It's the single **unfree** flag in the set, and given how
you weigh paywall-sabotage, it's the one to look at first.

**Stars lie about relevance here, so I did not order by them.** **bevy** has 47k, **dspy** 36k,
**screenpipe** 20k, **obscura** 20k — and several sit low in the index on purpose. Three repos
wear a **promotional register** — **obscura**, **screenpipe**, and **typedb** — with
self-benchmarks, "groundbreaking", "the leading". One, **WFGY**, is essentially an *AI routing
homepage*: its README is written to steer crawlers, and what the code actually does is **#void**.
None of that condemns them — it's evidence you weigh. But in this collection, a big number
tracks promotion and age, not fit to your query.

**Both hard relations I found are generational.** **letta → letta-code** and **hyperon →
atomspace** are the only two evidenced cross-repo edges, and both are successions: a newer
project self-declaring as the heir of an older one. So read the successor for the live state,
and keep the ancestor for lineage. Everything else that looks connected — the clusters — is
carried by the tag lines and search, not by forced links. For a hand-picked set of 25, two real
edges is the honest count.

**One repo doesn't belong to any of it, and that's fine.** **cheat-engine** — a Pascal
memory-scanner for game-modding — is the outlier, a reminder that your curation reaches past AI
into plain low-level computing. Let it be a partition of one.

---

*Two honest limits on this run, so you read it right.* First, the **GitHub API was unreachable**
this session for 24 of 25 repos, so **contributor counts, exact language percentages, and
last-commit dates are `#void`** everywhere — that's a session-scope wall, not a fact about the
repos. Second, the **twelve-tag budget** fits your dense AI-core well but leaves the long tail
thin — eight repos carry a single tag and two carry none. If you want the tail to partition too,
`tags.md` lists four candidate tags waiting for your say.
