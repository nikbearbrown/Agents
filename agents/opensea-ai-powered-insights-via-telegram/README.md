# OpenSea AI-Powered Insights via Telegram

Adapt the published “OpenSea AI-Powered Insights via Telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 10 executable nodes and 9 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["Telegram Trigger"]
  n2["Adds SessionId"]
  n3["Opensea Supervisor Brain"]
  n4["Opensea Supervisor Memory"]
  n5["OpenSea Analytics Agent Tool"]
  n6["OpenSea NFT Agent Tool"]
  n7["OpenSea Marketplace Agent Tool"]
  n8["Telegram"]
  n9["OpenSea AI-Powered Insights Agent"]
  n2 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n6 -->|"ai_tool out 0 to in 0"| n9
  n3 -->|"ai_languageModel out 0 to in 0"| n9
  n4 -->|"ai_memory out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n9
  n5 -->|"ai_tool out 0 to in 0"| n9
  n7 -->|"ai_tool out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n8
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
