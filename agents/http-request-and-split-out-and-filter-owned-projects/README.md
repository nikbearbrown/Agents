# http request and split out and filter owned projects

Adapt the published “http request and split out and filter owned projects” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["set credentials"]
  n1["login n8n"]
  n2["get tags"]
  n3["my-projects"]
  n4["Split Out"]
  n5["filter owned projects"]
  n6["Get folders"]
  n7["Split Out2"]
  n8["Remove Duplicates"]
  n9["Loop Over Items"]
  n10["get workflows"]
  n11["Move workflow to folder"]
  n12["Normalize names"]
  n13["Limit1"]
  n14["Create folders"]
  n15["set folder name #43; id"]
  n16["set folder name #43; id1"]
  n17["set global"]
  n18["Filter"]
  n19["Edit Fields"]
  n20["On form submission"]
  n21["Code"]
  n22["If no folder"]
  n23["If folder exists"]
  n24["set name"]
  n25["end import"]
  n26["pass all items"]
  n27["select tags to move"]
  n28["extract name from form"]
  n29["Split Out the tags"]
  n30["tags to string"]
  n21 -->|"main out 0 to in 0"| n27
  n18 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n23
  n2 -->|"main out 0 to in 0"| n30
  n24 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n10
  n19 -->|"main out 0 to in 0"| n24
  n6 -->|"main out 0 to in 0"| n22
  n3 -->|"main out 0 to in 0"| n4
  n22 -->|"main out 0 to in 0"| n7
  n22 -->|"main out 1 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n15
  n26 -->|"main out 0 to in 0"| n25
  n30 -->|"main out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n26
  n9 -->|"main out 1 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n1
  n23 -->|"main out 0 to in 0"| n16
  n23 -->|"main out 1 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n0
  n29 -->|"main out 0 to in 0"| n28
  n27 -->|"main out 0 to in 0"| n29
  n15 -->|"main out 0 to in 0"| n17
  n5 -->|"main out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n17
  n28 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n9
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
