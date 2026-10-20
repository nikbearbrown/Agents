# Madison_Content_Agent_MVP copy 1

Adapt the published “Madison_Content_Agent_MVP copy 1” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["Convert to File"]
  n2["Prompt"]
  n3["Quality check"]
  n4["Generation"]
  n5["Convert to File1"]
  n6["Respond to Webhook1"]
  n7["Visual Concepts"]
  n8["Respond to Webhook"]
  n9["brand voice"]
  n10["Schedule Trigger"]
  n11["HTTP Request"]
  n12["Edit Fields"]
  n13["Convert to File4"]
  n14["Split Out"]
  n15["Convert to File5"]
  n16["Compute Engagement"]
  n17["Filter Flagged"]
  n18["Filter Unflagged"]
  n19["Scoring Logic"]
  n20["Filter"]
  n21["Filter1"]
  n22["Discord1"]
  n23["Discord2"]
  n24["Discord3"]
  n25["Discord4"]
  n0 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n24
  n2 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n25
  n7 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n22
  n16 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n13
  n19 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n8
  n25 -->|"main out 0 to in 0"| n6
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/humanitariansai-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
