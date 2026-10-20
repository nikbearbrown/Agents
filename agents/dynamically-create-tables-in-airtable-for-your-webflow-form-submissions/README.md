# Dynamically create tables in Airtable for your Webflow form submissions

Adapt the published “Dynamically create tables in Airtable for your Webflow form submissions” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webflow Submission Trigger"]
  n1["Prepare form submission for workflow"]
  n2["Get Form Index Reference Table ID"]
  n3["Does Index Reference Table Exist#63;"]
  n4["#91;AIRTABLE#93; Create Index Reference Table"]
  n5["#91;AIRTABLE#93; Get Base Schema from list"]
  n6["#91;AIRTABLE#93; Create Webflow Form Table"]
  n7["Set New Webflow Form Table ID"]
  n8["#91;AIRTABLE#93; Insert Record In Form Index Reference Table"]
  n9["#91;AIRTABLE#93; Insert Record In Webflow Form Table"]
  n10["#91;AIRTABLE#93; Find Webflow Form Record In Form Index Reference Table"]
  n11["Set Webflow Form Table ID"]
  n12["Does This Webflow Form Table Exist#63;"]
  n11 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n1
  n7 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 1 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 1 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n11
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
