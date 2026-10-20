# Match Spotify Tracks to YouTube Videos

Adapt the published “Match Spotify Tracks to YouTube Videos” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 45 executable nodes and 50 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get playlist snapshot"]
  n1["Get playlist snapshot1"]
  n2["If different snapshot"]
  n3["Get all musics"]
  n4["Update to_delete to true"]
  n5["Add music"]
  n6["Compare Datasets"]
  n7["Spotify"]
  n8["No Operation, do nothing"]
  n9["Get all musics not in youtube playlist"]
  n10["Every day at noon"]
  n11["Every day at noon #43; 1mn"]
  n12["Every hour"]
  n13["Wait 1 hour"]
  n14["variables"]
  n15["Search video"]
  n16["Get video duration"]
  n17["Loop Over Items"]
  n18["If video duration #126;#61; music duration"]
  n19["Add music to playlist"]
  n20["Add youtube id to row"]
  n21["Discord"]
  n22["Discord1"]
  n23["Set youtube id to NOTFOUND if no matching"]
  n24["Aggregate"]
  n25["If no result"]
  n26["data"]
  n27["variables2"]
  n28["variables1"]
  n29["Loop Over Items1"]
  n30["data1"]
  n31["Get playlist items"]
  n32["Playlist items to be deleted"]
  n33["Get all musics that should be in playlist"]
  n34["Remove Duplicates"]
  n35["Remove video from playlist"]
  n36["Check for deleted videos"]
  n37["Set youtube_video_id to null"]
  n38["Get all musics to be deleted"]
  n39["Delete music"]
  n40["Every day at midnight"]
  n41["variables3"]
  n42["Reset NOTFOUND id to NULL"]
  n43["variables4"]
  n44["Every month"]
  n26 -->|"main out 0 to in 0"| n29
  n30 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 0 to in 0"| n26
  n24 -->|"main out 0 to in 0"| n23
  n14 -->|"main out 0 to in 0"| n0
  n12 -->|"main out 0 to in 0"| n14
  n28 -->|"main out 0 to in 0"| n9
  n27 -->|"main out 0 to in 0"| n7
  n27 -->|"main out 0 to in 0"| n3
  n41 -->|"main out 0 to in 0"| n33
  n41 -->|"main out 0 to in 0"| n31
  n41 -->|"main out 0 to in 0"| n38
  n43 -->|"main out 0 to in 0"| n42
  n44 -->|"main out 0 to in 0"| n43
  n13 -->|"main out 0 to in 0"| n1
  n25 -->|"main out 0 to in 0"| n24
  n25 -->|"main out 1 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n25
  n3 -->|"main out 0 to in 1"| n6
  n17 -->|"main out 0 to in 0"| n24
  n17 -->|"main out 1 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n5
  n6 -->|"main out 3 to in 0"| n4
  n29 -->|"main out 1 to in 0"| n30
  n10 -->|"main out 0 to in 0"| n27
  n34 -->|"main out 0 to in 0"| n35
  n31 -->|"main out 0 to in 0"| n32
  n31 -->|"main out 0 to in 1"| n36
  n16 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n29
  n20 -->|"main out 0 to in 0"| n21
  n40 -->|"main out 0 to in 0"| n41
  n0 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n2
  n11 -->|"main out 0 to in 0"| n28
  n36 -->|"main out 0 to in 0"| n37
  n35 -->|"main out 0 to in 0"| n39
  n38 -->|"main out 0 to in 1"| n32
  n32 -->|"main out 2 to in 0"| n34
  n18 -->|"main out 0 to in 0"| n19
  n18 -->|"main out 1 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n26
  n33 -->|"main out 0 to in 0"| n36
  n23 -->|"main out 0 to in 0"| n29
  n23 -->|"main out 0 to in 0"| n22
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
