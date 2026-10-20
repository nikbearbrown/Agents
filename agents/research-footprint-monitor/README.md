# Mycroft Agent 5 — Research Footprint Monitor

Adapt the published “Mycroft Agent 5 — Research Footprint Monitor” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 43 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Cron Trigger"]
  n1["Manual Pipeline Webhook"]
  n2["Fetch Watchlist"]
  n3["Scholar: NVIDIA"]
  n4["Scholar: AMD"]
  n5["Scholar: Intel"]
  n6["Scholar: Google"]
  n7["Scholar: Apple"]
  n8["Scholar: Microsoft"]
  n9["Scholar: Meta"]
  n10["Merge Scholar Results"]
  n11["Parse Scholar Data"]
  n12["Wikipedia: NVIDIA"]
  n13["Wikipedia: AMD"]
  n14["Wikipedia: Intel"]
  n15["Wikipedia: Google"]
  n16["Wikipedia: Apple"]
  n17["Wikipedia: Microsoft"]
  n18["Wikipedia: Meta"]
  n19["Merge Wikipedia Results"]
  n20["Parse Wikipedia Data"]
  n21["Combine Signals"]
  n22["Calculate Footprint Scores"]
  n23["Aggregate for Groq"]
  n24["Groq: Footprint Analyst"]
  n25["Parse Groq Response"]
  n26["Signal Assembler"]
  n27["Upsert to Supabase"]
  n28["Generate Report"]
  n29["Store Report in Supabase"]
  n30["Pipeline Response"]
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n17
  n2 -->|"main out 0 to in 0"| n18
  n3 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 1"| n10
  n5 -->|"main out 0 to in 2"| n10
  n6 -->|"main out 0 to in 3"| n10
  n7 -->|"main out 0 to in 4"| n10
  n8 -->|"main out 0 to in 5"| n10
  n9 -->|"main out 0 to in 6"| n10
  n10 -->|"main out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n19
  n13 -->|"main out 0 to in 1"| n19
  n14 -->|"main out 0 to in 2"| n19
  n15 -->|"main out 0 to in 3"| n19
  n16 -->|"main out 0 to in 4"| n19
  n17 -->|"main out 0 to in 5"| n19
  n18 -->|"main out 0 to in 6"| n19
  n19 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 1"| n21
  n21 -->|"main out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n26
  n26 -->|"main out 0 to in 0"| n27
  n27 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n29
  n29 -->|"main out 0 to in 0"| n30
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
