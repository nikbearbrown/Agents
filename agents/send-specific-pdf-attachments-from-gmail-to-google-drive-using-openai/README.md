# Send specific PDF attachments from Gmail to Google Drive using OpenAI

Adapt the published “Send specific PDF attachments from Gmail to Google Drive using OpenAI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Read PDF"]
  n1["Configure"]
  n2["Is PDF"]
  n3["Not a PDF"]
  n4["Is matched"]
  n5["This is a matched PDF"]
  n6["This is not a matched PDF"]
  n7["Iterate over email attachments"]
  n8["OpenAI matches PDF textual content"]
  n9["Merge"]
  n10["Upload file to folder"]
  n11["On email received"]
  n12["Ignore large PDFs"]
  n13["Is text within token limit#63;"]
  n14["Has attachments#63;"]
  n15["There are no attachments"]
  n9 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 1 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n13
  n1 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 1 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 1 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 0 to in 1"| n9
  n13 -->|"main out 1 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n9
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
