# My workflow 7

Adapt the published “My workflow 7” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook: Receive Transcript"]
  n1["Validate Input"]
  n2["DB: Insert earnings_call"]
  n3["Set Call Context"]
  n4["Process Section Response"]
  n5["DB: Insert transcript_section"]
  n6["Route by Section Type"]
  n7["Process Guidance Response"]
  n8["Process Risk Response"]
  n9["Process QA Response"]
  n10["DB: Insert guidance_signal"]
  n11["DB: Insert risk_admission"]
  n12["DB: Insert qa_pressure"]
  n13["DB: Log Agent Run"]
  n14["Fetch All Signals for Summary"]
  n15["Process Summary Response"]
  n16["DB: Insert call_summary"]
  n17["DB: Mark Call Complete"]
  n18["Final Response"]
  n19["Webhook Response"]
  n20["Groq: Generate Call Summary"]
  n21["Groq: Parse Transcript Sections"]
  n22["Groq: Extract Guidance Signals"]
  n23["Groq: Extract Risk Admissions"]
  n24["Groq: Map QA Pressure"]
  n25["Execute a SQL query"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n21
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n22
  n6 -->|"main out 0 to in 0"| n23
  n6 -->|"main out 1 to in 0"| n24
  n6 -->|"main out 2 to in 0"| n23
  n6 -->|"main out 2 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 0 to in 0"| n15
  n21 -->|"main out 0 to in 0"| n4
  n22 -->|"main out 0 to in 0"| n7
  n23 -->|"main out 0 to in 0"| n8
  n24 -->|"main out 0 to in 0"| n9
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
