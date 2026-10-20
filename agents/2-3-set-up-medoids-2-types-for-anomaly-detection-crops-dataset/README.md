# &#91;2/3&#93; Set up medoids (2 types) for anomaly detection (crops dataset)

Adapt the published “&#91;2/3&#93; Set up medoids (2 types) for anomaly detection (crops dataset)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 26 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Total Points in Collection"]
  n2["Cluster Distance Matrix"]
  n3["Scipy Sparse Matrix"]
  n4["Set medoid id"]
  n5["Get Medoid Vector"]
  n6["Prepare for Searching Threshold"]
  n7["Searching Score"]
  n8["Threshold Score"]
  n9["Set medoid threshold score"]
  n10["Split Out1"]
  n11["Merge"]
  n12["Textual #40;visual#41; crop descriptions"]
  n13["Embed text"]
  n14["Get Medoid by Text"]
  n15["Set text medoid id"]
  n16["Prepare for Searching Threshold1"]
  n17["Threshold Score1"]
  n18["Searching Text Medoid Score"]
  n19["Medoids Variables"]
  n20["Text Medoids Variables"]
  n21["Qdrant cluster variables"]
  n22["Info About Crop Clusters"]
  n23["Crop Counts"]
  n24["Split Out"]
  n25["Set text medoid threshold score"]
  n11 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n2
  n24 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 0 to in 1"| n11
  n23 -->|"main out 0 to in 0"| n22
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 0"| n25
  n5 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n5
  n20 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n3
  n22 -->|"main out 0 to in 0"| n24
  n21 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n20
  n1 -->|"main out 0 to in 0"| n23
  n18 -->|"main out 0 to in 0"| n17
  n6 -->|"main out 0 to in 0"| n7
  n16 -->|"main out 0 to in 0"| n18
  n0 -->|"main out 0 to in 0"| n21
  n12 -->|"main out 0 to in 0"| n10
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
