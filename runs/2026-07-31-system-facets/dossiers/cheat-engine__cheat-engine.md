---
status: ok
seed: 23
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests, license probe) · R4 WebFetch (page facts)
---

# cheat-engine/cheat-engine

    url          https://github.com/cheat-engine/cheat-engine
    description  "Cheat Engine. A development environment focused on modding"
                 ← About field, verbatim (R4)
    site         https://www.cheatengine.org

## #git

    stars          18.8k                   (R4)
    forks          2.7k                    (R4)
    watchers       338                     (R4)
    license        #void — GitHub reports "not visible" (R4) AND no license file exists
                   at root: LICENSE, LICENSE.md, LICENSE.txt, COPYING and
                   "Cheat Engine/LICENSE" all return 404 (R1 probe). the readme states
                   no license either. TWO independent sources agree the license is
                   absent from the places checked — recorded as a void with its probe,
                   not as "unlicensed", which would be a conclusion.
    open-issues    1.3k                    (R4)
    open-prs       35                      (R4)
    release-tag    #void — R2 gated, atom feeds gated. the readme links a `releases/
                   latest` path but names no version.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     NO manifest of any recognised kind at root (R1 sweep). the roles come
                   from the readme's own build instructions:
                   pascal/lazarus ← "Download Lazarus 2.2.2 … Select `cheatengine.lpi`"
                                  (S6); `.lpr` project files named throughout (S8)
                   c#/.net · c++  ← "*.SLN files require visual studio (Usually 2017)"
                                  (S9); DirectXMess.sln, DotNetcompiler.sln,
                                  monodatacollector.sln, cejvmti.sln, tcclib.sln (S8)
                   lua            ← "luaclient.lpr: Compile both 32- and 64-bit DLL's
                                  for {$luacode} capability" (S8); "the cscompile lua
                                  command" (S8)
    deep-links     readme    https://raw.githubusercontent.com/cheat-engine/cheat-engine/HEAD/README.md
                   site      https://www.cheatengine.org
                   wiki      https://wiki.cheatengine.org/index.php?title=Main_Page
                   forum     https://forum.cheatengine.org
                   releases  https://github.com/cheat-engine/cheat-engine/releases
                   patreon   https://www.patreon.com/cheatengine

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "Cheat Engine is a development environment focused on modding games and
         applications for personal use."
    S2  "# Download / * **[Latest Version](https://github.com/cheat-engine/cheat-engine/
         releases/latest)** / [Older versions](https://github.com/cheat-engine/
         cheat-engine/releases)"
    S3  "* [Website](https://www.cheatengine.org) * [Forum](https://forum.cheatengine.org)
         * [Forum (alternate)](https://opencheattables.com/) * [Forum (alternate)]
         (https://fearlessrevolution.com/index.php) * [Wiki](https://wiki.cheatengine.org
         /index.php?title=Main_Page)"
    S4  "## Social Media / * [Reddit](https://reddit.com/r/cheatengine) * [Twitter]
         (https://twitter.com/_cheatengine)"
    S5  "## Donate / * [Patreon](https://www.patreon.com/cheatengine) * [PayPal](…)"
    S6  "1. Download Lazarus 2.2.2 from https://sourceforge.net/projects/lazarus/… First
         install lazarus-2.2.2-fpc-3.2.2-win64.exe and then
         lazarus-2.2.2-fpc-3.2.2-cross-i386-win32-win64.exe"
    S7  "2. Run Lazarus and click on `Project->Open Project`. Select `cheatengine.lpi`
         from the `Cheat Engine` folder as the project. / 3. Click on `Run->Build` or
         press SHIFT+F9."
    S8  "Do not forget to compile secondary projects you'd like to use: /
         speedhack.lpr: Compile both 32- and 64-bit DLL's for speedhack capability /
         luaclient.lpr: … for {$luacode} capability /
         DirectXMess.sln: … for D3D overlay and snapshot capabilities /
         DotNetcompiler.sln: for the cscompile lua command /
         monodatacollector.sln: … to get Mono features to inspect the .NET environment of
         the process / dotnetdatacollector.sln: … to get .NET symbols /
         dotnetinvasivedatacollector.sln: … to add support for runtime JIT support /
         cejvmti.sln: … for Java inspection support /
         tcclib.sln: … to add {$C} and {$CCODE} support in scripts /
         vehdebug.lpr: … to add support for the VEH debugger interface /
         dbkkernel.sln: for kernelmode functions (settings->extra)"
    S9  "*.SLN files require visual studio (Usually 2017)"
    S10 "You will need to build the no-sig version and either boot with unsigned driver
         support, or sign the driver yourself"
    S11 "If you want to run or debug from the IDE on Windows you will need to run Lazarus
         as administrator."

## potential-relation spans — collected, NOT resolved

    "Download Lazarus 2.2.2 from https://sourceforge.net/projects/lazarus/…" (readme, S6)
       → names `Lazarus` — the build IDE, a dependency. out of collection.
    "*.SLN files require visual studio (Usually 2017)" (readme, S9)
       → names `Visual Studio` — a build tool. out of collection.
    "monodatacollector.sln: … to get Mono features" · "cejvmti.sln: … for Java
     inspection support" (readme, S8)
       → names `Mono` · `Java`/JVMTI — RUNTIMES the tool inspects, not projects it
         relates to.
    "[Forum (alternate)](https://opencheattables.com/)" · "[Forum (alternate)]
     (https://fearlessrevolution.com/index.php)" (readme, S3)
       → names two third-party COMMUNITY SITES, out of collection.
    → 0 edge candidates from this seed.

## flags-raw — what fetch itself revealed

    thin?          YES — 3.0 KB for an 18.8k-star repo, and its what/why content is ONE
                   sentence (S1). the remaining ~90% is a download link block, a link
                   list, donation links, and build instructions. the gist will have a
                   `what`, a `#void` for `why`, and a well-evidenced `how` — the
                   asymmetry is the finding.
    index-repo?    no.
    archived/moved no notice.
    LICENSE-VOID   the strongest single fact in this dossier: an 18.8k-star project with
                   no license discoverable by GitHub's classifier and no license file at
                   any of five probed root paths. recorded with the probe attached so
                   the user can weigh it, and NOT converted into a verdict about
                   redistribution rights.
    note-for-gist  NO PROMOTIONAL REGISTER AT ALL. no superlatives, no benchmarks, no
                   comparison table, no feature list. S1 is a plain scope statement.
                   the phrase "for personal use" in S1 is the only qualifying language
                   in the readme, and it sits in the same sentence as the description
                   GitHub displays. recorded verbatim, unelaborated.
    note-for-gist  DUAL-USE SURFACE, documented as build targets rather than pitched:
                   the components named in S8 include a kernel-mode driver requiring
                   unsigned-driver boot or self-signing (S8, S10), a VEH debugger
                   interface, process memory inspection across .NET/Mono/Java runtimes,
                   and a "speedhack" module. these are recorded as FACTS of what the
                   readme says the repo builds, each with its span. no verdict is
                   entered — but the user should see them plainly, and S1's "for
                   personal use" is recorded beside them as the project's own framing.
    note-for-gist  the build instructions pin a specific old toolchain (Lazarus 2.2.2,
                   Visual Studio "Usually 2017"). recorded as a dating cue, not as an
                   abandonment verdict — no dates are reachable in this container.
