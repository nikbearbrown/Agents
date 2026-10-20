# 💥🛠️Automate Blog Content Creation with GPT-4, Perplexity &amp; WordPress

Adapt the published “💥🛠️Automate Blog Content Creation with GPT-4, Perplexity &amp; WordPress” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 12 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Perplexity Research"]
  n1["When chat message received"]
  n2["Slack-List"]
  n3["Copywriting AI Agent"]
  n4["Format Research Output"]
  n5["Publish Article to WordPress"]
  n6["Send Email Notification"]
  n7["Notify Slack Channel"]
  n8["Generate SEO Blog Content #40;GPT-4o#41;"]
  n9["Start with Research Query Submission"]
  n10["Edit Workflow Variables"]
  n11["Notion-List"]
  n12["Insert Article in Notion"]
  n2 -->|"ai_tool out 0 to in 0"| n3
  n11 -->|"ai_tool out 0 to in 0"| n3
  n0 -->|"main out 0 to in 0"| n4
  n7 -->|"ai_tool out 0 to in 0"| n3
  n4 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n3
  n6 -->|"ai_tool out 0 to in 0"| n3
  n12 -->|"ai_tool out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n3
  n5 -->|"ai_tool out 0 to in 0"| n3
  n8 -->|"ai_languageModel out 0 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n0
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
