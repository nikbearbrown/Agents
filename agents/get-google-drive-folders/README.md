# get Google Drive folders

Adapt the published “get Google Drive folders” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Move Binary Data"]
  n1["IGNORE FILES"]
  n2["Create n8n_backups"]
  n3["Create n8n_old"]
  n4["GET CURRENT FOLDER"]
  n5["Code"]
  n6["If n8n_old"]
  n7["If1 n8n_backups"]
  n8["GET CURRENT FOLDER CREATES"]
  n9["Merge mensage"]
  n10["GET CURRENT BACKUPS1"]
  n11["MOVE INTO OLD FOLDER"]
  n12["UPLOAD WORKFLOWS"]
  n13["Item Lists"]
  n14["Split In Batches2"]
  n15["Split In Batches"]
  n16["n8n"]
  n17["LIST OLD BACKUPS"]
  n18["DELETE OLD BACKUP"]
  n19["Item Lists old"]
  n20["Split In Batches old"]
  n21["Schedule Trigger"]
  n22["Schedule Trigger1"]
  n16 -->|"main out 0 to in 0"| n0
  n5 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 1 to in 1"| n9
  n13 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 0"| n20
  n7 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 1 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n15
  n21 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n20
  n14 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n1
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
