# SEO Blog Generator with GPT-4o, Perplexity, and Telegram Integration

Adapt the published “SEO Blog Generator with GPT-4o, Perplexity, and Telegram Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 8 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Structured Output Parser"]
  n2["Metadata Generator"]
  n3["Merge"]
  n4["On form submission"]
  n5["Blog Content Generator"]
  n6["gpt-4o-mini"]
  n7["Combine Blog Details"]
  n8["Perplexity_Searcher"]
  n9["Tele HoangSP_Social_Media"]
  n10["AI Agent"]
  n11["OpenAI Chat Model1"]
  n12["AI Agent1"]
  n13["OpenAI Chat Model2"]
  n14["Metadata Extractor"]
  n15["Telegram"]
  n16["Simple Memory"]
  n17["Simple Memory1"]
  n3 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 1"| n3
  n16 -->|"ai_memory out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n10
  n11 -->|"ai_languageModel out 0 to in 0"| n10
  n13 -->|"ai_languageModel out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n10
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
