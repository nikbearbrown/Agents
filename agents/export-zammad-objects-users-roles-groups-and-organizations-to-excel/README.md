# Export Zammad Objects Users, Roles, Groups and Organizations to Excel

Adapt the published “Export Zammad Objects Users, Roles, Groups and Organizations to Excel” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Zammad Univeral User Object"]
  n2["Zammad Univeral Organization Object"]
  n3["Zammad Univeral Role Object"]
  n4["Get all Organizations"]
  n5["Get all Roles"]
  n6["Convert to Excel Organizations"]
  n7["Convert to Excel Roles"]
  n8["Convert to Excel Users"]
  n9["Get all Users"]
  n10["Zammad Univeral Group Object"]
  n11["Get all Groups"]
  n12["If"]
  n13["Basic Variables"]
  n14["Convert to Excel Groups"]
  n15["Filter Groups if needed"]
  n16["Filter Roles if needed"]
  n17["Filter Organizations if needed"]
  n12 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n17
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
