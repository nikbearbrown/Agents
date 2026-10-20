# My workflow 4

Adapt the published “My workflow 4” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Prepare Variables"]
  n1["GitHub: Get Repos"]
  n2["Batch Repos"]
  n3["GitHub: Get Languages"]
  n4["Aggregate Repo Data"]
  n5["arXiv: Search Papers"]
  n6["Parse arXiv XML"]
  n7["Manual Trigger"]
  n8["Input: Companies"]
  n9["Format Language Data"]
  n10["Format Research Data"]
  n11["Code"]
  n12["Code1"]
  n13["Code2"]
  n14["Code3"]
  n15["Code4"]
  n16["Code5"]
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 1 to in 0"| n16
  n3 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n13
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
