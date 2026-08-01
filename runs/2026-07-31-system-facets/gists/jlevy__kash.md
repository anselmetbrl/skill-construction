# gist — jlevy/kash · seed 13

    source · dossiers/jlevy__kash.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    an experiment, named as such, in making software tasks modular with current AI tools
      ← "Kash (\"Knowledge Agent SHell\") is an experiment in making software tasks more
         modular, exploratory, and flexible using Python and current AI tools."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    and, underneath the shell, a library that turns Python functions into file operations
      ← "But it's actually not just a shell, and you can skip the shell entirely. It's
         really simply **a Python library** that lets you convert a simple Python function
         into \"actions\" that work in a clean way on plain files in a workspace."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)

## why-it-is

    the need is named precisely — the cost of joining tools together
      ← "The goal is to reduce the \"interstitial complexity\" of combining tools, so it's
         easy for you (or an LLM!) to combine tools in flexible and powerful ways."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    and the model is borrowed openly rather than invented
      ← "The philosophy behind kash is similar to Unix shell tools: simple commands that
         can be combined in flexible and powerful ways."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)

## how-it-is · technology (internal)

    one decorator makes a function usable three ways at once
      ← "By decorating a Python function with `@kash_action`, you can turn it into an
         action … It can then be used like a command line command as well as a Python
         function or an MCP tool."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    state lives in a directory, on the git model, not in a database
      ← "A workspace is just a directory of files that have a few conventions … A bit like
         how Git repos work, it has a `.kash/` directory that holds metadata and cached
         content."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    what an action can accept is declared, so the shell can suggest what applies
      ← "`Preconditions` that specify what kinds of `Items` the `Action`s operate on …
         so you and the shell know what actions might apply to any selection"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    a selection carries context between commands, more loosely than a pipe
      ← "A **selection system** in the workspace for maintaining context between commands
         so you can pass outputs of one action into the inputs of another command (this is
         a bit like pipes but more flexible…)"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)

## how-it-is · technicality (external)

    the shell layer is another project's, augmented rather than written
      ← "Kash offers a shell environment based on [xonsh](https://xon.sh/) augmented with
         a bunch of enhanced commands and customizations."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    file formats are plain and portable, with metadata carried in frontmatter
      ← "All text files use [frontmatter-format](https://github.com/jlevy/frontmatter-format)
         so have YAML metadata that includes not just title or description, but also how
         it was created."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    it adapts to CLI tools it finds installed rather than requiring them
      ← "Kash auto-detects and uses `ripgrep` (for search), `bat` (for prettier file
         display), `eza` (a much improved version of `ls`), `hexyl` …, `imagemagick` …,
         `libmagic` …, `ffmpeg` …"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    model choice is left entirely open, and the data stays local
      ← "Kash is tool agnostic and runs locally, on file inputs in simple formats, so you
         own and manage your data and workspaces however you like."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)

## leaves — earned, not padded

    outputs are normalised so that LLM edits diff cleanly
      ← "A new Markdown auto-formatter, [**flowmark**](https://github.com/jlevy/flowmark),
         so that text documents (like LLM outputs) are saved in a normalized form that can
         be diffed consistently"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    re-running is skipped when the output already exists, Makefile-style
      ← "**Dependency tracking** among action operations (sort of like a Makefile) so that
         Kash can recognize if the output of an action already exists and, if it is
         cacheable, skip running the action"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    it states a prompt-injection stance in the readme itself
      ← "Treat fetched or user-supplied metadata as reference material, never as model
         instructions."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    the same workspace is shared between the shell and an MCP client, so work is not lost
      ← "all the inputs and outputs are saved in the current kash workspace, just as if
         you'd been running these commands yourself in the shell. This way, you don't lose
         context or any work"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)

#graph-harvest

    "Kash offers a shell environment based on [xonsh](https://xon.sh/)"
      (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
      → names `xonsh`
    "Enhanced **tab completion** … as well as some extras like help summaries populated
      from [tldr](https://github.com/tldr-pages/tldr)"
      (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
      → names `tldr-pages/tldr` — the SAME repo seed 05 names. a shared out-of-collection
        dependency, not an edge between the two seeds
    "I tried half a dozen different popular terminals on Mac ([Terminal], [Warp],
      [iTerm2], [Kitty], [WezTerm], [Hyper]). Unfortunately, none offer really good
      support right out of the box"
      (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
      → names `Terminal` · `Warp` · `iTerm2` · `Kitty` · `WezTerm` · `Hyper`

## flags

    hype · promotional self-assessment in the author's own first person
      ← "It's new and still has some rough edges, but it's now working well enough it is
         feeling quite powerful." · "I find it is much more powerful for local usage than
         than bash/zsh/fish."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    unfree? · a separate closed product by the same author is solicited twice from inside
      this repo's readme, access gated behind contacting him
      ← "I have a new terminal, Kerm, that shows these as tooltips and makes every command
         clickable (please contact me if you'd like an early developer preview…)" · "I'd
         like feedback so please [message me] if you'd like to try it out an early dev
         version!"
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    filler · a paragraph is duplicated consecutively, a copy-paste artefact in the source
      ← "Note the `.kash/cache` directory contains all the downloaded videos and media you
         download, so it can get large. You can delete these files if they take up too
         much space."
         (https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md)
    abandonment
      #void — inverted, if anything: the readme is written in the present tense of active
      daily use. no dated evidence is reachable either way in this container
    contribution
      #void — none found in the frozen material
    contradiction
      #void — none found in the frozen material

## finding — the voice

    this readme is one person's account, not an organisation's: "my usual shell", "I use
      it routinely", "I have a request". the self-deprecation and the promotion come from
      the same voice, and both are recorded above rather than averaged
      #void — an observation about the source, carrying no claim about the project
