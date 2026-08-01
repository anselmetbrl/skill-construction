# gist — dakra/ghostel · seed 04

    source · dossiers/dakra__ghostel.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a terminal emulator living inside Emacs, driven by another terminal's VT engine
      ← "**Ghostel** is a terminal emulator for Emacs powered by
         [libghostty-vt](https://ghostty.org/), the VT engine behind the
         [Ghostty](https://ghostty.org/) terminal."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)

## why-it-is

    #void — the readme states an AIM rather than a need: "It aims to be featureful,
      fast, robust and correct." no span says what was wrong before, or for whom. the
      comparison that would carry the why is deferred to an off-repo page which this
      run did not fetch.

## how-it-is · technology (internal)

    the VT layer is borrowed whole rather than reimplemented — that is the design
      ← "**Ghostel** is a terminal emulator for Emacs powered by [libghostty-vt] … the VT
         engine behind the [Ghostty] terminal."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    the native part arrives prebuilt, so the install has no toolchain step
      ← "The native module is a prebuilt binary that **auto-downloads on first use**. / No
         toolchain or build step required."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    the interaction model is five explicit input modes, not one
      ← "Ghostel offers five eat.el-style [input modes]" · "The default is **semi-char
         mode** (`C-c C-j`), which forwards almost all keys to the terminal besides a few
         exceptions" (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)

## how-it-is · technicality (external)

    it is installed as an ordinary Emacs package and started with one command
      ← "Install from [MELPA](https://melpa.org/#/ghostel): … (use-package ghostel
         :ensure t) … Then `M-x ghostel` to open a terminal. That's it."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    it reaches back into Emacs's own subsystems rather than sitting beside them
      ← "Make `eshell-visual-commands` run in a Ghostel buffer." · "Replace comint's
         built-in `ansi-color-process-output` with Ghostel's VT parser."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    shell awareness is on by default across four shells
      ← "Directory tracking and prompt navigation are on by default for local bash, zsh,
         fish or nushell sessions."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)

## leaves — earned, not padded

    the shell can call back into Emacs, but only through an explicit whitelist
      ← "To call Emacs functions from your shell you have to add them to the
         `ghostel-eval-cmds` whitelist"
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    two read-only modes are distinguished by whether output keeps moving
      ← "**copy mode** freezes the terminal, so if you have continuous output nothing
         \"scrolls away\" while you try to select something. **emacs mode** is *live* so
         new output keeps coming in while you scroll/select."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
    Windows support is documented down to the console-runtime detail
      ← "Releases include optional ConPTY support files from Microsoft's redistributable
         console runtime, which can improve latency and correctness compared with older
         inbox Windows ConPTY versions."
         (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)

#graph-harvest

    "Check the [documentation] for a full list of features or how it
      [compares](https://dakra.github.io/ghostel/#ghostel-vs-vterm) to
      [vterm](https://github.com/akermu/emacs-libvterm) or
      [eat](https://codeberg.org/akib/emacs-eat)."
      (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
      → names `vterm` (akermu/emacs-libvterm) · names `eat` (akib/emacs-eat)
    "Ghostel offers five eat.el-style [input modes]"
      (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
      → names `eat.el`
    "Replace comint's built-in `ansi-color-process-output` with Ghostel's VT parser."
      (https://raw.githubusercontent.com/dakra/ghostel/HEAD/README.md)
      → names `comint`

## flags

    hype
      #void — none found. the readme's strongest line is stated as an AIM, not an
      achievement: "It aims to be featureful, fast, robust and correct."
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material
