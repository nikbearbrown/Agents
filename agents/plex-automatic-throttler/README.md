# Plex Automatic Throttler

Adapt the published “Plex Automatic Throttler” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["Switch"]
  n2["Resume"]
  n3["Check if Local"]
  n4["Play"]
  n5["Don#39;t Do Anything"]
  n6["Pause"]
  n7["Stop"]
  n8["Get QB Cookie"]
  n9["Get QB Cookie1"]
  n10["Global Variables"]
  n11["Check Throttle State"]
  n12["Check if Throttled"]
  n13["Do Nothing"]
  n14["Check Throttle State2"]
  n15["Check if Throttled1"]
  n16["Do Nothing1"]
  n17["Throttle Connection"]
  n18["Resume Downloads"]
  n19["Disable Throttle"]
  n20["Enable Throttle"]
  n4 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n17
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 1 to in 0"| n4
  n1 -->|"main out 2 to in 0"| n6
  n1 -->|"main out 3 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n11
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 1 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 0 to in 0"| n3
  n18 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 1 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 1 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n15
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
