#!/usr/bin/env python3
"""checks — the mechanical gate for run 2026-07-31-system-facets.

every check is a COUNT with a definite answer. nothing here asks for judgment.
output is an EXHIBIT shown to the user, never a gate that silently passes.

gist line convention, so C1 is parseable:
    exactly 4 spaces + text   = a CLAIM HEAD. must be grounded.
    6 or more spaces + text   = continuation (wrapped claim, quote, or link).
    a claim is GROUNDED if its unit (head + continuations, up to the next head)
    contains either  ← "..." (http...)  or  #void.
"""
import re, sys, glob, os, collections

RUN = os.path.dirname(os.path.abspath(__file__))
G = sorted(glob.glob(os.path.join(RUN, "gists", "*.md")))
D = sorted(glob.glob(os.path.join(RUN, "dossiers", "*.md")))
EDGE_TYPES = {"alternative-to", "conflicts-with"}


def units(path, skip_harvest=True):
    """yield (lineno, head_text, unit_text) for every 4-space claim head.

    the #graph-harvest block is EXCLUDED by default: harvested spans are not claims.
    they carry their own format ("span" (link) -> names X) and their own check, C3.
    """
    lines = open(path).read().split("\n")
    if skip_harvest:
        out, inh = [], False
        for l in lines:
            if l.startswith("#graph-harvest"):
                inh = True
            elif inh and l.startswith("## "):
                inh = False
            out.append("" if inh else l)
        lines = out
    heads = [i for i, l in enumerate(lines)
             if re.match(r"^ {4}\S", l)]
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        yield i + 1, lines[i].strip(), "\n".join(lines[i:end])


def c1_grounding():
    """every gist claim head resolves to a quote+link or is a void."""
    bad = []
    total = 0
    for f in G:
        for ln, head, unit in units(f):
            total += 1
            if "#void" in unit:
                continue
            if "←" in unit and re.search(r"\(https?://", unit):
                continue
            bad.append((os.path.relpath(f, RUN), ln, head[:64]))
    return total, bad


def c2_graph_types():
    """coined edge types = 0. only the two sanctioned types may appear as edges."""
    bad = []
    for f in G:
        for ln, head, unit in units(f):
            m = re.findall(r"\[(?:edge|type):\s*([a-z-]+)\]", unit)
            for t in m:
                if t not in EDGE_TYPES:
                    bad.append((os.path.relpath(f, RUN), ln, t))
    return bad


def c3_graph_fill():
    """every harvest entry carries a verbatim quote, a link, and a resolved name.
    an empty harvest renders exactly #void — commentary in a harvest slot is a
    violation."""
    bad, entries = [], 0
    for f in G:
        rel = os.path.relpath(f, RUN)
        txt = open(f).read()
        if "#graph-harvest" not in txt:
            bad.append((rel, 0, "no #graph-harvest block"))
            continue
        block = txt.split("#graph-harvest", 1)[1].split("\n## ", 1)[0]
        if "#void" in block:
            continue                      # an honest empty harvest
        lines = block.split("\n")
        heads = [i for i, l in enumerate(lines) if re.match(r"^ {4}\S", l)]
        if not heads:
            bad.append((rel, 0, "harvest block neither #void nor populated"))
        for n, i in enumerate(heads):
            end = heads[n + 1] if n + 1 < len(heads) else len(lines)
            unit = "\n".join(lines[i:end])
            entries += 1
            if not unit.lstrip().startswith('"'):
                bad.append((rel, i + 1, "entry does not open with a verbatim quote"))
            elif not re.search(r"https?://", unit):
                bad.append((rel, i + 1, "entry carries no link"))
            elif "→ names" not in unit and "→ resolves" not in unit:
                bad.append((rel, i + 1, "entry resolves to no name"))
    return entries, bad


