# 📬 You will receive one email for every company in your calendar. These emails will look something like this:

Adapt the published “📬 You will receive one email for every company in your calendar. These emails will look something like this:” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Setup"]
  n1["Every morning #64; 7"]
  n2["Get meetings for today"]
  n3["Get attendees email domains"]
  n4["Split Out"]
  n5["Get recent LinkedIn posts"]
  n6["Enrich attendee company"]
  n7["Gmail"]
  n8["Combine all activity for a company"]
  n9["Extract data for email"]
  n10["Prepare email template"]
  n11["Keep only ones with the domain"]
  n12["Extract important data"]
  n13["Extract important data again"]
  n14["Ask AI to summerize"]
  n15["Switch"]
  n16["Wrap everything together"]
  n17["Get latest tweets"]
  n0 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 1 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 1"| n16
  n12 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n10
  n5 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 1"| n8
  n11 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n9
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
