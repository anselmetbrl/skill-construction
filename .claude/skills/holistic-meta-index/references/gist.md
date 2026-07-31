# gist — the inferred layer, written by the agent reading

> phases 3 (uni) + 4 (multi). the agent reads the dossier and infers. NO sub-LLM delegation.
> the gist is recompilable (not frozen). `evidence-over-verdict`, `void-over-hallucination`,
> `the-agent-does-the-reading`, `capture-over-judge` live in `spec.md §0.1`.

---

## the spine — FIXED, three angles, each DISTINCT

    what-it-is    (notion)     the thing itself, in one grounded line
    why-it-is     (question)   the problem/gap it answers — the question it is an answer to
    how-it-is     (mediation)  split in two:
                    technology   INTERNAL — what it is built of (langs, arch, engine)
                    technicality EXTERNAL — dependencies, stack-fit, how you adopt it

    rule   do NOT reuse one phrase across what/why/how. each angle is a different cut.
           `#void` any angle the repo genuinely does not answer — never pad.

## the leaves — EARNED, quote-grounded

    as many nodes as the repo actually yields, each carrying its evidence.
    a thin repo yields few leaves — that is a FINDING, stated plainly, not hidden.

## flags — impartial, evidence-carried (record; do not moralise)

    marketing-hype     a superlative asserted as established fact, in the project's own
                       promotional register ("groundbreaking", "the leading", self-benchmarks)
    seo/ai-filler      text written to route crawlers/rank, not to explain the code
    abandonment        stale in a way that matters (weigh significant-update, not bot-bumps)
    weak/fake contrib  contribution that looks thin or inflated
    unfree             paywall-sabotage — cloud hosting is fine; crippled self-hosting / a
                       license moved AWAY from open is the flag (A14)
    contradiction      the repo says two incompatible things — RECORD it, user resolves

## trust — subtractive

    starts whole, eroded by accumulated red flags. NEVER a computed score. a flag lowers
    trust; it does not condemn. the user weighs.

## uni pass (phase 3)   ·   augment from the repo ALONE

    one repo at a time, from its dossier. harvest any relation-quote into `#graph`
    (unresolved — phase 6 resolves targets). micro self-check after each.

## multi pass (phase 4)   ·   re-read from the evolved whole

    after ALL uni done: build `gists/_whole.md` (one compact line per repo, resident).
    re-read each gist against the whole, in batches — ADD relative position, do NOT
    rewrite the uni gist into a summary of the collection. highest-relevance first,
    whole-synthesis last (never bury either end in the middle). micro self-check per batch.
