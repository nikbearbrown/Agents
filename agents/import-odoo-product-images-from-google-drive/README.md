# Import Odoo Product Images from Google Drive

Adapt the published “Import Odoo Product Images from Google Drive” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Filter Images"]
  n1["Find Files"]
  n2["Decorate Images"]
  n3["Switch"]
  n4["Move Images"]
  n5["Schedule Trigger"]
  n6["Sum Images"]
  n7["Announce"]
  n8["Find Templates"]
  n9["Download Images Templates"]
  n10["Update Images Templates"]
  n11["Find Products"]
  n12["Download Images Products"]
  n13["Update Images Products"]
  n14["Convert Base64 Images Templates"]
  n15["Convert Base64 Images Products"]
  n16["Search Old Images"]
  n17["Drop Old Images"]
  n18["Click Manual"]
  n3 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 1 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n6
  n18 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n17
  n12 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n10
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
