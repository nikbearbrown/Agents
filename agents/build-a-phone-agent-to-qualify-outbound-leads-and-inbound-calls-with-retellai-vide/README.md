# Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide

Adapt the published “Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 11 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Detect new lead in Google Sheets"]
  n1["Send SMS reminder to call lead in 5 minutes"]
  n2["Wait 5 minutes before making call"]
  n3["Call new lead using RetellAI"]
  n4["Receive inbound call from RetellAI #40;webhook#41;"]
  n5["Check if phone number exists in Google Sheets"]
  n6["Send response to inbound webhook call"]
  n7["Receive post-call data from RetellAI #40;webhook#41;"]
  n8["Filter for analyzed calls only"]
  n9["Check if call was outbound"]
  n10["Update lead record in Google Sheets"]
  n11["Send call summary email"]
  n12["Generate call summary with OpenAI"]
  n13["Send confirmation email to lead"]
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 1 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
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
