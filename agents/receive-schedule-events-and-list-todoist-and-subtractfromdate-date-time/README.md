# receive schedule events and list todoist and subtractfromdate date time

Adapt the published “receive schedule events and list todoist and subtractfromdate date time” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["if after unsnooze date"]
  n1["at 5am"]
  n2["every 5 min"]
  n3["Get snoozed tasks"]
  n4["if task is not a subtask"]
  n5["If task has due date"]
  n6["Get date to unsnooze"]
  n7["Get inbox tasks to snooze"]
  n8["Set inbox project id"]
  n9["If not same project"]
  n10["Set args to move"]
  n11["Generate unique uuid for move"]
  n12["Merge all items into a list"]
  n13["Move the tasks"]
  n14["Set snoozed project id"]
  n1 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n11
  n3 -->|"main out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n0
  n5 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 1 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n12
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
