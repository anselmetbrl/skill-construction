# checks — the mechanical gate + the user's sample-audit

> what died here (ledger S4): the four-adjective self-judgment gate. it ran at every
> phase of the test run and passed every time while the artifacts collapsed — "the
> check becomes a ritual that always passes" fired in full. an LLM cannot police its
> own set-level quality. so: NOTHING below asks for judgment. every check is a COUNT
> with a definite answer, and the counts are SHOWN to the user as an exhibit.
> (the four prose-tests survive only as the stance's rule for conversational prose —
> CLAUDE.md territory, not artifact territory.)

---

## the counts — run at every phase exit, report in workbench.md

    C1  grounding        every #gist claim-line contains `← "…" (http…)` or is `#void`.
                         violations = 0.
                         shape: grep -EL each gist for lines failing the pattern.
                         (the test run measured 0 of 75 grounded. this check exists
                          because of that number.)
    C2  graph-types      edge types ∈ { alternative-to · conflicts-with }. coined
                         types = 0. a third kind found in the material → it appears as
                         a PROPOSAL in workbench.md, never as an edge.
    C3  graph-fill       every edge carries its quote+link. edges without = 0.
                         an empty #graph renders exactly `#void` — commentary,
                         "share-tag", "thematic cluster", "the hinge/bridge/outlier"
                         in an edge slot = violations. (test run: 25/25 slots filled,
                         2 real edges.)
    C4  counts-in-prose  star/fork/issue/contributor numbers outside glance lines = 0,
                         in INDEX and EMERGE both. including sentences that DENY
                         comparing ("stars did not lift them") — a count named in
                         prose is a comparison.
    C5  standalone       INDEX references to run-internal files (tags.md, gists/,
                         workbench, rulings…) = 0. repo links and deep source links
                         are the only pointers out.
    C6  voids-reported   tally #void per artifact and per field. REPORT the number —
                         it is an honesty rate the user reads, never a score to
                         minimise or a gap to fill.
    C7  tag-candidates   every candidate tag lists the repos it partitions and a
                         grounding span per repo. a candidate holding ONE repo is
                         marked partition-of-one — allowed as a proposal, never
                         silently minted into the set.
    C8  emerge-warrant   every EMERGE paragraph names ≥1 repo and derives from a
                         ruling the user ACCEPTED. paragraphs whose subject is the
                         USER (their curation, their taste, their signal) = 0.

## on failure

    fix in place or revert that unit under git and retry. list what failed and what
    was done in the check-report. a violation discovered and repaired stays VISIBLE —
    the report is the shadow's record, not a clean bill.

## the sample-audit — the only quality judgment, and it is the user's

    when      phase 7, after render. also any time the user asks.
    sample    the USER picks the repos. never the agent. (an agent-picked sample is
              the ritual again.)
    do        for every claim in the sampled entries: open the frozen dossier, find
              the span, verify quote and link resolve. report each miss with the
              failing line. fix. re-count. show before/after.
    close     the run is done when the user says the sample reads true — not when
              the counts pass. counts are necessary, never sufficient.
