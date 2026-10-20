# List existing Snapshots

Adapt the published “List existing Snapshots” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Set snapshot attributes"]
  n1["Schedule Trigger"]
  n2["When clicking #8216;Test workflow#8217;"]
  n3["Credential"]
  n4["Authorization"]
  n5["List instances"]
  n6["Split Out"]
  n7["UUID"]
  n8["TRACE ID"]
  n9["List snapshots"]
  n10["UUID1"]
  n11["Merge"]
  n12["get Date #38; Time"]
  n13["Delete existing snapshot"]
  n14["Create a new snapshot"]
  n15["Create a new snapshot1"]
  n16["UUID2"]
  n17["UUID3"]
  n18["UUID4"]
  n19["Formatted Date"]
  n20["Whether snapshot there is no snapshot"]
  n21["set snapshot attributes"]
  n7 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n14
  n17 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 1"| n11
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n7
  n19 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n17
  n21 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n12
  n20 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 1 to in 0"| n0
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
