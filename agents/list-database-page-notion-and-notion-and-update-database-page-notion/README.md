# list database page notion and notion and update database page notion

Adapt the published “list database page notion and notion and update database page notion” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get Team Members"]
  n1["Merge"]
  n2["Query Current Semester"]
  n3["Select Semester ID and Projects Count"]
  n4["Use Default Name if Not Specified"]
  n5["Select Project Showcase ID"]
  n6["Get Project Name #38; Idea"]
  n7["Create Project"]
  n8["If user exists"]
  n9["Create User"]
  n10["Query for User"]
  n11["Merge1"]
  n12["Merge2"]
  n13["Update Semester for User"]
  n14["Query User"]
  n15["Select Semester ID"]
  n16["Update Project Relation"]
  n17["Merge3"]
  n18["Concatenate SemesterIDs"]
  n19["Concatenate ProjectIDs"]
  n20["Merge4"]
  n21["Set Email"]
  n22["Team Creation"]
  n1 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 0 to in 0"| n14
  n21 -->|"main out 0 to in 1"| n20
  n14 -->|"main out 0 to in 1"| n12
  n14 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n21
  n22 -->|"main out 0 to in 0"| n6
  n22 -->|"main out 0 to in 0"| n0
  n22 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 0"| n20
  n8 -->|"main out 1 to in 0"| n9
  n10 -->|"main out 0 to in 1"| n11
  n0 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 1"| n1
  n5 -->|"main out 0 to in 1"| n17
  n4 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n1
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
