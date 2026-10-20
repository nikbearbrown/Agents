# receive local file events and default data loader and recursive character text splitter

Adapt the published “receive local file events and default data loader and recursive character text splitter” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 35 executable nodes and 38 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Local File Trigger"]
  n1["Default Data Loader"]
  n2["Recursive Character Text Splitter"]
  n3["Embeddings Mistral Cloud"]
  n4["Mistral Cloud Chat Model"]
  n5["Mistral Cloud Chat Model1"]
  n6["Prep Incoming Doc"]
  n7["Settings"]
  n8["Merge"]
  n9["Get Doc Types"]
  n10["Split Out Doc Types"]
  n11["For Each Doc Type..."]
  n12["Item List Output Parser"]
  n13["Vector Store Retriever"]
  n14["Embeddings Mistral Cloud1"]
  n15["Qdrant Vector Store1"]
  n16["Mistral Cloud Chat Model2"]
  n17["Split Out"]
  n18["Aggregate"]
  n19["Mistral Cloud Chat Model3"]
  n20["Discover"]
  n21["2secs"]
  n22["Get Generated Documents"]
  n23["Generate"]
  n24["Prep For AI"]
  n25["To Binary"]
  n26["Export to Folder"]
  n27["Get FileType"]
  n28["Import File"]
  n29["Extract from PDF"]
  n30["Extract from DOCX"]
  n31["Extract from TEXT"]
  n32["Summarization Chain"]
  n33["Qdrant Vector Store"]
  n34["Interview"]
  n21 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n24
  n20 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n28
  n18 -->|"main out 0 to in 0"| n23
  n34 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n20
  n25 -->|"main out 0 to in 0"| n26
  n28 -->|"main out 0 to in 0"| n27
  n24 -->|"main out 0 to in 0"| n9
  n27 -->|"main out 0 to in 0"| n29
  n27 -->|"main out 1 to in 0"| n30
  n27 -->|"main out 2 to in 0"| n31
  n9 -->|"main out 0 to in 0"| n10
  n29 -->|"main out 0 to in 0"| n6
  n30 -->|"main out 0 to in 0"| n6
  n31 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n33
  n6 -->|"main out 0 to in 0"| n32
  n0 -->|"main out 0 to in 0"| n7
  n1 -->|"ai_document out 0 to in 0"| n33
  n33 -->|"main out 0 to in 1"| n8
  n10 -->|"main out 0 to in 0"| n11
  n32 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n22
  n11 -->|"main out 1 to in 0"| n34
  n15 -->|"ai_vectorStore out 0 to in 0"| n13
  n13 -->|"ai_retriever out 0 to in 0"| n20
  n22 -->|"main out 0 to in 0"| n25
  n12 -->|"ai_outputParser out 0 to in 0"| n34
  n3 -->|"ai_embedding out 0 to in 0"| n33
  n4 -->|"ai_languageModel out 0 to in 0"| n34
  n14 -->|"ai_embedding out 0 to in 0"| n15
  n5 -->|"ai_languageModel out 0 to in 0"| n32
  n16 -->|"ai_languageModel out 0 to in 0"| n20
  n19 -->|"ai_languageModel out 0 to in 0"| n23
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
