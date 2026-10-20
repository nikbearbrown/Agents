# Student Assistant Automation System

Adapt the published “Student Assistant Automation System” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Gmail Trigger"]
  n1["If"]
  n2["Code in JavaScript"]
  n3["Code in JavaScript1"]
  n4["Schedule Trigger"]
  n5["Code in JavaScript2"]
  n6["2 days filter"]
  n7["combine"]
  n8["deadline"]
  n9["schedule"]
  n10["emails"]
  n11["Code in JavaScript3"]
  n12["Delete rows or columns from sheet"]
  n13["time table"]
  n14["deadline1"]
  n15["Schedule Trigger1"]
  n0 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 0 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n14
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nadjibdje--Student-Assistant-Automation-System.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
