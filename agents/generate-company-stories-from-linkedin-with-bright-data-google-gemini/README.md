# Generate Company Stories from LinkedIn with Bright Data &amp; Google Gemini

Adapt the published “Generate Company Stories from LinkedIn with Bright Data &amp; Google Gemini” workflow to other implementations while preserving its documented behavior.

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
  n7["Set LinkedIn URL"]
  n8["Google Gemini Chat Model1"]
  n9["Check on the errors"]
  n10["Perform LinkedIn Web Request"]
  n11["Check Snapshot Status"]
  n12["LinkedIn Data Extractor"]
  n13["Concise Summary Generator"]
  n14["Webhook Notifier for Data Extractor"]
  n15["Webhook Notifier for Summary Generator"]
  n16["Wait for 30 seconds"]
  n4 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 1 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n10
  n6 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n6
  n2 -->|"ai_document out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n14
  n1 -->|"ai_languageModel out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n15
  n8 -->|"ai_languageModel out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n5
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n7
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
