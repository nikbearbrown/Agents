# Loop over calls for analysis and Create Parent

Adapt the published “Loop over calls for analysis and Create Parent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Loop to next call"]
  n1["Execute Workflow Trigger"]
  n2["Create Notion DB Page"]
  n3["Post Slack Receipt"]
  n4["AI Team Processor"]
  n5["Update Slack Progress"]
  n6["Merge call data and parent notion id"]
  n7["Reduce down to 1 object"]
  n8["Get all older Calls"]
  n9["Isolate Only Call IDs"]
  n10["Only Process New Calls"]
  n11["Reduce down to One object"]
  n12["Bundle Slack Message Data"]
  n13["Merge Slack and Call Data"]
  n14["Loop Over Calls"]
  n15["Bundle Notion Parent Object Data"]
  n16["Bundle Processed Calls"]
  n17["Post Completed Calls Message"]
  n14 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 1 to in 0"| n6
  n14 -->|"main out 1 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 1"| n10
  n5 -->|"main out 0 to in 0"| n0
  n16 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 1"| n13
  n7 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 1"| n6
  n6 -->|"main out 0 to in 0"| n4
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
