---
status: ok
seed: 12
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# denful/den

    url          https://github.com/denful/den
    description  "Aspect-oriented, context-driven Nix configurations."
                 ← About field, verbatim (R4)
    site         https://den.denful.dev

## #git

    stars          530                     (R4)
    forks          49                      (R4)
    watchers       11                      (R4)
    license        Apache-2.0              (R4)
    open-issues    20                      (R4)
    open-prs       3                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. readme carries a release BADGE
                   whose rendered value is absent from raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     nix ← flake.nix at root (R1); every code sample in the readme is Nix
    deep-links     readme    https://raw.githubusercontent.com/denful/den/HEAD/README.md
                   docs      https://den.denful.dev
                   principles https://den.denful.dev/explanation/core-principles/
                   zero-to-den https://den.denful.dev/guides/from-zero-to-den/
                   flake-to-den https://den.denful.dev/guides/from-flake-to-den/
                   custom-classes https://den.denful.dev/guides/custom-classes/
                   motivation https://den.denful.dev/motivation/
                   templates https://den.denful.dev/tutorials/default/
                   sponsor   https://denful.dev/sponsor

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "# den — Aspect-oriented, Context-driven Nix"
    S2  "**Write a feature once. Run it on every host, user, and platform you have — and
         share it with anyone, flake or not.**"
    S3  "Den turns Nix configuration into composable **features** instead of per-host
         piles of modules."
    S4  "A Den _aspect_ is a plain function: give it context (your hosts and users) and it
         returns configuration for every Nix class it touches — `nixos`, `darwin`,
         `homeManager`, `hjem`, or a class you invent."
    S5  "That one idea — **a feature as a function** — is what makes the rest possible."
    S6  "- **One feature, everywhere, in one place.** Stop scattering a single concern
         across separate `nixos`, `darwin`, and `homeManager` files. An aspect holds all
         of it together."
    S7  "- **Reuse across hosts, users — and across projects.** Share aspects between
         machines, between people, and between _flake and non-flake_ setups, without
         forcing everyone to download each other's inputs."
    S8  "- **No `mkIf` / `enable` clutter.** The shape of the context _is_ the condition —
         a function that asks for `{ host, user }` simply doesn't run where there's no
         user. Conditionals disappear."
    S9  "- **Hosts shape their users, users shape their hosts.** Cross-entity
         configuration flows both ways, without coupling them together."
    S10 "- **Bring your own classes and whole pipelines.** Custom Nix classes, machine
         fleets, MicroVM guests, terranix, standalone neovim — if you can walk it as
         data, Den can configure it."
    S11 "Four concepts, one job each: - **Entity** — _what exists_: a host, user, or home.
         - **Aspect** — _what it does_: a feature, spanning Nix classes. - **Policy** —
         _how entities relate_: topology and routing between them. - **Quirk** —
         _structured data aspects share_, without coupling."
    S12 "**Feature-first, not host-first.** Traditional setups start from hosts and push
         modules down; Den [flips that] — features are primary, hosts just select them."
    S13 "**Den embraces your Nix.** With or without flakes, flake-parts, or home-manager.
         Zero dependencies. Every part is optional and replaceable — Den works with the
         setup you already have, and gets out of the way."
    S14 "den.aspects.gaming = { host, user }: { nixos = { pkgs, ... }: {
         programs.steam.enable = true; }; … includes = [ den.aspects.performance ];
         # aspects compose / provides.emulation = { nixos = { /* ... */ }; };  # and nest
         };"                                             ← the readme's central example
    S15 "# a MicroVM / nix run github:denful/den?dir=templates/microvm#runnable-microvm
         / # a standalone neovim / nix run github:denful/den?dir=templates/nvf-standalone
         #my-neovim / # a qemu VM / nix run github:denful/den"
    S16 "- [noflake](https://den.denful.dev/tutorials/noflake) — npins + `lib.evalModules`
         + nix-maid"                                     ← Templates list
    S17 "> den and [vic](https://bsky.app/profile/oeiuwq.bsky.social)'s [aspect libs]
         (https://denful.dev) made for you with Love++ and AI--."
    S18 "> Den is also running on internal infra at **The European Commission**."
    S19 "Growing adoption: [usage search](https://github.com/search?q=den.aspects+
         language%3ANix&type=code)"
    S20 "### In the wild - [`@vic`](https://github.com/vic/vix) — fleet-sharing config
         from Den's author - [`@quasigod`](https://tangled.org/quasigod.xyz/nixconfig) —
         custom namespaces + angle brackets - [`@Gwenodai`] … - [`@adda`] …"
    S21 "> Den takes the Dendritic pattern to a whole new level, and I cannot imagine
         going back.\\ — `@adda`, early Den adopter (after Dendritic flake-parts and
         Unify)"                                         ← What people say
    S22 "> I'm super impressed with den so far, I'm excited to try out some new patterns
         that Unify couldn't easily do.\\ — `@quasigod`, author of [Unify]"
                                                         ← What people say
    S23 "> Den is a playground for some very advanced concepts… some of its ideas will
         play a role in future Nix areas. There are some raw diamonds in Den.\\ —
         `@Doc-Steve`, author of the [Dendritic Design Guide]"
                                                         ← What people say
    S24 "> Thanks for the awesome library and the support for non-flakes… it's positively
         brilliant! I really hope this gets wider adoption.\\ — `@vczf`"
                                                         ← What people say

