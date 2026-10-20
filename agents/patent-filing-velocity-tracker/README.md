# Patent Filing Velocity Tracker

Adapt the published “Patent Filing Velocity Tracker” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Manual Run Trigger"]
  n1["Dashboard Webhook"]
  n2["Fetch Patent Data"]
  n3["1A: Structural Clean"]
  n4["1B: Category Classifier #43; Velocity Pre-Scorer"]
  n5["Aggregate for Claude"]
  n6["Claude 1: Velocity Score"]
  n7["Claude 2: Concept Novelty"]
  n8["Claude 3: Inventor Network"]
  n9["Claude 4: Cross-Company Convergence"]
  n10["Claude 5: Strategic Intent"]
  n11["Anthropic Model 1"]
  n12["Anthropic Model 2"]
  n13["Anthropic Model 3"]
  n14["Anthropic Model 4"]
  n15["Anthropic Model 5"]
  n16["Merge Claude Outputs"]
  n17["Signal Aggregator"]
  n18["Insert to Supabase"]
  n19["Check Trigger Type"]
  n20["If Webhook"]
  n21["Pipeline Response"]
  n22["Build Dashboard HTML"]
  n23["Serve Dashboard HTML"]
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n22
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 1"| n16
  n8 -->|"main out 0 to in 2"| n16
  n9 -->|"main out 0 to in 3"| n16
  n10 -->|"main out 0 to in 4"| n16
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n21
  n22 -->|"main out 0 to in 0"| n23
  n11 -->|"ai_languageModel out 0 to in 0"| n6
  n12 -->|"ai_languageModel out 0 to in 0"| n7
  n13 -->|"ai_languageModel out 0 to in 0"| n8
  n14 -->|"ai_languageModel out 0 to in 0"| n9
  n15 -->|"ai_languageModel out 0 to in 0"| n10
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
