# Events Webhook Trigger

Adapt the published “Events Webhook Trigger” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Parse Webhook"]
  n1["Close Modal Popup"]
  n2["Idea Selector Modal"]
  n3["Route Message"]
  n4["Route Message1"]
  n5["Create Folder"]
  n6["Select Folder"]
  n7["Loop Over Items"]
  n8["Success Response"]
  n9["Check if uploaded successfully"]
  n10["move on to next"]
  n11["No Operation, do nothing"]
  n12["Aggregate"]
  n13["Route Action"]
  n14["Webhook"]
  n15["Failure Response"]
  n16["Respond to Slack Webhook - Success"]
  n17["Respond to Slack Webhook - No Action"]
  n18["Download File Binary"]
  n19["Upload to S3 Bucket"]
  n20["Post Image to Channel"]
  n21["Split Out Files"]
  n14 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 1 to in 0"| n17
  n3 -->|"main out 2 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 1 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 1 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n13
  n19 -->|"main out 0 to in 0"| n9
  n18 -->|"main out 0 to in 0"| n19
  n11 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n8
  n9 -->|"main out 1 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n4
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
