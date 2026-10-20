# Business WhatsApp AI RAG Chatbot

Adapt the published “Business WhatsApp AI RAG Chatbot” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Respond to Webhook"]
  n1["AI Agent"]
  n2["OpenAI Chat Model"]
  n3["When clicking #8216;Test workflow#8217;"]
  n4["Qdrant Vector Store"]
  n5["Create collection"]
  n6["Refresh collection"]
  n7["Get folder"]
  n8["Download Files"]
  n9["Embeddings OpenAI"]
  n10["Default Data Loader"]
  n11["Token Splitter"]
  n12["Verify"]
  n13["Respond"]
  n14["is Message#63;"]
  n15["Only message"]
  n16["Send"]
  n17["Window Buffer Memory"]
  n18["OpenAI Chat Model1"]
  n19["Retrive Qdrant Vector Store"]
  n20["Embeddings OpenAI2"]
  n21["RAG"]
  n21 -->|"ai_tool out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n0
  n13 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 1 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n4
  n11 -->|"ai_textSplitter out 0 to in 0"| n10
  n9 -->|"ai_embedding out 0 to in 0"| n4
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n20 -->|"ai_embedding out 0 to in 0"| n19
  n18 -->|"ai_languageModel out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n7
  n10 -->|"ai_document out 0 to in 0"| n4
  n17 -->|"ai_memory out 0 to in 0"| n1
  n19 -->|"ai_vectorStore out 0 to in 0"| n21
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n6
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
