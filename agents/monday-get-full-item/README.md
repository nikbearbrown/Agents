# MONDAY GET FULL ITEM

Adapt the published “MONDAY GET FULL ITEM” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["GET ALL COLUMNS"]
  n1["GET ALL RELATIONS"]
  n2["PULL LINKEDPULSE1"]
  n3["GET LINKEDPULSES1"]
  n4["SPLIT LINKED PULSES1"]
  n5["SPLIT SUBITEMS1"]
  n6["GET EACH SUBITEM1"]
  n7["GET ALL COLUMNS1"]
  n8["GET ALL COLUMNS2"]
  n9["Aggregate1"]
  n10["PULL SUBITEMS"]
  n11["GET ITEM"]
  n12["GET ALL COLUMNS3"]
  n13["Merge4"]
  n14["Aggregate"]
  n15["Merge"]
  n16["Merge2"]
  n17["Merge1"]
  n18["Execute Workflow Trigger"]
  n19["Execute Workflow"]
  n20["Edit Fields"]
  n15 -->|"main out 0 to in 1"| n17
  n16 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 1"| n15
  n20 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 0 to in 1"| n16
  n12 -->|"main out 0 to in 1"| n13
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n2
  n18 -->|"main out 0 to in 0"| n11
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
