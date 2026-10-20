# Automate Google Analytics Reporting - AlexK1919

Adapt the published “Automate Google Analytics Reporting - AlexK1919” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Get Page Engagement Stats for this week"]
  n2["Get Page Engagement Stats for prior week"]
  n3["Get Google Search Results for this week"]
  n4["Get Country views data for this week"]
  n5["Aggregate Data"]
  n6["Get Google Search Results for prior week"]
  n7["Get Country views data for prior week"]
  n8["Parse - Get Page Engagement This Week"]
  n9["Parse - Get Page Engagement Prior Week"]
  n10["Parse - Get Google Search This Week"]
  n11["Parse - Get Google Search Prior Week"]
  n12["Parse - Country Views This Week"]
  n13["Parse - Country Views Prior Week"]
  n14["Set urlStrings"]
  n15["Format Data"]
  n16["Input All"]
  n17["Email the Report"]
  n18["Schedule Trigger"]
  n16 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n17
  n5 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n13
  n8 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n9
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
