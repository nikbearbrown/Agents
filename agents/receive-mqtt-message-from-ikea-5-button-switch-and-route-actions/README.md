# Receive MQTT message from IKEA 5-button Switch, and route actions.

Adapt the published “Receive MQTT message from IKEA 5-button Switch, and route actions.” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Spotify Next"]
  n1["Spotify Resume"]
  n2["Spotify Pause"]
  n3["Spotify API - Volume up 5pct"]
  n4["Spotify API - Volume down 5pct"]
  n5["Spotify API - Get Available Devices"]
  n6["Extract Individual Devices"]
  n7["Select Device by Name to get device_id"]
  n8["Custom Function 1 - P1"]
  n9["Custom Function 2 - P2"]
  n10["Custom Function 1 - P3"]
  n11["Spotify API - Activate Target Playback Device"]
  n12["Route to Requested Function"]
  n13["Custom Function 2 - P1"]
  n14["Filter"]
  n15["Globals"]
  n16["Custom Function 2 - P3"]
  n17["Oops. How was this reached#63;"]
  n18["Spotify API - Get Device Status"]
  n19["Already playing on Target Device#63;"]
  n20["Is Playing#63;"]
  n21["Spotify Prev"]
  n22["MQTT Trigger - Remote Switch"]
  n23["Remote Action -#62; Function Router"]
  n14 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n23
  n20 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 1 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 1 to in 0"| n4
  n12 -->|"main out 2 to in 0"| n20
  n12 -->|"main out 3 to in 0"| n8
  n12 -->|"main out 4 to in 0"| n13
  n12 -->|"main out 5 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n19
  n23 -->|"main out 0 to in 0"| n21
  n23 -->|"main out 1 to in 0"| n0
  n23 -->|"main out 2 to in 0"| n18
  n23 -->|"main out 3 to in 0"| n18
  n23 -->|"main out 4 to in 0"| n18
  n23 -->|"main out 5 to in 0"| n18
  n23 -->|"main out 6 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 1 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
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
