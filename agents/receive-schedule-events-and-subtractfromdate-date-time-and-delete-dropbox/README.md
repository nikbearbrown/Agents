# receive schedule events and subtractfromdate date time and delete dropbox

Adapt the published “receive schedule events and subtractfromdate date time and delete dropbox” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["PURGE DAYS"]
  n2["DELETE OLD BACKUPS"]
  n3["GET WORKFLOWS"]
  n4["MAKE JSON FILES"]
  n5["UPLOAD WORKFLOWS"]
  n6["DESTINATION FOLDER"]
  n7["WAIT FOR MOVE TO FINISH"]
  n8["GET CURRENT BACKUPS"]
  n9["IGNORE FOLDERS"]
  n10["MOVE INTO OLD FOLDER"]
  n11["LIST OLD BACKUPS"]
  n12["CHECK DATES"]
  n13["GET CURRENT DATE"]
  n1 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 1"| n7
  n6 -->|"main out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n3
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
