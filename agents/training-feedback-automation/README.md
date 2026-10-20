# Training Feedback Automation

Adapt the published “Training Feedback Automation” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 12 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Airtable Trigger"]
  n1["Webhook - Action Task Poor"]
  n2["Switch1"]
  n3["LinkedIn"]
  n4["Poor - Send Email"]
  n5["Call Usertask - Create task"]
  n6["Call Usertask - Create Task - Pair and good"]
  n7["Send Email after WebHook"]
  n8["Call Usertask - Detail Task"]
  n9["Send Email - Information for marcketing"]
  n10["Switch"]
  n11["Call Usertask - Create Task - Dissatisfaction"]
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n6
  n10 -->|"main out 2 to in 0"| n6
  n10 -->|"main out 3 to in 0"| n3
  n10 -->|"main out 4 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 1 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n8
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
