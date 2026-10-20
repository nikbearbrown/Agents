# Media Narrative Tracker — Mycroft Agent 3 (Groq)

Adapt the published “Media Narrative Tracker — Mycroft Agent 3 (Groq)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Cron Trigger"]
  n1["Manual Pipeline Webhook"]
  n2["Fetch Watchlist"]
  n3["Fetch FT RSS"]
  n4["Fetch Reuters RSS"]
  n5["Fetch Seeking Alpha RSS"]
  n6["Fetch CNBC RSS"]
  n7["Fetch Yahoo Finance RSS"]
  n8["Parse #38; Clean Articles"]
  n9["Deduplicate Against Supabase"]
  n10["Aggregate for Groq"]
  n11["Groq 1: Core Claim Extractor"]
  n12["Groq 2: Information Age Scorer"]
  n13["Groq 3: Company Mention Extractor"]
  n14["Signal Assembler"]
  n15["Insert to Supabase"]
  n16["Generate Report"]
  n17["Store Report in Supabase"]
  n18["Pipeline Response"]
  n19["Merge"]
  n20["Merge1"]
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 1"| n19
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n20
  n12 -->|"main out 0 to in 1"| n20
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n13 -->|"main out 0 to in 2"| n20
  n5 -->|"main out 0 to in 2"| n19
  n19 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 3"| n19
  n7 -->|"main out 0 to in 4"| n19
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
