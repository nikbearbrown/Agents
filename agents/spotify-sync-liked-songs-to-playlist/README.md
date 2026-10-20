# Spotify Sync Liked Songs to Playlist

Adapt the published “Spotify Sync Liked Songs to Playlist” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Start"]
  n1["Schedule Trigger"]
  n2["Sort first added to first item"]
  n3["Gotify Send deleted n from x"]
  n4["Loop delete old"]
  n5["Spotify delete old"]
  n6["Edit set Vars"]
  n7["Edit success to del"]
  n8["Filter Playlist x"]
  n9["Compare Datasets"]
  n10["count added"]
  n11["Loop add missing"]
  n12["Spotify add Missing to x"]
  n13["Edit snapshot to added"]
  n14["Cound deleted"]
  n15["Sort"]
  n16["Set pluri"]
  n17["Merge"]
  n18["Gotify"]
  n19["Edit set intern vars"]
  n20["END"]
  n21["Spotify get Liked Songs"]
  n22["Spotify get all playlists"]
  n23["Spotify get Tracks of X"]
  n15 -->|"main out 0 to in 1"| n9
  n17 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n23
  n16 -->|"main out 0 to in 1"| n17
  n10 -->|"main out 0 to in 0"| n18
  n14 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 1 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 1 to in 0"| n20
  n9 -->|"main out 2 to in 0"| n20
  n9 -->|"main out 3 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 1 to in 0"| n12
  n1 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n21
  n19 -->|"main out 0 to in 0"| n22
  n13 -->|"main out 0 to in 0"| n10
  n21 -->|"main out 0 to in 0"| n2
  n23 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n11
  n22 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n17
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
