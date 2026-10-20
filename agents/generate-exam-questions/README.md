# Generate Exam Questions

Adapt the published “Generate Exam Questions” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 32 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Qdrant Vector Store"]
  n2["Create collection"]
  n3["Refresh collection"]
  n4["Embeddings OpenAI"]
  n5["Default Data Loader"]
  n6["Token Splitter"]
  n7["Converto di MD"]
  n8["Get Doc"]
  n9["Vector Store Retriever"]
  n10["Qdrant Vector Store1"]
  n11["Convert to File"]
  n12["Google Gemini Chat Model"]
  n13["Item List Output Parser"]
  n14["Loop Over Items"]
  n15["Google Gemini Chat Model1"]
  n16["Google Gemini Chat Model2"]
  n17["Item List Output Parser1"]
  n18["Loop Over Items1"]
  n19["Google Gemini Chat Model3"]
  n20["Qdrant Vector Store2"]
  n21["Embeddings OpenAI2"]
  n22["Structured Output Parser"]
  n23["RAG"]
  n24["Google Gemini Chat Model4"]
  n25["Open questions"]
  n26["Closed questions"]
  n27["Answer questions"]
  n28["Answer and create options"]
  n29["Write open"]
  n30["Write closed"]
  n31["Embeddings OpenAI1"]
  n23 -->|"ai_tool out 0 to in 0"| n28
  n8 -->|"main out 0 to in 0"| n7
  n29 -->|"main out 0 to in 0"| n14
  n30 -->|"main out 0 to in 0"| n18
  n7 -->|"main out 0 to in 0"| n26
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n14
  n6 -->|"ai_textSplitter out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 1 to in 0"| n27
  n27 -->|"main out 0 to in 0"| n29
  n26 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 1 to in 0"| n28
  n4 -->|"ai_embedding out 0 to in 0"| n1
  n31 -->|"ai_embedding out 0 to in 0"| n10
  n21 -->|"ai_embedding out 0 to in 0"| n20
  n3 -->|"main out 0 to in 0"| n8
  n5 -->|"ai_document out 0 to in 0"| n1
  n10 -->|"ai_vectorStore out 0 to in 0"| n9
  n20 -->|"ai_vectorStore out 0 to in 0"| n23
  n9 -->|"ai_retriever out 0 to in 0"| n27
  n13 -->|"ai_outputParser out 0 to in 0"| n25
  n12 -->|"ai_languageModel out 0 to in 0"| n25
  n17 -->|"ai_outputParser out 0 to in 0"| n26
  n22 -->|"ai_outputParser out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n30
  n15 -->|"ai_languageModel out 0 to in 0"| n27
  n16 -->|"ai_languageModel out 0 to in 0"| n26
  n19 -->|"ai_languageModel out 0 to in 0"| n28
  n24 -->|"ai_languageModel out 0 to in 0"| n23
  n0 -->|"main out 0 to in 0"| n3
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
