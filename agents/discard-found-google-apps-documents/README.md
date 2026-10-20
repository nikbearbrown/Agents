# Discard found Google Apps documents

Adapt the published “Discard found Google Apps documents” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Config"]
  n1["Edit Fields"]
  n2["Filter"]
  n3["Deduplicate Keep First"]
  n4["Deduplicate Keep Last"]
  n5["Send Duplicates to Trash"]
  n6["No Operation, do nothing"]
  n7["Is Flagged"]
  n8["Google Drive Trigger"]
  n9["Drop Google Apps files"]
  n10["Working Folder"]
  n11["Google Drive"]
  n12["Keep First/Last"]
  n13["Trash/Flag Duplicates"]
  n0 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 1 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 1 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n0
  n4 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 1 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n12
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
