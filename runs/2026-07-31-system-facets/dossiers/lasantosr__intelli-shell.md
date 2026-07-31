---
status: ok
seed: 05
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# lasantosr/intelli-shell

    url          https://github.com/lasantosr/intelli-shell
    description  "Like IntelliSense, but for shells"   ← About field, verbatim (R4)
    site         https://lasantosr.github.io/intelli-shell/

## #git

    stars          1.3k                    (R4)
    forks          23                      (R4)
    watchers       3                       (R4)
    license        Apache-2.0              (R4) — confirmed by readme S22
    open-issues    4                       (R4)
    open-prs       0                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. readme carries a version BADGE
                   whose rendered value is absent from raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust ← Cargo.toml present at root (R1); crates.io badges in readme
                   toml ← ./default_config.toml referenced as the config surface (S16)
    deep-links     readme    https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md
                   book      https://lasantosr.github.io/intelli-shell/
                   install   https://lasantosr.github.io/intelli-shell/guide/installation.html
                   ai-guide  https://lasantosr.github.io/intelli-shell/guide/introduction_to_ai.html#how-to-enable-ai
                   keybinds  https://lasantosr.github.io/intelli-shell/configuration/keybindings.html
                   crates.io https://crates.io/crates/intelli-shell
                   config    ./default_config.toml

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "IntelliShell is a powerful command template and snippet manager for your shell.
         It goes far beyond a simple history search, transforming your terminal into a
         structured, searchable, and intelligent library of your commands."
    S2  "<em>Like IntelliSense, but for shells!</em>"
    S3  "Works on **Bash**, **Zsh**, **Fish**, **Nushell**, and **PowerShell**, with
         standalone binaries for Linux, macOS, and Windows."
    S4  "- **Seamless Shell Integration**: Search with `ctrl+space`, bookmark with
         `ctrl+b` or fix with `ctrl+x`"
    S5  "- **Dynamic Variables**: Create command templates with `{{variables}}` and
         replace them on the fly"
    S6  "- **Smart Completions**: Power up your variables with dynamic suggestions from
         any command"
    S7  "- **AI-Powered Commands**: Generate, fix, and import commands effortlessly using
         local or remote LLMs"
    S8  "- **Highly Configurable**: Tailor search modes, keybindings, themes, and even
         search-ranking algorithms"
    S9  "- **Workspace-Aware**: Automatically discovers and loads commands from your
         workspace's directory"
    S10 "- **Import / Export**: Share your command library using files, HTTP endpoints,
         or even Gists"
    S11 "- **TLDR Integration**: Fetch and import command examples from
         [tldr](https://github.com/tldr-pages/tldr) pages"
    S12 "- **Flexible Interface**: Choose between a non-intrusive (inline) or an
         immersive (full-screen) TUI"
    S13 "- **Visual Destructive Feedback**: Highlight potentially destructive commands
         (configurable via tags or custom regexes) to prevent accidental executions"
    S14 "**`ctrl+x`**: Diagnose and try to fix a failing command (requires AI to be
         enabled)"
    S15 "**Keep variables secret**: If you have a variable you don't want to save in your
         suggestion history (like a token or a comment), wrap its name in an extra pair
         of brackets: `echo \"{{{message}}}\"`"
    S16 "check out the [default configuration file](./default_config.toml) for a complete
         list of all available options"
    S17 "**Define workspace-specific commands**: Create a [`.intellishell`](./.intellishell)
         file in your workspace's root directory and commit it to git. These commands are
         temporary, prioritized in search results, and don't clutter your global library."
    S18 "**Import everything**: Use the AI-powered import to extract command templates
         from virtually any text. Point it at a blog post, a cheatsheet, or even your own
         shell history to turn useful examples into reusable commands."
    S19 "**Learn Commands on the Fly**: Can't find the command you're looking for? Just
         describe it in natural language and press `ctrl+x` while searching to let the AI
         write it for you."
    S20 "**Format variables**: Apply formatting functions directly within your variable
         placeholders … `git checkout -b {{feature|bugfix}}/{{{description:kebab}}}`"
    S21 "**Name your variables wisely**: … Suggestions are grouped by variable name and
         root cmd. Use the same name to share suggestions, or different names to keep
         them separate."
    S22 "IntelliShell is licensed under the Apache License, Version 2.0."
    S23 "_To skip profile updates, set `INTELLI_SKIP_PROFILE` environment variable to `1`
         before installing._"
    S24 "**Core Philosophy** | **Recall**: \"What was that exact command I ran
         yesterday?\" | **Intent**: \"How do I perform this common task?\""
                                                        ← the comparison table's last row

## potential-relation spans — collected, NOT resolved

    "A common question is: \"How is this different from my shell's history (`ctrl+r`) or
     enhanced history tools like [Atuin](https://atuin.sh/)?\" / The key distinction is
     that they solve different problems and are **complementary tools**, not
     competitors." (readme, §IntelliShell vs. Shell History)
       → names `Atuin` · names `shell history` / `ctrl+r`
       → NOTE the span itself REFUSES the rivalry framing while making the comparison.
         if this ever becomes an edge, that refusal is part of the evidence.
    "- **TLDR Integration**: Fetch and import command examples from
     [tldr](https://github.com/tldr-pages/tldr) pages" (readme, S11)
       → names `tldr-pages/tldr` — an integration/data source, recorded so the workbench
         resolves and discards it as a #git fact rather than an edge.
    "<em>Like IntelliSense, but for shells!</em>" (readme, S2)
       → names `IntelliSense` — a product analogy, not a project relation.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  S1 "powerful … It goes far beyond a simple history search" and S2's
                   tagline are promotional register. S13's "prevent accidental
                   executions" is a safety claim. recorded as spans; the gist flags.
    note-for-gist  the readme instructs `curl … install.sh | sh` as the primary install
                   path (curl-to-shell). recorded as a fact for the user to weigh.
    note-for-gist  AI features are OPT-IN per S3-step-3 ("_(optional)_ [Enable AI
                   features]") and `ctrl+x` is documented as "requires AI to be enabled"
                   (S14) — the dependency is stated, not hidden.
