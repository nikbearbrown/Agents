# receive local file events and read write file and default data loader

Adapt the published “receive local file events and read write file and default data loader” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Local File Trigger"]
  n1["When clicking #34;Test workflow#34;"]
  n2["Set Variables"]
  n3["Read File"]
  n4["Embeddings Mistral Cloud"]
  n5["Default Data Loader"]
  n6["Recursive Character Text Splitter"]
  n7["Prepare Embedding Document"]
  n8["Chat Trigger"]
  n9["Question and Answer Chain"]
  n10["Mistral Cloud Chat Model"]
  n11["Vector Store Retriever"]
  n12["Embeddings Mistral Cloud1"]
  n13["Remap for File_Added Flow"]
  n14["Search For Existing Point"]
  n15["Has Existing Point#63;"]
  n16["Delete Existing Point"]
  n17["Search For Existing Point1"]
  n18["Has Existing Point#63;1"]
  n19["Delete Existing Point1"]
  n20["Handle File Event"]
  n21["Qdrant Vector Store"]
  n22["Qdrant Vector Store1"]
  n3 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 1 to in 0"| n17
  n20 -->|"main out 2 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n2
  n5 -->|"ai_document out 0 to in 0"| n21
  n15 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n16
  n22 -->|"ai_vectorStore out 0 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n13
  n11 -->|"ai_retriever out 0 to in 0"| n9
  n4 -->|"ai_embedding out 0 to in 0"| n21
  n10 -->|"ai_languageModel out 0 to in 0"| n9
  n12 -->|"ai_embedding out 0 to in 0"| n22
  n13 -->|"main out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n21
  n17 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n2
  n6 -->|"ai_textSplitter out 0 to in 0"| n5
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
