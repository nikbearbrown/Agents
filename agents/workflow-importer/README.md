# Workflow Importer

Adapt the published “Workflow Importer” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 37 executable nodes and 40 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Extract from File"]
  n1["Export Credentials"]
  n2["Get Credentials Data"]
  n3["Binary to JSON"]
  n4["Merge"]
  n5["Collect Credentials to Replace"]
  n6["Settings"]
  n7["Prepare Request Data"]
  n8["Get Workflows"]
  n9["No Operation"]
  n10["Determine Workflow Source"]
  n11["Error1"]
  n12["Error"]
  n13["Split Out Workflows"]
  n14["Get Workflow Names"]
  n15["Sort by updatedAt DESC"]
  n16["No Operation1"]
  n17["Rename Keys"]
  n18["Create Workflow"]
  n19["Upload File"]
  n20["Choose Workflow"]
  n21["Success"]
  n22["Choose Instance"]
  n23["On form submission"]
  n24["Generate Instance Options"]
  n25["Get Selected Workflow"]
  n26["Split Out Nodes"]
  n27["Filter Out Nodes Having Credentials"]
  n28["Extract Credentials"]
  n29["Remove Duplicate Credentials by Name"]
  n30["Map Credentials"]
  n31["Get Selected Credentials"]
  n32["Add Old Names"]
  n33["Replace Credentials in Workflow"]
  n34["Generate Credential Options"]
  n35["Create Empty Credentials"]
  n36["Get Missing Credentials"]
  n4 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n24
  n17 -->|"main out 0 to in 1"| n4
  n19 -->|"main out 0 to in 0"| n0
  n9 -->|"main out 0 to in 0"| n4
  n32 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 0"| n13
  n8 -->|"main out 1 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n26
  n3 -->|"main out 0 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n25
  n18 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 1 to in 0"| n11
  n30 -->|"main out 0 to in 0"| n36
  n30 -->|"main out 0 to in 0"| n31
  n26 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n20
  n23 -->|"main out 0 to in 0"| n10
  n28 -->|"main out 0 to in 0"| n29
  n13 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n8
  n25 -->|"main out 0 to in 0"| n1
  n25 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n14
  n36 -->|"main out 0 to in 0"| n35
  n35 -->|"main out 0 to in 0"| n32
  n31 -->|"main out 0 to in 1"| n5
  n10 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 1 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n22
  n34 -->|"main out 0 to in 0"| n30
  n5 -->|"main out 0 to in 0"| n33
  n33 -->|"main out 0 to in 0"| n18
  n27 -->|"main out 0 to in 0"| n28
  n29 -->|"main out 0 to in 0"| n34
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
