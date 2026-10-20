# Printify Automation - Update Title and Description - AlexK1919

Adapt the published “Printify Automation - Update Title and Description - AlexK1919” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Printify - Get Shops"]
  n2["Printify - Get Products"]
  n3["Split Out"]
  n4["Loop Over Items"]
  n5["Split - id, title, desc"]
  n6["Calculator"]
  n7["Wikipedia"]
  n8["Printify - Update Product"]
  n9["Brand Guidelines #43; Custom Instructions"]
  n10["Google Sheets Trigger"]
  n11["Printify - Get Shops1"]
  n12["GS - Add Product Option"]
  n13["Update Product Option"]
  n14["If1"]
  n15["Number of Options"]
  n16["Calculate Options"]
  n17["Remember Options"]
  n18["Generate Title and Desc"]
  n19["If"]
  n19 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n4
  n14 -->|"main out 1 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n4
  n7 -->|"ai_tool out 0 to in 0"| n18
  n6 -->|"ai_tool out 0 to in 0"| n18
  n4 -->|"main out 1 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n19
  n11 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 0 to in 0"| n17
  n12 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n1
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
