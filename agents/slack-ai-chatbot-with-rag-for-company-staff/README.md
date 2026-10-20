# Slack AI Chatbot with RAG for company staff

Adapt the published “Slack AI Chatbot with RAG for company staff” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["Simple Memory"]
  n2["Embeddings OpenAI1"]
  n3["RAG"]
  n4["Calculator"]
  n5["Get message"]
  n6["Send message"]
  n7["When clicking #8216;Test workflow#8217;"]
  n8["Create collection"]
  n9["Refresh collection"]
  n10["Get folder"]
  n11["Download Files"]
  n12["Default Data Loader"]
  n13["Token Splitter"]
  n14["Qdrant Vector Store1"]
  n15["Embeddings OpenAI2"]
  n16["Anthropic Chat Model"]
  n3 -->|"ai_tool out 0 to in 0"| n0
  n0 -->|"main out 0 to in 0"| n6
  n4 -->|"ai_tool out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n0
  n1 -->|"ai_memory out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n14
  n13 -->|"ai_textSplitter out 0 to in 0"| n12
  n2 -->|"ai_embedding out 0 to in 0"| n3
  n15 -->|"ai_embedding out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n10
  n12 -->|"ai_document out 0 to in 0"| n14
  n16 -->|"ai_languageModel out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n9
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
