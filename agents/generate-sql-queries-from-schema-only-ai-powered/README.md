# Generate SQL queries from schema only - AI-powered

Adapt the published “Generate SQL queries from schema only - AI-powered” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Window Buffer Memory"]
  n2["No Operation, do nothing"]
  n3["List all tables in a database"]
  n4["Extract database schema"]
  n5["Add table name to output"]
  n6["Convert data to binary"]
  n7["Save file locally"]
  n8["Extract data from file"]
  n9["Chat Trigger"]
  n10["AI Agent"]
  n11["When clicking #34;Test workflow#34;"]
  n12["Combine schema data and chat input"]
  n13["Load the schema from the local file"]
  n14["Extract SQL query"]
  n15["Check if query exists"]
  n16["Format query results"]
  n17["Run SQL query"]
  n18["Prepare final output"]
  n19["Combine query result and chat answer"]
  n10 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n15
  n0 -->|"ai_languageModel out 0 to in 0"| n10
  n16 -->|"main out 0 to in 0"| n19
  n1 -->|"ai_memory out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 1"| n19
  n15 -->|"main out 1 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n8
  n19 -->|"main out 0 to in 0"| n18
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
