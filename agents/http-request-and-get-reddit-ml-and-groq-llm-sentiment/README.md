# http request and get reddit ml and groq llm sentiment

Adapt the published “http request and get reddit ml and groq llm sentiment” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Process StackOverflow"]
  n1["Get StackOverflow"]
  n2["Manual Trigger"]
  n3["Combine All Data"]
  n4["Process Reddit ML"]
  n5["Get Reddit ML"]
  n6["Process GitHub"]
  n7["Get GitHub"]
  n8["Groq LLM Sentiment"]
  n9["Process Groq Sentiment"]
  n10["Groq Topic Classification"]
  n11["Topic Clustering Engine"]
  n12["Signal-to-Noise Filter"]
  n13["Social Sentiment Output"]
  n14["Enhanced Data Export"]
  n15["Prepare for Google Sheets"]
  n16["Store in Google Sheets"]
  n0 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n0
  n2 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 0 to in 0"| n6
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
