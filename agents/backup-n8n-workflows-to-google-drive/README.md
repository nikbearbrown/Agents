# backup n8n workflows to google drive

Adapt the published “backup n8n workflows to google drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Get all n8n Workflows"]
  n2["Backup to Google Drive2"]
  n3["Loop Over Items"]
  n4["Backup to Google Drive4"]
  n5["ifDriveEmpty"]
  n6["firstWorkflowJson"]
  n7["JsonToFile"]
  n8["CodeJsonToFile1"]
  n9["Limit"]
  n10["Workflow Data"]
  n11["successEmail"]
  n12["failureEmail"]
  n13["getDriveFileData"]
  n14["When Executed by Another Workflow"]
  n15["Execute Workflow"]
  n16["Parameters"]
  n17["Discord"]
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n4
  n16 -->|"main out 0 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 1 to in 0"| n6
  n10 -->|"main out 0 to in 0"| n16
  n8 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 1 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n12
  n4 -->|"main out 1 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n10
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
