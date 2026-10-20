# PREPARATION (in Supabase)

Adapt the published “PREPARATION (in Supabase)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Google Drive"]
  n1["Default Data Loader"]
  n2["Question and Answer Chain"]
  n3["OpenAI Chat Model"]
  n4["Vector Store Retriever"]
  n5["Recursive Character Text Splitter1"]
  n6["Customize Response"]
  n7["When chat message received"]
  n8["Retrieve by Query"]
  n9["Embeddings OpenAI Retrieval"]
  n10["Embeddings OpenAI Insertion"]
  n11["Placeholder #40;File/Content to Upsert#41;"]
  n12["Embeddings OpenAI Upserting"]
  n13["Insert Documents"]
  n14["Retrieve Rows from Table"]
  n15["Update Documents"]
  n0 -->|"main out 0 to in 0"| n13
  n3 -->|"ai_languageModel out 0 to in 0"| n2
  n8 -->|"ai_vectorStore out 0 to in 0"| n4
  n1 -->|"ai_document out 0 to in 0"| n13
  n4 -->|"ai_retriever out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n2
  n10 -->|"ai_embedding out 0 to in 0"| n13
  n9 -->|"ai_embedding out 0 to in 0"| n8
  n12 -->|"ai_embedding out 0 to in 0"| n15
  n5 -->|"ai_textSplitter out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n15
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