def c4_counts_in_prose():
    """star/fork/issue/contributor numbers outside glance lines = 0, in gists.

    COLLISION, recorded 2026-07-31 and OPEN for the user (see decisions.md D1):
    C4 exists to stop the AGENT comparing repos by count. claims-resolve-to-spans
    requires every claim to carry its verbatim quote. when a project's OWN readme
    states a count and that count IS the evidence for a flag, the two rules collide.
    resolution taken, provisionally: a count inside a verbatim quoted span is NOT a
    violation, but it is COUNTED AND LISTED SEPARATELY so nothing is hidden. a count
    in the agent's own prose remains a violation. the user rules on whether this
    stands.
    """
    pat = re.compile(r"\b\d[\d,.]*\s*k?\s*(stars?|forks?|watchers?|contributors?)\b", re.I)
    bad, quoted = [], []
    for f in G:
        rel = os.path.relpath(f, RUN)
        lines = open(f).read().split("\n")
        for i, l in enumerate(lines, 1):
            if not pat.search(l):
                continue
            # inside a quoted span? the unit's head carries ← and the line is a quote
            unit_start = i - 1
            while unit_start > 0 and not re.match(r"^ {4}\S", lines[unit_start]):
                unit_start -= 1
            unit = "\n".join(lines[unit_start:i])
            if "←" in unit or l.strip().startswith(("←", '"')):
                quoted.append((rel, i, l.strip()[:64]))
            else:
                bad.append((rel, i, l.strip()[:64]))
    return bad, quoted


def c6_voids():
    """tally #void per gist. an honesty rate, never a score to minimise."""
    t = {}
    for f in G:
        t[os.path.basename(f)[:-3]] = open(f).read().count("#void")
    return t


def c7_flag_grounding():
    """every flag that FIRED carries a quote; every flag that did not is a void."""
    bad, fired = [], 0
    for f in G:
        txt = open(f).read()
        if "## flags" not in txt:
            bad.append((os.path.relpath(f, RUN), "no flags section"))
            continue
        block = txt.split("## flags", 1)[1]
        for ln, head, unit in units_from_text(block, f):
            if "#void" in unit:
                continue
            fired += 1
            if not ("←" in unit and re.search(r"\(https?://", unit)):
                bad.append((os.path.relpath(f, RUN), ln, head[:64]))
    return fired, bad


def units_from_text(text, label):
    lines = text.split("\n")
    heads = [i for i, l in enumerate(lines) if re.match(r"^ {4}\S", l)]
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        yield i + 1, lines[i].strip(), "\n".join(lines[i:end])


def c9_coverage():
    """one gist per dossier, no orphans either way."""
    dn = {os.path.basename(p)[:-3] for p in D}
    gn = {os.path.basename(p)[:-3] for p in G}
    return sorted(dn - gn), sorted(gn - dn)


if __name__ == "__main__":
    print("=" * 66)
    print("CHECK REPORT — run 2026-07-31-system-facets")
    print("=" * 66)

    tot, bad = c1_grounding()
    print(f"\nC1 grounding      {tot} claim heads · violations = {len(bad)}")
    for f, ln, h in bad[:40]:
        print(f"    {f}:{ln}  {h}")

    b2 = c2_graph_types()
    print(f"\nC2 graph-types    coined types = {len(b2)}")
    for f, ln, t in b2:
        print(f"    {f}:{ln}  '{t}'")

    filled, b3 = c3_graph_fill()
    print(f"\nC3 graph-fill     resolved harvest lines = {filled} · malformed blocks = {len(b3)}")
    for row in b3:
        print(f"    {row}")

    b4, q4 = c4_counts_in_prose()
    print(f"\nC4 counts-in-prose violations = {len(b4)}"
          f" · counts inside quoted evidence = {len(q4)} [see decisions.md D1, OPEN]")
    for f, ln, l in b4:
        print(f"    VIOLATION {f}:{ln}  {l}")
    for f, ln, l in q4:
        print(f"    quoted    {f}:{ln}  {l}")

    v = c6_voids()
    print(f"\nC6 voids-reported total = {sum(v.values())} across {len(v)} gists")
    for k in sorted(v, key=lambda x: -v[x]):
        print(f"    {v[k]:>3}  {k}")

    fired, b7 = c7_flag_grounding()
    print(f"\nC7 flag-grounding fired flags = {fired} · ungrounded = {len(b7)}")
    for row in b7:
        print(f"    {row}")

    miss, orph = c9_coverage()
    print(f"\nC9 coverage       dossiers without gist = {len(miss)} · orphan gists = {len(orph)}")
    for m in miss:
        print(f"    missing gist: {m}")
    for o in orph:
        print(f"    orphan gist:  {o}")

    print()
    fail = len(bad) + len(b2) + len(b3) + len(b4) + len(b7) + len(miss) + len(orph)
    print(f"TOTAL VIOLATIONS = {fail}")
