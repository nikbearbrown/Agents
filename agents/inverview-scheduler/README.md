# Inverview Scheduler

Adapt the published “Inverview Scheduler” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model2"]
  n1["Window Buffer Memory2"]
  n2["OpenAI Chat Model4"]
  n3["Run Get Availability"]
  n4["check day names"]
  n5["Convert Output to JSON"]
  n6["Interview Scheduler"]
  n7["If Final Output"]
  n8["Respond for More Info"]
  n9["Parse to JSON"]
  n10["Set Meeting with Google"]
  n11["Final Response to User"]
  n12["Generate Interview Times"]
  n13["Check My Calendar"]
  n14["Split Events into 30 min blocks"]
  n15["Add Blocked Field"]
  n16["Generate 30 Minute Timeslots"]
  n17["Combine My Calendar with All Slots"]
  n18["Check if Calendar Blocked"]
  n19["Return string of all available times"]
  n20["Get Availability"]
  n21["When chat message received"]
  n9 -->|"ai_outputParser out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 1 to in 0"| n8
  n4 -->|"ai_tool out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n14
  n0 -->|"ai_languageModel out 0 to in 0"| n6
  n2 -->|"ai_languageModel out 0 to in 0"| n5
  n6 -->|"main out 0 to in 0"| n7
  n3 -->|"ai_tool out 0 to in 0"| n6
  n1 -->|"ai_memory out 0 to in 0"| n6
  n5 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 1"| n17
  n14 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n18
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
