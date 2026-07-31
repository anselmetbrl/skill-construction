---
status: ok
seed: 07
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# h4ckf0r0day/obscura

    url          https://github.com/h4ckf0r0day/obscura
    description  "The headless browser for AI agents and web scraping"
                 ← About field, verbatim (R4)
    site         https://obscura.sh · docs https://docs.obscura.sh

## #git

    stars          19.9k                   (R4)
    forks          1.4k                    (R4)
    watchers       65                      (R4)
    license        Apache-2.0              (R4) — confirmed by readme S30
    open-issues    23                      (R4)
    open-prs       18                      (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme links a `latest`
                   download path but names no version.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust ← Cargo.toml at root (R1); "written in Rust" (S2), "Requires
                        Rust 1.75+" (S16)
                   v8/c++ ← embedded, from the build notes: "V8 compiles from source"
                        (S16), stealth build "also compiles BoringSSL" (S17). a
                        vendored engine, not a repo language manifest.
    deep-links     readme    https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md
                   docs      https://docs.obscura.sh
                   site      https://obscura.sh
                   releases  https://github.com/h4ckf0r0day/obscura/releases
                   docker    https://hub.docker.com/r/h4ckf0r0day/obscura
                   benchmark-repo https://github.com/h4ckf0r0day/obscura-benchmark
                   waitlist  https://tally.so/r/gDWzdD
                   demo      https://cal.com/obscura/quick-chat

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "**The open-source headless browser for AI agents and web scraping.**<br>
         Lightweight, stealthy, and built in Rust."
    S2  "Obscura is a headless browser engine written in Rust, built for web scraping and
         AI agent automation. It runs real JavaScript via V8, supports the Chrome
         DevTools Protocol, and acts as a drop-in replacement for headless Chrome with
         Puppeteer and Playwright."
    S3  "### Why Obscura over headless Chrome? / Designed for automation at scale, not
         desktop browsing."
    S4  "| Memory | **30 MB** | 200+ MB | | Binary size | **70 MB** | 300+ MB | |
         Anti-detect | **Built-in** | None | | Page load | **85 ms** | ~500 ms | |
         Startup | **Instant** | ~2s |"                 ← the vs-Chrome comparison table
    S5  "## 🎉 10,000 stars and what's next"
    S6  "We are working on **Obscura Cloud** the hosted version, with managed
         infrastructure, residential proxies, and dedicated support. For people who want
         the engine without operating it themselves."
    S7  "The open-source engine stays Apache-2.0, fully featured. No feature gating,
         ever."
    S8  "**Obscura** is supported by sponsors who help keep development independent."
    S9  "No Chrome, no Node.js, no dependencies."
    S10 "Release archives include both `obscura` and `obscura-worker`; keep them in the
         same directory for the parallel `scrape` command."
    S11 "Archives ending in `-stealth.tar.gz` or `-stealth.zip` additionally include the
         wreq/BoringSSL transport used for TLS impersonation."
    S12 "Linux release builds target Ubuntu 22.04 so the downloaded binary remains usable
         on common LTS servers with glibc 2.35+."
    S13 "Multi-stage build on `distroless/cc`, no shell, no package manager, ~57 MB
         compressed."
    S14 "# With stealth mode (anti-detection + tracker blocking) / cargo build --release
         --features stealth"
    S15 "Obscura implements the Chrome DevTools Protocol for Puppeteer/Playwright
         compatibility."
    S16 "Requires Rust 1.75+ ([rustup.rs](https://rustup.rs)). First build takes ~5 min
         (V8 compiles from source, cached after)."
    S17 "The stealth build also compiles BoringSSL and generates bindings, so it needs
         CMake, Clang, and the libclang/LLVM development libraries."
    S18 "| Page | Obscura | Chrome | | Static HTML | **51 ms** | ~500 ms | | JS + XHR +
         fetch | **84 ms** | ~800 ms | | Dynamic scripts | **78 ms** | ~700 ms |"
                                                        ← the Benchmarks table
    S19 "The full benchmark suite (WPT conformance, obstacle course, real-world corpus,
         and vs-Chrome speed) lives in a separate repo:
         https://github.com/h4ckf0r0day/obscura-benchmark"
    S20 "### Anti-fingerprinting / - Per-session fingerprint randomization (GPU, screen,
         canvas, audio, battery) / - Realistic `navigator.userAgentData` (Chrome 145,
         high-entropy values) / - `event.isTrusted = true` for dispatched events / -
         Hidden internal properties (`Object.keys(window)` safe) / - Native function
         masking (`Function.prototype.toString()` → `[native code]`) / -
         `navigator.webdriver = undefined` (matches real Chrome)"
    S21 "### Tracker Blocking / - 3,520 domains blocked / - Blocks analytics, ads,
         telemetry, and fingerprinting scripts / - Prevents trackers from loading
         entirely / - Enabled automatically with `--stealth`"
    S22 "| `--obey-robots` | off | Respect robots.txt |"  ← `obscura serve` flag table
    S23 "Obscura ships an MCP server that exposes browser automation tools to AI agents
         (Claude Desktop, Cursor, etc.)."
    S24 "| `browser_navigate` | Navigate to a URL … | | `browser_snapshot` | Return the
         current page URL, title, and body text | | `browser_click` | Click an element by
         CSS selector | …"                               ← the MCP tools table
    S25 "Obscura embeds V8 directly. Use `--v8-flags` to pass raw flags through to V8,
         same syntax as Chromium's `--js-flags` and Node's command-line flags."
    S26 "Obscura caps the page's script-execution phase so one slow or hung page cannot
         stall a worker. The default budget is 30s"
    S27 "// Obscura handles the POST, follows the 302 redirect, maintains cookies"
                                                        ← login example comment
    S28 "| **LP** | getMarkdown (DOM-to-Markdown conversion) |"   ← CDP domain table
    S29 "- **[Hermes agent plugin](https://github.com/SGavrl/hermes-plugin-obscura)**: run
         [Hermes](https://github.com/NousResearch/hermes-agent) agent browser tasks on
         Obscura."
    S30 "## License / Apache 2.0"

## potential-relation spans — collected, NOT resolved

    "acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright"
     (readme, S2)
       → names `headless Chrome` · `Puppeteer` · `Playwright` — out of collection.
    "### Why Obscura over headless Chrome?" (readme, S3) + the comparison table (S4)
       → names `headless Chrome` as the explicit foil. out of collection.
    "No Chrome, no Node.js, no dependencies." (readme, S9)
       → names `Chrome` · `Node.js` as absent dependencies. out of collection.
    "run [Hermes](https://github.com/NousResearch/hermes-agent) agent browser tasks on
     Obscura" (readme, S29)
       → names `NousResearch/hermes-agent` — out of collection. NOTE seed 09's readme
         separately names a "Hermes Skills Hub" at nousresearch.com; both mentions are
         out-of-collection and neither makes an edge between the seeds.
    "exposes browser automation tools to AI agents (Claude Desktop, Cursor, etc.)"
     (readme, S23)  → names AI CLIENTS, out of collection.

## flags-raw — what fetch itself revealed

    thin?          no — 23 KB, the largest readme fetched so far.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  SELF-BENCHMARKS, two separate tables (S4, S18), every row bolding
                   Obscura's figure against an approximated Chrome figure ("~500 ms",
                   "200+ MB"). the full suite is stated to live in a repo the project
                   itself controls (S19), which was NOT fetched. the numbers are
                   recorded verbatim as CLAIMS; nothing here verifies them.
    note-for-gist  SPONSOR APPARATUS — six proxy vendors (SX.org, NodeMaven,
                   ProxyEmpire, 9Proxy, Rapidproxy, Thordata), each with tracked
                   referral links (`?ref=obscura`, `?c=40h-N7`, `utm_source=…`) and
                   affiliate discount codes (`Obscura3gb`, `OBSCURA35`, `OBSCURA40`,
                   `RAPID10`). the readme frames this as "sponsors who help keep
                   development independent" (S8). recorded in full as a fact; the
                   subtraction is the user's.
    note-for-gist  STALE COUNT — the readme headline reads "🎉 10,000 stars and what's
                   next" (S5) while the page reports a figure roughly double that. the
                   discrepancy is a dating cue for the readme, recorded here in the
                   dossier where counts are permitted. it must NOT reach gist or index
                   prose (C4).
    note-for-gist  COMMERCIAL ADJACENCY — a hosted "Obscura Cloud" with a waitlist and a
                   booking link sits beside the pledge "No feature gating, ever" (S6,
                   S7). the unfree? flag asks specifically about crippled self-hosting;
                   the readme asserts the opposite in its own words. both spans
                   recorded; the user rules.
    note-for-gist  DUAL-USE SURFACE — stealth mode is documented as fingerprint
                   randomisation, `navigator.webdriver = undefined`, native-function
                   masking and TLS impersonation (S11, S20), and `--obey-robots` is
                   documented as DEFAULT OFF (S22). these are recorded as documented
                   FACTS of what the tool does, with their spans. no verdict is entered
                   here — but the user should see them plainly, and they are the kind of
                   thing an index exists to surface rather than smooth over.
    note-for-gist  a Trendshift ranking badge sits at the top of the readme — a
                   third-party popularity widget. recorded as a fact.
