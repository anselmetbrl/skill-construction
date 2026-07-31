# screenpipe/screenpipe
what-it-is   a local-first tool that continuously records screen + audio into a searchable, AI-queryable memory of what you did
why-it-is    give you (and your agents) a private recall of everything on your computer, without sending it to the cloud
how-it-is
  technology   Rust core + desktop app; event-driven capture (app switches/clicks/typing pauses) + the OS accessibility tree, OCR fallback; local SQLite FTS5
  technicality CLI or desktop app; MCP — "Works with Claude Desktop, Cursor, VS Code... any MCP-compatible client"; "pipes are agents triggered by your work activity"
leaves       "100% local... all yours" · event-driven capture (not every frame — less CPU/storage) · MCP integration
flags        promotional-register — "YC S26", "outperforming Google, Microsoft, and OpenAI models", "the leading... most popular option" · UNFREE-signal (A14) — the license moved AWAY from open: "we updated our license to keep screenpipe sustainable"; now "source-available", not OSI-open
trust        eroded — heavy sales framing plus a license that stepped back from open; the local-first tech itself is real. user weighs, especially the unfree flag
#graph       "the leading source-available alternative to Rewind.ai / Microsoft Recall / Granola / Otter.ai" → alternative-to (targets NOT in collection) · agent-memory + capture theme: letta (08), normcap (24), obscura (07), stereOS (11)
