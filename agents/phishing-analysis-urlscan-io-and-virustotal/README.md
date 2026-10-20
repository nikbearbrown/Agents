# Phishing_analysis__URLScan_io_and_Virustotal_

Adapt the published “Phishing_analysis__URLScan_io_and_Virustotal_” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["sends slack message"]
  n2["Split In Batches"]
  n3["Mark as read"]
  n4["VirusTotal: Scan URL"]
  n5["VirusTotal: Get report"]
  n6["Schedule Trigger"]
  n7["Find indicators of compromise"]
  n8["URLScan: Get report"]
  n9["URLScan: Scan URL"]
  n10["Has URL#63;"]
  n11["No error#63;"]
  n12["Not empty#63;"]
  n13["Wait 1 Minute"]
  n14["Get all unread messages"]
  n15["Merge Reports"]
  n10 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 1 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 1 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n2
  n13 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 1 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 1"| n15
  n14 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n14
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
