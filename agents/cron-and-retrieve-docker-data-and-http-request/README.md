# Dashboard

Adapt the published “Dashboard” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Cron"]
  n1["Dashboard Configuration"]
  n2["Retrieve Docker Data"]
  n3["Docker Pulls"]
  n4["Docker Stars"]
  n5["Retrieve npm Data"]
  n6["GitHub Watchers"]
  n7["GitHub Forks"]
  n8["GitHub Open Issues"]
  n9["GitHub Stars"]
  n10["npm Maintenance"]
  n11["npm Popularity"]
  n12["npm Quality"]
  n13["npm Final"]
  n14["Product Hunt Rating"]
  n15["Product Hunt Reviews"]
  n16["Product Hunt Votes"]
  n17["Product Hunt Comments"]
  n18["GitHub"]
  n19["Retrieve Product Hunt Data"]
  n20["Massage npm Data"]
  n21["Massage Product Hunt Data"]
  n22["Massage Docker Data"]
  n23["Massage GitHub Data"]
  n0 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 0 to in 0"| n23
  n20 -->|"main out 0 to in 0"| n10
  n20 -->|"main out 0 to in 0"| n12
  n20 -->|"main out 0 to in 0"| n11
  n20 -->|"main out 0 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n20
  n22 -->|"main out 0 to in 0"| n4
  n22 -->|"main out 0 to in 0"| n3
  n23 -->|"main out 0 to in 0"| n9
  n23 -->|"main out 0 to in 0"| n6
  n23 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n22
  n1 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n14
  n21 -->|"main out 0 to in 0"| n15
  n21 -->|"main out 0 to in 0"| n16
  n21 -->|"main out 0 to in 0"| n17
  n19 -->|"main out 0 to in 0"| n21
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
