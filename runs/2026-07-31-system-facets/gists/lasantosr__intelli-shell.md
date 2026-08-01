# gist — lasantosr/intelli-shell · seed 05

    source · dossiers/lasantosr__intelli-shell.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a library of command TEMPLATES, not a history — the distinction is the product
      ← "IntelliShell is a powerful command template and snippet manager for your shell.
         It goes far beyond a simple history search, transforming your terminal into a
         structured, searchable, and intelligent library of your commands."
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    templates carry holes you fill at use time
      ← "- **Dynamic Variables**: Create command templates with `{{variables}}` and
         replace them on the fly"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)

## why-it-is

    stated as a distinction of INTENT from RECALL, in a dedicated section
      ← "**Core Philosophy** | **Recall**: \"What was that exact command I ran
         yesterday?\" | **Intent**: \"How do I perform this common task?\""
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    and as a curation argument against the unfiltered log
      ← "your shell history is an automatic, unfiltered log of everything you've ever
         typed—the good, the bad, and the typos. / IntelliShell, by contrast, is your
         personal, curated collection of command \"recipes\""
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)

## how-it-is · technology (internal)

    the whole interaction is keybindings on the live shell line
      ← "- **Seamless Shell Integration**: Search with `ctrl+space`, bookmark with
         `ctrl+b` or fix with `ctrl+x`"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    suggestions are keyed by variable name and root command, which the user controls
      ← "Suggestions are grouped by variable name and root cmd. Use the same name to share
         suggestions, or different names to keep them separate."
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    even the ranking algorithm is exposed as configuration
      ← "- **Highly Configurable**: Tailor search modes, keybindings, themes, and even
         search-ranking algorithms"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)

## how-it-is · technicality (external)

    it is a standalone binary spanning five shells and three platforms
      ← "Works on **Bash**, **Zsh**, **Fish**, **Nushell**, and **PowerShell**, with
         standalone binaries for Linux, macOS, and Windows."
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    the library is portable through ordinary files and public gists
      ← "- **Import / Export**: Share your command library using files, HTTP endpoints, or
         even Gists"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    a repo-local file makes commands travel with the project, in git
      ← "Create a [`.intellishell`](./.intellishell) file in your workspace's root
         directory and commit it to git. These commands are temporary, prioritized in
         search results, and don't clutter your global library."
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)

## leaves — earned, not padded

    the AI layer is opt-in and its dependency is stated at the point of use
      ← "**`ctrl+x`**: Diagnose and try to fix a failing command (requires AI to be
         enabled)" (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    secrets have a syntax for staying out of the suggestion store
      ← "**Keep variables secret**: If you have a variable you don't want to save in your
         suggestion history (like a token or a comment), wrap its name in an extra pair of
         brackets: `echo \"{{{message}}}\"`"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    destructive commands are visually marked before they run
      ← "- **Visual Destructive Feedback**: Highlight potentially destructive commands
         (configurable via tags or custom regexes) to prevent accidental executions"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)

#graph-harvest

    "A common question is: \"How is this different from my shell's history (`ctrl+r`) or
      enhanced history tools like [Atuin](https://atuin.sh/)?\" / The key distinction is
      that they solve different problems and are **complementary tools**, not
      competitors."
      (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
      → names `Atuin` — and the span REFUSES the rivalry framing while making the
        comparison. that refusal is part of the evidence.
    "- **TLDR Integration**: Fetch and import command examples from
      [tldr](https://github.com/tldr-pages/tldr) pages"
      (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
      → names `tldr-pages/tldr`

## flags

    hype · promotional framing in the opening sentence and the tagline
      ← "IntelliShell is a powerful command template and snippet manager … It goes far
         beyond a simple history search" · "<em>Like IntelliSense, but for shells!</em>"
         (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    contribution · the primary documented install path pipes a remote script to a shell
      ← "curl -sSf https://raw.githubusercontent.com/lasantosr/intelli-shell/main/install.sh
         | sh" (https://raw.githubusercontent.com/lasantosr/intelli-shell/HEAD/README.md)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    unfree?
      #void — none found. AI features are opt-in and use the user's own LLM, local or
      remote; no edition tiering or account gate is stated
    contradiction
      #void — none found in the frozen material
