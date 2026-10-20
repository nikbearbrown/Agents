# Line Save File to Google Drive and Log File's URL

Adapt the published “Line Save File to Google Drive and Log File's URL” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get Config"]
  n1["Create Date Folder"]
  n2["Set Date Folder ID"]
  n3["Create File Type Folder"]
  n4["Upload File to Google Drive"]
  n5["Determine Folder Info"]
  n6["Search Date Folder"]
  n7["Merge Event and Config Data"]
  n8["Check Existing Date Folder"]
  n9["Check Existing File Type Folder"]
  n10["Merge Final Parent Folder Data"]
  n11["Search File Type Folder"]
  n12["Set File Type Folder ID"]
  n13["Configure Final Parent Folder ID"]
  n14["Process Event and Config Data"]
  n15["Get File Binary Content"]
  n16["Log File Details to Google Sheet"]
  n17["Check Reply Enabled Flag"]
  n18["Check if Store by Date is Enabled"]
  n19["Check if Store by File Type is Enabled"]
  n20["LINE Webhook Listener"]
  n21["Send LINE Reply Message"]
  n22["Validate File Type"]
  n0 -->|"main out 0 to in 1"| n7
  n1 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n10
  n22 -->|"main out 0 to in 0"| n4
  n5 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n0
  n3 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n22
  n11 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 1"| n10
  n17 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 1 to in 0"| n18
  n7 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 1 to in 0"| n19
  n13 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 1 to in 0"| n2
  n19 -->|"main out 0 to in 0"| n3
  n19 -->|"main out 1 to in 0"| n12
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
