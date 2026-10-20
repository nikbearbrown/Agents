# Always Authenticate Your Server!

Adapt the published “Always Authenticate Your Server!” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When Executed by Another Workflow"]
  n1["Operation"]
  n2["Github MCP Server"]
  n3["Get Latest Issues"]
  n4["Add Issue Comment"]
  n5["Simplify Issues"]
  n6["Aggregate Results"]
  n7["Get Issue Comments"]
  n8["Get Comments"]
  n9["Simplify Comments"]
  n10["Aggregate Comments"]
  n11["Get Many Issues"]
  n12["Get Single Issue"]
  n13["Create Comment"]
  n14["Get Response"]
  n1 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 1 to in 0"| n12
  n1 -->|"main out 2 to in 0"| n13
  n8 -->|"main out 0 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n8
  n4 -->|"ai_tool out 0 to in 0"| n2
  n3 -->|"ai_tool out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n10
  n7 -->|"ai_tool out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n1
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
