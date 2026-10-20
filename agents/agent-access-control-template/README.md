# Agent Access Control Template

Adapt the published “Agent Access Control Template” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Simple Memory"]
  n1["OpenAI Chat Model"]
  n2["Check permissions"]
  n3["Telegram Trigger"]
  n4["Set input"]
  n5["Get user permissions"]
  n6["When Executed by Another Workflow"]
  n7["Settings"]
  n8["OpenAI Chat Model1"]
  n9["Simple Memory1"]
  n10["Check permissions1"]
  n11["list_granted_roles"]
  n12["list_allowed_tools"]
  n13["calculator"]
  n14["Wikipedia"]
  n15["get_coordinates"]
  n16["get_weather"]
  n17["weather_agent"]
  n18["Weather Agent"]
  n19["Unknown user"]
  n20["Reply: unknown user"]
  n21["Reply with results"]
  n22["Main Agent"]
  n7 -->|"main out 0 to in 0"| n18
  n4 -->|"main out 0 to in 0"| n22
  n14 -->|"ai_tool out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n21
  n13 -->|"ai_tool out 0 to in 0"| n2
  n16 -->|"ai_tool out 0 to in 0"| n10
  n19 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 1 to in 0"| n4
  n0 -->|"ai_memory out 0 to in 0"| n22
  n17 -->|"ai_tool out 0 to in 0"| n2
  n9 -->|"ai_memory out 0 to in 0"| n18
  n15 -->|"ai_tool out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n5
  n2 -->|"ai_tool out 0 to in 0"| n22
  n1 -->|"ai_languageModel out 0 to in 0"| n22
  n10 -->|"ai_tool out 0 to in 0"| n18
  n8 -->|"ai_languageModel out 0 to in 0"| n18
  n12 -->|"ai_tool out 0 to in 0"| n2
  n11 -->|"ai_tool out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n19
  n6 -->|"main out 0 to in 0"| n7
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
