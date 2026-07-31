# chaosprint/glicol
what-it-is   a graph-oriented live-coding language with its own Rust audio-DSP engine
why-it-is    real-time, memory-safe audio synthesis across browser/VST/embedded, without C/C++'s hazards
how-it-is
  technology   Rust (language + engine), compiled to WASM for the web; a purpose-built engine, deliberately NOT mapped onto an existing lib
  technicality runs in browsers (CDN/NPM), VST plugins, Bela board; JS interop for visuals (Hydra)
leaves       "Near-native, garbage-collection-free and memory-safe real-time audio in web browsers" · decentralised collaborative live-coding (yjs)
flags        none
trust        whole
#graph       harvested: "instead of mapping it to existing audio lib like SuperCollider, I decide to do it the hard way" → alternative-to SuperCollider (NOT in collection → drops at resolve)
