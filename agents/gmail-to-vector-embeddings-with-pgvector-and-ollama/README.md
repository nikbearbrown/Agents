# Gmail to Vector Embeddings with PGVector and Ollama

Adapt the published “Gmail to Vector Embeddings with PGVector and Ollama” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Embeddings Ollama"]
  n1["Default Data Loader"]
  n2["Recursive Character Text Splitter"]
  n3["Gmail Trigger"]
  n4["Loop Over Items"]
  n5["Split Out"]
  n6["Was manually triggered#63;"]
  n7["Manual Trigger"]
  n8["No Operation, do nothing"]
  n9["Set before and after dates"]
  n10["Extract email fields"]
  n11["Store structured"]
  n12["Store vectorized"]
  n13["Create the table"]
  n14["Explode interval into weeks"]
  n15["Get a batch of messages"]
  n5 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 1 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 1 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n6
  n0 -->|"ai_embedding out 0 to in 0"| n12
  n1 -->|"ai_document out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 1 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n5
  n2 -->|"ai_textSplitter out 0 to in 0"| n1
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
