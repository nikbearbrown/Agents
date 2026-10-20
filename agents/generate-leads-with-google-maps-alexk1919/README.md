# Generate Leads with Google Maps - AlexK1919

Adapt the published “Generate Leads with Google Maps - AlexK1919” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 36 executable nodes and 40 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["Run workflow every hours"]
  n2["Execute Workflow Trigger"]
  n3["Check Max Retries1"]
  n4["Stop and Error1"]
  n5["GMaps API"]
  n6["Update Status to Success"]
  n7["Add rows in Google Sheets"]
  n8["Set Row Number"]
  n9["Set Zip"]
  n10["Set Place ID"]
  n11["Exponential Backoff"]
  n12["Remove Duplicates"]
  n13["Wait"]
  n14["Check Max Retries"]
  n15["Stop and Error"]
  n16["Exponential Backoff1"]
  n17["Wait1"]
  n18["Settings"]
  n19["GS - Get Subcategory"]
  n20["Subcategory"]
  n21["GS - Get Zip Codes"]
  n22["Place Array"]
  n23["Loop Zips"]
  n24["Loop Subcats"]
  n25["GS - Get Status"]
  n26["Check Max Retries2"]
  n27["Stop and Error2"]
  n28["Exponential Backoff2"]
  n29["Wait2"]
  n30["Limit"]
  n31["Zips"]
  n32["Filter Zips"]
  n33["Filter Subcategories"]
  n34["If Empty"]
  n35["Split Out"]
  n13 -->|"main out 0 to in 0"| n3
  n31 -->|"main out 0 to in 0"| n32
  n30 -->|"main out 0 to in 0"| n23
  n17 -->|"main out 0 to in 0"| n14
  n29 -->|"main out 0 to in 0"| n26
  n9 -->|"main out 0 to in 0"| n5
  n34 -->|"main out 0 to in 0"| n24
  n34 -->|"main out 1 to in 0"| n22
  n18 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n34
  n23 -->|"main out 1 to in 0"| n19
  n35 -->|"main out 0 to in 0"| n30
  n32 -->|"main out 0 to in 0"| n8
  n22 -->|"main out 0 to in 0"| n10
  n20 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 1 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n35
  n25 -->|"main out 0 to in 0"| n6
  n25 -->|"main out 1 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n7
  n26 -->|"main out 0 to in 0"| n27
  n21 -->|"main out 0 to in 0"| n31
  n11 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n17
  n28 -->|"main out 0 to in 0"| n29
  n33 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n33
  n2 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n24
  n6 -->|"main out 1 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n25
  n7 -->|"main out 1 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n18
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
