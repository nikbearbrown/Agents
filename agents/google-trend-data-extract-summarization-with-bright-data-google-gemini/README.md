# Google Trend Data Extract, Summarization with Bright Data &amp; Google Gemini

Adapt the published “Google Trend Data Extract, Summarization with Bright Data &amp; Google Gemini” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Markdown to Textual Data Extractor"]
  n2["Set URL and Bright Data Zone"]
  n3["Initiate a Webhook Notification for Markdown to Textual Data Extraction"]
  n4["Google Gemini Chat Model for Data Extract"]
  n5["Perform Bright Data Web Request"]
  n6["Create a binary data"]
  n7["Structured Data Extractor"]
  n8["Summarize Google Trends"]
  n9["Initiate a Webhook Notification for Summarization"]
  n10["Write the file to disk"]
  n11["Google Gemini Chat Model for Summarization"]
  n12["Google Gemini Chat Model for Structured Data Extract"]
  n13["Send Summary to Gmail"]
  n6 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n8
  n2 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n7
  n4 -->|"ai_languageModel out 0 to in 0"| n1
  n11 -->|"ai_languageModel out 0 to in 0"| n8
  n12 -->|"ai_languageModel out 0 to in 0"| n7
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
