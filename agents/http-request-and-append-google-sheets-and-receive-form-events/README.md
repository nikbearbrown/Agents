# http request and append google sheets and receive form events

Adapt the published “http request and append google sheets and receive form events” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 12 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Snapshot Progress"]
  n1["HTTP Request- Post API call to Bright Data"]
  n2["Wait - Polling Bright Data"]
  n3["If - Checking status of Snapshot - if data is ready or not"]
  n4["HTTP Request - Getting data from Bright Data"]
  n5["OpenAI Chat Model"]
  n6["Google Sheets - Adding All Reviews"]
  n7["On form submission - Amazon Reviews"]
  n8["Aggregating all reviews"]
  n9["Basic LLM Chain - Summary of Recent reviews"]
  n10["OpenAI- Generating image"]
  n11["Gmail - Sending creative to Media Buyers"]
  n5 -->|"ai_languageModel out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n2
  n3 -->|"main out 1 to in 0"| n4
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
