# hacker news and split out and qdrant vector store

Adapt the published “hacker news and split out and qdrant vector store” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Hacker News"]
  n2["Split Out"]
  n3["Get Comments"]
  n4["Qdrant Vector Store"]
  n5["Embeddings OpenAI"]
  n6["Default Data Loader"]
  n7["Recursive Character Text Splitter"]
  n8["Set Variables"]
  n9["Clear Existing Comments"]
  n10["Get Payload of Points"]
  n11["Clusters To List"]
  n12["OpenAI Chat Model"]
  n13["Only Clusters With 3#43; points"]
  n14["Set Variables1"]
  n15["Prep Output For Export"]
  n16["Export To Sheets"]
  n17["Execute Workflow Trigger"]
  n18["Trigger Insights"]
  n19["Prep Values For Trigger"]
  n20["Find Comments"]
  n21["Apply K-means Clustering Algorithm"]
  n22["Information Extractor"]
  n2 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n13
  n5 -->|"ai_embedding out 0 to in 0"| n4
  n12 -->|"ai_languageModel out 0 to in 0"| n22
  n6 -->|"ai_document out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n10
  n7 -->|"ai_textSplitter out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n8
  n21 -->|"main out 0 to in 0"| n11
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
