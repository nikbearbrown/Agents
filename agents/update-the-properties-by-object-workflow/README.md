# Update the properties by object Workflow

Adapt the published “Update the properties by object Workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split by object"]
  n1["Fetch properties from Hubspot"]
  n2["Define crm_type"]
  n3["Split results"]
  n4["Transforms the results"]
  n5["Append to Google sheet"]
  n6["Erase Google sheet"]
  n7["Define array of objects"]
  n8["Start here to update your field list"]
  n9["File upload form"]
  n10["To get the first line of file"]
  n11["Set the real fields"]
  n12["Get the fields from the sheet"]
  n13["Merge fields and data"]
  n14["Check if all fields from input are defined"]
  n15["If all fields are defined"]
  n16["Creates the correspondance table"]
  n17["Form to set the correponding field for each input field"]
  n18["Get the content of file"]
  n19["Split all records to import"]
  n20["Define properties"]
  n21["Uploads to Hubspot"]
  n22["Form response"]
  n23["Remove hidden and starting with hs_ props fields"]
  n24["Set the values for each field"]
  n25["Set the values for each field1"]
  n3 -->|"main out 0 to in 0"| n23
  n2 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n22
  n11 -->|"main out 0 to in 1"| n13
  n13 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n0
  n18 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n24
  n15 -->|"main out 1 to in 0"| n16
  n19 -->|"main out 0 to in 0"| n20
  n1 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n14
  n24 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n11
  n25 -->|"main out 0 to in 0"| n19
  n16 -->|"main out 0 to in 0"| n17
  n8 -->|"main out 0 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n15
  n23 -->|"main out 0 to in 0"| n4
  n17 -->|"main out 0 to in 0"| n25
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
