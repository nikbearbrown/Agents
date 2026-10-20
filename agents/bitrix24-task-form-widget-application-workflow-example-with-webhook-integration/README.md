# Bitrix24 Task Form Widget Application Workflow example with Webhook Integration

Adapt the published “Bitrix24 Task Form Widget Application Workflow example with Webhook Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Bitrix24 Handler"]
  n1["Extract Credentials"]
  n2["Check Event Type"]
  n3["Is Installation#63;"]
  n4["Register Placement"]
  n5["Process Settings"]
  n6["Installation Response"]
  n7["Has Valid Settings#63;"]
  n8["Get Task Data"]
  n9["Format Task Data"]
  n10["Task View Response"]
  n11["Error Response"]
  n12["Save Installation Settings"]
  n13["Set Settings Data"]
  n14["Create Settings File"]
  n15["Read Installation Settings"]
  n16["If Installation finished"]
  n17["Installation finished Response"]
  n18["Merge Installation info"]
  n19["Extract Installation Settings"]
  n20["Merge request data with installation settings"]
  n8 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 1 to in 0"| n15
  n3 -->|"main out 1 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 1 to in 0"| n4
  n16 -->|"main out 1 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 1"| n18
  n19 -->|"main out 0 to in 1"| n20
  n20 -->|"main out 0 to in 0"| n5
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
