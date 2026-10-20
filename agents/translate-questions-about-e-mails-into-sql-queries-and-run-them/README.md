# Translate questions about e-mails into SQL queries and run them

Adapt the published “Translate questions about e-mails into SQL queries and run them” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Add table name to output"]
  n1["Convert data to binary"]
  n2["Save file locally"]
  n3["Extract data from file"]
  n4["Chat Trigger"]
  n5["When clicking #34;Test workflow#34;"]
  n6["Combine schema data and chat input"]
  n7["Load the schema from the local file"]
  n8["Extract SQL query"]
  n9["Check if query exists"]
  n10["Format query results"]
  n11["Combine query result and chat answer"]
  n12["List all columns in a table"]
  n13["List all tables in a database"]
  n14["Ollama Chat Model"]
  n15["Postgres"]
  n16["Add trailing semicolon"]
  n17["Check for trailing semicolon"]
  n18["WorkflowTrigger"]
  n19["If ran manually"]
  n20["If file exists or already retried generating it"]
  n21["AI Agent"]
  n22["Format empty output"]
  n21 -->|"main out 0 to in 0"| n8
  n15 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n7
  n19 -->|"main out 1 to in 0"| n7
  n18 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n17
  n14 -->|"ai_languageModel out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 1"| n11
  n9 -->|"main out 0 to in 0"| n15
  n9 -->|"main out 1 to in 0"| n22
  n16 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n1
  n12 -->|"main out 0 to in 0"| n0
  n17 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 1 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 0 to in 0"| n13
  n6 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n3
  n20 -->|"main out 1 to in 0"| n13
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
