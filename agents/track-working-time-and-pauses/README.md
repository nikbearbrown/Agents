# Track Working Time and Pauses

Adapt the published “Track Working Time and Pauses” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Create new page"]
  n1["Update page with end date"]
  n2["If pause_in_minuten is empty"]
  n3["If page responded"]
  n4["If page exist"]
  n5["If page exist1"]
  n6["If"]
  n7["Set Break Duration"]
  n8["Update break duration for current day"]
  n9["Set break duration for current day"]
  n10["Get notion page by date"]
  n11["Set Message - End time already tracked"]
  n12["Set Message - End time tracked"]
  n13["Set Message - Start time not yet tracked"]
  n14["Set Message - Start not yet tracked"]
  n15["Set Message - Break time tracked"]
  n16["Set Message - Break time updated"]
  n17["Set Message - Start time already tracked"]
  n18["Set Message - Start time already tracked1"]
  n19["Get notion page with todays date"]
  n20["Switch"]
  n21["Get notion page with todays date1"]
  n22["Respond to Webhook"]
  n23["Webhook - Track Time"]
  n6 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 1 to in 0"| n11
  n20 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 1 to in 0"| n7
  n20 -->|"main out 2 to in 0"| n21
  n4 -->|"main out 0 to in 0"| n17
  n4 -->|"main out 1 to in 0"| n0
  n5 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 1 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n18
  n3 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 1 to in 0"| n14
  n7 -->|"main out 0 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 1 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n22
  n19 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n22
  n16 -->|"main out 0 to in 0"| n22
  n21 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n16
  n11 -->|"main out 0 to in 0"| n22
  n17 -->|"main out 0 to in 0"| n22
  n13 -->|"main out 0 to in 0"| n22
  n18 -->|"main out 0 to in 0"| n22
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
