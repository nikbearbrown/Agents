# for each user id and slack and search slack

Adapt the published “for each user id and slack and search slack” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["For Each User ID..."]
  n1["Get User"]
  n2["Search for Invite Requests"]
  n3["Get Existing Invite EventID"]
  n4["Should Create Event#63;"]
  n5["Create Event"]
  n6["Get Invite Reactions"]
  n7["Get Invite Replies"]
  n8["Extract Invite Reactions"]
  n9["Get Old EventId"]
  n10["Add Attendee to Event"]
  n11["Get Event Details"]
  n12["Is Attending"]
  n13["Get User Email"]
  n14["Should Add Attendee#63;"]
  n15["Structured Output Parser"]
  n16["SerpAPI"]
  n17["OpenAI Chat Model"]
  n18["Wikipedia"]
  n19["Schedule Trigger"]
  n20["Reply Invite with EventId"]
  n21["Calendar Event Booking Agent"]
  n16 -->|"ai_tool out 0 to in 0"| n21
  n1 -->|"main out 0 to in 0"| n14
  n18 -->|"ai_tool out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n20
  n12 -->|"main out 0 to in 0"| n0
  n13 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n11
  n19 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n6
  n17 -->|"ai_languageModel out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n21
  n4 -->|"main out 1 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n12
  n15 -->|"ai_outputParser out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n4
  n21 -->|"main out 0 to in 0"| n5
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
