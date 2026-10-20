# Mycroft - SEC Filings Analysis Agent

Adapt the published “Mycroft - SEC Filings Analysis Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["If"]
  n1["Set Variables"]
  n2["Setup Github Repo"]
  n3["Set Path Variables"]
  n4["Setup Python Enviornment and Output Directories"]
  n5["Edgar_Fetcher"]
  n6["Validate Fetcher"]
  n7["Financial Analyzer"]
  n8["Narrative Parser"]
  n9["Error Handling"]
  n10["Cleanup"]
  n11["Webhook"]
  n12["Respond to Webhook"]
  n13["If1"]
  n14["Respond to Webhook1"]
  n15["Read/Write Files from Disk"]
  n16["Read/Write Files from Disk1"]
  n17["Parse Results"]
  n18["Parse Both Results"]
  n0 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 1 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n13
  n8 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 1 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n14
  n18 -->|"main out 0 to in 0"| n12
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
