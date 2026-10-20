# Entra User to Zammad User Sync

Adapt the published “Entra User to Zammad User Sync” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Get Groups from Entra"]
  n2["Remove outer Array"]
  n3["Select Entra Zammad default Group"]
  n4["Remove outer Array from Entra User"]
  n5["Zammad Univeral User Object"]
  n6["Get Zammad Users"]
  n7["Merge"]
  n8["Get Members of the default group"]
  n9["Find new Zammad Users"]
  n10["Update Zammad User"]
  n11["Create Zammad User"]
  n12["Deactivate Zammad User"]
  n13["Find removed Users"]
  n14["If"]
  n15["Select only active Users and entra_obect_type#61;#34;user#34;"]
  n14 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 3 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 1"| n7
  n5 -->|"main out 0 to in 1"| n9
  n5 -->|"main out 0 to in 1"| n13
  n8 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n13
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
