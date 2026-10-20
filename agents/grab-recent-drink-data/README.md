# Grab recent drink data

Adapt the published “Grab recent drink data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["slack_action_payload"]
  n1["slack_action_drink_data"]
  n2["OpenAI"]
  n3["Schedule Trigger"]
  n4["Limit"]
  n5["Google Sheets - Get Target"]
  n6["Summarize"]
  n7["combine data"]
  n8["If"]
  n9["Wait"]
  n10["slack drink webhook"]
  n11["Slack send drink notification"]
  n12["Send to Slack with confirm"]
  n13["Edit Fields-Set progress"]
  n14["Google Sheets - log water value to sheet"]
  n15["Google Sheets - Get Today Water Log"]
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 1 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 1"| n7
  n2 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 0 to in 2"| n7
  n7 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n0
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n6
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
