# Extract &amp; Summarize Indeed Company Info with Bright Data and Google Gemini

Adapt the published “Extract &amp; Summarize Indeed Company Info with Bright Data and Google Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Google Gemini Chat Model For Summarization"]
  n2["Set Indeed Search Query"]
  n3["Perform Indeed Web Request"]
  n4["Indeed Expert AI Agent"]
  n5["Google Gemini Chat Model"]
  n6["Markdown to Textual Data Extractor"]
  n7["Indeed Summarization"]
  n8["Convert Markdown to HTML"]
  n9["Initiate a Webhook Notification for Markdown to HTML Response"]
  n10["Google Gemini Chat Model for AI Agent"]
  n11["Initiate a Webhook Request"]
  n12["Initiate a Webhook Notification for Summarization"]
  n7 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n9
  n5 -->|"ai_languageModel out 0 to in 0"| n6
  n11 -->|"ai_tool out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n7
  n10 -->|"ai_languageModel out 0 to in 0"| n4
  n1 -->|"ai_languageModel out 0 to in 0"| n7
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
