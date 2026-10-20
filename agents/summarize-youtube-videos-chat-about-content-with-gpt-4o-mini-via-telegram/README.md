# Summarize YouTube Videos &amp; Chat About Content with GPT-4o-mini via Telegram

Adapt the published “Summarize YouTube Videos &amp; Chat About Content with GPT-4o-mini via Telegram” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split Transcript into Segments"]
  n1["Extract YouTube URL from Input"]
  n2["Extract Video ID from URL"]
  n3["gpt-4o-mini"]
  n4["Generate Summary with GPT-4o-mini"]
  n5["Concatenate Transcript Segments"]
  n6["Trigger on Telegram Message"]
  n7["Extract YouTube Transcript"]
  n8["Send Summary via Telegram"]
  n9["Receive YouTube URL via Webhook"]
  n10["Send Response to Webhook"]
  n11["Telegram Trigger"]
  n12["Retrieve Transcript from Google Docs"]
  n13["Update Transcript in Google Docs"]
  n14["Handle User Questions via AI"]
  n15["OpenAI Chat Model"]
  n16["Window Buffer Memory"]
  n17["Google Docs2"]
  n18["Send AI Response via Telegram"]
  n3 -->|"ai_languageModel out 0 to in 0"| n4
  n17 -->|"ai_tool out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n14
  n15 -->|"ai_languageModel out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n18
  n1 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n4
  n5 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n13
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
