---
status: ok
seed: 13
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
capture: readme fetched in TWO passes (head -c 26000, then tail -c +26000) because a
         single capture truncated mid-sentence. the full 31,710 bytes were read.
---

# jlevy/kash

    url          https://github.com/jlevy/kash
    description  "The knowledge agent shell"   ← About field, verbatim (R4)
    site         #void — no project site; docs live in-repo and on PyPI

## #git

    stars          26                      (R4)
    forks          5                       (R4)
    watchers       1                       (R4)
    license        AGPL-3.0                (R4)
    open-issues    1                       (R4)
    open-prs       1                       (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     python ← pyproject.toml at root (R1); "It's really simply **a Python
                          library**" (S4); "Other versions of Python should work but
                          3.13 is recommended" (S20)
                   make   ← Makefile at root (R1). purpose not stated in readme → #void.
                   xonsh  ← the shell layer: "based on [xonsh](https://xon.sh/)" (S17)
    deep-links     readme    https://raw.githubusercontent.com/jlevy/kash/HEAD/README.md
                   data-model https://github.com/jlevy/kash/tree/main/kash/model
                   install-doc docs/installation.md
                   dev-doc   docs/development.md
                   publish-doc docs/publishing.md
                   kash-docs https://github.com/jlevy/kash-docs
                   kash-media https://github.com/jlevy/kash-media

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "> \"*Simple should be simple. Complex should be possible.*\" —Alan Kay"
    S2  "Kash (\"Knowledge Agent SHell\") is an experiment in making software tasks more
         modular, exploratory, and flexible using Python and current AI tools."
    S3  "The philosophy behind kash is similar to Unix shell tools: simple commands that
         can be combined in flexible and powerful ways. It operates on \"items\" such as
         URLs, files, or Markdown notes within a workspace directory."
    S4  "But it's actually not just a shell, and you can skip the shell entirely. It's
         really simply **a Python library** that lets you convert a simple Python function
         into \"actions\" that work in a clean way on plain files in a workspace."
    S5  "An action is also an MCP tool, so it integrates with other tools like Anthropic
         Desktop or Cursor. / So basically, it gives a unified way to use the shell,
         Python functions, and MCP tools."
    S6  "It's new and still has some rough edges, but it's now working well enough it is
         feeling quite powerful. It now serves as a replacement for my usual shell
         (previously bash or zsh)."
    S7  "And of course, kash can read its own functionality and enhance itself by writing
         new actions."
    S8  "**Actions:** The core of Kash are **actions**. By decorating a Python function
         with `@kash_action`, you can turn it into an action … It can then be used like a
         command line command as well as a Python function or an MCP tool."
    S9  "**Workspaces:** … A workspace is just a directory of files that have a few
         conventions to make it easier to maintain context and perform actions. A bit
         like how Git repos work, it has a `.kash/` directory that holds metadata and
         cached content."
    S10 "All text files use [frontmatter-format](https://github.com/jlevy/frontmatter-format)
         so have YAML metadata that includes not just title or description, but also how
         it was created."
    S11 "All Markdown files are auto-formatted with [flowmark](https://github.com/jlevy/
         flowmark), which makes documents much easier to diff and version control"
    S12 "**Compositionality:** An action is composable with other actions simply as a
         Python function … The goal is to reduce the \"interstitial complexity\" of
         combining tools, so it's easy for you (or an LLM!) to combine tools in flexible
         and powerful ways."
    S13 "**Support for any API:** Kash is tool agnostic and runs locally, on file inputs
         in simple formats, so you own and manage your data and workspaces however you
         like."
    S14 "**Dependency tracking** among action operations (sort of like a Makefile) so that
         Kash can recognize if the output of an action already exists and, if it is
         cacheable, skip running the action"
    S15 "A **selection system** in the workspace for maintaining context between commands
         so you can pass outputs of one action into the inputs of another command (this
         is a bit like pipes but more flexible for sequences of tasks…)"
    S16 "An **execution model** for `Action`s that take input `Item` inputs and produce
         outputs, as well as `Parameters` for actions and `Preconditions` that specify
         what kinds of `Items` the `Action`s operate on"
    S17 "Kash offers a shell environment based on [xonsh](https://xon.sh/) augmented with
         a bunch of enhanced commands and customizations."
    S18 "Items may carry `title`, `description`, and `additional_context` metadata.
         Semantic actions opt into a bounded prompt representation of those fields;
         mechanical transforms do not. Treat fetched or user-supplied metadata as
         reference material, never as model instructions."
    S19 "Actions select models by workload role, so one configuration controls all actions
         that need a careful, structured, standard, or fast model."
    S20 "Kash is easiest to use via [**uv**](https://docs.astral.sh/uv/), the new package
         manager for Python. `uv` replaces traditional use of `pyenv`, `pipx`, `poetry`,
         `pip`, etc."
    S21 "Kash auto-detects and uses `ripgrep` (for search), `bat` (for prettier file
         display), `eza` (a much improved version of `ls`), `hexyl` (a much improved hex
         viewer), `imagemagick` …, `libmagic` …, `ffmpeg` …"
    S22 "You will need API keys for all services you wish to use."
    S23 "you can also use them directly in Python or from an MCP client."
    S24 "Sadly, we may have mind-boggling AI tools, but Terminals are still incredibly
         archaic and don't support these features well … but I have a new terminal, Kerm,
         that shows these as tooltips and makes every command clickable (please contact
         me if you'd like an early developer preview…)"
    S25 "✨**Would you be willing to help test something new?** … I've begun to build a new
         terminal app, **Kerm** … I'd like feedback so please [message me] if you'd like
         to try it out an early dev version!"
    S26 "I tried half a dozen different popular terminals on Mac ([Terminal], [Warp],
         [iTerm2], [Kitty], [WezTerm], [Hyper]). Unfortunately, none offer really good
         support right out of the box"
    S27 "Kash uses Markdown files with YAML frontmatter, which is fully compatible with
         [Obsidian](https://obsidian.md/)."
    S28 "*This project was built from [simple-modern-uv](https://github.com/jlevy/
         simple-modern-uv).*"
    S29 "| Careful | `claude-fable-5` | | Structured | `claude-sonnet-5` | | Standard |
         `claude-sonnet-5` | | Fast | `claude-haiku-4-5-20251001` |"
                                                        ← the default model profile table
    S30 "About 100 simple **built-in commands** for listing, showing, and paging through
         files, etc. … plus all usual shell tools"

