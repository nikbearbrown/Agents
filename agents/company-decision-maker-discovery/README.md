# 🏢 Company Decision Maker Discovery

Adapt the published “🏢 Company Decision Maker Discovery” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Google Sheets Trigger"]
  n1["Apollo Organization Enrichment"]
  n2["Create Apollo People Search URL"]
  n3["Loop Over Items #40;1000 per Batch#41;"]
  n4["Apollo Find Decision Makers"]
  n5["Add Contacts"]
  n6["Apollo Enrich Decision Makers"]
  n7["Create Apollo People Enrichment Payload"]
  n8["Enrich Contacts"]
  n9["Loop Over Items For Bulk Enrichment #40;10 per batch#41;"]
  n10["Determine Contact#39;s Department"]
  n11["Apollo Organization Search"]
  n12["Add Company Website"]
  n13["Approve Company Website"]
  n14["Add Company Details"]
  n15["Select Unprocessed Companies"]
  n16["Is Domain Already Provided#63;"]
  n17["Summarize Core Business"]
  n18["Split Out Batched Decision Maker Response"]
  n19["Split Out Batched Enrichment Response"]
  n20["Send Weekly Report"]
  n21["Retrieve Verified Leads"]
  n22["Derive Past Week#39;s Lead Gen. Metrics"]
  n23["Weekly Report Trigger"]
  n24["Merge Rows Which Now All Contain Domains"]
  n5 -->|"main out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n24
  n0 -->|"main out 0 to in 0"| n15
  n23 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n22
  n17 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n3
  n16 -->|"main out 0 to in 1"| n24
  n16 -->|"main out 1 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n18
  n3 -->|"main out 1 to in 0"| n2
  n22 -->|"main out 0 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n19
  n9 -->|"main out 1 to in 0"| n7
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
