# Mycroft - Patent Intelligence System Enhanced

Adapt the published “Mycroft - Patent Intelligence System Enhanced” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Set Variables"]
  n1["Initialize Logging"]
  n2["Setup Github Repo"]
  n3["Log: Repo Cloned"]
  n4["Set Path Variables"]
  n5["Setup Environment and Output Directories"]
  n6["Log: Environment Setup"]
  n7["Extract Patents"]
  n8["Log: Patents Extracted"]
  n9["Check Extraction Success"]
  n10["Process Patents"]
  n11["Log: Processing Complete"]
  n12["Read Processed Data"]
  n13["Read Metrics"]
  n14["Log: Results Loaded"]
  n15["Send Report Email"]
  n16["Cleanup and Save Data"]
  n17["Log Completion"]
  n18["Error Notification"]
  n19["Log Error"]
  n20["Cleanup Repository Error"]
  n21["Webhook"]
  n22["Respond to Webhook"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 1 to in 0"| n18
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n20
  n21 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n22
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