## potential-relation spans — collected, NOT resolved

    "Den takes the Dendritic pattern to a whole new level … (after Dendritic flake-parts
     and Unify)" (readme, S21, a QUOTED THIRD PARTY)
       → names `Dendritic` · names `Unify` — out of collection.
    "I'm excited to try out some new patterns that Unify couldn't easily do." (readme,
     S22, a QUOTED THIRD PARTY)  → names `Unify` (codeberg.org/quasigod/unify)
    "**Den embraces your Nix.** With or without flakes, flake-parts, or home-manager."
     (readme, S13)  → names `flake-parts` · `home-manager` — compatibility targets.
    "Custom Nix classes, machine fleets, MicroVM guests, terranix, standalone neovim"
     (readme, S10)  → names `terranix` · `MicroVM` · `neovim` — configuration targets.
    "- [noflake] — npins + `lib.evalModules` + nix-maid" (readme, S16)
       → names `npins` · `nix-maid` — template ingredients, out of collection.

    NOTE for the workbench: EVERY comparative span in this readme is inside a
    third-party TESTIMONIAL, not in the project's own voice. den itself never positions
    against a named alternative. that distinction is preserved here and must survive
    into any edge proposal — a quoted stranger's comparison is weaker evidence than a
    project's own claim, and the user rules on it knowing which it is.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  the readme carries a dedicated "What people say" section of FOUR
                   attributed testimonials (S21-S24), plus an "In the wild" adopter list
                   (S20) and an adoption-search link (S19). this is social-proof
                   apparatus — the contribution/adoption-signal material the gist flags.
                   recorded with every quote attached; totalling them into a score is
                   forbidden, and the subtraction is the user's.
    note-for-gist  S18 — "running on internal infra at **The European Commission**" — is
                   an institutional adoption claim with NO citation in the readme.
                   recorded verbatim as an unsourced claim.
    note-for-gist  S17 — "made for you with Love++ and AI--" — is an explicit,
                   quantified-looking statement about AI authorship of the project.
                   recorded as a span; it is the author's claim, unverified here.
    note-for-gist  S13's "Zero dependencies" sits beside a readme that names npins,
                   nix-maid, flake-parts, home-manager and terranix as things Den works
                   WITH. no contradiction is asserted here — "works with" and "depends
                   on" differ — but both spans are recorded so the user can rule.
