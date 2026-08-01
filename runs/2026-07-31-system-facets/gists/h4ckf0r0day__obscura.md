# gist — h4ckf0r0day/obscura · seed 07

    source · dossiers/h4ckf0r0day__obscura.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a headless browser engine written from scratch, aimed at scraping and agents
      ← "Obscura is a headless browser engine written in Rust, built for web scraping and
         AI agent automation. It runs real JavaScript via V8, supports the Chrome
         DevTools Protocol, and acts as a drop-in replacement for headless Chrome with
         Puppeteer and Playwright."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

## why-it-is

    stated as a purpose mismatch in the incumbent, not as a missing feature
      ← "### Why Obscura over headless Chrome? / Designed for automation at scale, not
         desktop browsing."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

## how-it-is · technology (internal)

    a real JS engine is embedded rather than driven, and exposed for tuning
      ← "Obscura embeds V8 directly. Use `--v8-flags` to pass raw flags through to V8,
         same syntax as Chromium's `--js-flags` and Node's command-line flags."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    a per-page execution budget keeps one bad page from stalling a worker
      ← "Obscura caps the page's script-execution phase so one slow or hung page cannot
         stall a worker. The default budget is 30s"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    stealth is a compile-time feature, not the default build
      ← "# With stealth mode (anti-detection + tracker blocking) / cargo build --release
         --features stealth"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

## how-it-is · technicality (external)

    it speaks the incumbent's wire protocol, so existing clients attach unchanged
      ← "Obscura implements the Chrome DevTools Protocol for Puppeteer/Playwright
         compatibility."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    the binary carries no runtime dependencies of the thing it replaces
      ← "No Chrome, no Node.js, no dependencies."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    it also exposes itself to agents directly, as a tool server
      ← "Obscura ships an MCP server that exposes browser automation tools to AI agents
         (Claude Desktop, Cursor, etc.)."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

## leaves — earned, not padded

    large bodies stream rather than buffer, with a stated cache ceiling
      ← "Response bodies over the cache limit (`OBSCURA_NETWORK_BODY_BUFFER_BYTES`,
         default 2 MiB) are not retained, so raise that limit when you intend to stream
         large downloads."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    robots.txt compliance exists as a flag and is documented as OFF by default
      ← "| `--obey-robots` | off | Respect robots.txt |"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    the anti-detection surface is enumerated precisely rather than gestured at
      ← "- Per-session fingerprint randomization (GPU, screen, canvas, audio, battery) …
         - Native function masking (`Function.prototype.toString()` → `[native code]`) -
         `navigator.webdriver = undefined` (matches real Chrome)"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    TLS-level impersonation ships only in the stealth archives
      ← "Archives ending in `-stealth.tar.gz` or `-stealth.zip` additionally include the
         wreq/BoringSSL transport used for TLS impersonation."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)

#graph-harvest

    "acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright"
      (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
      → names `headless Chrome` · names `Puppeteer` · names `Playwright`
    "### Why Obscura over headless Chrome? / Designed for automation at scale, not
      desktop browsing."
      (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
      → names `headless Chrome` as the explicit foil
    "run [Hermes](https://github.com/NousResearch/hermes-agent) agent browser tasks on
      Obscura."
      (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
      → names `NousResearch/hermes-agent`

## flags

    hype · two self-benchmark tables against an approximated baseline, every row bolding
      its own figure, with the full suite in a repo the project itself controls
      ← "| Memory | **30 MB** | 200+ MB | | Binary size | **70 MB** | 300+ MB | | Page
         load | **85 ms** | ~500 ms | | Startup | **Instant** | ~2s |" · "| Static HTML |
         **51 ms** | ~500 ms |"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    contribution · six proxy vendors carry tracked referral links and affiliate discount
      codes, framed as sponsorship that keeps development independent
      ← "**Obscura** is supported by sponsors who help keep development independent." ·
         "🎁 Use code **Obscura3gb** to get a **free 3GB trial**." · "🎁 Use code
         **OBSCURA35** for a **35% recurring discount**."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    contradiction · a hosted commercial tier is announced beside a pledge of no gating
      ← "We are working on **Obscura Cloud** the hosted version, with managed
         infrastructure, residential proxies, and dedicated support." · "The open-source
         engine stays Apache-2.0, fully featured. No feature gating, ever."
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    filler · a stale headline count sits at the top of the readme, contradicted by the
      repository's own current figure
      ← "## 🎉 10,000 stars and what's next"
         (https://raw.githubusercontent.com/h4ckf0r0day/obscura/HEAD/README.md)
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    unfree?
      #void — the readme asserts the opposite in its own words ("No feature gating,
      ever"), and nothing in the frozen material shows a crippled self-hosted path. the
      commercial adjacency is recorded above as a contradiction, not as a paywall

## finding — dual-use surface, documented not pitched

    the stealth build is documented as fingerprint randomisation, webdriver masking and
      TLS impersonation, and robots.txt compliance is off by default. these are recorded
      as facts of what the tool does, with their spans above; no verdict is entered here
      #void — an observation about the source, carrying no judgment
