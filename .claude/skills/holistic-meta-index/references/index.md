# index — one flat list, unfolding per repo

> phase 7. THE deliverable. `orientation-not-substitution`, `signal-over-saturation`,
> `failures-stay-visible` live in `spec.md §0.1`.

## form
    ONE artifact — the index IS the shortlist. no second leaderboard.
    a FLAT, relevance-ordered list · each repo appears exactly ONCE · no category nesting
    (so no repo needs a single "primary" home). the ONLY tree is intra-repo: glance → unfold.

## per repo
    header   NN · owner/repo — one-line notion
    glance   lang-roles · stars · contributors · significant-update cue · official description
             (#void any field the fetch could not reach — failures stay visible)
    tags     a DEDICATED line, always visible, never folded, so IDE text-search reaches it
    unfold   #git (origin-truth + links) · #gist (what/why/how) · #graph (relations)

## rank & display
    relevance-to-query orders ATTENTION. DISPLAY ≠ COMPARISON: stars/counts are shown for
    first-glance, NEVER ranked or compared by. a big star count never lifts a repo up the list.

## standalone
    reading only the index must suffice to grasp each repo — never force opening a gist file.

## navigate
    the tag legend (top) + IDE text-search on the tag lines regroups any cluster on demand,
    without nesting. flags (HYPE / UNFREE / FILLER) are shown inline, never hidden.
