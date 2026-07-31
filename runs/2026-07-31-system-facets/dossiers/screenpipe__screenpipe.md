---
status: ok
seed: 25
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests, LICENSE.md) · R4 WebFetch (page facts)
---

# screenpipe/screenpipe

    url          https://github.com/screenpipe/screenpipe
    description  "YC (S26) | Record your screen 24/7 and plug into your agents. Local,
                 private, secure. Connect to OpenClaw, Hermes agent and 100+ apps"
                 ← About field, verbatim (R4)
    site         https://screenpi.pe · docs https://docs.screenpi.pe

## #git

    stars          20.7k                   (R4)
    forks          2.0k                    (R4)
    watchers       111                     (R4)
    license        GitHub reports "Not visible" (R4). FETCHED DIRECTLY (R1, LICENSE.md,
                   200): "# Screenpipe Commercial License / Copyright (c) 2024-2026
                   Mediar, Inc. (dba Screenpipe). All rights reserved."
                   → NOT an OSI licence. a custom commercial licence granting free use
                     for "Personal, non-commercial use", "Non-profit, educational, or
                     research use", and "Evaluation, development, and testing for up to
                     seven (7) days, at any organization size" (S24). "Commercial Use" is
                     defined to include use "in a business or production environment"
                     (S23).
                   → the readme's own word for this is "source-available", used five
                     times, never "open source" (S8, S17, S20). recorded as accurate
                     self-description.
    open-issues    78                      (R4)
    open-prs       58                      (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme links a releases page
                   but names no version.
    release-date   #void — no reachable source. the readme's news list carries DATES
                   without years: "06/10", "05/29", "05/14" (S2).
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4. the readme embeds a contrib.rocks
                   image, which renders remotely and carries no count in raw source.
    lang-roles     rust ← Cargo.toml at root (R1); "Desktop app built with Tauri (Rust +
                        TypeScript)" (S21)
                   typescript ← same span; "JavaScript/TypeScript SDK available" (S16);
                        npm entry points `npx screenpipe record` and
                        `screenpipe-mcp@latest` (S5)
                   sqlite ← "Local SQLite with FTS5 full-text search" (S21)
    deep-links     readme    https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/README.md
                   license   https://raw.githubusercontent.com/screenpipe/screenpipe/HEAD/LICENSE.md
                   docs      https://docs.screenpi.pe
                   site      https://screenpi.pe
                   teams     https://screenpi.pe/team
                   releases  https://github.com/screenpipe/screenpipe/releases
                   contributing CONTRIBUTING.md
                   translations docs/translations/README.md
                   pii-model https://screenpipe.github.io/screenleak/

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "screenpipe remembers how you actually work / It captures what you see, say, and
         do, locally, 24/7, then turns real work into searchable memory, SOPs, and
         automations for AI agents."
    S2  "- 06/10 - **we updated our license to keep screenpipe sustainable** — more
         funding, more shipping, better product / - 05/29 - **we released an [alpha
         version of our AI PII model](…) outperforming Google, Microsoft, and OpenAI
         models** on computer recording data and running at 9ms on consumer device /
         - 05/14 - **we joined YC S26**"
    S3  "screenpipe turns your computer into a personal AI that knows everything you've
         done. record. search. automate. all local, all private, all yours"
    S4  "- **remember everything** - never forget what you saw, heard, or did - **run
         agents that work based on what you do** - pipes are agents triggered by your work
         activity - **search with ai** - find anything using natural language - **100%
         local** - your data lives on your machine only - **source-available** - inspect,
         modify, audit ([LICENSE.md](LICENSE.md))"
    S5  "npx screenpipe record … npx screenpipe setup / # or / claude mcp add screenpipe
         -- npx -y screenpipe-mcp@latest"
    S6  "- captures full accessibility tree, OCR as fallback, transcription, speakers,
         keyboard inputs, app switches - 5-10% cpu usage - 0.5-3gb ram - ~20gb
         storage/month - filters (window, app, chrome extensions, passwords, proprietary
         AI PII model) - optional encryption at rest - works offline"
    S7  "Instead of recording every second, screenpipe listens for meaningful events — app
         switches, clicks, typing pauses, scrolling — and captures a screenshot only when
         something actually changes. Each capture pairs a screenshot with the
         accessibility tree … If accessibility data isn't available (e.g. remote desktops,
         games), it falls back to OCR."
    S8  "screenpipe is a source-available application that continuously captures your
         screen and audio, creating a searchable, AI-powered memory of everything you do
         on your computer."                              ← LLM reference block
    S9  "Pipes are scheduled AI agents defined as markdown files. Each pipe is a `pipe.md`
         with a prompt and schedule — screenpipe runs an AI coding agent (like pi or
         claude-code) that queries your screen data, calls APIs, writes files, and takes
         actions."
    S10 "Each pipe supports YAML frontmatter fields that give admins deterministic,
         OS-level control over what data AI agents can access: - **App & window
         filtering**: `allow-apps`, `deny-apps`, `deny-windows` … - **Endpoint gating**:
         `allow-raw-sql: false`, `allow-frames: false`"
    S11 "Enforced at three layers — skill gating (AI never learns denied endpoints), agent
         interception (blocked before execution), and server middleware (per-pipe
         cryptographic tokens). Not prompt-based. Deterministic."
    S12 "**100% local by default**: All data stored on your device in a local SQLite
         database. Nothing sent to external servers."     ← Privacy and security
    S13 "**Does screenpipe send my data to the cloud?** / Screen frames, audio,
         transcripts, and the search index are stored locally by default. That does not
         mean the desktop app makes no network requests: / - Product analytics is enabled
         by default through PostHog. It uses a stable installation identifier and, when
         you sign in, may associate account details such as your email with app,
         hostname, operating-system, hardware, and other device or feature metadata. / -
         Sentry receives crash and error diagnostics while telemetry is enabled."   ← FAQ
    S14 "You can disable telemetry in **Settings → Privacy → Analytics**, then apply the
         settings change."                                ← FAQ
    S15 "| Feature | screenpipe | Rewind / Limitless | Microsoft Recall | Granola | |
         Source-available | ✅ fully auditable | ❌ | ❌ | ❌ | | Data storage | 100%
         local | Cloud required | Local (Windows) | Cloud | | Pricing | Source-available ·
         app from $25/mo | Subscription | Bundled with Windows | Subscription |"
    S16 "Full REST API running on localhost (default port 3030). Endpoints for searching
         screen content, audio, frames. Raw SQL access to the underlying SQLite database.
         JavaScript/TypeScript SDK available."
    S17 "The source is available for personal, non-commercial use (see [LICENSE.md]). The
         signed desktop app uses a subscription: - **Standard**: $25/month … - **Pro**:
         $50/seat/month … - **Enterprise**: $150/seat/month … Existing lifetime licenses
         remain valid; new lifetime purchases are no longer sold."
    S18 "Make sure to understand the main branch is moving fast and breaking things, if
         you're looking for a stable version check app releases … and use the git commit
         accordingly (production app is behind paywall)."
    S19 "See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, maintainers, and how to
         submit PRs. AI/vibe-coded PRs welcome!"
    S20 "It is the leading source-available alternative to Rewind.ai (now Limitless),
         Microsoft Recall, Granola, and Otter.ai. If you're looking for a rewind
         alternative, recall alternative, or a private local screen recorder with AI,
         screenpipe is the most popular option you can fully audit."   ← LLM reference
    S21 "6. **UI layer**: Desktop app built with Tauri (Rust + TypeScript)." · "3.
         **Storage**: Local SQLite with FTS5 full-text search. Screenshots saved as JPEGs
         on disk (~300 MB/8hr vs ~2 GB with continuous recording)."
    S22 "**Privacy boundary**: Admins control what gets captured and what AI accesses.
         They never see the actual data — everything stays on each employee's device." ·
         "**Override rules**: Employees can add stricter filters … but cannot weaken
         admin-set rules."
    S23 "\"Commercial Use\" means any use of the Licensed Work: (a) in a business or
         production environment; (b) to generate revenue or to support revenue-generating
         activity; or (c) by or on behalf of a for-profit entity, after the Evaluation
         period."                                         ← LICENSE.md (R1)
    S24 "You may use, copy, modify, and run the Licensed Work at no charge for: - Personal,
         non-commercial use; - Non-profit, educational, or research use; - Evaluation,
         development, and testing for up to seven (7) days, at any organization size."
                                                          ← LICENSE.md (R1)
    S25 "Built by screenpipe (Mediar, Inc.). Founded 2024. Based in San Francisco, CA."
    S26 "**Local AI support**: Use Ollama or any local model — no data sent to any cloud."

