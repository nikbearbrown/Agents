# Marketing Insights Processing

Adapt the published “Marketing Insights Processing” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Execute Workflow Trigger"]
  n1["Create Marketing Insight Data"]
  n2["Check if Recurring Topics Found"]
  n3["Wait for rate limiting - Recurring"]
  n4["Split Out Recurring Topics"]
  n5["Create Recurring Topics Data"]
  n6["Bundle Recurring Topics Data to 1 object"]
  n7["Merge Recurring Topics Thread"]
  n8["Check if Marketing Insight Data Found"]
  n9["Wait for rate limiting - Marketing Insights"]
  n10["Split out Insights"]
  n11["Bundle Marketing Insights Data to 1 object"]
  n12["Merge Marketing Insights Thread"]
  n13["Check if Actionable Insights Data Found"]
  n14["Wait for rate limiting - Actionable Insights"]
  n15["Split Out Actionable Insights"]
  n16["Create Actionable Insights Data"]
  n17["Bundle Actionable Insights Data to 1 object"]
  n18["Merge Actionable Insights Thread"]
  n10 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n17
  n3 -->|"main out 0 to in 0"| n4
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 1 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 1 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n18
  n9 -->|"main out 0 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n15
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
