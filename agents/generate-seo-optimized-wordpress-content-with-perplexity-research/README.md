# 🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research

Adapt the published “🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Wordpress"]
  n1["OpenAI Chat Model"]
  n2["Structured Output Parser"]
  n3["Create Title, Slug, Meta"]
  n4["Create HTML"]
  n5["Merge"]
  n6["Upload Image to Wordpress"]
  n7["Set Image on Wordpress Post"]
  n8["On form submission"]
  n9["Perplexity Research"]
  n10["Cleanup Links"]
  n11["Copywriter AI Agent"]
  n12["Cleanup HTML"]
  n13["GET Image"]
  n14["Set Image URL"]
  n15["Send Success Message to Telegram"]
  n16["gpt-4o-mini"]
  n17["Combine Blog Details"]
  n5 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n5
  n16 -->|"ai_languageModel out 0 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n0
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n13
  n1 -->|"ai_languageModel out 0 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n4
  n11 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 1"| n5
  n9 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n12
  n3 -->|"main out 0 to in 2"| n5
  n2 -->|"ai_outputParser out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n15
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
