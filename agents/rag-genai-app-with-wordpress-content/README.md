# RAG &amp; GenAI App With WordPress Content

Adapt the published “RAG &amp; GenAI App With WordPress Content” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 45 executable nodes and 45 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Embeddings OpenAI"]
  n2["Default Data Loader"]
  n3["Token Splitter"]
  n4["Embeddings OpenAI1"]
  n5["OpenAI Chat Model"]
  n6["Postgres Chat Memory"]
  n7["Respond to Webhook"]
  n8["Set fields"]
  n9["Embeddings OpenAI2"]
  n10["Default Data Loader1"]
  n11["Token Splitter1"]
  n12["Markdown1"]
  n13["Postgres"]
  n14["Aggregate"]
  n15["Aggregate1"]
  n16["Aggregate2"]
  n17["Wordpress - Get all posts"]
  n18["Wordpress - Get all pages"]
  n19["Set fields1"]
  n20["Filter - Only published #38; unprotected content"]
  n21["HTML To Markdown"]
  n22["Supabase - Store workflow execution"]
  n23["Every 30 seconds"]
  n24["Wordpress - Get posts modified after last workflow execution"]
  n25["Wordpress - Get posts modified after last workflow execution1"]
  n26["Set fields2"]
  n27["Filter - Only published and unprotected content"]
  n28["Loop Over Items"]
  n29["Set fields3"]
  n30["Set fields4"]
  n31["Store documents on Supabase"]
  n32["Store workflow execution id and timestamptz"]
  n33["Aggregate documents"]
  n34["Postgres - Create documents table"]
  n35["Postgres - Create workflow execution history table"]
  n36["Merge Wordpress Posts and Pages"]
  n37["Merge retrieved WordPress posts and pages"]
  n38["Postgres - Filter on existing documents"]
  n39["Supabase - Delete row if documents exists"]
  n40["Switch"]
  n41["When chat message received"]
  n42["Supabase - Retrieve documents from chatinput"]
  n43["AI Agent"]
  n44["Supabase Vector Store"]
  n40 -->|"main out 0 to in 0"| n39
  n40 -->|"main out 1 to in 0"| n30
  n43 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n24
  n13 -->|"main out 0 to in 0"| n25
  n14 -->|"main out 0 to in 0"| n22
  n12 -->|"main out 0 to in 0"| n31
  n15 -->|"main out 0 to in 0"| n32
  n16 -->|"main out 0 to in 0"| n29
  n8 -->|"main out 0 to in 0"| n43
  n19 -->|"main out 0 to in 0"| n20
  n26 -->|"main out 0 to in 0"| n27
  n29 -->|"main out 0 to in 0"| n28
  n30 -->|"main out 0 to in 0"| n28
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n28 -->|"main out 0 to in 0"| n12
  n28 -->|"main out 1 to in 0"| n38
  n11 -->|"ai_textSplitter out 0 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n13
  n21 -->|"main out 0 to in 0"| n44
  n1 -->|"ai_embedding out 0 to in 0"| n44
  n5 -->|"ai_languageModel out 0 to in 0"| n43
  n4 -->|"ai_embedding out 0 to in 0"| n42
  n9 -->|"ai_embedding out 0 to in 0"| n31
  n33 -->|"main out 0 to in 0"| n8
  n2 -->|"ai_document out 0 to in 0"| n44
  n10 -->|"ai_document out 0 to in 0"| n31
  n6 -->|"ai_memory out 0 to in 0"| n43
  n44 -->|"main out 0 to in 0"| n14
  n18 -->|"main out 0 to in 1"| n36
  n17 -->|"main out 0 to in 0"| n36
  n41 -->|"main out 0 to in 0"| n42
  n31 -->|"main out 0 to in 0"| n15
  n36 -->|"main out 0 to in 0"| n19
  n34 -->|"main out 0 to in 0"| n35
  n0 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n18
  n38 -->|"main out 0 to in 0"| n40
  n37 -->|"main out 0 to in 0"| n26
  n39 -->|"main out 0 to in 0"| n16
  n42 -->|"main out 0 to in 0"| n33
  n20 -->|"main out 0 to in 0"| n21
  n27 -->|"main out 0 to in 0"| n28
  n24 -->|"main out 0 to in 0"| n37
  n25 -->|"main out 0 to in 1"| n37
```

[Diagram source](workflow.mmd)

## Implementations

| Implementation | Status |
|---|---|
| [n8n](implementations/n8n/README.md) | Sanitized source available; not runtime-tested |
| [Plain Python](implementations/python/README.md) | Planned |
| [Pydantic AI](implementations/pydantic-ai/README.md) | Planned |
| [CrewAI Flow](implementations/crewai-flow/README.md) | Planned |
| [CrewAI Crew](implementations/crewai-crew/README.md) | Planned |
| [LangGraph](implementations/langgraph/README.md) | Planned |

## Build or operate with an assistant

[Claude](prompts/claude.md) · [Codex](prompts/codex.md) · [Grok Bot](prompts/grok-bot.md) · [Muse](prompts/muse.md) · [Dots](prompts/dots.md)

Build instructions and operating instructions are separate. These are untested prompts, not additional working implementations.

## Attribution

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/zie619-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
