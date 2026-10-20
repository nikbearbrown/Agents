# 🚨 Change your Base ID and Table ID here!

Adapt the published “🚨 Change your Base ID and Table ID here!” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get Base Schema"]
  n1["On form submission"]
  n2["Filter Unsupported FieldTypes"]
  n3["Combine Fields"]
  n4["Render Form"]
  n5["Files To List"]
  n6["Fields to List"]
  n7["Covert to n8n Form Fields"]
  n8["Filter Table"]
  n9["Baserow List Fields"]
  n10["Covert to n8n Form Fields1"]
  n11["Combine Fields1"]
  n12["Filter Unsupported FieldTypes1"]
  n13["Render Form1"]
  n14["Baserow Create Row"]
  n15["On form submission1"]
  n16["Files To List1"]
  n17["Baserow Upload File"]
  n18["Baserow Update Row"]
  n19["Group By FieldName"]
  n20["Update Airtable Row"]
  n21["Prep Data for Insert1"]
  n22["Prep Data for Insert"]
  n23["Airtable Create Record"]
  n24["Show Completion#33;"]
  n25["Show Completion#33;1"]
  n4 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n20
  n3 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n16
  n18 -->|"main out 0 to in 0"| n24
  n19 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n0
  n9 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 0 to in 0"| n9
  n20 -->|"main out 0 to in 0"| n25
  n22 -->|"main out 0 to in 0"| n23
  n21 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n11
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
