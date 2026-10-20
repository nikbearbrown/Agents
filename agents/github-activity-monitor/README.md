# GitHub Commit Velocity Tracker

Adapt the published “GitHub Commit Velocity Tracker” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Cron Trigger"]
  n1["Manual Pipeline Webhook"]
  n2["Fetch Watchlist"]
  n3["Fetch NVIDIA GitHub"]
  n4["Fetch AMD GitHub"]
  n5["Fetch Intel GitHub"]
  n6["Fetch Google GitHub"]
  n7["Fetch Apple GitHub"]
  n8["Fetch Microsoft GitHub"]
  n9["Fetch Meta GitHub"]
  n10["Merge GitHub Results"]
  n11["Parse #38; Calculate Velocity"]
  n12["Load Previous Run from Supabase"]
  n13["Calculate Week-over-Week Delta"]
  n14["Aggregate for Groq"]
  n15["Groq: Activity Classifier"]
  n16["Parse Groq Response"]
  n17["Signal Assembler"]
  n18["Upsert to Supabase"]
  n19["Generate Report"]
  n20["Store Report in Supabase"]
  n21["Pipeline Response"]
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n9
  n3 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 1"| n10
  n5 -->|"main out 0 to in 2"| n10
  n6 -->|"main out 0 to in 3"| n10
  n7 -->|"main out 0 to in 4"| n10
  n8 -->|"main out 0 to in 5"| n10
  n9 -->|"main out 0 to in 6"| n10
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n21
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
