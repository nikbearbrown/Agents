# AutoClip – Automatically Generate Video Clips and Upload to YouTube

Adapt the published “AutoClip – Automatically Generate Video Clips and Upload to YouTube” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Start AutoClip Workflow"]
  n1["Retrieve Video Background Data"]
  n2["Retrieve Quote Data"]
  n3["List Video Background Files"]
  n4["Configure Music Background Folder ID"]
  n5["List Music Background Files"]
  n6["Retrieve Music Background Data"]
  n7["Merge File Selection Data"]
  n8["Select Random Video, Music #38; Quote"]
  n9["Download Selected Video Background"]
  n10["Download Selected Music Background"]
  n11["Save Video Background Locally"]
  n12["Save Music Background Locally"]
  n13["Prepare Overlay Text #40;Quote #38; Author#41;"]
  n14["Generate Final Video Clip"]
  n15["Initiate YouTube Resumable Upload"]
  n16["Read output file"]
  n17["Upload Video to YouTube"]
  n18["Update Quote Upload Status"]
  n19["Mark Background as Used"]
  n16 -->|"main out 0 to in 0"| n17
  n2 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n4
  n17 -->|"main out 0 to in 0"| n18
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n8
  n18 -->|"main out 0 to in 0"| n19
  n5 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 2"| n7
  n1 -->|"main out 0 to in 1"| n7
  n15 -->|"main out 0 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 0 to in 0"| n5
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