## potential-relation spans — collected, NOT resolved

    "It is the leading source-available alternative to Rewind.ai (now Limitless),
     Microsoft Recall, Granola, and Otter.ai." (readme, S20)
       → names `Rewind.ai` / `Limitless` · `Microsoft Recall` · `Granola` · `Otter.ai`
       → ALL FOUR out of collection. the span asserts leadership over them without
         citation, which is part of the evidence if ever weighed.
    the comparison table (readme, S15) names the same set again, row by row, with ❌/✅
       → same four targets, same outcome.
    "screenpipe runs an AI coding agent (like pi or claude-code)" (readme, S9) ·
     "**AI coding assistants**: Cursor, Claude Code, Cline, Continue, OpenCode, Gemini
     CLI" (readme, Integrations)
       → names AI CLIENTS. out of collection.
       → NOTE the About field (R4) additionally names `OpenClaw` and `Hermes agent`.
         `Hermes` also appears in seed 07's readme (as an agent plugin) and seed 09's (as
         a skills hub). all three mentions are OUT of collection and none makes an edge
         between the seeds. recorded so the workbench discards it explicitly.
    "**Note-taking**: Obsidian, Notion" · "**Local AI**: Ollama, any OpenAI-compatible
     model server" (readme, Integrations) · "Whisper (Large-V3-Turbo) … or Deepgram"
     (readme) · "Apple Vision on macOS, Windows native OCR, or Tesseract on Linux"
     (readme)  → names INTEGRATIONS and DEPENDENCIES. #git facts, not edges.
       → NOTE `Tesseract` also appears in seed 24 (normcap) as its OCR engine. a shared
         out-of-collection dependency, NOT an edge. recorded explicitly.
    "outperforming Google, Microsoft, and OpenAI models" (readme, S2)
       → names model VENDORS in a benchmark claim. not projects in this collection.
    → 0 in-collection edge candidates.

