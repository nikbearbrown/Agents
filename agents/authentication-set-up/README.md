# My workflow 2

Adapt the published “My workflow 2” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Token Request"]
  n1["Assign Credentials"]
  n2["Dartagnan Project list"]
  n3["Create email template"]
  n4["List Available Email Template Braze"]
  n5["Filtered Project Campaign"]
  n6["Filtering Dartagnan Campaigns"]
  n7["Split Out"]
  n8["Filtering Braze Email Template"]
  n9["Not existing In Braze"]
  n10["Existing In Braze"]
  n11["Dartagnan HTML #38; MEDIA To Update"]
  n12["Encode Content To Update"]
  n13["Dartagnan HTML #38; MEDIA Campagne to Create"]
  n14["Encode Content to Create"]
  n15["If campaign is modified recently"]
  n16["Filter Braze vs Dartagnan"]
  n17["Embed image in HTML"]
  n18["Embed image in HTML 1"]
  n19["Every 5 minutes start"]
  n20["Update existing email template in Braze"]
  n7 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n5
  n12 -->|"main out 0 to in 0"| n20
  n14 -->|"main out 0 to in 0"| n3
  n16 -->|"main out 0 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 0 to in 1"| n10
  n8 -->|"main out 0 to in 1"| n9
  n11 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n18
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
