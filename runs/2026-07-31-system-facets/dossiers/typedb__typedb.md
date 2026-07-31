---
status: ok
seed: 14
fetched: 2026-07-31
rungs: R1 raw.githubusercontent (readme, manifests) · R4 WebFetch (page facts)
---

# typedb/typedb

    url          https://github.com/typedb/typedb
    description  "TypeDB: Built for systems, not records"   ← About field, verbatim (R4)
    site         https://typedb.com/

## #git

    stars          4.4k                    (R4)
    forks          369                     (R4)
    watchers       112                     (R4)
    license        MPL-2.0                 (R4) — confirmed by readme S23
    open-issues    280                     (R4)
    open-prs       15                      (R4)
    release-tag    #void — R2 gated, atom feeds gated. readme carries a release BADGE
                   whose rendered value is absent from raw source.
    release-date   #void — no reachable source
    commit-dates   #void — no reachable source
    contributors   #void — js-rendered, dropped by R4
    lang-roles     rust  ← Cargo.toml at root (R1); named in readme S21
                   bazel ← "Compiling TypeDB CE from source using Bazel" (S18); Bazel
                         named again in S21
                   typeql ← the project's own query language, the readme's code samples
                   NOTE the readme documents BOTH a Bazel and a Cargo build path (S18,
                        S19) — two build systems, recorded as a fact.
    deep-links     readme    https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md
                   docs      https://typedb.com/docs
                   features  https://typedb.com/features
                   philosophy https://typedb.com/docs/home/what-is-typedb
                   get-started https://typedb.com/docs/home/get-started/overview
                   academy   https://typedb.com/docs/academy
                   deploy    https://typedb.com/deploy
                   typeql    https://github.com/typedb/typeql
                   studio    https://github.com/typedb/typedb-studio
                   community https://github.com/typedb-osi
                   license   https://github.com/typedb/typedb/blob/master/LICENSE

