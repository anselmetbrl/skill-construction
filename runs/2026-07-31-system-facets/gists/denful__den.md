# gist — denful/den · seed 12

    source · dossiers/denful__den.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a way of writing Nix configuration as features rather than as per-host modules
      ← "Den turns Nix configuration into composable **features** instead of per-host
         piles of modules."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    and the whole idea reduces to one shape — a feature is a function of context
      ← "That one idea — **a feature as a function** — is what makes the rest possible."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)

## why-it-is

    stated as a concrete complaint about where a single concern currently lives
      ← "- **One feature, everywhere, in one place.** Stop scattering a single concern
         across separate `nixos`, `darwin`, and `homeManager` files. An aspect holds all
         of it together."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    and as an inversion of the usual direction of control
      ← "**Feature-first, not host-first.** Traditional setups start from hosts and push
         modules down; Den [flips that] — features are primary, hosts just select them."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)

## how-it-is · technology (internal)

    an aspect is a plain function returning configuration for many Nix classes at once
      ← "A Den _aspect_ is a plain function: give it context (your hosts and users) and it
         returns configuration for every Nix class it touches — `nixos`, `darwin`,
         `homeManager`, `hjem`, or a class you invent."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    conditionals disappear because the function signature IS the condition
      ← "- **No `mkIf` / `enable` clutter.** The shape of the context _is_ the condition —
         a function that asks for `{ host, user }` simply doesn't run where there's no
         user. Conditionals disappear."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    four named concepts carry the whole model, one job each
      ← "- **Entity** — _what exists_ … - **Aspect** — _what it does_ … - **Policy** —
         _how entities relate_: topology and routing between them. - **Quirk** —
         _structured data aspects share_, without coupling."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)

## how-it-is · technicality (external)

    it is designed to attach to whatever Nix setup already exists, flakes or not
      ← "**Den embraces your Nix.** With or without flakes, flake-parts, or home-manager.
         Zero dependencies. Every part is optional and replaceable — Den works with the
         setup you already have, and gets out of the way."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    sharing aspects does not force the recipient to adopt the sender's inputs
      ← "Share aspects between machines, between people, and between _flake and non-flake_
         setups, without forcing everyone to download each other's inputs."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    the class set is open, so the configurable surface is not fixed to NixOS
      ← "- **Bring your own classes and whole pipelines.** Custom Nix classes, machine
         fleets, MicroVM guests, terranix, standalone neovim — if you can walk it as data,
         Den can configure it."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)

## leaves — earned, not padded

    aspects compose and nest, shown in the readme's central example
      ← "includes = [ den.aspects.performance ];   # aspects compose /
         provides.emulation = { nixos = { /* ... */ }; };  # and nest"
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    configuration flows in both directions between hosts and users
      ← "- **Hosts shape their users, users shape their hosts.** Cross-entity
         configuration flows both ways, without coupling them together."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    templates are runnable without installing anything first
      ← "# a MicroVM / nix run github:denful/den?dir=templates/microvm#runnable-microvm"
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)

#graph-harvest

    "Den takes the Dendritic pattern to a whole new level, and I cannot imagine going
      back.\\ — `@adda`, early Den adopter (after Dendritic flake-parts and Unify)"
      (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
      → names `Dendritic` · names `Unify` — inside a QUOTED THIRD PARTY, not den's voice
    "I'm super impressed with den so far, I'm excited to try out some new patterns that
      Unify couldn't easily do.\\ — `@quasigod`, author of [Unify]"
      (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
      → names `Unify` — again inside a quoted third party
    "**Den embraces your Nix.** With or without flakes, flake-parts, or home-manager."
      (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
      → names `flake-parts` · names `home-manager` as compatibility targets

## flags

    contribution · a dedicated testimonial section of four attributed quotes, plus an
      adopter list and an adoption-search link
      ← "> Den is a playground for some very advanced concepts… some of its ideas will
         play a role in future Nix areas. There are some raw diamonds in Den.\\ —
         `@Doc-Steve`" · "Growing adoption: [usage search](https://github.com/search?q=
         den.aspects+language%3ANix&type=code)"
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    contribution · an institutional adoption claim with no citation
      ← "> Den is also running on internal infra at **The European Commission**."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    hype · an authorship claim about AI involvement, stated as a quantified slogan
      ← "> den and [vic](https://bsky.app/profile/oeiuwq.bsky.social)'s [aspect libs]
         (https://denful.dev) made for you with Love++ and AI--."
         (https://raw.githubusercontent.com/denful/den/HEAD/README.md)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — "Zero dependencies" sits beside a readme naming npins, nix-maid,
      flake-parts, home-manager and terranix as things Den works WITH. "works with" and
      "depends on" differ, so no contradiction is asserted; both spans are recorded above

## finding — every comparison is in someone else's voice

    den itself never positions against a named alternative. all three comparative spans
      in the harvest sit inside third-party testimonials. a quoted stranger's comparison
      is weaker evidence than a project's own claim, and the distinction is preserved
      here so any edge ruling is made knowing which it is
      #void — an observation about the source, carrying no claim about the project
