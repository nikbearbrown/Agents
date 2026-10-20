# pinecone vector store and receive chat events and download google drive

Adapt the published “pinecone vector store and receive chat events and download google drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["Pinecone Vector Store"]
  n2["When chat message received"]
  n3["OpenAI Chat Model1"]
  n4["Set file URL in Google Drive"]
  n5["Download file"]
  n6["Default Data Loader"]
  n7["Embeddings OpenAI2"]
  n8["Embeddings OpenAI"]
  n9["Recursive Character Text Splitter"]
  n10["Set max chunks to send to model"]
  n11["Get top chunks matching query"]
  n12["Prepare chunks"]
  n13["Answer the query based on chunks"]
  n14["Compose citations"]
  n15["Generate response"]
  n5 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n15
  n8 -->|"ai_embedding out 0 to in 0"| n1
  n7 -->|"ai_embedding out 0 to in 0"| n11
  n3 -->|"ai_languageModel out 0 to in 0"| n13
  n6 -->|"ai_document out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n4
  n9 -->|"ai_textSplitter out 0 to in 0"| n6
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
