# YouTube to X Post- AlexK1919

Adapt the published “YouTube to X Post- AlexK1919” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Post to X"]
  n1["Fetch Latest Videos"]
  n2["Calculator"]
  n3["Wikipedia"]
  n4["Check Every 2 Hours"]
  n5["Calculator2"]
  n6["GS - Add Tweet"]
  n7["GS - Update Tweet"]
  n8["When clicking #34;Test workflow#34;"]
  n9["Discord"]
  n10["Remove Duplicates"]
  n11["Generate X Post"]
  n12["Set Fields"]
  n13["Wikipedia1"]
  n14["Rewrite X Post to 220 Characters"]
  n15["Verify character limit constraints"]
  n16["Slack"]
  n17["Gmail"]
  n18["Set Final Fields"]
  n19["If Array is empty#63;"]
  n0 -->|"main out 0 to in 0"| n7
  n3 -->|"ai_tool out 0 to in 0"| n11
  n2 -->|"ai_tool out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n10
  n13 -->|"ai_tool out 0 to in 0"| n14
  n5 -->|"ai_tool out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n6
  n10 -->|"main out 0 to in 0"| n19
  n19 -->|"main out 1 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 1 to in 0"| n18
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
