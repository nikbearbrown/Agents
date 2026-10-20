# LINE Assistant with Google Calendar and Gmail Integration

Adapt the published “LINE Assistant with Google Calendar and Gmail Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["Window Buffer Memory"]
  n2["OpenAI Chat Model"]
  n3["Wikipedia"]
  n4["OpenAI"]
  n5["Switch Between Text and Others"]
  n6["Line Receiving"]
  n7["Error Handling from AI Response"]
  n8["Text Cleansing"]
  n9["Line Answering #40;Error Case#41;"]
  n10["Line Answering #40;Ordinary Case#41;"]
  n11["Google Calendar Create"]
  n12["Google Calendar Read"]
  n13["Gmail Read"]
  n4 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n4
  n3 -->|"ai_tool out 0 to in 0"| n0
  n13 -->|"ai_tool out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 0"| n10
  n2 -->|"ai_languageModel out 0 to in 0"| n0
  n12 -->|"ai_tool out 0 to in 0"| n0
  n1 -->|"ai_memory out 0 to in 0"| n0
  n11 -->|"ai_tool out 0 to in 0"| n0
  n5 -->|"main out 0 to in 0"| n0
  n5 -->|"main out 1 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 1 to in 0"| n9
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
