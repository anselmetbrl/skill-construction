---
status: ok
seed: 24
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests, LICENSE, pyproject) · R4 WebFetch (page facts)
---

# dynobo/normcap

    url          https://github.com/dynobo/normcap
    description  "OCR powered screen-capture tool to capture information instead of
                 images"   ← About field, verbatim (R4)
    site         https://dynobo.github.io/normcap/

## #git

    stars          2.7k                    (R4)
    forks          124                     (R4)
    watchers       14                      (R4)
    license        GitHub reports "not visible" (R4) — the auto-detector did not
                   classify it. RESOLVED DIRECTLY from two files (R1):
                   LICENSE exists (200) and opens "NormCap: OCR-powered screen-capture
                   tool … Copyright (C) 2021  dynobo";
                   pyproject.toml declares `license = "GPL-3.0+"` with
                   `license-files = [ "LICENSE" ]` and the OSI classifier
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)".
                   → GPL-3.0+, declared in the manifest. the classifier miss is the
                     finding; all sources recorded.
    open-issues    73                      (R4)
    open-prs       9                       (R4)
    release-tag    v0.6.0 — evidenced TWICE without needing the gated routes:
                   pyproject.toml declares `version = "0.6.0"` (R1), and the readme's
                   download links are pinned to `/releases/download/v0.6.0/` (S5, S7).
                   → the ONLY seed in this run with a version resolvable from frozen
                     material rather than left #void.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4. the readme embeds a contrib.rocks
                   image, which renders remotely and carries no count in raw source.
    lang-roles     python ← pyproject.toml at root (R1); "for **Python >=3.10**" (S8)
                   qt     ← "[pyside6] - _bindings for Qt UI Framework_" (S16)
    deep-links     readme    https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md
                   docs      https://dynobo.github.io/normcap/
                   faqs      https://dynobo.github.io/normcap/#faqs
                   changelog https://github.com/dynobo/normcap/blob/main/CHANGELOG
                   releases  https://github.com/dynobo/normcap/releases
                   pypi      https://pypi.org/project/normcap
                   flathub   https://flathub.org/apps/details/com.github.dynobo.normcap
                   aur       https://aur.archlinux.org/packages/normcap
                   weblate   https://hosted.weblate.org/projects/normcap/ui/
                   license   https://raw.githubusercontent.com/dynobo/normcap/HEAD/LICENSE

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "**_OCR powered screen-capture tool to capture information instead of images. For
         Linux, macOS and Windows._**"
    S2  "Choose **_one_** of the options for a prebuilt release."
    S3  "It's recommended to install NormCap from [Flathub](https://flathub.org): flatpak
         install flathub com.github.dynobo.normcap"
    S4  "- [NormCap-0.6.0-x86_64.AppImage](…) - ⚠️ ***deprecated*** (Requires [fuse](…))"
    S5  "- [NormCap-0.6.0-x86_64-Windows.msi](https://github.com/dynobo/normcap/releases/
         download/v0.6.0/NormCap-0.6.0-x86_64-Windows.msi) (Installer)"
    S6  "**Note:** You must allow the unsigned application on first start: \"System
         Preferences\" → \"Security & Privacy\" → \"General\" → \"Open anyway\". You also
         need to allow NormCap to take screenshots."
    S7  "- [NormCap-0.6.0-arm64-macOS.dmg](…/releases/download/v0.6.0/…) (Installer for
         M1)"
    S8  "As an _alternative_ to the prebuilt packages above, you can install the [NormCap
         Python package](https://pypi.org/project/normcap/) for **Python >=3.10**, but it
         requires more setup"
    S9  "# Install dependencies (Ubuntu/Debian) / sudo apt install build-essential
         tesseract-ocr tesseract-ocr-eng libtesseract-dev libleptonica-dev wl-clipboard"
    S10 "1\\. Install `Tesseract 5` by using the [installer provided by UB Mannheim]"
    S11 "- Create an environment variable `TESSDATA_PREFIX` and set it to _your_ Tesseract
         base folder"
    S12 "Prerequisites for setting up a development environment: [**uv**](…), and
         [**Tesseract >=5.0**](…) (including **language data**)."
    S13 "# Create virtual env and install dependencies / uv sync / # Register pre-commit
         hook / uv run prek install / # Run NormCap in virtual env / uv run python -m
         normcap"
    S14 "Please use [Weblate](https://hosted.weblate.org/projects/normcap/ui/) to
         complement or correct text for existing languages as well as for adding new
         languages."
    S15 "#TODO: [HIGH] Describe service and desktop file setup"   ← inside the Linux
                                                                    install code block
    S16 "This project uses the following non-standard libraries: - [pyside6](…) -
         _bindings for Qt UI Framework_"
    S17 "And it depends on external software: - [tesseract](…) - _OCR engine_ -
         [zxing-cpp](…) - _QR & barcode detection_ - [wl-clipboard](…) - _Wayland
         clipboard utilities_ - [xclip](…) - _CLI to the X11 clipboard_"
    S18 "Packaging is done with: - [briefcase](…) - _converting Python projects into
         standalone apps_ / Thanks to the maintainers of those nice tools!"
    S19 "## Similar open source tools / If NormCap doesn't fit your needs, try these
         alternatives (no particular order):"
    S20 "## Why \"NormCap\"? / See [XKCD](https://xkcd.com):"
    S21 "## Certification / ![WOMM]"   ← a "Works On My Machine" badge image
    S22 "NormCap:  OCR-powered screen-capture tool to capture information instead of
         images / Copyright (C) 2021  dynobo"                       ← LICENSE (R1)
    S23 "license = \"GPL-3.0+\" / license-files = [ \"LICENSE\" ]"   ← pyproject.toml (R1)

## potential-relation spans — collected, NOT resolved

    the RICHEST alternative-naming block in the run. one span, ten named targets:

    "## Similar open source tools / If NormCap doesn't fit your needs, try these
     alternatives (no particular order): - [TextSnatcher] (Linux) - [GreenShot] (Windows,
     macOS) - [TextShot] (Windows) - [gImageReader] (Linux, Windows) - [Capture2Text]
     (Windows) - [Frog] (Linux) - [Textinator] (macOS) - [Text-Grab] (Windows) -
     [dpScreenOCR] (Linux, Windows) - [PowerToys Text Extractor] (Windows)" (readme, S19)
       → names `TextSnatcher` · `GreenShot` · `TextShot` · `gImageReader` ·
         `Capture2Text` · `Frog` · `Textinator` · `Text-Grab` · `dpScreenOCR` ·
         `PowerToys Text Extractor`
       → ALL TEN resolve OUT of collection. zero are seeds of this run.
       → the span's own framing is cooperative, not competitive: "If NormCap doesn't fit
         your needs, try these". if this ever bore on an edge, that framing is evidence.

    "- [tesseract](…) - _OCR engine_ - [zxing-cpp](…) - _QR & barcode detection_ -
     [wl-clipboard](…) - [xclip](…)" (readme, S17) · "[pyside6]" (S16) · "[briefcase]"
     (S18)   → names DEPENDENCIES. #git facts, not edges.
    "[uv](https://docs.astral.sh/uv/…)" (readme, S12)
       → names `uv`. NOTE seed 13 (kash) also names `uv` as its install path — a shared
         out-of-collection tool, NOT an edge between the two seeds. recorded so the
         workbench discards it explicitly.

    → 0 in-collection edge candidates, from ten named alternatives. that ratio is
      itself worth the workbench's plain statement.

## flags-raw — what fetch itself revealed

    thin?          no — 8.6 KB, and unusually EVENLY distributed: install paths for three
                   OSes, a dev setup, a credits list, an alternatives list.
    index-repo?    no. S19 is a courtesy list inside a tool's own readme, not an
                   aggregation repo. NOT recursed into.
    archived/moved no notice. one component is self-marked deprecated: the AppImage
                   build (S4), flagged with ⚠️ in the readme itself.
    note-for-gist  NO PROMOTIONAL REGISTER, and an actively self-effacing posture: it
                   points readers AT ten competing tools (S19), certifies itself with a
                   "Works On My Machine" joke badge (S21), and explains its own name via
                   an XKCD comic (S20). the strongest claim in the readme is its plain
                   one-line description (S1). recorded as a fact about the material.
    note-for-gist  an unfinished authoring marker ships INSIDE a user-facing install
                   code block: "#TODO: [HIGH] Describe service and desktop file setup"
                   (S15). a reader copying the Linux block copies the TODO. recorded as
                   an observation about the material.
    note-for-gist  S6 documents that the macOS build is UNSIGNED and requires a
                   security-override to launch, plus screenshot permission. recorded as
                   a documented fact of what installing costs the user.
