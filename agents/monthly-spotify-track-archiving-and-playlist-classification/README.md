# Monthly Spotify Track Archiving and Playlist Classification

Adapt the published “Monthly Spotify Track Archiving and Playlist Classification” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 33 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Retrieve relevant info"]
  n1["Batch preparation"]
  n2["Get Track details"]
  n3["Split Out"]
  n4["Anthropic Chat Model"]
  n5["Get Playlist"]
  n6["Get Tracks"]
  n7["Structured Output Parser"]
  n8["Playlists informations"]
  n9["Filter my playlist"]
  n10["Split Out1"]
  n11["Batch preparation1"]
  n12["Merge"]
  n13["Simplify Tracks informations"]
  n14["Limit"]
  n15["Get logged tracks"]
  n16["Excluding logged tracks"]
  n17["Filter"]
  n18["Split Out2"]
  n19["Manual Verification"]
  n20["Spotify"]
  n21["Aggregate by 200 tracks"]
  n22["Monthly Trigger"]
  n23["Get logged playlists"]
  n24["Log new tracks"]
  n25["Log new playlists"]
  n26["Excluding logged playlists"]
  n27["Limit2"]
  n28["Classify new tracks"]
  n29["Basic LLM Chain - AI Classification"]
  n14 -->|"main out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n11
  n27 -->|"main out 0 to in 0"| n23
  n3 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n18
  n10 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 1"| n19
  n5 -->|"main out 0 to in 0"| n9
  n22 -->|"main out 0 to in 0"| n5
  n22 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n15 -->|"main out 0 to in 0"| n16
  n11 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n8
  n28 -->|"main out 0 to in 0"| n21
  n28 -->|"main out 0 to in 0"| n19
  n4 -->|"ai_languageModel out 0 to in 0"| n29
  n23 -->|"main out 0 to in 0"| n26
  n8 -->|"main out 0 to in 1"| n26
  n8 -->|"main out 0 to in 0"| n27
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 1"| n12
  n21 -->|"main out 0 to in 0"| n29
  n16 -->|"main out 0 to in 0"| n24
  n16 -->|"main out 0 to in 0"| n28
  n7 -->|"ai_outputParser out 0 to in 0"| n29
  n26 -->|"main out 0 to in 0"| n25
  n13 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 1"| n16
  n29 -->|"main out 0 to in 0"| n10
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
