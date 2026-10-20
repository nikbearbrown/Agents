# Prevent concurrent workflow runs using Redis

Adapt the published “Prevent concurrent workflow runs using Redis” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When Executed by Another Workflow"]
  n1["Switch"]
  n2["When clicking #8216;Test workflow#8217;"]
  n3["If2"]
  n4["Is Workflow Active"]
  n5["Set Workflow Active"]
  n6["Set Workflow Finished"]
  n7["Get Key"]
  n8["Set Key"]
  n9["UnSet Key"]
  n10["Set Timeout"]
  n11["set continue"]
  n12["If"]
  n13["Is Workflow Active1"]
  n14["Stop and Error"]
  n15["No Operation, do nothing"]
  n16["Set Workflow Active1"]
  n17["Set Workflow Finished1"]
  n18["Wait"]
  n19["If1"]
  n20["Is Workflow Active2"]
  n21["Stop and Error1"]
  n22["Set Workflow Finished2"]
  n23["Wait1"]
  n24["Wait2"]
  n25["Wait3"]
  n26["Set Workflow #34;started#34;"]
  n27["Set Workflow #34;finishing#34;"]
  n28["Set Workflow #34;loading#34;"]
  n29["Is Workflow Active3"]
  n30["Switch1"]
  n12 -->|"main out 0 to in 0"| n16
  n12 -->|"main out 1 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n26
  n19 -->|"main out 1 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n17
  n23 -->|"main out 0 to in 0"| n28
  n24 -->|"main out 0 to in 0"| n27
  n25 -->|"main out 0 to in 0"| n22
  n1 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 1 to in 0"| n8
  n1 -->|"main out 2 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n12
  n20 -->|"main out 0 to in 0"| n19
  n29 -->|"main out 0 to in 0"| n30
  n16 -->|"main out 0 to in 0"| n15
  n28 -->|"main out 0 to in 0"| n24
  n26 -->|"main out 0 to in 0"| n23
  n15 -->|"main out 0 to in 0"| n18
  n27 -->|"main out 0 to in 0"| n25
  n0 -->|"main out 0 to in 0"| n10
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
