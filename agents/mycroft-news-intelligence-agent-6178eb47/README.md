# Mycroft - News Intelligence Agent

Adapt the published “Mycroft - News Intelligence Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Company List"]
  n1["Build Query"]
  n2["Merge"]
  n3["normalizenewsapi"]
  n4["NewsApiKey"]
  n5["HTTP Request"]
  n6["XML"]
  n7["ProcessNewData"]
  n8["Edit Fields"]
  n9["HTTP Request1"]
  n10["RiskCalculator"]
  n11["Insert rows in a table"]
  n12["Alert Generator Code Node"]
  n13["Send email"]
  n14["DailyGeneratorCode"]
  n15["Webhook"]
  n16["Respond to Webhook"]
  n17["Set Variables"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n9
  n6 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 1"| n2
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n17
  n14 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n0
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
