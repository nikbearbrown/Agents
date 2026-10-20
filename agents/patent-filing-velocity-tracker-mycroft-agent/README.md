# Patent Filing Velocity Tracker — Mycroft Agent

Adapt the published “Patent Filing Velocity Tracker — Mycroft Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 38 executable nodes and 46 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook Trigger"]
  n1["Security Gate"]
  n2["IF Authorized"]
  n3["Unauthorized Response"]
  n4["Fetch Previous Run"]
  n5["Fetch Patent Data"]
  n6["Merge Fetch Outputs"]
  n7["1A: Structural Clean"]
  n8["1B: Classify #43; Quality Weight"]
  n9["Patent Count Gate"]
  n10["Aggregate for Claude"]
  n11["Anthropic Model 1"]
  n12["Anthropic Model 2"]
  n13["Anthropic Model 3"]
  n14["Anthropic Model 4"]
  n15["Anthropic Model 5"]
  n16["Anthropic Model 6"]
  n17["Claude 1: Velocity Score"]
  n18["Claude 2: Concept Novelty"]
  n19["Claude 3: Inventor Network"]
  n20["Claude 4: Cross-Company Convergence"]
  n21["Claude 5: Strategic Intent"]
  n22["Claude 6: Breakthrough Detection"]
  n23["Merge Claude Outputs"]
  n24["Signal Aggregator"]
  n25["Insert to Supabase"]
  n26["Parse Insert #43; Build Errors"]
  n27["Write Error Log"]
  n28["Newsletter Gate"]
  n29["Log Newsletter Skipped"]
  n30["Anthropic Model Newsletter"]
  n31["Generate Newsletter"]
  n32["Fetch Subscribers"]
  n33["Send Email"]
  n34["Insert Newsletter Run"]
  n35["Mycroft Orchestration Emit"]
  n36["Converge Outputs"]
  n37["Webhook Response"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 1 to in 0"| n3
  n4 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 0 to in 1"| n6
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n18
  n10 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n21
  n10 -->|"main out 0 to in 0"| n22
  n11 -->|"ai_languageModel out 0 to in 0"| n17
  n12 -->|"ai_languageModel out 0 to in 0"| n18
  n13 -->|"ai_languageModel out 0 to in 0"| n19
  n14 -->|"ai_languageModel out 0 to in 0"| n20
  n15 -->|"ai_languageModel out 0 to in 0"| n21
  n16 -->|"ai_languageModel out 0 to in 0"| n22
  n30 -->|"ai_languageModel out 0 to in 0"| n31
  n17 -->|"main out 0 to in 0"| n23
  n18 -->|"main out 0 to in 1"| n23
  n19 -->|"main out 0 to in 2"| n23
  n20 -->|"main out 0 to in 3"| n23
  n21 -->|"main out 0 to in 4"| n23
  n22 -->|"main out 0 to in 5"| n23
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n24 -->|"main out 0 to in 0"| n28
  n24 -->|"main out 0 to in 0"| n35
  n25 -->|"main out 0 to in 0"| n26
  n26 -->|"main out 0 to in 0"| n27
  n26 -->|"main out 0 to in 0"| n36
  n28 -->|"main out 0 to in 0"| n31
  n28 -->|"main out 1 to in 0"| n29
  n29 -->|"main out 0 to in 1"| n36
  n31 -->|"main out 0 to in 0"| n32
  n32 -->|"main out 0 to in 0"| n33
  n33 -->|"main out 0 to in 0"| n34
  n34 -->|"main out 0 to in 1"| n36
  n35 -->|"main out 0 to in 2"| n36
  n36 -->|"main out 0 to in 0"| n37
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
