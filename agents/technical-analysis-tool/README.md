# Technical Analysis Tool

Adapt the published “Technical Analysis Tool” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Window Buffer Memory"]
  n1["AI Agent"]
  n2["Structured Output Parser"]
  n3["GPT 4o"]
  n4["Generate HTML"]
  n5["Send Stock Analysis"]
  n6["Adjust HTML Colors"]
  n7["Think"]
  n8["Generate Variables For API"]
  n9["Set Variables"]
  n10["Get News Data"]
  n11["Analyse API Input"]
  n12["Workflow Input Trigger"]
  n13["Download Chart"]
  n14["Get Chart URL"]
  n15["Get Price History"]
  n16["Get Bollinger Bands"]
  n17["Get MACD"]
  n18["Merge"]
  n19["Calculate Support Resistance"]
  n20["Organizing Data"]
  n21["Merge-2"]
  n22["ChatGPT 4o"]
  n23["Set Variable"]
  n24["Warp as JSON for GPT"]
  n25["Set Final Response"]
  n26["Set Stock Symbol and API Key"]
  n27["First Technical Analysis"]
  n28["Schedule Trigger1"]
  n29["Technical Analysis Tool"]
  n30["Trends Analysis Tool"]
  n31["On form submission"]
  n32["Refine Text"]
  n18 -->|"main out 0 to in 0"| n20
  n7 -->|"ai_tool out 0 to in 0"| n1
  n3 -->|"ai_languageModel out 0 to in 0"| n1
  n21 -->|"main out 0 to in 0"| n24
  n1 -->|"main out 0 to in 0"| n32
  n17 -->|"main out 0 to in 2"| n18
  n22 -->|"main out 0 to in 0"| n25
  n32 -->|"main out 0 to in 0"| n4
  n23 -->|"main out 0 to in 0"| n21
  n4 -->|"main out 0 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n27
  n20 -->|"main out 0 to in 1"| n21
  n15 -->|"main out 0 to in 0"| n19
  n28 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n5
  n31 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 1"| n18
  n30 -->|"ai_tool out 0 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n22
  n0 -->|"ai_memory out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n26
  n29 -->|"ai_tool out 0 to in 0"| n1
  n27 -->|"main out 0 to in 0"| n23
  n2 -->|"ai_outputParser out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n9
  n19 -->|"main out 0 to in 0"| n18
  n26 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n15
  n26 -->|"main out 0 to in 0"| n16
  n26 -->|"main out 0 to in 0"| n17
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/zie619-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
