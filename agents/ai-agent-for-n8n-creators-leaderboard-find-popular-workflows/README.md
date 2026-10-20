# 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows

Adapt the published “🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

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
  n5["Take Top 25 Creators"]
  n6["Aggregate"]
  n7["Filter By Creator Username"]
  n8["gpt-4o-mini"]
  n9["When Executed by Another Workflow"]
  n10["When chat message received"]
  n11["Workflow Tool"]
  n12["creator-summary"]
  n13["Workflow Response"]
  n14["n8n Creator Stats Agent"]
  n15["Save creator-summary.md"]
  n16["Summary Report"]
  n17["Ollama Chat Model"]
  n18["Creators Data"]
  n19["Workflows Data"]
  n20["Merge Creators #38; Workflows"]
  n21["Split Out Creators"]
  n22["Split Out Workflows"]
  n23["Sort By Top Weekly Creator Inserts"]
  n24["Sort By Top Weekly Workflow Inserts"]
  n25["Take Top 300 Workflows"]
  n26["Window Buffer Memory"]
  n6 -->|"main out 0 to in 0"| n13
  n8 -->|"ai_languageModel out 0 to in 0"| n14
  n18 -->|"main out 0 to in 0"| n20
  n11 -->|"ai_tool out 0 to in 0"| n14
  n19 -->|"main out 0 to in 1"| n20
  n12 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n1
  n21 -->|"main out 0 to in 0"| n23
  n4 -->|"main out 0 to in 0"| n21
  n3 -->|"main out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n24
  n5 -->|"main out 0 to in 0"| n18
  n26 -->|"ai_memory out 0 to in 0"| n14
  n25 -->|"main out 0 to in 0"| n19
  n14 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n2
  n23 -->|"main out 0 to in 0"| n5
  n24 -->|"main out 0 to in 0"| n25
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
