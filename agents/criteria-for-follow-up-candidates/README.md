# 💡Criteria For Follow Up Candidates

Adapt the published “💡Criteria For Follow Up Candidates” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Twilio Trigger"]
  n1["OpenAI Chat Model1"]
  n2["Find Follow-Up Candidates"]
  n3["Send Follow Up Message"]
  n4["Update Follow-Up Count and Date"]
  n5["Create/Update Session"]
  n6["Get Existing Chat Session"]
  n7["Every 24hrs"]
  n8["Send Reply"]
  n9["Send Confirmation"]
  n10["User Request STOP"]
  n11["Check For Command Words"]
  n12["Structured Output Parser"]
  n13["Auto-fixing Output Parser"]
  n14["OpenAI Chat Model2"]
  n15["Generate Follow Up Message"]
  n16["OpenAI Chat Model3"]
  n17["Get Availability"]
  n18["Get Existing Booking"]
  n19["Find Existing Booking"]
  n20["Reschedule Booking"]
  n21["Cancel Booking"]
  n22["Create a Booking"]
  n23["Appointment Scheduling Agent1"]
  n7 -->|"main out 0 to in 0"| n2
  n21 -->|"ai_tool out 0 to in 0"| n23
  n0 -->|"main out 0 to in 0"| n11
  n22 -->|"ai_tool out 0 to in 0"| n23
  n17 -->|"ai_tool out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n9
  n1 -->|"ai_languageModel out 0 to in 0"| n15
  n14 -->|"ai_languageModel out 0 to in 0"| n13
  n16 -->|"ai_languageModel out 0 to in 0"| n23
  n20 -->|"ai_tool out 0 to in 0"| n23
  n18 -->|"ai_tool out 0 to in 0"| n23
  n5 -->|"main out 0 to in 0"| n8
  n19 -->|"ai_tool out 0 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 1 to in 0"| n6
  n12 -->|"ai_outputParser out 0 to in 0"| n13
  n13 -->|"ai_outputParser out 0 to in 0"| n23
  n2 -->|"main out 0 to in 0"| n15
  n6 -->|"main out 0 to in 0"| n23
  n15 -->|"main out 0 to in 0"| n4
  n23 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n3
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