## spans — verbatim quote bank (R1 readme unless noted)

    S1  "**TypeDB** is a next-gen database with a modern programming paradigm that lets
         you build data applications faster, safer, and more elegantly."
    S2  "Its intuitive and powerful data model unifies the strengths of relational,
         document and graph databases without their shortcomings."
    S3  "**TypeQL**, its groundbreaking query language, is declarative, functional, and
         strongly-typed, drastically simplifying data handling and logic."
    S4  "So now, even the most nested and interconnected datasets can be managed with
         ease. With TypeDB, we've reinvented the database for the modern programming era."
    S5  "* TypeDB was crafted to natively express and combine diverse data features,
         allowing users to build advanced data models from a set of simple and intuitive
         building blocks."
    S6  "* TypeDB's type system provides safety and flexibility at the same time, which
         makes both prototyping and building performant, production-ready data
         applications fast, elegant, and _enjoyable_."
    S7  "* With TypeDB, and its query language TypeQL, we envision databases catching up
         with modern typed programming languages, allowing users to write clear,
         intuitive, and easy to maintain code."
    S8  "TypeDB schemas are based on a modern type system that natively supports
         inheritance and interfaces, and follows a [conceptual data modeling] approach,
         in which user-defined types subtype (based on their function) three root types:
         entities, relations, and attributes."
    S9  "- *Entities* are independent objects, - *Relations* depend on their *role*
         interfaces played by either entities or relations, - *Attributes* are properties
         with a value that can be *owned* by entities or relations."
    S10 "Interface and inheritance for these types can be combined in many ways, resulting
         in highly expressive ways of modeling data."
    S11 "define / attribute full-name, value string; … entity user, owns full-name, owns
         email @unique, plays mentorship:trainee; … relation mentorship, relates mentor,
         relates trainee;"                               ← the schema example
    S12 "The syntax of TypeQL is fully variablizable and provides native support for
         polymorphic queries. The language is based on [fully declarative and composable]
         patterns, mirroring the structure of natural language."
    S13 "match $user isa user, has full-name $name, has email $email; # This returns all
         users of any type"                              ← the query example
    S14 "match $user-type sub user; $user isa $user-type, … # This returns all users and
         their type"                                     ← the polymorphic query example
    S15 "Functions, a new concept in TypeDB 3.0 and a cornerstone of TypeQL's query model,
         are like modularizable subqueries you can re-use and invoke whenever you want."
    S16 "TypeDB breaks down the patchwork of existing database paradigms into three
         fundamental ingredients: [types], [inheritance], and [interfaces]."
    S17 "* [TypeDB Cloud](https://cloud.typedb.com) — multi-cloud DBaaS * [TypeDB
         Enterprise](mailto://enterprise@typedb.com) — allows you to deploy TypeDB Cloud
         in your own environment * **TypeDB Community Edition (CE)** — Open-source
         edition of TypeDB ← _This repository_"
    S18 "> Note: You DO NOT NEED to compile TypeDB from the source if you just want to use
         TypeDB."
    S19 "### Compiling TypeDB CE from source using Cargo / **For macs:** / Install
         prerequisites: 1. Rustup 2. `brew install protoc`"
    S20 "TypeDB comes with a mature ecosystem including language drivers and a graphical
         user interface: **[TypeDB Studio!](studio.typedb.com)**"
    S21 "Today TypeDB and TypeQL use [RocksDB](https://rocksdb.org),
         [Rust](https://www.rust-lang.org/), [pest](https://pest.rs/),
         [Bazel](https://bazel.build), [gRPC](https://grpc.io), and
         [ZeroMQ](https://zeromq.org)."
    S22 "In the past, TypeDB was enabled by various open-source products and communities
         that we are hugely thankful to: [Speedb], [ANTLR], [Apache Cassandra], [Apache
         Hadoop], [Apache Spark], [Apache TinkerPop], [Caffeine], [JanusGraph], and
         [SCIP]."
    S23 "It's released under the Mozilla Public License 2.0 (MPL 2.0)."
    S24 "Package repository hosting is graciously provided by [Cloudsmith]
         (https://cloudsmith.com). Cloudsmith is the only fully hosted, cloud-native,
         universal package management solution"

## potential-relation spans — collected, NOT resolved

    "Its intuitive and powerful data model unifies the strengths of relational, document
     and graph databases without their shortcomings." (readme, S2)
       → names database CATEGORIES, not projects. no resolvable target.
    "TypeDB breaks down the patchwork of existing database paradigms" (readme, S16)
       → the same: a category-level positioning, no named project.
    "Today TypeDB and TypeQL use [RocksDB], [Rust], [pest], [Bazel], [gRPC], and
     [ZeroMQ]." (readme, S21)
       → names DEPENDENCIES. #git facts, not edges.
    "In the past, TypeDB was enabled by … [Speedb], [ANTLR], [Apache Cassandra], [Apache
     Hadoop], [Apache Spark], [Apache TinkerPop], [Caffeine], [JanusGraph], and [SCIP]."
     (readme, S22)   → names FORMER dependencies, out of collection.
    "**[TypeQL](https://github.com/typedb/typeql)**" · "**[TypeDB Studio]
     (https://github.com/typedb/typedb-studio)**" (readme, Useful links)
       → names two SAME-OWNER repos, neither a seed of this run.

    NOTE for the workbench: this readme positions against database PARADIGMS
    (relational, document, graph) and never against a named competing project. a
    category is not a name and cannot be name-resolved against the collection — no
    edge candidate arises from S2 or S16.

## flags-raw — what fetch itself revealed

    thin?          no.
    index-repo?    no.
    archived/moved no notice.
    note-for-gist  HYPE — a dense concentration of superlative register in the opening
                   four sentences: "next-gen" (S1), "groundbreaking" (S3), "drastically
                   simplifying" (S3), "we've reinvented the database for the modern
                   programming era" (S4), plus "mature ecosystem" (S20). recorded with
                   spans attached; the gist flags, the user weighs.
    note-for-gist  EDITION TIERING — three editions are named (S17): Cloud (DBaaS),
                   Enterprise (self-deployed Cloud, contact-by-email only), and CE,
                   which is this repository and is the open-source one. the readme
                   does NOT state what CE lacks relative to the paid tiers, and points
                   at an off-repo comparison page for that. so the unfree? question
                   cannot be answered from frozen material: the tiering is a FACT, the
                   crippling is #void. recorded as exactly that, undecided.
    note-for-gist  S24 — the package-hosting thank-you carries a vendor superlative
                   ("the only fully hosted, cloud-native, universal package management
                   solution") in the READMEs own voice about a third party. recorded.
