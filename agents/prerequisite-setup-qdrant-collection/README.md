# Prerequisite: Setup Qdrant Collection

Adapt the published “Prerequisite: Setup Qdrant Collection” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 37 executable nodes and 34 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Insert"]
  n1["Search"]
  n2["Recommend"]
  n3["Qdrant MCP Server"]
  n4["When Executed by Another Workflow"]
  n5["Operation"]
  n6["Compare"]
  n7["Recommend API"]
  n8["Get Embeddings"]
  n9["Preferences to Items"]
  n10["Aggregate Embeddings"]
  n11["Get Embeddings1"]
  n12["Aggregate Embeddings1"]
  n13["Group Search API"]
  n14["Has Results#63;"]
  n15["Simplify Group Results"]
  n16["Empty Compare Response"]
  n17["Aggregate Compare Response"]
  n18["Embeddings OpenAI"]
  n19["Default Data Loader"]
  n20["Recursive Character Text Splitter"]
  n21["Simplify Recommend Response"]
  n22["Get Insert Response"]
  n23["Get Search Response"]
  n24["Insert Reviews"]
  n25["Search Reviews"]
  n26["Split Out Companies"]
  n27["Filter By CompanyId"]
  n28["Aggregate Recommend Response"]
  n29["Has Results#63;1"]
  n30["Empty Compare Response1"]
  n31["Embeddings OpenAI1"]
  n32["ListCompanies"]
  n33["List by Facet API"]
  n34["Create Facet Index"]
  n35["Create Collection"]
  n36["When clicking #8216;Test workflow#8217;"]
  n0 -->|"ai_tool out 0 to in 0"| n3
  n1 -->|"ai_tool out 0 to in 0"| n3
  n6 -->|"ai_tool out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n33
  n5 -->|"main out 1 to in 0"| n24
  n5 -->|"main out 2 to in 0"| n25
  n5 -->|"main out 3 to in 0"| n11
  n5 -->|"main out 4 to in 0"| n9
  n2 -->|"ai_tool out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n17
  n14 -->|"main out 1 to in 0"| n16
  n29 -->|"main out 0 to in 0"| n28
  n29 -->|"main out 1 to in 0"| n30
  n32 -->|"ai_tool out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n10
  n24 -->|"main out 0 to in 0"| n22
  n25 -->|"main out 0 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n26
  n35 -->|"main out 0 to in 0"| n34
  n18 -->|"ai_embedding out 0 to in 0"| n24
  n31 -->|"ai_embedding out 0 to in 0"| n25
  n19 -->|"ai_document out 0 to in 0"| n24
  n27 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n27
  n21 -->|"main out 0 to in 0"| n29
  n20 -->|"ai_textSplitter out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n5
  n36 -->|"main out 0 to in 0"| n35
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
