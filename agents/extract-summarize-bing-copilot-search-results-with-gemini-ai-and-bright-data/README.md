# Extract &amp; Summarize Bing Copilot Search Results with Gemini AI and Bright Data

Adapt the published “Extract &amp; Summarize Bing Copilot Search Results with Gemini AI and Bright Data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

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
  n8["Structured Output Parser"]
  n9["Check on the errors"]
  n10["Check Snapshot Status"]
  n11["Structured Data Extractor"]
  n12["Concise Summary Creator"]
  n13["Wait for 30 seconds"]
  n14["Structured Data Webhook Notifier"]
  n15["Summary Webhook Notifier"]
  n16["Perform a Bing Copilot Request"]
  n4 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 1 to in 0"| n13
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n6
  n2 -->|"ai_document out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n15
  n1 -->|"ai_languageModel out 0 to in 0"| n12
  n8 -->|"ai_outputParser out 0 to in 0"| n11
  n7 -->|"ai_languageModel out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n14
  n16 -->|"main out 0 to in 0"| n5
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n16
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
