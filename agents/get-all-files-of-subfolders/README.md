# Get all files of subfolders

Adapt the published “Get all files of subfolders” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["Whether type is file"]
  n2["Set new path for subfolder"]
  n3["Set new path for file"]
  n4["Webhook"]
  n5["Execute Workflow Trigger"]
  n6["Set folder-paths for from and to"]
  n7["Create to folder if necessary"]
  n8["Get all folders/files in from-folder"]
  n9["Loop over files and folders"]
  n10["Consolidate all files and folders found"]
  n11["Create subfolder in to-folder"]
  n12["Get all folders/files in found subfolder"]
  n13["Whether there is are more files or subfolders found"]
  n14["Consolidate all found files"]
  n15["Loop Over all files"]
  n16["Move file to destination"]
  n17["Delete from-folder"]
  n18["Set paths"]
  n19["Whether the request is valid"]
  n20["Stop and Error: request not valid"]
  n21["Whether the request is valid1"]
  n22["Stop and Error: request not valid1"]
  n4 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 1 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 1 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n21
  n16 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 1 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 1 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n8
  n21 -->|"main out 0 to in 0"| n6
  n21 -->|"main out 1 to in 0"| n22
  n6 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 1 to in 0"| n9
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
