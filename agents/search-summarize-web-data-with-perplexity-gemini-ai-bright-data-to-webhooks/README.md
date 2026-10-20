# Search &amp; Summarize Web Data with Perplexity, Gemini AI &amp; Bright Data to Webhooks

Adapt the published “Search &amp; Summarize Web Data with Perplexity, Gemini AI &amp; Bright Data to Webhooks” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Google Gemini Chat Model"]
  n2["Default Data Loader"]
  n3["Recursive Character Text Splitter"]
  n4["If"]
  n5["Set Snapshot Id"]
  n6["Download Snapshot"]
  n7["Google Gemini Chat Model1"]
  n8["Wait"]
  n9["Check on the errors"]
  n10["Webhook Notifier"]
  n11["Perplexity Search Request"]
  n12["Check Snapshot Status"]
  n13["Readable Data Extractor"]
  n14["Summarization of search result"]
  n4 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 1 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n6
  n2 -->|"ai_document out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n14
  n1 -->|"ai_languageModel out 0 to in 0"| n14
  n7 -->|"ai_languageModel out 0 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n10
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n11
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
