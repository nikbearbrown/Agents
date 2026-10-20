# ↔️ Airtable Batch Processing

Adapt the published “↔️ Airtable Batch Processing” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 35 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["upsert"]
  n1["random data"]
  n2["When clicking #8216;Test workflow#8217;"]
  n3["Split Out"]
  n4["batch 10"]
  n5["Airtable Subprocess"]
  n6["Switch"]
  n7["insert"]
  n8["rate limit#63;"]
  n9["Wait 0.2s to prevent rate limits"]
  n10["retry request"]
  n11["rate limit#63;1"]
  n12["retry request1"]
  n13["rate limit#63;2"]
  n14["retry request2"]
  n15["Aggregate3"]
  n16["Edit Fields4"]
  n17["Aggregate2"]
  n18["Edit Fields2"]
  n19["Aggregate1"]
  n20["Edit Fields1"]
  n21["update"]
  n22["Airtable Batch"]
  n23["Set Fields"]
  n24["Aggregate"]
  n25["Wait 5s2"]
  n26["Wait 5s"]
  n27["Wait 5s1"]
  n28["return merged output"]
  n6 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 1 to in 0"| n20
  n6 -->|"main out 2 to in 0"| n18
  n7 -->|"main out 0 to in 0"| n11
  n21 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n8
  n26 -->|"main out 0 to in 1"| n10
  n27 -->|"main out 0 to in 1"| n12
  n25 -->|"main out 0 to in 1"| n14
  n4 -->|"main out 0 to in 0"| n28
  n4 -->|"main out 1 to in 0"| n6
  n24 -->|"main out 0 to in 0"| n22
  n3 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 0"| n0
  n19 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n7
  n17 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n21
  n15 -->|"main out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n24
  n8 -->|"main out 0 to in 0"| n26
  n8 -->|"main out 1 to in 0"| n9
  n20 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n27
  n11 -->|"main out 1 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n25
  n13 -->|"main out 1 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n1
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
