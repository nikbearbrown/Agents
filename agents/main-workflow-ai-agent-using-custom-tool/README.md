# Main workflow: AI agent using custom tool

Adapt the published “Main workflow: AI agent using custom tool” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["OpenAI Chat Model1"]
  n2["Simple Memory"]
  n3["When Executed by Another Workflow"]
  n4["AI Agent"]
  n5["List columns tool"]
  n6["Get column values tool"]
  n7["Get customer tool"]
  n8["Set Google Sheet URL"]
  n9["Get Google sheet contents"]
  n10["Check operation"]
  n11["Get column names"]
  n12["Prepare column data"]
  n13["Filter"]
  n14["Prepare output"]
  n13 -->|"main out 0 to in 0"| n14
  n2 -->|"ai_memory out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n12
  n10 -->|"main out 2 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n14
  n7 -->|"ai_tool out 0 to in 0"| n4
  n5 -->|"ai_tool out 0 to in 0"| n4
  n1 -->|"ai_languageModel out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n9
  n6 -->|"ai_tool out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n8
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