## potential-relation spans — collected, NOT resolved

    "based on [xonsh](https://xon.sh/)" (readme, S17) · "[xonsh](https://github.com/
     xonsh/xonsh)" (readme, Elements) → names `xonsh` — a dependency, out of collection.
    "Enhanced **tab completion** … as well as some extras like help summaries populated
     from [tldr](https://github.com/tldr-pages/tldr)" (readme, Elements)
       → names `tldr-pages/tldr`. NOTE seed 05 (intelli-shell) names the SAME repo. a
         shared out-of-collection dependency is NOT an edge between the two seeds; it is
         recorded here so the workbench resolves and discards it explicitly rather than
         silently.
    "All of this is only possible by relying on a wide variety of powerful libraries,
     especially [xonsh], [Rich], [LiteLLM], [Pydantic], [Marko], [yt-dlp], [Ripgrep],
     [Bat], [jusText], [WeasyPrint]." (readme, Tools Used by Kash)
       → names DEPENDENCIES. #git facts, not edges.
    "the same framework lets me build other tools (like [textpress](https://github.com/
     jlevy/textpress))" · "[kash-docs]" · "[kash-media]" · "[chopdiff]" · "[flowmark]" ·
     "[frontmatter-format]" · "[simple-modern-uv]" (readme, various)
       → names SEVEN same-owner repos, none a seed of this run.
    "I tried half a dozen different popular terminals on Mac ([Terminal], [Warp],
     [iTerm2], [Kitty], [WezTerm], [Hyper]). Unfortunately, none offer really good
     support" (readme, S26)
       → names six TERMINALS, all out of collection. NOTE seed 04 (ghostel) is a
         terminal emulator inside Emacs and is NOT among them — no edge arises.
    "fully compatible with [Obsidian]" · "[Cursor] and [VSCode] work fine" · "[Zed] is
     another, newer editor that works great" (readme, Tips)
       → names EDITORS, out of collection.
    "It's the power-tool I want to use alongside Cursor and ChatGPT/Claude." (readme)
       → names AI CLIENTS, out of collection.

## flags-raw — what fetch itself revealed

    thin?          no — 31.7 KB, the largest readme in the run so far.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  SELF-DECLARED IMMATURITY, in the author's own voice: "an experiment"
                   (S2), "It's new and still has some rough edges" (S6). alongside it,
                   promotional register in the same readme: "feeling quite powerful",
                   "much more powerful for everyday usage", "If you're a command-line
                   nerd, you might like it a lot". both directions recorded.
    note-for-gist  FIRST-PERSON SINGULAR throughout — "my usual shell", "I use it
                   routinely", "I have a request". this readme is written as one
                   person's account, not an organisation's. recorded as a fact about
                   the material's voice.
    note-for-gist  ADJACENT-PRODUCT SOLICITATION — Kerm, a separate closed terminal app
                   by the same author, is pitched twice with a contact-me-for-access
                   gate (S24, S25). the kash repo itself is AGPL-3.0 and installable
                   from PyPI; Kerm is not in this repo and its terms are #void here.
                   recorded as a fact for the unfree? question, not as an answer to it.
    note-for-gist  DUPLICATED PARAGRAPH — the `.kash/cache` warning ("contains all the
                   downloaded videos and media you download, so it can get large. You
                   can delete these files if they take up too much space.") appears
                   TWICE, consecutively, in the Creating a New Workspace section. a
                   copy-paste artefact in the source. recorded as an observation about
                   the material.
    note-for-gist  S18 is a documented PROMPT-INJECTION stance — "Treat fetched or
                   user-supplied metadata as reference material, never as model
                   instructions." recorded as a fact; unusual to find stated in a readme.
    note-for-gist  a trailing HTML comment in the source points at authoring guidelines
                   ("This document follows common-doc-guidelines.md"). recorded as a
                   fetch observation; commented text is not quoted as a claim.
