# Workflow A — Extract &amp; Store Raw Data

Adapt the published “Workflow A — Extract &amp; Store Raw Data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Fetch TechCrunch"]
  n2["Fetch VentureBeat"]
  n3["Fetch HackerNews"]
  n4["Fetch ArXiv"]
  n5["Fetch Reddit"]
  n6["Parse TechCrunch"]
  n7["Parse VentureBeat"]
  n8["Parse HackerNews"]
  n9["Parse ArXiv"]
  n10["Parse Reddit"]
  n11["Store TechCrunch"]
  n12["Store VentureBeat"]
  n13["Store HackerNews"]
  n14["Store ArXiv"]
  n15["Store Reddit"]
  n16["Verify #8212; Count Stored Items"]
  n17["Check #8212; New Items Exist#63;"]
  n18["Trigger #8212; Start Workflow B"]
  n19["Log #8212; Skip"]
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n16
  n12 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 1 to in 0"| n19
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
