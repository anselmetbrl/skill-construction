---
status: ok
seed: 04
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# dakra/ghostel

    url          https://github.com/dakra/ghostel
    description  "Terminal emulator powered by libghostty"   ← About field, verbatim (R4)
    site         https://dakra.github.io/ghostel/

## #git

    stars          807                     (R4)
    forks          47                      (R4)
    watchers       11                      (R4)
    license        GPL-3.0-or-later        (R4) — confirmed by readme badge
    open-issues    11                      (R4)
    open-prs       3                       (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme carries a release
                   BADGE (img.shields.io/github/v/release/dakra/ghostel) whose rendered
                   value is not in the raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     Makefile at root (R1) — no language manifest.
                   emacs-lisp ← the package is installed as an Emacs package and all
                              readme examples are `use-package` elisp: S6, S9, S12
                   native-module ← "The native module is a prebuilt binary that
                              auto-downloads on first use": S5. the module's own source
                              language is NOT stated in the readme → #void.
    deep-links     readme    https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md
                   manual    https://dakra.github.io/ghostel/#features
                   vs-vterm  https://dakra.github.io/ghostel/#ghostel-vs-vterm
                   arch      https://dakra.github.io/ghostel/#architecture
                   perf      https://dakra.github.io/ghostel/#performance
                   melpa     https://melpa.org/#/ghostel
                   changelog CHANGELOG.md

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "**Ghostel** is a terminal emulator for Emacs powered by
         [libghostty-vt](https://ghostty.org/), the VT engine behind the
         [Ghostty](https://ghostty.org/) terminal."
    S2  "It aims to be featureful, fast, robust and correct."
    S3  "Ghostel's features include synchronized output, true color, the Kitty keyboard
         and graphics protocols, hyperlinks, desktop notifications, progress reports and
         a lot more."
    S4  "Shell integration (directory tracking, prompt navigation) all works out of the
         box for bash, zsh, fish and nushell."
    S5  "**Requirements:** Emacs 28.1+ with dynamic module support, on macOS, Linux,
         FreeBSD, Android/Termux, or native Windows. / The native module is a prebuilt
         binary that **auto-downloads on first use**. / No toolchain or build step
         required."
    S6  "Install from [MELPA](https://melpa.org/#/ghostel): … (use-package ghostel
         :ensure t) … Then `M-x ghostel` to open a terminal. That's it."
    S7  "Windows release binaries are built for common native Windows Emacs builds on
         x86_64 and aarch64. Releases include optional ConPTY support files from
         Microsoft's redistributable console runtime, which can improve latency and
         correctness compared with older inbox Windows ConPTY versions."
    S8  "These ship with the Ghostel package, no separate install necessary. / Just
         enable what you want:"                                  ← Extensions
    S9  "Make `eshell-visual-commands` run in a Ghostel buffer."
    S10 "Run all `compile` commands in a Ghostel buffer."
    S11 "Replace comint's built-in `ansi-color-process-output` with Ghostel's VT parser."
    S12 "If you use an Emacs Lisp input method (Korean Hangul, Japanese, Chinese, or any
         other Quail-based method), add Ghostel support"
    S13 "Ghostel offers five eat.el-style [input modes]"
    S14 "The default is **semi-char mode** (`C-c C-j`), which forwards almost all keys to
         the terminal besides a few exceptions (e.g. `M-x`, `C-c`)."
    S15 "In **char mode** (`C-c M-d`), *all* keys go to the terminal."
    S16 "**line mode** (`C-c C-l`) is similar to `M-x shell` in that Ghostel is like a
         normal Emacs buffer and *no* key gets sent to the terminal."
    S17 "**emacs** (`C-c C-e`) and **copy mode** (`C-c C-t`) give you normal Emacs
         navigation over the read-only terminal buffer … **copy mode** freezes the
         terminal, so if you have continuous output nothing \"scrolls away\" … **emacs
         mode** is *live*"
    S18 "Directory tracking and prompt navigation are on by default for local bash, zsh,
         fish or nushell sessions."
    S19 "To call Emacs functions from your shell you have to add them to the
         `ghostel-eval-cmds` whitelist"
    S20 "Note: in alt-screen apps — vim, less, fullscreen TUIs like Claude Code
         (`/tui fullscreen`) — ESC is by default sent to the app instead of switching to
         normal state"
    S21 "| `btop`: true color and full TUI rendering | `yazi`: inline image preview via
         the Kitty graphics |"                                   ← screenshot captions
    S22 "In copy mode, mouse selection remains normal Emacs selection even if the
         terminal app enabled mouse tracking."
    S23 "If you're an evil user you can install the [evil-ghostel] extension"

## potential-relation spans — collected, NOT resolved

    "Check the [documentation] for a full list of features or how it
     [compares](https://dakra.github.io/ghostel/#ghostel-vs-vterm) to
     [vterm](https://github.com/akermu/emacs-libvterm) or
     [eat](https://codeberg.org/akib/emacs-eat)." (readme)
       → names `vterm` (akermu/emacs-libvterm) · names `eat` (akib/emacs-eat)
    "Ghostel offers five eat.el-style [input modes]" (readme, S13)
       → names `eat.el`
    "Replace comint's built-in `ansi-color-process-output` with Ghostel's VT parser."
     (readme, S11)                                    → names `comint`
    "powered by [libghostty-vt], the VT engine behind the [Ghostty] terminal" (readme, S1)
       → names `libghostty-vt` / `Ghostty` — a DEPENDENCY, recorded here so the
         workbench resolves it mechanically and discards it as a #git fact, not an edge.
    "fullscreen TUIs like Claude Code (`/tui fullscreen`)" (readme, S20)
       → names `Claude Code` — an example of an app run INSIDE ghostel, not a rival.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  S2 ("aims to be featureful, fast, robust and correct") is stated as an
                   AIM, not an achievement — a distinction the gist should preserve
                   rather than flatten into a claim.
    note-for-gist  the readme points at a dedicated comparison page rather than making
                   the comparison inline. the page is NOT fetched — the relation spans
                   above are the readme's own words, and a claim needing that page must
                   re-fetch it into a new record first.
