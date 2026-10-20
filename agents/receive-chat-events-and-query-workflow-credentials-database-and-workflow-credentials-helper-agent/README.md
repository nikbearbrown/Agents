# receive chat events and query workflow credentials database and workflow credentials helper agent

Adapt the published “receive chat events and query workflow credentials database and workflow credentials helper agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 9 executable nodes and 7 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Test workflow#34;"]
  n1["Map Workflows #38; Credentials"]
  n2["Save to Database"]
  n3["Chat Trigger"]
  n4["Query Workflow Credentials Database"]
  n5["OpenAI Chat Model"]
  n6["Window Buffer Memory"]
  n7["Workflow Credentials Helper Agent"]
  n8["n8n"]
  n8 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n7
  n5 -->|"ai_languageModel out 0 to in 0"| n7
  n6 -->|"ai_memory out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n8
  n4 -->|"ai_tool out 0 to in 0"| n7
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
