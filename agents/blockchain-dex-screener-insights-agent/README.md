# Blockchain DEX Screener Insights Agent

Adapt the published “Blockchain DEX Screener Insights Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["OpenAI Chat Model"]
  n2["Window Buffer Memory"]
  n3["Telegram Trigger"]
  n4["Blockchain DEX Screener Insights Agent"]
  n5["Telegram"]
  n6["Adds SessionId"]
  n7["DexScreener Latest Token Profiles"]
  n8["DexScreener Latest Boosted Tokens"]
  n9["DexScreener Top Token Boosts"]
  n10["DexScreener Search Pairs"]
  n11["DexScreener Check Orders Paid for Token"]
  n12["DexScreener Get Pairs by Chain and Pair Address"]
  n13["DexScreener Token Pools"]
  n14["DexScreener Pairs by Token Address"]
  n6 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n6
  n1 -->|"ai_languageModel out 0 to in 0"| n4
  n2 -->|"ai_memory out 0 to in 0"| n4
  n13 -->|"ai_tool out 0 to in 0"| n4
  n10 -->|"ai_tool out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n6
  n9 -->|"ai_tool out 0 to in 0"| n4
  n8 -->|"ai_tool out 0 to in 0"| n4
  n7 -->|"ai_tool out 0 to in 0"| n4
  n14 -->|"ai_tool out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n11 -->|"ai_tool out 0 to in 0"| n4
  n12 -->|"ai_tool out 0 to in 0"| n4
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
