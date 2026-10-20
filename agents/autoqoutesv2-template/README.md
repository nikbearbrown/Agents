# AutoQoutesV2_template

Adapt the published “AutoQoutesV2_template” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Generate Image"]
  n2["Get image"]
  n3["Update image background URL"]
  n4["Image-to-Video"]
  n5["Wait image 2 min"]
  n6["Wait video 5 min"]
  n7["Get Video"]
  n8["Generate Audio"]
  n9["Get data from Google Sheet"]
  n10["Update Sound background URL"]
  n11["Update video background URL"]
  n12["Upload Sound to Google Drive"]
  n13["Save Video Background Locally1"]
  n14["Get Binary Video Background"]
  n15["Save Music Background Locally1"]
  n16["Prepare Overlay Text #40;Quote #38; Author#41;1"]
  n17["Generate Final Video Clip1"]
  n18["Initiate YouTube Resumable Upload"]
  n19["Read output file"]
  n20["Upload Video to YouTube"]
  n21["Update Quote Upload Status"]
  n7 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n15
  n1 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n21
  n17 -->|"main out 0 to in 0"| n18
  n9 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n17
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
