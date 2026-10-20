# Insert and retrieve documents

Adapt the published “Insert and retrieve documents” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["Fetch Essay List"]
  n2["Extract essay names"]
  n3["Split out into items"]
  n4["Fetch essay texts"]
  n5["Limit to first 3"]
  n6["Extract Text Only"]
  n7["Recursive Character Text Splitter1"]
  n8["Generate response"]
  n9["Compose citations"]
  n10["Answer the query based on chunks"]
  n11["Prepare chunks"]
  n12["Set max chunks to send to model"]
  n13["Embeddings OpenAI2"]
  n14["When chat message received"]
  n15["Milvus Vector Store in retrieval"]
  n16["Milvus Vector Store"]
  n17["Embeddings OpenAI"]
  n18["Default Data Loader"]
  n19["OpenAI Chat Model"]
  n11 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n8
  n17 -->|"ai_embedding out 0 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n16
  n4 -->|"main out 0 to in 0"| n6
  n19 -->|"ai_languageModel out 0 to in 0"| n10
  n13 -->|"ai_embedding out 0 to in 0"| n15
  n18 -->|"ai_document out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n1
  n7 -->|"ai_textSplitter out 0 to in 0"| n18
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
