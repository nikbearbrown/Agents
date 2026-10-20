# AI Agent to chat with you Search Console Data, using OpenAI and Postgres

Adapt the published “AI Agent to chat with you Search Console Data, using OpenAI and Postgres” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Postgres Chat Memory"]
  n1["OpenAI Chat Model"]
  n2["Set fields"]
  n3["Webhook - ChatInput"]
  n4["Respond to Webhook"]
  n5["Call Search Console Tool"]
  n6["Tool calling"]
  n7["Switch"]
  n8["Set fields - Consruct API CALL"]
  n9["Set fields - Create searchConsoleDataArray"]
  n10["Set fields - Create searchConsoleDataArray 2"]
  n11["Search Console - Get Custom Insights"]
  n12["#35;#35; Search Console - Get List of Properties"]
  n13["Array aggregation - response to AI Agent"]
  n14["Array aggregation - response to AI Agent1"]
  n15["AI Agent"]
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 1 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n15
  n6 -->|"main out 0 to in 0"| n8
  n1 -->|"ai_languageModel out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n2
  n0 -->|"ai_memory out 0 to in 0"| n15
  n5 -->|"ai_tool out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n14
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
