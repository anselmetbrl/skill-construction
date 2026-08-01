# gist — dynobo/normcap · seed 24

    source · dossiers/dynobo__normcap.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a screen-capture tool whose output is text rather than an image
      ← "**_OCR powered screen-capture tool to capture information instead of images. For
         Linux, macOS and Windows._**"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)

## why-it-is

    the need is compressed into the tool's own one-line description — information, not
      pixels — and the readme adds nothing further
      ← "OCR powered screen-capture tool to capture information instead of images."
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)

## how-it-is · technology (internal)

    the OCR is not its own; it is an external engine the tool depends on
      ← "And it depends on external software: - [tesseract](https://github.com/
         tesseract-ocr/tesseract) - _OCR engine_"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    it reads codes as well as text, through a second engine
      ← "- [zxing-cpp](https://github.com/zxing-cpp/zxing-cpp) - _QR & barcode detection_"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    the clipboard path is display-server-specific, and both are named
      ← "- [wl-clipboard](https://github.com/bugaevc/wl-clipboard) - _Wayland clipboard
         utilities_ - [xclip](https://github.com/astrand/xclip) - _CLI to the X11
         clipboard_"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    the interface is Qt through Python bindings
      ← "This project uses the following non-standard libraries: - [pyside6](https://
         pypi.org/project/PySide6/) - _bindings for Qt UI Framework_"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)

## how-it-is · technicality (external)

    the recommended Linux path is a sandboxed package, not a system install
      ← "It's recommended to install NormCap from [Flathub](https://flathub.org): flatpak
         install flathub com.github.dynobo.normcap"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    the Python package is offered as the harder alternative, and says so
      ← "As an _alternative_ to the prebuilt packages above, you can install the [NormCap
         Python package](https://pypi.org/project/normcap/) for **Python >=3.10**, but it
         requires more setup"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    that path requires the OCR engine and language data installed by hand, per distro
      ← "# Install dependencies (Ubuntu/Debian) / sudo apt install build-essential
         tesseract-ocr tesseract-ocr-eng libtesseract-dev libleptonica-dev wl-clipboard"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    translation is delegated to a hosted platform rather than to pull requests
      ← "Please use [Weblate](https://hosted.weblate.org/projects/normcap/ui/) to
         complement or correct text for existing languages as well as for adding new
         languages."
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    the licence is declared in the manifest rather than left to detection
      ← "license = \"GPL-3.0+\" / license-files = [ \"LICENSE\" ]"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/pyproject.toml)

## leaves — earned, not padded

    the macOS build is unsigned, and the readme says what that costs the user
      ← "**Note:** You must allow the unsigned application on first start: \"System
         Preferences\" → \"Security & Privacy\" → \"General\" → \"Open anyway\". You also
         need to allow NormCap to take screenshots."
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    one distribution format is marked deprecated in place rather than quietly dropped
      ← "- [NormCap-0.6.0-x86_64.AppImage](…) - ⚠️ ***deprecated***"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    the readme points its readers at ten competing tools, by name and platform
      ← "## Similar open source tools / If NormCap doesn't fit your needs, try these
         alternatives (no particular order):"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)

#graph-harvest

    "## Similar open source tools / If NormCap doesn't fit your needs, try these
      alternatives (no particular order): - [TextSnatcher](https://github.com/RajSolai/
      TextSnatcher) (Linux) - [GreenShot](https://getgreenshot.org/) (Windows, macOS) -
      [TextShot](https://github.com/ianzhao05/textshot) (Windows) - [gImageReader](https://
      github.com/manisandro/gImageReader) (Linux, Windows) - [Capture2Text](https://
      sourceforge.net/projects/capture2text) (Windows) - [Frog](https://github.com/
      TenderOwl/Frog) (Linux) - [Textinator](https://github.com/RhetTbull/textinator)
      (macOS) - [Text-Grab](https://github.com/TheJoeFin/Text-Grab) (Windows) -
      [dpScreenOCR](https://danpla.github.io/dpscreenocr/) (Linux, Windows) - [PowerToys
      Text Extractor](https://learn.microsoft.com/en-us/windows/powertoys/text-extractor)
      (Windows)"
      (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
      → names `TextSnatcher` · `GreenShot` · `TextShot` · `gImageReader` · `Capture2Text`
        · `Frog` · `Textinator` · `Text-Grab` · `dpScreenOCR` · `PowerToys Text Extractor`
        — ten targets, cooperatively framed, all resolving OUT of collection
    "Prerequisites for setting up a development environment: [**uv**](https://
      docs.astral.sh/uv/getting-started/installation/)"
      (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
      → names `uv` — the same tool seed 13 names as its install path; a shared
        out-of-collection dependency, not an edge between the two seeds

## flags

    filler · an unfinished authoring marker ships inside a user-facing install code block,
      so a reader copying the Linux instructions copies the TODO
      ← "#TODO: [HIGH] Describe service and desktop file setup"
         (https://raw.githubusercontent.com/dynobo/normcap/HEAD/README.md)
    hype
      #void — none found, and the posture is actively the opposite: the readme sends
      readers to ten alternatives, certifies itself with a joke badge, and explains its
      own name through a comic
    abandonment
      #void — the AppImage format is self-marked deprecated, recorded above as a leaf; no
      dated evidence about the project itself is reachable in this container
    contribution
      #void — none found in the frozen material
    unfree?
      #void — none found. GPL-3.0+, prebuilt binaries for three platforms, no edition
      tiering, no paywalled feature, no account gate stated
    contradiction
      #void — none found in the frozen material

## finding — the run's richest naming block resolves to nothing

    ten alternatives named in one span, every one of them outside this collection. the
      ratio is worth stating plainly rather than leaving as an absence
      #void — an observation about the source, carrying no claim about the project
