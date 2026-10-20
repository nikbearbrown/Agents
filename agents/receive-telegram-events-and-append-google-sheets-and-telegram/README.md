# receive telegram events and append google sheets and telegram

Adapt the published “receive telegram events and append google sheets and telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["If"]
  n2["Deep Work"]
  n3["Break"]
  n4["Initiate Static Data"]
  n5["Increment Count"]
  n6["Record Deep Work"]
  n7["Record Long Break"]
  n8["Instructions Message"]
  n9["start or stop#63;"]
  n10["Long Break Notification"]
  n11["Clear Variables1"]
  n12["Clear Variables2"]
  n13["#60; 4 Cycles"]
  n14["Short Break Notification"]
  n15["Back to Work Notification"]
  n16["Start Cycle Notification"]
  n17["End of Session Notification"]
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 1 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 1 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 1 to in 0"| n17
  n5 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n3
  n16 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n11
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
