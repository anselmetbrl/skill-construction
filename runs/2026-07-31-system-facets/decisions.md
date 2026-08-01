# decisions — collisions the agent hit, and what it did pending your ruling

> everything here is OPEN unless marked otherwise. the agent took a provisional path so
> the run could continue; none of these is settled, and none was decided quietly.
> this file is not `rulings.md` — nothing here is yours yet.

---

## D1 · C4 collides with claims-resolve-to-spans   — OPEN

    hit at      phase 3, gist of seed 07 (h4ckf0r0day/obscura)

    the rule    C4: "star/fork/issue/contributor numbers outside glance lines = 0 …
                including sentences that DENY comparing — a count named in prose is a
                comparison."
    the other   claims-resolve-to-spans: "every claim carries `← \"quote\" (link)` …
                a paraphrase without a span is authorship, not evidence — forbidden."

    the case    obscura's readme carries a stale headline: "## 🎉 10,000 stars and what's
                next", while the repository's current figure is roughly double it. that
                staleness is a real filler/dating signal and belongs in the flag roster.
                but the ONLY honest way to record it is to quote it — and the quote
                contains a count. so:
                  · quote it        → C4 fires.
                  · paraphrase it   → authorship, forbidden, and the evidence is gone.
                  · drop the flag   → a real signal is silently discarded.
                all three are bad. that is a genuine collision between two rules, not a
                mistake in either.

    taken       counts inside a VERBATIM QUOTED SPAN are not violations, but they are
                counted and listed SEPARATELY in the check report, under their own
                heading, so nothing is hidden. counts in the AGENT's own prose remain
                violations and still read as zero.
    reasoning   C4's target is the agent comparing repos by number. a project's own
                sentence, quoted as evidence about that project, is not the agent
                comparing — it is the agent showing what the project said.
    cost        the carve-out is exactly the kind of thing that could be gamed: a
                comparison could be smuggled in by wrapping it in quotes. the mitigation
                is that quoted counts are LISTED, not merely tolerated, so any smuggling
                is visible in the report.

    your call   accept · narrow it · reject and drop the flag · rewrite C4 outright.
                the skill's own line on this: "a check becomes satisfiable by gaming its
                count → the check is rewritten WITH the user, and the gaming is
                recorded." this is the recording.

---

## D2 · seed 17 inclusion   — OPEN, defaulting to IN

    raised at   phase 1 (flag F1), restated at the phase 2 exit, unanswered twice
    the case    anselmetbrl/skill-construction is this run's own home and the home of
                the skill executing it.
    taken       carried IN, and its dossier PINNED to 6c1763a3 — the default-branch head
                that pre-dates every commit this run has made. so the run cannot cite
                material it is itself writing.
    still open  whether it appears in the INDEX at all. that is a set-level inclusion
                judgment and it is yours. the agent will not decide it by default beyond
                keeping it where you put it.

---

## D3 · phase 1 cannot classify before fetching   — OPEN, skill defect

    raised at   phase 1 (flag F3), recorded in seeds.md
    the case    SKILL.md says "classify every link BEFORE fetching". before fetching, the
                only evidence is the URL string. anything richer comes from trained
                memory, which is unfrozen material.
    taken       structural-only classification; the index-repo guard DEFERRED into fetch,
                where a real dossier can reveal an index-repo without recursion.
    outcome     the guard held. 0 of 25 seeds turned out to be index-repos; three were
                assessed at fetch and recorded as borderline-but-no (glicol's monorepo,
                atomspace's sibling list, WFGY's self-indexing tree), none recursed into.
    still open  whether SKILL.md's phase 1 should be rewritten to say what it can
                actually do. a ledger question, not a run question.
