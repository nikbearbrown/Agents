# Personal Portfolio Resume CV Chatbot

Adapt the published “Personal Portfolio Resume CV Chatbot” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Embeddings Google Gemini"]
  n1["Schedule Trigger"]
  n2["Google Gemini Chat Model"]
  n3["Google Drive - Resume CV File Created"]
  n4["Google Drive - Resume CV File Updated"]
  n5["Download CV File From Google Drive"]
  n6["Pinecone - Vector Store forr CV Content"]
  n7["CV File Data Loader"]
  n8["CV content - Recursive Character Text Splitter"]
  n9["Chat API - webhook"]
  n10["Personal CV AI Agent Assistant"]
  n11["Chat API Response - Webhook"]
  n12["Chat Memory - Window Buffer"]
  n13["Resume lookup : Vector Store Tool"]
  n14["Resume Vector Store #40;Retrieval#41;"]
  n15["Resume Embeddings Google Gemini #40;retrieval#41;"]
  n16["Resume Google Gemini Chat Model #40;retrieval#41;"]
  n17["Save Conversation API - Webhook"]
  n18["Save Conversation - NocoDB"]
  n19["Save Conversation API Webhook - Response"]
  n20["NocoDB - get all todays conversation"]
  n21["Group Conversation By Unique Session #43; Email - Code"]
  n22["Format HTML Display For email"]
  n23["Send Report To Gmail"]
  n1 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n10
  n7 -->|"ai_document out 0 to in 0"| n6
  n0 -->|"ai_embedding out 0 to in 0"| n6
  n2 -->|"ai_languageModel out 0 to in 0"| n10
  n18 -->|"main out 0 to in 0"| n19
  n12 -->|"ai_memory out 0 to in 0"| n10
  n22 -->|"main out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"ai_vectorStore out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n18
  n13 -->|"ai_tool out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n21
  n3 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n5
  n15 -->|"ai_embedding out 0 to in 0"| n14
  n16 -->|"ai_languageModel out 0 to in 0"| n13
  n8 -->|"ai_textSplitter out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n22
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
