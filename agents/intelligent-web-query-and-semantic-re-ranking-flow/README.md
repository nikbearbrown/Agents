# Intelligent Web Query and Semantic Re-Ranking Flow

Adapt the published “Intelligent Web Query and Semantic Re-Ranking Flow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Date #38; Time"]
  n1["Webhook"]
  n2["Auto-fixing Output Parser6"]
  n3["Auto-fixing Output Parser"]
  n4["Structured Output Parser1"]
  n5["Query-1 Combined"]
  n6["Respond to Webhook"]
  n7["Semantic Search - Result Re-Ranker"]
  n8["Query"]
  n9["Webhook Call"]
  n10["Semantic Search -Query Maker"]
  n11["Anthropic Chat Model"]
  n12["OpenAI Chat Model"]
  n13["Structured Output Parser2"]
  n14["Parser Model"]
  n15["Agent Model"]
  n8 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n0
  n15 -->|"ai_languageModel out 0 to in 0"| n7
  n15 -->|"ai_languageModel out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n10
  n14 -->|"ai_languageModel out 0 to in 0"| n2
  n14 -->|"ai_languageModel out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n7
  n3 -->|"ai_outputParser out 0 to in 0"| n10
  n4 -->|"ai_outputParser out 0 to in 0"| n3
  n13 -->|"ai_outputParser out 0 to in 0"| n2
  n2 -->|"ai_outputParser out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n6
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
