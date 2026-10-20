# YT AI News Playlist Creator/AI News Form Updater

Adapt the published “YT AI News Playlist Creator/AI News Form Updater” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Read Channel Names"]
  n1["Get Videos"]
  n2["Split Out"]
  n3["Create Playlist"]
  n4["Delete Old Playlist"]
  n5["YouTube"]
  n6["Filter Out Upcoming"]
  n7["Save Playlist ID"]
  n8["Google Sheets"]
  n9["Telegram"]
  n10["0715 Trigger"]
  n11["Get Channels"]
  n12["Update Google Sheet"]
  n13["When clicking #8216;Test workflow#8217;"]
  n14["Read Channel Names1"]
  n5 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n2
  n10 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n0
  n0 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n14
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
