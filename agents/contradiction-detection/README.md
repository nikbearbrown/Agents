# Contradiction_detection_agent

Adapt the published “Contradiction_detection_agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Manual Trigger"]
  n1["Set Company Input"]
  n2["DB: Fetch Earnings Guidance Signals"]
  n3["DB: Fetch Risk Admissions"]
  n4["DB: Fetch QA Pressure Map"]
  n5["DB: Fetch News Signals"]
  n6["DB: Fetch Tech Stack Signals"]
  n7["Aggregate All Signals"]
  n8["Run Pattern Detection Engine"]
  n9["Build Groq Prompt"]
  n10["LLM Needed#63;"]
  n11["Groq: Analyse Contradictions"]
  n12["Process Groq Response"]
  n13["No-Flag Passthrough"]
  n14["DB: Insert Contradiction Report"]
  n15["Fan Out Flags"]
  n16["DB: Insert Contradiction Flag"]
  n17["Build Final Report"]
  n18["Execute a SQL query"]
  n19["Execute a SQL query1"]
  n20["Execute a SQL query2"]
  n21["Execute a SQL query3"]
  n22["HTTP Request"]
  n23["Process News Response"]
  n24["DB: Save News Signals"]
  n25["Merge"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n22
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 1"| n25
  n3 -->|"main out 0 to in 4"| n25
  n4 -->|"main out 0 to in 0"| n25
  n5 -->|"main out 0 to in 3"| n25
  n6 -->|"main out 0 to in 2"| n25
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n5
  n25 -->|"main out 0 to in 0"| n7
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
