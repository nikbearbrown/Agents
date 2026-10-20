# 🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting

Adapt the published “🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["stats_aggregate_creators"]
  n1["stats_aggregate_workflows"]
  n2["Global Variables"]
  n3["Parse Workflow Data"]
  n4["Parse Creators Data"]
  n5["Aggregate"]
  n6["gpt-4o-mini"]
  n7["When Executed by Another Workflow"]
  n8["Workflow Tool"]
  n9["creator-summary"]
  n10["Workflow Response"]
  n11["Save creator-summary.md"]
  n12["Creators Data"]
  n13["Workflows Data"]
  n14["Merge Creators #38; Workflows"]
  n15["Split Out Creators"]
  n16["Split Out Workflows"]
  n17["Sort By Top Weekly Creator Inserts"]
  n18["Sort By Top Weekly Workflow Inserts"]
  n19["Schedule Trigger"]
  n20["Take Top 10 Creators"]
  n21["Take Top 50 Workflows"]
  n22["Google Drive"]
  n23["Convert Markdown to HTML"]
  n24["n8n Creators Stats Agent"]
  n25["Google Gemini Chat Model"]
  n26["Create Top 10 Workflows List"]
  n27["Convert Top 10 Markdown to HTML"]
  n28["Gmail Creators #38; Workflows Report"]
  n29["Telegram Top 10 Workflows List"]
  n30["Gmail Top 10 Workflows List"]
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"ai_languageModel out 0 to in 0"| n24
  n12 -->|"main out 0 to in 0"| n14
  n8 -->|"ai_tool out 0 to in 0"| n24
  n13 -->|"main out 0 to in 1"| n14
  n9 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n24
  n15 -->|"main out 0 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n18
  n20 -->|"main out 0 to in 0"| n12
  n21 -->|"main out 0 to in 0"| n13
  n23 -->|"main out 0 to in 0"| n28
  n25 -->|"ai_languageModel out 0 to in 0"| n26
  n24 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n22
  n24 -->|"main out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n5
  n26 -->|"main out 0 to in 0"| n27
  n26 -->|"main out 0 to in 0"| n29
  n27 -->|"main out 0 to in 0"| n30
  n7 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n21
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
