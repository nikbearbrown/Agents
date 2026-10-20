# Google Drive Automation

Adapt the published “Google Drive Automation” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["Monitor Google Drive for New Files"]
  n2["Download File from Google Drive"]
  n3["Extract PDF Content"]
  n4["Insert Document into Pinecone Vector Store"]
  n5["Generate Document Embeddings #40;Google Gemini#41;"]
  n6["Clean and Normalize PDF Text"]
  n7["Load Document Data for Processing"]
  n8["Split Document Text into Chunks"]
  n9["Chat Message Trigger"]
  n10["Retrieve Relevant Documents from Pinecone"]
  n11["Generate Query Embeddings #40;Google Gemini#41;"]
  n12["Generate Chat Prompt with Context"]
  n13["OpenRouter Chat Model Interface"]
  n3 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n3
  n13 -->|"ai_languageModel out 0 to in 0"| n0
  n8 -->|"ai_textSplitter out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n0
  n7 -->|"ai_document out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n2
  n11 -->|"ai_embedding out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n12
  n5 -->|"ai_embedding out 0 to in 0"| n4
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
