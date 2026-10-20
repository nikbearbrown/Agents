# TechStackComparativeAgentWorkflow

Adapt the published “TechStackComparativeAgentWorkflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Validate Input"]
  n1["Prepare Variables"]
  n2["GitHub: Get Repos"]
  n3["Batch Repos #40;Top 5#41;"]
  n4["GitHub: Get Languages"]
  n5["Aggregate Repo Data"]
  n6["arXiv: Search Papers"]
  n7["Error: Invalid Input"]
  n8["Parse arXiv XML"]
  n9["When clicking #8216;Execute workflow#8217;"]
  n10["Split Out"]
  n11["set"]
  n12["set1"]
  n13["Convert to File"]
  n14["Edit Fields"]
  n15["Edit Fields1"]
  n16["Code"]
  n17["Edit Fields2"]
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 1 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n17
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n10
  n12 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n3
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
