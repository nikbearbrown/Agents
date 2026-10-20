# Indeed Company Data Scraper &amp; Summarization with Airtable, Bright Data and Google Gemini

Adapt the published “Indeed Company Data Scraper &amp; Summarization with Airtable, Bright Data and Google Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Google Gemini Chat Model For Summarization"]
  n2["Webhook HTTP Request"]
  n3["Perform Indeed Web Request"]
  n4["Indeed Expert AI Agent"]
  n5["Google Gemini Chat Model"]
  n6["Markdown to Textual Data Extractor"]
  n7["Convert Markdown to HTML"]
  n8["Initiate a Webhook Notification for Markdown to HTML Response"]
  n9["Set Bright Data Zone"]
  n10["Loop Over Items"]
  n11["Airtable"]
  n12["If Link field is not empty"]
  n13["Wait"]
  n14["Indeed Summarizer"]
  n15["Google Gemini Chat Model for AI Agent"]
  n13 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 1 to in 0"| n13
  n14 -->|"main out 0 to in 0"| n4
  n9 -->|"main out 0 to in 0"| n11
  n2 -->|"ai_tool out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n8
  n5 -->|"ai_languageModel out 0 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n9
  n6 -->|"main out 0 to in 0"| n14
  n15 -->|"ai_languageModel out 0 to in 0"| n4
  n1 -->|"ai_languageModel out 0 to in 0"| n14
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
