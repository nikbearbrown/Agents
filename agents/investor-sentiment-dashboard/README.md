# Retail Investor Anxiety Index

Adapt the published “Retail Investor Anxiety Index” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 36 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Manual Run Trigger"]
  n2["Fetch WSB"]
  n3["Fetch Investing"]
  n4["Fetch Stocks"]
  n5["Merge Reddit Feeds"]
  n6["1A: Raw Merge #38; Structural Clean"]
  n7["1B: Linguistic #38; Relevance Filter"]
  n8["Keyword Pre-Scorer"]
  n9["Aggregate for Claude"]
  n10["Claude 1: Anxiety Score"]
  n11["Claude 2: Narrative Velocity"]
  n12["Claude 3: Herd Detection"]
  n13["Claude 4: Conviction vs Uncertainty"]
  n14["Claude 5: Crowd Cycle Stage"]
  n15["Anthropic Model 1"]
  n16["Anthropic Model 2"]
  n17["Anthropic Model 3"]
  n18["Anthropic Model 4"]
  n19["Anthropic Model 5"]
  n20["Merge Claude Outputs"]
  n21["Signal Aggregator"]
  n22["Persist to File"]
  n23["Generate Quickchart URLs"]
  n24["Write output.json"]
  n25["Insert to Supabase"]
  n26["Pipeline Response"]
  n27["Dashboard Webhook"]
  n28["Build Dashboard Response"]
  n29["Serve Dashboard HTML"]
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 1"| n5
  n4 -->|"main out 0 to in 2"| n5
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 0 to in 0"| n20
  n11 -->|"main out 0 to in 1"| n20
  n12 -->|"main out 0 to in 2"| n20
  n13 -->|"main out 0 to in 3"| n20
  n14 -->|"main out 0 to in 4"| n20
  n20 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n26
  n15 -->|"ai_languageModel out 0 to in 0"| n10
  n16 -->|"ai_languageModel out 0 to in 0"| n11
  n17 -->|"ai_languageModel out 0 to in 0"| n12
  n18 -->|"ai_languageModel out 0 to in 0"| n13
  n19 -->|"ai_languageModel out 0 to in 0"| n14
  n27 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n29
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
