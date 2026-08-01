# gist — QuackHack-McBlindy/yo · seed 15

    source · dossiers/QuackHack-McBlindy__yo.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a voice assistant split evenly between a compile-time and a run-time half
      ← "`yo` is: - *50%* **Nix: compile-time grammar compiler** - *50%* **Rust: run-time
         deterministic interpreter with some fuzziness on top**"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    what it does, end to end, is turn spoken sentences into shell invocations
      ← "At runtime it takes input, runs it through exact and fuzzy matching against the
         pre‑compiled patterns, extracts any parameter, and executes the corresponding
         script with those arguments – effectively translating plain‑language commands
         into system shell actions."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

## why-it-is

    stated by NEGATION — the readme says what it refuses to be before what it is for
      ← "`yo` is **NOT**: - **❌ An LLM with shell access!**"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    and the properties that follow read as the reasons for that refusal
      ← "- **Safe** - Rule based, user defines the rules. - **Offline** - No internet
         required after setup."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

## how-it-is · technology (internal)

    grammar is expanded and compiled to regex ahead of time, not matched at runtime
      ← "It takes declarative sentence templates with optional parameters and entity
         lists, expands them into all possible variants, generates optimized regular
         expressions."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    fuzziness sits on top of that, tolerant enough that no word need be correct
      ← "Thanks to fuzzy parameter resolution, not a single word needs to be correct for
         it to find and execute the right script."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    the models are local and named, for both directions of speech
      ← "**`yo` uses ONNX Runtime for text-to-speech inference and wake-word detection.**
         **GGML-based bin models from the Whisper family is used for speech-to-text.**"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    a slower shell-only path exists for people who do not want the Rust half
      ← "*But if you don't like Rust, or have a basic setup you can use Bash instead by
         setting:* `yo.legacy = true;` / Which only relies on `pkgs.jq` and
         `pkgs.coreutils`."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

## how-it-is · technicality (external)

    three deployment shapes are offered, one of them a microcontroller
      ← "`yo` supports usage from: - **NixOS module** - **Full Rust version (scripts in
         Toml) for non Nix users** - **Client support for any Linux/**[ESP32] **that has
         i2s configured**"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    the NixOS path is a module with server and client as separate services
      ← "services.yo-rs = { … server = { enable = true; shellTranslate = true; …" · "#
         Microphone client (streams audio - RMS based VAD) / client = { enable = true;"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    the non-Nix path swaps the grammar compiler for a TOML one
      ← "If your not on a NixOS system you can choose to compile the grammar using
         `yo-toml` *(Rust)* instead of Nix. This involves creating your voice sentences
         and commands using `.toml` files"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

## leaves — earned, not padded

    the intent handler is swappable for an existing home-automation one
      ← "# You can use Home Assistant's intent handler instead: # execCommand = '' # curl
         -X POST \"http://HOME_ASSISTANT_IP:8123/api/conversation/process\""
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    the whole thing is stated to run on one port with few dependencies
      ← "- **Lightweight** - Very few dependencies. - **Simple** - Everything neatly
         packaged and runs on one port."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)

#graph-harvest

    "# You can use Home Assistant's intent handler instead"
      (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
      → names `Home Assistant` — offered by the readme as an alternative backend

## flags

    hype · superlative speed framing, doubled inside a single bullet
      ← "- **Very Fast** - Pre-compiled indexing, smartt priority ordering & Rust high
         performance makes it super fast."
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    hype · two pasted terminal transcripts serve as the performance evidence, with no
      comparison figure and no methodology
      ← "└─⏰ do took 283.959385ms" · "└─⏰ do took 183.835µs / 07:17 / Approx: `~0.184 ms`"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    contribution · funding apparatus appears twice, header and footer, with a wallet
      ← "> 🦆🧑‍🦯 says ⮞ Hi! I'm QuackHack-McBlindy! Like my work? Buy me a coffee, or
         become a sponsor. Thanks for supporting open source/hungry developers ♥️🦆!"
         (https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md)
    filler
      #void — none found. the readme is technical throughout; its typos are polish, not
      filler, and are not treated as a flag
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    unfree?
      #void — none found. no edition tiering, paywalled feature, or account gate stated
    contradiction
      #void — none found in the frozen material

## finding — the negative self-definition

    of the whole collection, this is the only readme that defines itself primarily
      against a KIND of system rather than a named one, and the kind it refuses is the
      architecture several other seeds in this collection are. the span is recorded under
      why-it-is; any observation drawn ACROSS repos from it is session material and is
      not made here
      #void — an observation about the source, carrying no claim about other projects
