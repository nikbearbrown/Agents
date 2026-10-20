# Build a Chatbot, Voice Agent and Phone Agent with Voiceflow, Google Calendar and RAG

Adapt the published “Build a Chatbot, Voice Agent and Phone Agent with Voiceflow, Google Calendar and RAG” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["n8n_order"]
  n1["Google Calendar"]
  n2["OpenAI Chat Model3"]
  n3["Concert start date"]
  n4["n8n_appointment"]
  n5["Retrive Qdrant Vector Store"]
  n6["Embeddings OpenAI2"]
  n7["RAG"]
  n8["OpenAI Chat Model2"]
  n9["OpenAI Chat Model1"]
  n10["Retrive Agent"]
  n11["n8n_rag"]
  n12["Tracking response"]
  n13["Calendar response"]
  n14["Webhook tracking response"]
  n15["API URL Tracking"]
  n16["Webhook calendar response"]
  n17["Structured Output Parser"]
  n18["Webhook RAG response"]
  n19["When clicking #8216;Test workflow#8217;"]
  n20["Qdrant Vector Store"]
  n21["Create collection"]
  n22["Refresh collection"]
  n23["Get folder"]
  n24["Download Files"]
  n25["Embeddings OpenAI"]
  n26["Default Data Loader"]
  n27["Token Splitter"]
  n7 -->|"ai_tool out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n15
  n23 -->|"main out 0 to in 0"| n24
  n10 -->|"main out 0 to in 0"| n18
  n24 -->|"main out 0 to in 0"| n20
  n27 -->|"ai_textSplitter out 0 to in 0"| n26
  n1 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n16
  n25 -->|"ai_embedding out 0 to in 0"| n20
  n12 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n1
  n6 -->|"ai_embedding out 0 to in 0"| n5
  n9 -->|"ai_languageModel out 0 to in 0"| n7
  n8 -->|"ai_languageModel out 0 to in 0"| n10
  n2 -->|"ai_languageModel out 0 to in 0"| n3
  n22 -->|"main out 0 to in 0"| n23
  n26 -->|"ai_document out 0 to in 0"| n20
  n17 -->|"ai_outputParser out 0 to in 0"| n3
  n5 -->|"ai_vectorStore out 0 to in 0"| n7
  n19 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 0 to in 0"| n22
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
