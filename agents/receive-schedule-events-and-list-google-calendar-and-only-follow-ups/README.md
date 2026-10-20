# receive schedule events and list google calendar and only follow ups

Adapt the published “receive schedule events and list google calendar and only follow ups” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Get Past Events"]
  n2["Loop Over Items"]
  n3["Flag to Follow Up"]
  n4["Only Follow Ups"]
  n5["Get Emails Since"]
  n6["Output"]
  n7["Availability"]
  n8["Model"]
  n9["Meeting Availability Agent"]
  n10["Generate Message"]
  n11["Meetings"]
  n12["Model1"]
  n13["Meeting Booking Agent"]
  n14["Mark as Seen"]
  n15["Send for Human Approval"]
  n8 -->|"ai_languageModel out 0 to in 0"| n9
  n12 -->|"ai_languageModel out 0 to in 0"| n13
  n6 -->|"ai_outputParser out 0 to in 0"| n9
  n11 -->|"ai_tool out 0 to in 0"| n13
  n7 -->|"ai_tool out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 1 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n10
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
