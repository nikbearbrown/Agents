# get last execution timestamp and set new last execution timestamp and get zendesk comments for tickets

Adapt the published “get last execution timestamp and set new last execution timestamp and get zendesk comments for tickets” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["NoOp"]
  n1["Get last execution timestamp"]
  n2["Set new last execution timestamp"]
  n3["Pipedrive person Id found"]
  n4["NoOp1"]
  n5["Get Zendesk comments for tickets"]
  n6["Add comments to tickets"]
  n7["Add Pipedrive person Id to Zendesk tickets"]
  n8["Get tickets updated after last execution"]
  n9["Channel is email"]
  n10["Rename fields and keep only needed fields"]
  n11["Search persons by email"]
  n12["Remove duplicates to make search efficient"]
  n13["Set search email"]
  n14["Process commenst per ticket"]
  n15["New comment"]
  n16["Split comments to seperate items"]
  n17["Add comment as a note in Pipedrive"]
  n18["NoOp2"]
  n19["Every day at 09:00"]
  n20["Done processing"]
  n15 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 1 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 1 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 1 to in 0"| n0
  n13 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 1 to in 0"| n4
  n14 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 1"| n6
  n16 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n20
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 1"| n7
  n7 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n11
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
