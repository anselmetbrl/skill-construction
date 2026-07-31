# lasantosr/intelli-shell
what-it-is   a command-template and snippet manager for the shell — "Like IntelliSense, but for shells"
why-it-is    flat shell history loses reusable, parameterized commands; it makes them a searchable library
how-it-is
  technology   Rust, shipped as standalone binaries
  technicality Bash/Zsh/Fish/Nushell/PowerShell on Linux/macOS/Windows; ctrl+space search; optional local OR remote LLMs
leaves       `{{variables}}` templates · TLDR-pages import · destructive-command highlighting · inline/full-screen TUI
flags        none
trust        whole
#graph       self-distinguishes from shell history ("complementary tools, not competitors") · shell cluster: kash (13), yo (15)

## position (multi-pass)
C6 shells · env · MED. shell-command node; the light-AI middle between kash (AI shell) and yo (non-LLM).
