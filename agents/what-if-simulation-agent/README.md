# What-If Simulation Agent

Adapt the published “What-If Simulation Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["#127919; Webhook #8212; Receive Simulation Request"]
  n1["#128269; Parse #38; Validate Input"]
  n2["#128200; Sim 1 #8212; Growth vs Sentiment Tradeoff"]
  n3["#9878;#65039; Sim 2 #8212; Risk Appetite Simulator"]
  n4["#127919; Sim 3 #8212; Threshold Break Simulator"]
  n5["#129504; Aggregate #38; Score All Simulations"]
  n6["#129302; Groq #8212; Generate Investment Insights"]
  n7["#128260; Parse Groq Response"]
  n8["#128452;#65039; Prepare DB Record"]
  n9["#128190; Save to PostgreSQL"]
  n10["#128202; Build Final Response"]
  n11["#9989; Respond to Webhook"]
  n12["#128221; Build AI Prompt"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n6
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
