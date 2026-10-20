# Sub-workflow: Return the capitals of fictional countries

Adapt the published “Sub-workflow: Return the capitals of fictional countries” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["OpenAI"]
  n2["Simple Memory"]
  n3["When Executed by Another Workflow"]
  n4["Tool to call the workflow below"]
  n5["Tool: Get current date and time"]
  n6["List countries#63;"]
  n7["Mapping data"]
  n8["Concatenate country names"]
  n9["Return country list"]
  n10["Mapping data1"]
  n11["Get the matching country#39;s details"]
  n12["Return specific capital"]
  n7 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 1"| n11
  n2 -->|"ai_memory out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 1 to in 0"| n11
  n6 -->|"main out 1 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n1
  n4 -->|"ai_tool out 0 to in 0"| n1
  n5 -->|"ai_tool out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n6
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
