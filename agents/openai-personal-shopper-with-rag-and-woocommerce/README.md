# OpenAI Personal Shopper with RAG and WooCommerce

Adapt the published “OpenAI Personal Shopper with RAG and WooCommerce” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["Window Buffer Memory"]
  n2["Calculator"]
  n3["Edit Fields"]
  n4["OpenAI Chat Model"]
  n5["RAG"]
  n6["Qdrant Vector Store"]
  n7["Embeddings OpenAI"]
  n8["OpenAI Chat Model1"]
  n9["personal_shopper"]
  n10["Information Extractor"]
  n11["OpenAI Chat Model2"]
  n12["Google Drive2"]
  n13["Google Drive1"]
  n14["Embeddings OpenAI3"]
  n15["Default Data Loader2"]
  n16["Token Splitter1"]
  n17["When clicking #8216;Test workflow#8217;"]
  n18["HTTP Request"]
  n19["Qdrant Vector Store1"]
  n20["AI Agent"]
  n5 -->|"ai_tool out 0 to in 0"| n20
  n2 -->|"ai_tool out 0 to in 0"| n20
  n3 -->|"main out 0 to in 0"| n10
  n18 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n13
  n16 -->|"ai_textSplitter out 0 to in 0"| n15
  n9 -->|"ai_tool out 0 to in 0"| n20
  n7 -->|"ai_embedding out 0 to in 0"| n6
  n4 -->|"ai_languageModel out 0 to in 0"| n20
  n14 -->|"ai_embedding out 0 to in 0"| n19
  n8 -->|"ai_languageModel out 0 to in 0"| n5
  n11 -->|"ai_languageModel out 0 to in 0"| n10
  n6 -->|"ai_vectorStore out 0 to in 0"| n5
  n15 -->|"ai_document out 0 to in 0"| n19
  n1 -->|"ai_memory out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n20
  n0 -->|"main out 0 to in 0"| n3
  n17 -->|"main out 0 to in 0"| n18
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
