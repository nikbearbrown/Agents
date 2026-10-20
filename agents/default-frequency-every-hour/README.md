# Default frequency: every hour

Adapt the published “Default frequency: every hour” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 12 executable nodes and 11 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get video details"]
  n1["Schedule Trigger"]
  n2["Filter out shorts"]
  n3["Get latest 15 videos of each channel"]
  n4["Get my subscriptions"]
  n5["Check for errors"]
  n6["Only keep channels with unwatched videos"]
  n7["Keep only videos published since last run"]
  n8["Send an email for each new video"]
  n9["If the HTTP request failed, throw the error"]
  n10["Split out subscriptions to process individually"]
  n11["Filter out channels"]
  n5 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 1 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n3
  n4 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n6
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
