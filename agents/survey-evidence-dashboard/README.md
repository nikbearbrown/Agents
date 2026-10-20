# My workflow 5

Adapt the published “My workflow 5” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Survey Data Webhook"]
  n1["Daily Survey Check"]
  n2["Validate Survey Data"]
  n3["Clean and Preprocess Data"]
  n4["Prepare Analysis Prompt"]
  n5["Prepare Segmentation Prompt"]
  n6["Aggregate and Enrich Results"]
  n7["Prepare Slack Notification"]
  n8["Send Slack Notification"]
  n9["HTTP Request"]
  n10["Extract from File"]
  n11["Message a model"]
  n12["Message a model1"]
  n13["Update Grafana Dashboards"]
  n14["Prepare Grafana Config"]
  n15["Code"]
  n16["Switch"]
  n17["Code1"]
  n18["Insert Sentiment Distribution"]
  n19["Insert NPS Score"]
  n20["Fetch UID"]
  n0 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n8
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 1 to in 0"| n19
  n17 -->|"main out 0 to in 0"| n2
  n18 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n14
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
