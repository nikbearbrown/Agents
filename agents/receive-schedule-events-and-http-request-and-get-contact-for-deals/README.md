# receive schedule events and http request and get contact for deals

Adapt the published “receive schedule events and http request and get contact for deals” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Get Deals"]
  n2["Get contact for deals"]
  n3["Unassigned Deals"]
  n4["Split out deals"]
  n5["Assign by Region"]
  n6["Assign deal to John"]
  n7["Assign to Max"]
  n8["Assign to Eeden"]
  n9["Assign to Peter"]
  n10["Get company of contact#40;s#41;"]
  n11["Assign US deals by company size"]
  n12["Assign deal to Edward"]
  n13["Assign to Michael"]
  n14["Assign to Suka"]
  n15["Assign DE deals by company size"]
  n1 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 1 to in 0"| n15
  n5 -->|"main out 2 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 1 to in 0"| n13
  n15 -->|"main out 2 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 1 to in 0"| n7
  n11 -->|"main out 2 to in 0"| n8
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
