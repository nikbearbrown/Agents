# MCP_SUPABASE_AGENT

Adapt the published “MCP_SUPABASE_AGENT” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["MCP_SUPABASE"]
  n1["RAG"]
  n2["Embeddings OpenAI"]
  n3["DELETE_ROW_INSCRICOES_CURSOS"]
  n4["GET_ROW_AGENT_MESSAGE"]
  n5["CREATE_ROW_AGENT_MESSAGE"]
  n6["DELETE_ROW_AGENT_MESSAGE"]
  n7["UPDATE_ROW_AGENT_MESSAGE"]
  n8["GET_MANY_ROW_AGENT_MESSAGE"]
  n9["CREATE_ROW_AGENT_TASKS"]
  n10["GET_ROW_AGENT_TASKS"]
  n11["DELETE_ROW_AGENT_TASKS"]
  n12["UPDATE_ROW_AGENT_TASKS"]
  n13["GET_MANY_ROW_AGENT_TASKS"]
  n14["CREATE_ROW_AGENT_STATUS"]
  n15["GET_ROW_AGENT_STATUS"]
  n16["DELETE_ROW_AGENT_STATUS"]
  n17["UPDATE_ROW_AGENT_STATUS"]
  n18["GET_MANY_ROW_AGENT_STATUS"]
  n19["CREATE_ROW_AGENT_KNOWLEDGE"]
  n20["GET_ROW_AGENT_KNOWLEDGE"]
  n21["UPDATE_ROW_INSCRICOES_AGENT_KNOWLEDGE"]
  n22["GET_MANY_ROW_AGENT_KNOWLEDGE"]
  n1 -->|"ai_tool out 0 to in 0"| n0
  n2 -->|"ai_embedding out 0 to in 0"| n1
  n10 -->|"ai_tool out 0 to in 0"| n0
  n15 -->|"ai_tool out 0 to in 0"| n0
  n4 -->|"ai_tool out 0 to in 0"| n0
  n9 -->|"ai_tool out 0 to in 0"| n0
  n11 -->|"ai_tool out 0 to in 0"| n0
  n12 -->|"ai_tool out 0 to in 0"| n0
  n14 -->|"ai_tool out 0 to in 0"| n0
  n16 -->|"ai_tool out 0 to in 0"| n0
  n20 -->|"ai_tool out 0 to in 0"| n0
  n17 -->|"ai_tool out 0 to in 0"| n0
  n5 -->|"ai_tool out 0 to in 0"| n0
  n6 -->|"ai_tool out 0 to in 0"| n0
  n13 -->|"ai_tool out 0 to in 0"| n0
  n7 -->|"ai_tool out 0 to in 0"| n0
  n18 -->|"ai_tool out 0 to in 0"| n0
  n19 -->|"ai_tool out 0 to in 0"| n0
  n8 -->|"ai_tool out 0 to in 0"| n0
  n3 -->|"ai_tool out 0 to in 0"| n0
  n22 -->|"ai_tool out 0 to in 0"| n0
  n21 -->|"ai_tool out 0 to in 0"| n0
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
