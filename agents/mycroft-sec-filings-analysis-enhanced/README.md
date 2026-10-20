# Mycroft - SEC_Filings_Analysis_Enhanced

Adapt the published “Mycroft - SEC_Filings_Analysis_Enhanced” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Set Variables"]
  n1["Initialize Logging"]
  n2["Setup Github Repo"]
  n3["Log: Repo Cloned"]
  n4["Set Path Variables"]
  n5["Setup Python Enviornment and Output Directories"]
  n6["Log: Python Setup"]
  n7["Edgar_Fetcher"]
  n8["Validate Fetcher"]
  n9["Log: Fetcher Complete"]
  n10["If"]
  n11["Financial Analyzer"]
  n12["Narrative Parser"]
  n13["Validate Financial Metrics"]
  n14["Validate Narrative Content"]
  n15["Log: Financial Complete"]
  n16["Log: Narrative Complete"]
  n17["Merge Results"]
  n18["Log: Merge Complete"]
  n19["Save to Database"]
  n20["Log: Saved"]
  n21["Cleanup Temp Directories"]
  n22["Log Completion"]
  n23["Error Handling"]
  n24["Log Error"]
  n25["Cleanup On Error"]
  n26["Webhook"]
  n27["Respond to Webhook"]
  n28["Code in JavaScript"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n0
  n22 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n27
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
