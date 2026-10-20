# Brand Content Extract, Summarize &amp; Sentiment Analysis with Bright Data

Adapt the published “Brand Content Extract, Summarize &amp; Sentiment Analysis with Bright Data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Markdown to Textual Data Extractor"]
  n2["Set URL and Bright Data Zone"]
  n3["AI Sentiment Analyzer with the structured response"]
  n4["Initiate a Webhook Notification for Markdown to Textual Data Extraction"]
  n5["Initiate a Webhook Notification for AI Sentiment Analyzer"]
  n6["Google Gemini Chat Model for Summary"]
  n7["Google Gemini Chat Model for Data Extract"]
  n8["Google Gemini Chat Model for Sentiment Analyzer"]
  n9["Initiate a Webhook Notification for Summarization"]
  n10["Perform Bright Data Web Request"]
  n11["Summarize Content"]
  n12["Create a binary data for textual data"]
  n13["Create a binary data for sentiment analysis"]
  n14["Write the AI Sentiment analysis file to disk"]
  n15["Write the textual file to disk"]
  n16["Create a binary data for summary"]
  n17["Write the summary file to disk"]
  n11 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n16
  n2 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n12
  n6 -->|"ai_languageModel out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n15
  n7 -->|"ai_languageModel out 0 to in 0"| n1
  n13 -->|"main out 0 to in 0"| n14
  n8 -->|"ai_languageModel out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n13
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
