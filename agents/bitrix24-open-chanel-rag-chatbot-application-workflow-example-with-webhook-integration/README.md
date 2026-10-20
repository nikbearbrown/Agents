# Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration

Adapt the published “Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 36 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Bitrix24 Handler"]
  n1["Credentials"]
  n2["Validate Token"]
  n3["Route Event"]
  n4["Process Message"]
  n5["Process Join"]
  n6["Process Install"]
  n7["Register Bot"]
  n8["Send Message"]
  n9["Send Join Message"]
  n10["Process Delete"]
  n11["Success Response"]
  n12["Error Response"]
  n13["Merge parameters for Subworkflow"]
  n14["Get a list of available storages"]
  n15["Get a list of List of Files and Folders"]
  n16["Get a list of Folders files"]
  n17["Download file"]
  n18["Default Data Loader"]
  n19["Recursive Character Text Splitter"]
  n20["Split Out folder files and folders"]
  n21["Filter for files"]
  n22["Move files to Vector stored folder"]
  n23["Execute Workflow Trigger"]
  n24["Qdrant Vector Store"]
  n25["Embeddings Ollama"]
  n26["Vector Store Retriever"]
  n27["Question and Answer Chain"]
  n28["Prepare output parameters"]
  n29["Embeddings Ollama1"]
  n30["Google Gemini Chat Model"]
  n31["Qdrant Vector Store1"]
  n32["Execute subworkflow"]
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 1"| n13
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n5
  n3 -->|"main out 2 to in 0"| n6
  n3 -->|"main out 3 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n13
  n8 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n22
  n17 -->|"main out 0 to in 0"| n24
  n10 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n1
  n21 -->|"main out 0 to in 0"| n17
  n25 -->|"ai_embedding out 0 to in 0"| n24
  n9 -->|"main out 0 to in 0"| n11
  n29 -->|"ai_embedding out 0 to in 0"| n31
  n18 -->|"ai_document out 0 to in 0"| n24
  n32 -->|"main out 0 to in 0"| n11
  n31 -->|"ai_vectorStore out 0 to in 0"| n26
  n26 -->|"ai_retriever out 0 to in 0"| n27
  n23 -->|"main out 0 to in 0"| n14
  n30 -->|"ai_languageModel out 0 to in 0"| n27
  n28 -->|"main out 0 to in 0"| n8
  n27 -->|"main out 0 to in 0"| n28
  n16 -->|"main out 0 to in 0"| n20
  n14 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 0"| n32
  n19 -->|"ai_textSplitter out 0 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n21
  n15 -->|"main out 0 to in 0"| n16
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
