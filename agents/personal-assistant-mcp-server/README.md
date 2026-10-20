# Personal Assistant MCP server

Adapt the published “Personal Assistant MCP server” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["Google Gemini Chat Model"]
  n2["Simple Memory"]
  n3["MCP Server Trigger"]
  n4["MCP Client"]
  n5["Create event"]
  n6["Update event"]
  n7["Draft email"]
  n8["Personal Assistant"]
  n9["Add new row"]
  n10["Find row"]
  n11["Update row"]
  n12["Find emails"]
  n13["Find single event"]
  n14["Find multiple events"]
  n10 -->|"ai_tool out 0 to in 0"| n3
  n4 -->|"ai_tool out 0 to in 0"| n8
  n11 -->|"ai_tool out 0 to in 0"| n3
  n9 -->|"ai_tool out 0 to in 0"| n3
  n7 -->|"ai_tool out 0 to in 0"| n3
  n12 -->|"ai_tool out 0 to in 0"| n3
  n5 -->|"ai_tool out 0 to in 0"| n3
  n6 -->|"ai_tool out 0 to in 0"| n3
  n2 -->|"ai_memory out 0 to in 0"| n8
  n13 -->|"ai_tool out 0 to in 0"| n3
  n14 -->|"ai_tool out 0 to in 0"| n3
  n1 -->|"ai_languageModel out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n8
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
