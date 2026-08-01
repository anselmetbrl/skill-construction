# gist — typedb/typedb · seed 14

    source · dossiers/typedb__typedb.md, frozen 2026-07-31
      #void — provenance line, not a claim

## what-it-is

    a database whose organising claim is a type system, with its own query language
      ← "**TypeDB** is a next-gen database with a modern programming paradigm that lets
         you build data applications faster, safer, and more elegantly." · "**TypeQL**,
         its groundbreaking query language, is declarative, functional, and
         strongly-typed"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    this repository specifically is the open edition of three
      ← "**TypeDB Community Edition (CE)** — Open-source edition of TypeDB ← _This
         repository_"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)

## why-it-is

    stated as a gap between databases and typed programming languages
      ← "With TypeDB, and its query language TypeQL, we envision databases catching up
         with modern typed programming languages, allowing users to write clear,
         intuitive, and easy to maintain code."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    and as a refusal to pick one of the existing data models
      ← "Its intuitive and powerful data model unifies the strengths of relational,
         document and graph databases without their shortcomings."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)

## how-it-is · technology (internal)

    everything subtypes one of three roots, chosen by function
      ← "user-defined types subtype (based on their function) three root types: entities,
         relations, and attributes."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    relations are defined by the roles their participants play, not by foreign keys
      ← "- *Relations* depend on their *role* interfaces played by either entities or
         relations, - *Attributes* are properties with a value that can be *owned* by
         entities or relations."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    the query language is variable-first, which is what makes polymorphic queries work
      ← "The syntax of TypeQL is fully variablizable and provides native support for
         polymorphic queries."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    types themselves are queryable, not just instances
      ← "match $user-type sub user; $user isa $user-type, has full-name $name, has email
         $email; # This returns all users and their type"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    subqueries are reusable and named, a stated addition in 3.0
      ← "Functions, a new concept in TypeDB 3.0 and a cornerstone of TypeQL's query model,
         are like modularizable subqueries you can re-use and invoke whenever you want."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)

## how-it-is · technicality (external)

    the storage and parsing layers are named third-party components
      ← "Today TypeDB and TypeQL use [RocksDB](https://rocksdb.org),
         [Rust](https://www.rust-lang.org/), [pest](https://pest.rs/),
         [Bazel](https://bazel.build), [gRPC](https://grpc.io), and
         [ZeroMQ](https://zeromq.org)."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    two build systems are documented, Bazel first and Cargo second
      ← "### Compiling TypeDB CE from source using Bazel" · "### Compiling TypeDB CE from
         source using Cargo"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    the readme steers users away from building at all
      ← "> Note: You DO NOT NEED to compile TypeDB from the source if you just want to use
         TypeDB."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)

## leaves — earned, not padded

    the schema language reads as declarations with modifiers, not DDL
      ← "entity user, owns full-name, owns email @unique, plays mentorship:trainee;" ·
         "relation mentorship, relates mentor, relates trainee;"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    the same query shape narrows by type without changing structure
      ← "match $user isa user, … # This returns all users of any type" · "match $user isa
         employee, … # This returns only users who are employees"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    the project credits a long list of technologies it has since moved off
      ← "In the past, TypeDB was enabled by various open-source products and communities
         that we are hugely thankful to: [Speedb], [ANTLR], [Apache Cassandra], [Apache
         Hadoop], [Apache Spark], [Apache TinkerPop], [Caffeine], [JanusGraph], and [SCIP]."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)

#graph-harvest

    #void — this readme positions against database PARADIGMS (relational, document,
      graph) and never against a named competing project. a category is not a name and
      cannot be resolved against the collection, so no edge candidate arises.

## flags

    hype · a dense run of superlatives in the opening four sentences
      ← "a next-gen database" · "its groundbreaking query language" · "drastically
         simplifying data handling and logic" · "With TypeDB, we've reinvented the
         database for the modern programming era."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    hype · a vendor superlative asserted in the readme's own voice about a third party
      ← "Cloudsmith is the only fully hosted, cloud-native, universal package management
         solution, that enables your organization to create, store and share packages in
         any format, to any place, with total confidence."
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    unfree? · three editions are named, two of them commercial, and one requires email
      ← "* [TypeDB Cloud](https://cloud.typedb.com) — multi-cloud DBaaS * [TypeDB
         Enterprise](mailto://enterprise@typedb.com) — allows you to deploy TypeDB Cloud in
         your own environment * **TypeDB Community Edition (CE)** — Open-source edition"
         (https://raw.githubusercontent.com/typedb/typedb/HEAD/README.md)
    filler
      #void — none found in the frozen material
    abandonment
      #void — no dated evidence reachable; release and commit dates are #void for this
      repo in this container
    contribution
      #void — none found in the frozen material
    contradiction
      #void — none found in the frozen material

## finding — the tiering is a fact, the crippling is unknown

    the readme names three editions but never states what CE lacks against the paid
      tiers, deferring that to an off-repo comparison page this run did not fetch. so the
      unfree? question cannot be answered from frozen material: the tiering is evidenced
      above, the crippling is not
      #void — the answer is absent from the source, not withheld by the reading
