# NeurochainAI Basic API Integration

Adapt the published “NeurochainAI Basic API Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Code"]
  n2["HTTP Request3"]
  n3["Telegram2"]
  n4["Telegram1"]
  n5["Telegram4"]
  n6["Telegram3"]
  n7["Telegram5"]
  n8["Telegram6"]
  n9["Telegram7"]
  n10["NeurochainAI - REST API"]
  n11["TYPING - ACTION"]
  n12["AI Response"]
  n13["No response"]
  n14["Prompt too short"]
  n15["Switch2"]
  n16["Code1"]
  n17["Switch"]
  n18["NeurochainAI - Flux"]
  n19["Switch1"]
  n1 -->|"main out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n3
  n17 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 1 to in 0"| n11
  n17 -->|"main out 2 to in 0"| n11
  n19 -->|"main out 0 to in 0"| n8
  n19 -->|"main out 1 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 1 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n9
  n2 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n1
  n18 -->|"main out 1 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 1 to in 0"| n15
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
