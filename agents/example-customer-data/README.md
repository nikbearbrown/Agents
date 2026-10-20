# Example Customer Data

Adapt the published “Example Customer Data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 12 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Scheduled Start: Daily Churn Check"]
  n1["Fetch Customer Data from Sheet"]
  n2["Filter High Churn Risk #38; No Campaign Customers"]
  n3["Check if Eligible Customers Found"]
  n4["Process Each Eligible Customer"]
  n5["Generate Win-Back Offer"]
  n6["#40;LLM Model for Offer Generation#41;"]
  n7["#40;Parse Offer JSON#41;"]
  n8["Log Sent Offer in System Log"]
  n9["Send Win-Back Offer via Email"]
  n10["Set #39;Not Found#39; Status"]
  n11["Log #39;Not Found#39; in System Log"]
  n7 -->|"ai_outputParser out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n2
  n4 -->|"main out 1 to in 0"| n5
  n6 -->|"ai_languageModel out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 1 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n1
  n2 -->|"main out 0 to in 0"| n3
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
