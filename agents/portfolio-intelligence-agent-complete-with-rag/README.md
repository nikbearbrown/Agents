# Portfolio Intelligence Agent - Complete with RAG

Adapt the published “Portfolio Intelligence Agent - Complete with RAG” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Manual Trigger"]
  n1["Schedule Trigger"]
  n2["Read Holdings File"]
  n3["Parse JSON Holdings"]
  n4["Calculate Portfolio Metrics"]
  n5["Read Previous Summaries"]
  n6["Fetch #38; Extract Stock Prices"]
  n7["Parse Summaries CSV"]
  n8["Calculate Daily Return"]
  n9["Read Knowledge Base1"]
  n10["Parse Knowledge Base CSV"]
  n11["Read Portfolio History CSV"]
  n12["Parse Portfolio History Data"]
  n13["Build Portfolio Analysis"]
  n14["RAG-Retrieve Context"]
  n15["Extract AI Summary"]
  n16["Split Out"]
  n17["Generate AI Summary #40;Groq#41;"]
  n18["Send a message"]
  n19["Append Portfolio History1"]
  n20["Convert Holdings to CSV"]
  n21["Convert Summary to CSV"]
  n22["Append Daily Summary"]
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n21
  n15 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n22
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
