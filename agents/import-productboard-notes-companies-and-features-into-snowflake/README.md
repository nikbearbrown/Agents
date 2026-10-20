# Import Productboard Notes, Companies and Features into Snowflake

Adapt the published “Import Productboard Notes, Companies and Features into Snowflake” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 31 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Manual mapping feature"]
  n1["get productboard companies"]
  n2["Manual mapping companies"]
  n3["get productboard notes"]
  n4["Manual mapping notes"]
  n5["Split features"]
  n6["Split companies"]
  n7["Split notes"]
  n8["Split features in notes"]
  n9["Combine Feature ID #43; Note ID"]
  n10["get productboard features"]
  n11["Update Productboard Notes"]
  n12["Empty Table Productboard Notes"]
  n13["#91;CREATE#93; PRODUCTBOARD_NOTES"]
  n14["#91;CREATE#93; PRODUCTBOARD_COMPANIES"]
  n15["Update Productboard Companies"]
  n16["Manual mapping companies db"]
  n17["Manual mapping notes db"]
  n18["Empty Table Productboard Companies"]
  n19["#91;CREATE#93; PRODUCTBOARD_NOTES_FEATURES"]
  n20["Manual mapping feature note IDs db"]
  n21["Update Productboard Note and Feature IDs"]
  n22["Empty Table Productboard Note and Feature IDs"]
  n23["Loop Over Items notes"]
  n24["Loop Over Items features notes"]
  n25["#91;CREATE#93; PRODUCTBOARD_FEATURES"]
  n26["Empty Table Productboard Features"]
  n27["Loop Over Items features"]
  n28["Manual mapping features db"]
  n29["Update Productboard Features"]
  n30["Schedule Trigger"]
  n31["Slack"]
  n32["Count Notes Last 7 days and Unprocessed"]
  n7 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n32
  n5 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n2
  n30 -->|"main out 0 to in 0"| n26
  n4 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 1 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n27
  n3 -->|"main out 0 to in 0"| n7
  n17 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n9
  n27 -->|"main out 0 to in 0"| n18
  n27 -->|"main out 1 to in 0"| n28
  n2 -->|"main out 0 to in 0"| n16
  n11 -->|"main out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n5
  n28 -->|"main out 0 to in 0"| n29
  n1 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 0"| n24
  n29 -->|"main out 0 to in 0"| n27
  n15 -->|"main out 0 to in 0"| n22
  n12 -->|"main out 0 to in 0"| n3
  n24 -->|"main out 1 to in 0"| n20
  n26 -->|"main out 0 to in 0"| n10
  n18 -->|"main out 0 to in 0"| n1
  n20 -->|"main out 0 to in 0"| n21
  n32 -->|"main out 0 to in 0"| n31
  n21 -->|"main out 0 to in 0"| n24
  n22 -->|"main out 0 to in 0"| n12
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
