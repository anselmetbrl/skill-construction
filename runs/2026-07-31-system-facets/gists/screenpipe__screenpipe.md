# gist — screenpipe/screenpipe · seed 25

    source · dossiers/screenpipe__screenpipe.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    continuous local capture of screen and audio, turned into queryable memory
      ← "It captures what you see, say, and do, locally, 24/7, then turns real work into
         searchable memory, SOPs, and automations for AI agents."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    the licence category is stated accurately and consistently — source-available, not open
      ← "- **source-available** - inspect, modify, audit ([LICENSE.md](LICENSE.md))"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## why-it-is

    the need is stated as recall, in the tagline, and the audiences are enumerated
      ← "screenpipe remembers how you actually work"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    with one audience named in terms of a specific difficulty
      ← "- **People with ADHD** who frequently lose track of tabs, documents, and
         conversations"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## how-it-is · technology (internal)

    capture is event-driven rather than continuous, which is the central design choice
      ← "Instead of recording every second, screenpipe listens for meaningful events — app
         switches, clicks, typing pauses, scrolling — and captures a screenshot only when
         something actually changes."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    text comes from the accessibility tree first, with OCR as the fallback
      ← "Each capture pairs a screenshot with the accessibility tree (the structured text
         the OS already knows about: buttons, labels, text fields). If accessibility data
         isn't available (e.g. remote desktops, games), it falls back to OCR."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    storage and search are one ordinary local database
      ← "**Storage**: Local SQLite with FTS5 full-text search. Screenshots saved as JPEGs
         on disk (~300 MB/8hr vs ~2 GB with continuous recording)."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    the plugin unit is a markdown file holding a prompt and a schedule
      ← "Pipes are scheduled AI agents defined as markdown files. Each pipe is a `pipe.md`
         with a prompt and schedule — screenpipe runs an AI coding agent (like pi or
         claude-code) that queries your screen data, calls APIs, writes files, and takes
         actions."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    what a pipe may read is declared in frontmatter, down to the endpoint
      ← "- **App & window filtering**: `allow-apps`, `deny-apps`, `deny-windows` (glob
         patterns) … - **Endpoint gating**: `allow-raw-sql: false`, `allow-frames: false`"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    those limits are enforced structurally rather than by instructing the model
      ← "Enforced at three layers — skill gating (AI never learns denied endpoints), agent
         interception (blocked before execution), and server middleware (per-pipe
         cryptographic tokens). Not prompt-based. Deterministic."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## how-it-is · technicality (external)

    the app is Rust and TypeScript through Tauri
      ← "**UI layer**: Desktop app built with Tauri (Rust + TypeScript)."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    it exposes itself to assistants as a tool server, in one command
      ← "claude mcp add screenpipe -- npx -y screenpipe-mcp@latest"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    and to developers as a local REST API with raw database access
      ← "Full REST API running on localhost (default port 3030). … Raw SQL access to the
         underlying SQLite database. JavaScript/TypeScript SDK available."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    inference can be kept local through a named local model server
      ← "**Local AI support**: Use Ollama or any local model — no data sent to any cloud."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

## leaves — earned, not padded

    admins can constrain capture without gaining access to what was captured
      ← "**Privacy boundary**: Admins control what gets captured and what AI accesses.
         They never see the actual data — everything stays on each employee's device."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    and employees may tighten those rules but not loosen them
      ← "**Override rules**: Employees can add stricter filters (e.g. also block personal
         email) but cannot weaken admin-set rules."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    specific applications can be excluded from audio capture by bundle id
      ← "On macOS 14.4+, you can exclude specific apps from system-audio capture by listing
         their bundle IDs in `~/.screenpipe/audio-exclusions.json`."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    the main branch is declared unstable, and the stable path is named as paid
      ← "Make sure to understand the main branch is moving fast and breaking things, if
         you're looking for a stable version check app releases … (production app is
         behind paywall)."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)

#graph-harvest

    "It is the leading source-available alternative to Rewind.ai (now Limitless),
      Microsoft Recall, Granola, and Otter.ai."
      (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
      → names `Rewind.ai` / `Limitless` · `Microsoft Recall` · `Granola` · `Otter.ai`
    "| Feature | screenpipe | Rewind / Limitless | Microsoft Recall | Granola | |
      Source-available | ✅ fully auditable | ❌ | ❌ | ❌ |"
      (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
      → names the same four again, row by row, with uncited negative marks
    "**AI coding assistants**: Cursor, Claude Code, Cline, Continue, OpenCode, Gemini CLI"
      (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
      → names six AI clients as integrations

## flags

    contradiction · the privacy section and the FAQ state opposite things about network
      traffic, in the same file
      ← "**100% local by default**: All data stored on your device in a local SQLite
         database. Nothing sent to external servers." · "That does not mean the desktop app
         makes no network requests: - Product analytics is enabled by default through
         PostHog. … - Sentry receives crash and error diagnostics"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    unfree? · the source is not open-licensed, and commercial use is defined broadly
      ← "\"Commercial Use\" means any use of the Licensed Work: (a) in a business or
         production environment; (b) to generate revenue or to support revenue-generating
         activity" · "Evaluation, development, and testing for up to seven (7) days, at any
         organization size."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/LICENSE.md)
    unfree? · the licence was changed, and the change is announced without a year
      ← "- 06/10 - **we updated our license to keep screenpipe sustainable** — more
         funding, more shipping, better product"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    filler · a collapsed block holds keyword-stuffed prose aimed at retrieval rather than
      at a reader
      ← "If you're looking for a rewind alternative, recall alternative, or a private local
         screen recorder with AI, screenpipe is the most popular option you can fully
         audit."
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    hype · a benchmark claim against three named vendors, linking the project's own alpha
      page and carrying no methodology
      ← "we released an [alpha version of our AI PII model](https://screenpipe.github.io/
         screenleak/) outperforming Google, Microsoft, and OpenAI models** on computer
         recording data and running at 9ms on consumer device"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    contribution · an explicit stance on AI-generated contributions
      ← "AI/vibe-coded PRs welcome!"
         (https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md)
    abandonment
      #void — the news list carries day/month with no year, so recency cannot be
      established from frozen material; release and commit dates are #void in this
      container

## finding — the capture surface, with its countervailing controls

    the tool continuously records screen, system audio, microphone, keyboard input and the
      accessibility tree, and exposes raw SQL over the result. it also ships per-pipe
      permissions enforced in three layers, audio exclusions and optional encryption at
      rest. both are recorded above with their spans; neither cancels the other
      #void — an observation about the source, carrying no verdict
