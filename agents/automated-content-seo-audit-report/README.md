# Automated Content SEO Audit Report

Adapt the published “Automated Content SEO Audit Report” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Set Fields"]
  n1["When clicking #8216;Start#8217;"]
  n2["Check Task Status"]
  n3["Create Task"]
  n4["If"]
  n5["Wait"]
  n6["Get RAW Audit Data"]
  n7["Extract URLs"]
  n8["Loop Over Items"]
  n9["Query GSC API"]
  n10["Wait1"]
  n11["Map GSC Data to URL"]
  n12["Merge GSC Data with RAW Data"]
  n13["Build Report Structure"]
  n14["Generate HTML Report"]
  n15["Extract 404 #38; 301"]
  n16["Loop Over Items1"]
  n17["Map URLs Data"]
  n18["Get Source URLs Data"]
  n19["Download Report"]
  n4 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 1 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n8
  n17 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 1 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 1 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n15
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
