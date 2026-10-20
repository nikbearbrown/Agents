# Standup Bot - Worker

Adapt the published “Standup Bot - Worker” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["publish report"]
  n1["get user data"]
  n2["open-standup-dialog#63;"]
  n3["Action from MM"]
  n4["Slash Cmd from MM"]
  n5["config#63;"]
  n6["open config dialog"]
  n7["Prep Config Dialog"]
  n8["callback ID#63;"]
  n9["standup-config"]
  n10["standup-answers"]
  n11["Prep Config Override"]
  n12["Override Config"]
  n13["Read Config 1"]
  n14["Read Config 2"]
  n15["confirm success"]
  n16["Read Config 3"]
  n17["Filter Due Standups"]
  n18["Prep Request Standup"]
  n19["Create Channel"]
  n20["Remind Users"]
  n21["Get User"]
  n22["Prep Reminder"]
  n23["Prep Standup Dialog"]
  n24["open standup dialog"]
  n25["Prep Report"]
  n26["Delete ReminderPost"]
  n27["Update Post"]
  n28["Every hour"]
  n5 -->|"main out 0 to in 0"| n13
  n21 -->|"main out 0 to in 0"| n19
  n28 -->|"main out 0 to in 0"| n16
  n25 -->|"main out 0 to in 0"| n0
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 1 to in 0"| n10
  n8 -->|"main out 3 to in 0"| n2
  n22 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n17
  n1 -->|"main out 0 to in 0"| n25
  n3 -->|"main out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n22
  n0 -->|"main out 0 to in 0"| n27
  n9 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n6
  n17 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 0 to in 0"| n24
  n11 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n23
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
