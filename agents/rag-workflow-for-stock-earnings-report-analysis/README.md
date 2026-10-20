# RAG Workflow For Stock Earnings Report Analysis

Adapt the published “RAG Workflow For Stock Earnings Report Analysis” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Pinecone Vector Store"]
  n1["Embeddings Google Gemini"]
  n2["Default Data Loader"]
  n3["Recursive Character Text Splitter"]
  n4["Loop Over Items"]
  n5["When clicking #8216;Test workflow#8217;"]
  n6["AI Agent"]
  n7["Vector Store Tool"]
  n8["Google Gemini Chat Model1"]
  n9["OpenAI Chat Model"]
  n10["Pinecone Vector Store #40;Retrieval#41;"]
  n11["Save Report to Google Docs"]
  n12["Embeddings Google Gemini #40;retrieval#41;"]
  n13["List Of Files To Load #40;Google Sheets#41;"]
  n14["Download File From Google Drive"]
  n6 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 1 to in 0"| n14
  n9 -->|"ai_languageModel out 0 to in 0"| n6
  n7 -->|"ai_tool out 0 to in 0"| n6
  n2 -->|"ai_document out 0 to in 0"| n0
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"ai_embedding out 0 to in 0"| n0
  n8 -->|"ai_languageModel out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n0
  n10 -->|"ai_vectorStore out 0 to in 0"| n7
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n6
  n12 -->|"ai_embedding out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n4
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
