# Way 1 - We call the subworklow for each file in the specified folder

Adapt the published “Way 1 - We call the subworklow for each file in the specified folder” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["Dropbox - List watched folder"]
  n2["Switch File vs Folder"]
  n3["Switch File vs Folder1"]
  n4["NocoDB - Get know files to exclude"]
  n5["Merge - Keep only new items"]
  n6["Just a quick answer to Dropbox - webhook validation"]
  n7["Respond to Dropbox in less than 10sec"]
  n8["Dropbox get files"]
  n9["NocoDB - Add this file in the table"]
  n10["set_folder A"]
  n11["set_folder to watch B"]
  n12["Execute Workflow - what i want to do for this folder/file A"]
  n13["Execute Workflow - Something to do for new files"]
  n0 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 1 to in 0"| n6
  n10 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 1"| n5
  n9 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n11
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
