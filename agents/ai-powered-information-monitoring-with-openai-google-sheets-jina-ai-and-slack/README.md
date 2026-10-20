# AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack

Adapt the published “AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Basic LLM Chain"]
  n2["Schedule Trigger"]
  n3["RSS Read"]
  n4["Relevance Classification for Topic Monitoring"]
  n5["Google Sheets - Get RSS Feed url followed"]
  n6["Slack1"]
  n7["Google Sheets - Get article monitored database"]
  n8["Code"]
  n9["No Operation, do nothing"]
  n10["If"]
  n11["Jina AI - Read URL"]
  n12["Set field - existing_url"]
  n13["OpenAI Chat Model1"]
  n14["Set fields - Not relevant articles"]
  n15["Google Sheets - Add relevant articles"]
  n16["Google Sheets - Add relevant article"]
  n17["Set Fields - Relevant Articles"]
  n10 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 1 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n17
  n2 -->|"main out 0 to in 0"| n7
  n0 -->|"ai_languageModel out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n1
  n13 -->|"ai_languageModel out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n3
  n4 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 1 to in 0"| n14
  n7 -->|"main out 0 to in 0"| n12
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
