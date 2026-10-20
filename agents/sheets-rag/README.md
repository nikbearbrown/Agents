# SHEETS RAG

Adapt the published “SHEETS RAG” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["create table query"]
  n1["create insertion query"]
  n2["Google Drive Trigger"]
  n3["execute_query_tool"]
  n4["Google Gemini Chat Model"]
  n5["get_postgres_schema"]
  n6["change_this"]
  n7["is not in database"]
  n8["table exists#63;"]
  n9["fetch sheet data"]
  n10["remove table"]
  n11["create table"]
  n12["perform insertion"]
  n13["Execute Workflow Trigger"]
  n14["When chat message received"]
  n15["response output"]
  n16["sql query executor"]
  n17["schema finder"]
  n18["schema to string"]
  n19["AI Agent With SQL Query Prompt"]
  n6 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n11
  n3 -->|"ai_tool out 0 to in 0"| n19
  n7 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 1 to in 0"| n10
  n16 -->|"main out 0 to in 0"| n15
  n5 -->|"ai_tool out 0 to in 0"| n19
  n2 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n17
  n4 -->|"ai_languageModel out 0 to in 0"| n19
  n14 -->|"main out 0 to in 0"| n19
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
