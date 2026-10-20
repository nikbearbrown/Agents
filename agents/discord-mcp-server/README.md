# Discord MCP Server

Adapt the published “Discord MCP Server” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 10 executable nodes and 9 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Send Discord Message to Channel"]
  n1["Add Role To Member"]
  n2["Remove Role from member"]
  n3["Discord MCP Server Trigger"]
  n4["Get channels of server by server ID"]
  n5["Get members of server by server ID"]
  n6["Send DM and Wait for reply"]
  n7["Send to Channel and Wait for Reply"]
  n8["Send DM to User"]
  n9["Get Discord Server IDs"]
  n8 -->|"ai_tool out 0 to in 0"| n3
  n1 -->|"ai_tool out 0 to in 0"| n3
  n9 -->|"ai_tool out 0 to in 0"| n3
  n2 -->|"ai_tool out 0 to in 0"| n3
  n6 -->|"ai_tool out 0 to in 0"| n3
  n0 -->|"ai_tool out 0 to in 0"| n3
  n5 -->|"ai_tool out 0 to in 0"| n3
  n7 -->|"ai_tool out 0 to in 0"| n3
  n4 -->|"ai_tool out 0 to in 0"| n3
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