## flags-raw — what fetch itself revealed

    thin?          no — 21 KB, dense and technically specific.
    index-repo?    no.
    archived/moved no notice.

    CONTRADICTION — the strongest in the run, both spans in the SAME readme:
                   S12 (Privacy and security): "**100% local by default**: All data
                   stored on your device in a local SQLite database. **Nothing sent to
                   external servers.**"
                   S13 (FAQ, further down): "That does not mean the desktop app makes no
                   network requests: - Product analytics is **enabled by default** through
                   PostHog. It uses a stable installation identifier and, when you sign
                   in, may associate account details such as your email with app,
                   hostname, operating-system, hardware, and other device or feature
                   metadata. - Sentry receives crash and error diagnostics"
                   → "Nothing sent to external servers" and "analytics enabled by default
                     through PostHog" cannot both hold. BOTH spans recorded; the
                     resolution is the user's, not the agent's. note also that S13 is the
                     more detailed and more honest of the two, and that S14 documents the
                     opt-out.

    unfree?        the flag applies and the evidence is unambiguous, so it is recorded
                   plainly rather than hedged:
                   · the licence is a custom commercial licence, not OSI (LICENSE.md).
                   · free use is limited to personal/non-commercial/non-profit, plus a
                     SEVEN-DAY evaluation at any organisation size (S24).
                   · "Commercial Use" includes any use "in a business or production
                     environment" (S23).
                   · "production app is behind paywall" — the project's own words (S18).
                   · the app subscription runs $25 / $50 / $150 per seat per month (S17).
                   · a licence CHANGE is announced in the news list: "we updated our
                     license to keep screenpipe sustainable" (S2), undated by year.
                   → the readme is CONSISTENT in saying "source-available" and never
                     "open source". that accuracy is recorded alongside the flag.

    note-for-gist  SEO/LLM-DIRECTED TEXT — a collapsed "📖 LLM reference" block holds
                   keyword-stuffed prose aimed at retrieval: "If you're looking for a
                   rewind alternative, recall alternative, or a private local screen
                   recorder with AI, screenpipe is the most popular option you can fully
                   audit" (S20). unlike seed 20, this block is VISIBLE to a human who
                   expands it and contains no instructions to the reading model — a
                   distinction worth preserving rather than collapsing the two cases.
    note-for-gist  UNVERIFIED BENCHMARK — "outperforming Google, Microsoft, and OpenAI
                   models on computer recording data and running at 9ms on consumer
                   device" (S2), linking the project's own alpha model page, which was
                   NOT fetched. recorded as a claim.
    note-for-gist  SELF-BENCHMARK TABLE against four named commercial products (S15),
                   every row favourable, no methodology. recorded as a claim.
    note-for-gist  "AI/vibe-coded PRs welcome!" (S19) — an explicit contribution-quality
                   stance. recorded as a fact for the contribution flag; not scored.
    note-for-gist  the news list dates are day/month with NO YEAR (S2), so the readme's
                   recency cannot be established from frozen material. recorded as a
                   dating gap, not an abandonment verdict.
    note-for-gist  CAPTURE SURFACE, documented plainly by the project: continuous screen,
                   system audio, microphone, keyboard input and accessibility-tree
                   capture (S6), with raw SQL access to the resulting database (S16).
                   recorded as documented facts of what the tool does. the readme also
                   documents the countervailing controls — per-pipe permissions enforced
                   in three layers (S10, S11), audio exclusions, optional encryption at
                   rest (S6). both sides recorded; the user weighs.
