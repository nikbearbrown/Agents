# Sub-Agent for scheduling calendar events

Adapt the published “Sub-Agent for scheduling calendar events” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model2"]
  n1["Respond to Webhook"]
  n2["calendarAgent"]
  n3["When chat message received"]
  n4["taskAgent"]
  n5["Window Buffer Memory"]
  n6["Map Fields"]
  n7["Map Fields1"]
  n8["Exclude Previews from Speech"]
  n9["Main Agent"]
  n10["OpenAI Chat Model"]
  n11["HTTP Request"]
  n12["Settings"]
  n13["Format output"]
  n14["Notion Task Agent"]
  n15["Window Buffer Memory1"]
  n16["Get calendar availability"]
  n17["Book appointment"]
  n18["Google Calendar Agent"]
  n19["OpenAI Chat Model1"]
  n20["Settings1"]
  n21["Format output1"]
  n22["Window Buffer Memory2"]
  n23["Webhook"]
  n23 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n18
  n4 -->|"ai_tool out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n9
  n11 -->|"ai_tool out 0 to in 0"| n14
  n2 -->|"ai_tool out 0 to in 0"| n9
  n17 -->|"ai_tool out 0 to in 0"| n18
  n14 -->|"main out 0 to in 0"| n13
  n10 -->|"ai_languageModel out 0 to in 0"| n14
  n19 -->|"ai_languageModel out 0 to in 0"| n18
  n0 -->|"ai_languageModel out 0 to in 0"| n9
  n5 -->|"ai_memory out 0 to in 0"| n9
  n18 -->|"main out 0 to in 0"| n21
  n15 -->|"ai_memory out 0 to in 0"| n14
  n22 -->|"ai_memory out 0 to in 0"| n18
  n16 -->|"ai_tool out 0 to in 0"| n18
  n3 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n1
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
