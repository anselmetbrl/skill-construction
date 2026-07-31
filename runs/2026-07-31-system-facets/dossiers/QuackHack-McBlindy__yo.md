---
status: ok
seed: 15
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# QuackHack-McBlindy/yo

    url          https://github.com/QuackHack-McBlindy/yo
    description  "Yo is a compie-time grammar compiler (Nix) and a runtime deterministic
                 interpretor (Rust). In simple terms it's a rapid fast and flexible
                 full-stack voice assistant."   ← About field, verbatim (R4), typos
                 included as written
    site         #void — no project site in readme; docs are in-repo

## #git

    stars          23                      (R4)
    forks          0                       (R4)
    watchers       0                       (R4)
    license        MIT                     (R4) — confirmed by readme S20
    open-issues    0                       (R4)
    open-prs       0                       (R4)
    release-tag    #void — R2 gated, atom feeds gated
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     nix   ← flake.nix at root (R1); "*50%* **Nix: compile-time grammar
                         compiler**" (S1)
                   rust  ← no ROOT Cargo.toml; the readme locates it in-tree:
                         "--manifest-path ./packages/yo-rs/Cargo.toml" (S14)
                   bash  ← an alternate legacy path: "you can use Bash instead by
                         setting: `yo.legacy = true;`" (S13)
                   toml  ← "creating your voice sentences and commands using `.toml`
                         files" (S14)
    deep-links     readme    https://raw.githubusercontent.com/QuackHack-McBlindy/yo/HEAD/README.md
                   examples  https://github.com/QuackHack-McBlindy/yo/tree/main/examples
                   fuzz-doc  https://github.com/QuackHack-McBlindy/yo/tree/main/docs/FUZZ.md
                   features-doc https://github.com/QuackHack-McBlindy/yo/tree/main/docs/FEATURES.md
                   esp32     https://github.com/QuackHack-McBlindy/yo-esp
                   author-bin https://github.com/QuackHack-McBlindy/dotfiles/tree/main/bin

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "`yo` is: - *50%* **Nix: compile-time grammar compiler** - *50%* **Rust: run-time
         deterministic interpreter with some fuzziness on top**"
    S2  "It takes declarative sentence templates with optional parameters and entity
         lists, expands them into all possible variants, generates optimized regular
         expressions."
    S3  "At runtime it takes input, runs it through exact and fuzzy matching against the
         pre‑compiled patterns, extracts any parameter, and executes the corresponding
         script with those arguments – effectively translating plain‑language commands
         into system shell actions."
    S4  "`yo` supports usage from: - **NixOS module** - **Full Rust version (scripts in
         Toml) for non Nix users** - **Client support for any Linux/**[ESP32] **that has
         i2s configured**"
    S5  "`yo` is a **full-stack voice assistant** that's: - **Very Fast** - Pre-compiled
         indexing, smartt priority ordering & Rust high performance makes it super fast."
    S6  "- **Lightweight** - Very few dependencies. - **Simple** - Everything neatly
         packaged and runs on one port. - **Safe** - Rule based, user defines the rules.
         - **Offline** - No internet required after setup."
    S7  "- **Easy to deploy** - Using the NixOS module or containerized clients via
         Docker. - **Plug & Play** - Using the `examples/` scripts."
    S8  "`yo` is **NOT**: - **❌ An LLM with shell access!**"
    S9  "Thanks to fuzzy parameter resolution, not a single word needs to be correct for
         it to find and execute the right script."
    S10 "16:03:13 ❯ yo do \"seetlt ao tiimezrr fobor twoz hourazs ninre minuotes
         twentyonz<e secondips\" … └─⮞ --hours 2 └─⮞ --minutes 9 └─⮞ --seconds 21
         └─⏰ do took 283.959385ms"                      ← the runtime example
    S11 "Now you can speak your wake word *(default: `\"yo bitch\"`)* & ask what time it
         is."
    S12 "❯ yo do \"what time is it\" … └─⏰ do took 183.835µs / 07:17 / Approx: `~0.184 ms`"
    S13 "*But if you don't like Rust, or have a basic setup you can use Bash instead by
         setting:* `yo.legacy = true;` / Which only relies on `pkgs.jq` and
         `pkgs.coreutils`."
    S14 "If your not on a NixOS system you can choose to compile the grammar using
         `yo-toml` *(Rust)* instead of Nix. This involves creating your voice sentences
         and commands using `.toml` files"
    S15 "**`yo` uses ONNX Runtime for text-to-speech inference and wake-word detection.**
         **GGML-based bin models from the Whisper family is used for speech-to-text.**"
    S16 "# You can use Home Assistant's intent handler instead: # execCommand = '' #
         curl -X POST \"http://HOME_ASSISTANT_IP:8123/api/conversation/process\" …"
                                                        ← commented block in the module
    S17 "server = { … shellTranslate = true; demo = true; # imports /examples/*.nix"
    S18 "# Microphone client (streams audio - RMS based VAD) / client = { enable = true;
         # starts the microphone client"
    S19 "> 🦆🧑‍🦯 says ⮞ Hi! I'm QuackHack-McBlindy! Like my work? Buy me a coffee, or
         become a sponsor. Thanks for supporting open source/hungry developers ♥️🦆!"
    S20 "## **License** / **MIT** <br> Contributions are welcomed."
    S21 "Run the following command to download a tiny GGML model and `amy` an `en_US` TTS
         model: … huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.bin …
         huggingface.co/rhasspy/piper-voices/…/en_US-amy-medium.onnx"

## potential-relation spans — collected, NOT resolved

    "`yo` is **NOT**: - **❌ An LLM with shell access!**" (readme, S8)
       → names a CATEGORY, not a project. no resolvable target — but it is the readme's
         only adversarial positioning, and it positions against a KIND of system rather
         than a named one. recorded so the workbench can confirm it yields no edge.
    "# You can use Home Assistant's intent handler instead" (readme, S16)
       → names `Home Assistant` — out of collection, and an ALTERNATIVE backend the
         readme itself offers.
    "**`yo` uses ONNX Runtime …** **GGML-based bin models from the Whisper family …**"
     (readme, S15)  → names `ONNX Runtime` · `GGML` · `Whisper` — dependencies.
    "huggingface.co/ggerganov/whisper.cpp" · "huggingface.co/rhasspy/piper-voices"
     (readme, S21)  → names `whisper.cpp` · `piper` — model sources, out of collection.
    "[ESP32](https://github.com/QuackHack-McBlindy/yo-esp)" (readme, S4)
       → names `QuackHack-McBlindy/yo-esp` — same owner, NOT a seed of this run.

## flags-raw — what fetch itself revealed

    thin?          no — the readme is 10 KB and substantially technical.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  SELF-BENCHMARKS, unusual in kind: two runtime transcripts with
                   measured timings pasted from the author's own terminal (S10: 283.9 ms
                   for a fuzzy multi-parameter parse; S12: 183.8 µs for a bare command).
                   they are demonstrations, not a comparison table, and no rival figure
                   appears. recorded verbatim as claims; nothing here verifies them.
    note-for-gist  PROMOTIONAL REGISTER, self-aware in tone: "Very Fast … makes it super
                   fast" (S5), "rapid fast and flexible" (About). typos appear in the
                   About field ("compie-time", "interpretor") and in the readme
                   ("smartt", "If your not") — recorded as facts about the material's
                   polish, not as a judgment of the project.
    note-for-gist  S8 is an explicit NEGATIVE self-definition — the project states what
                   it is not, and what it is not is the architecture most of this
                   collection's agent-adjacent seeds are. recorded as a span; any
                   observation drawn ACROSS repos from it is session material.
    note-for-gist  the wake word default (S11) is profane. recorded plainly as a fact of
                   the documented default, without comment.
    note-for-gist  funding apparatus — GitHub Sponsors and Buy-Me-a-Coffee badges appear
                   twice (header and footer) with a dedicated section and a crypto wallet
                   handle (S19). recorded as a fact; no total, no score.
