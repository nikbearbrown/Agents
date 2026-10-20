# RAG on living data

Adapt the published “RAG on living data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Embeddings OpenAI"]
  n1["Token Splitter"]
  n2["Loop Over Items"]
  n3["Question and Answer Chain"]
  n4["Vector Store Retriever"]
  n5["OpenAI Chat Model"]
  n6["When chat message received"]
  n7["Schedule Trigger"]
  n8["Limit"]
  n9["Limit1"]
  n10["Delete old embeddings if exist"]
  n11["Get page blocks"]
  n12["Default Data Loader"]
  n13["Input Reference"]
  n14["Notion Trigger"]
  n15["Get updated pages"]
  n16["Supabase Vector Store1"]
  n17["Supabase Vector Store"]
  n18["Concatenate to single string"]
  n8 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n13
  n1 -->|"ai_textSplitter out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n18
  n13 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 1 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n15
  n0 -->|"ai_embedding out 0 to in 0"| n17
  n0 -->|"ai_embedding out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n13
  n5 -->|"ai_languageModel out 0 to in 0"| n3
  n12 -->|"ai_document out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n9
  n16 -->|"ai_vectorStore out 0 to in 0"| n4
  n4 -->|"ai_retriever out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n3
  n18 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n8
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
