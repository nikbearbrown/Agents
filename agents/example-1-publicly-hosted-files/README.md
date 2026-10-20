# Example 1. Publicly Hosted Files

Adapt the published “Example 1. Publicly Hosted Files” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Mistral Upload"]
  n1["When clicking #8216;Test workflow#8217;"]
  n2["Mistral Signed URL"]
  n3["Import PDF"]
  n4["Import Image"]
  n5["Mistral Upload1"]
  n6["Mistral Signed URL1"]
  n7["Mistral DOC OCR"]
  n8["Mistral IMAGE OCR"]
  n9["Document URL"]
  n10["Image URL"]
  n11["Mistral DOC OCR1"]
  n12["Mistral IMAGE OCR1"]
  n13["Document URL1"]
  n14["Document Understanding"]
  n15["Image URL1"]
  n16["Document Mis-Understanding#63;"]
  n10 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n16
  n3 -->|"main out 0 to in 0"| n0
  n9 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n10
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
