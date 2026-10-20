# 🎦🚀 YouTube Video Comment Analysis Agent

Adapt the published “🎦🚀 YouTube Video Comment Analysis Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When Executed by Another Workflow"]
  n1["Create YouTube API URL"]
  n2["Get YouTube Video Details"]
  n3["Merge YouTube Details #38; Transcript"]
  n4["Create One JSON Object"]
  n5["Workflow Variables"]
  n6["Combine Comments"]
  n7["Split Out Comments"]
  n8["Get YouTube Video Comments"]
  n9["When clicking #8216;Test workflow#8217;"]
  n10["Create YouTube API URL for Comments"]
  n11["Gmail Report"]
  n12["gpt-4o-mini"]
  n13["Markdown to HTML"]
  n14["YouTube Video Report Agent"]
  n15["Get Video Comments with Pagination"]
  n16["Save Report to Google Drive"]
  n12 -->|"ai_languageModel out 0 to in 0"| n14
  n6 -->|"main out 0 to in 1"| n3
  n13 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n8
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
