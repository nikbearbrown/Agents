# Check if the song is present in the database

Adapt the published “Check if the song is present in the database” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get current date"]
  n1["Get last 10 liked tracks"]
  n2["Check if track is saved"]
  n3["Is not saved"]
  n4["Create song entry"]
  n5["Get all user playlist"]
  n6["Get monthly playlist"]
  n7["Get playlist in DB"]
  n8["Monthly playlist exist in Spotify #63;"]
  n9["Playlist exist in DB #63;"]
  n10["Create playlist in Spotify"]
  n11["Create playlist in DB1"]
  n12["Create playlist in DB"]
  n13["Merge"]
  n14["Clean op"]
  n15["Clean op2"]
  n16["Get this month playlist in DB"]
  n17["Get this month tracks in DB"]
  n18["Add song to the playlist"]
  n19["For each tracks in liked song"]
  n20["For each monthly tracks in DB"]
  n21["Get this month tracks in Spotify"]
  n22["Filter1"]
  n23["Song is not present in the playlist #63;"]
  n24["Clean op1"]
  n25["Schedule Trigger"]
  n26["End"]
  n13 -->|"main out 0 to in 0"| n16
  n22 -->|"main out 0 to in 0"| n23
  n14 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n19
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n25 -->|"main out 0 to in 0"| n0
  n4 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n9
  n6 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n14
  n5 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 1 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n24
  n1 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n26
  n20 -->|"main out 1 to in 0"| n21
  n19 -->|"main out 0 to in 1"| n13
  n19 -->|"main out 1 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n17
  n21 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 1 to in 0"| n10
  n23 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 1 to in 0"| n24
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
