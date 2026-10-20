# subscribe subscriber klicktipp and split out guest bookings and split out guest cancellations

Adapt the published “subscribe subscriber klicktipp and split out guest bookings and split out guest cancellations” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Subscribe invitee booking in KlickTipp"]
  n1["Subscribe guest booking in KlickTipp"]
  n2["Subscribe guest cancellation in KlickTipp"]
  n3["Subscribe invitee cancellation in KlickTipp"]
  n4["Split Out guest bookings"]
  n5["Split Out guest cancellations"]
  n6["Guests booking check"]
  n7["Subscribe invitee to empty guest addresses field"]
  n8["New Calendly event"]
  n9["Convert data for KlickTipp"]
  n10["Check event - booking or cancellation#63;"]
  n11["List guests for booking"]
  n12["List guests for cancellation"]
  n13["Guests cancellation check"]
  n14["Rescheduling check"]
  n15["Invitee did not add guests to the booking"]
  n16["Event was rescheduled"]
  n17["No guest email addresses found"]
  n8 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 1 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 1 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 1 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n10
  n12 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 1 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n13
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
