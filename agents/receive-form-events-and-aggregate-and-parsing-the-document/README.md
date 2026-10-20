# My workflow 3

Adapt the published “My workflow 3” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 34 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On form submission4"]
  n1["Loop Over Items1"]
  n2["If2"]
  n3["Aggregate1"]
  n4["Google Gemini Chat Model5"]
  n5["split the binary item"]
  n6["Parsing the document"]
  n7["Check the parsing status"]
  n8["Provide the markdown"]
  n9["Google Gemini Chat Model6"]
  n10["Markdown"]
  n11["Gmail"]
  n12["Code"]
  n13["Convert to File"]
  n14["AI Agent"]
  n15["Google Gemini Chat Model"]
  n16["Information Extractor"]
  n17["Google Gemini Chat Model1"]
  n18["Convert to File4"]
  n19["Pinecone Vector Store"]
  n20["Embeddings Mistral Cloud"]
  n21["Default Data Loader"]
  n22["Recursive Character Text Splitter"]
  n23["When chat message received"]
  n24["Question and Answer Chain"]
  n25["Google Gemini Chat Model2"]
  n26["Vector Store Retriever"]
  n27["Pinecone Vector Store1"]
  n28["Embeddings Mistral Cloud1"]
  n29["AI Agent1"]
  n30["Google Gemini Chat Model3"]
  n31["Translator Agent"]
  n32["Analyzer Agent"]
  n2 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 1 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n31
  n32 -->|"main out 0 to in 0"| n10
  n32 -->|"main out 0 to in 0"| n14
  n32 -->|"main out 0 to in 0"| n16
  n32 -->|"main out 0 to in 0"| n18
  n13 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 1 to in 0"| n6
  n31 -->|"main out 0 to in 0"| n32
  n31 -->|"main out 0 to in 0"| n18
  n21 -->|"ai_document out 0 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n1
  n27 -->|"ai_vectorStore out 0 to in 0"| n26
  n26 -->|"ai_retriever out 0 to in 0"| n24
  n7 -->|"main out 0 to in 0"| n2
  n20 -->|"ai_embedding out 0 to in 0"| n19
  n15 -->|"ai_languageModel out 0 to in 0"| n14
  n28 -->|"ai_embedding out 0 to in 0"| n27
  n17 -->|"ai_languageModel out 0 to in 0"| n16
  n25 -->|"ai_languageModel out 0 to in 0"| n24
  n30 -->|"ai_languageModel out 0 to in 0"| n29
  n4 -->|"ai_languageModel out 0 to in 0"| n31
  n9 -->|"ai_languageModel out 0 to in 0"| n32
  n24 -->|"main out 0 to in 0"| n29
  n23 -->|"main out 0 to in 0"| n24
  n22 -->|"ai_textSplitter out 0 to in 0"| n21
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
