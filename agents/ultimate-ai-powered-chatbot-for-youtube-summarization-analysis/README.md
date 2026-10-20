# ⚡📽️ Ultimate AI-Powered Chatbot for YouTube Summarization &amp; Analysis

Adapt the published “⚡📽️ Ultimate AI-Powered Chatbot for YouTube Summarization &amp; Analysis” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get YouTube Transcript"]
  n1["When Executed by Another Workflow"]
  n2["When chat message received"]
  n3["Window Buffer Memory"]
  n4["gpt-4o-mini1"]
  n5["YouTube Video Agent"]
  n6["Create YouTube API URL"]
  n7["Split Out Transcript Segments"]
  n8["Combine Transcript Segments"]
  n9["Get YouTube Video Details"]
  n10["Merge YouTube Details #38; Transcript"]
  n11["Create One JSON Object"]
  n12["Respond with YouTube Details #38; Transcript"]
  n13["Workflow Variables"]
  n14["YouTube Processing Tool"]
  n15["DeepSeek-V3 Chat"]
  n4 -->|"ai_languageModel out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n6
  n13 -->|"main out 0 to in 0"| n0
  n3 -->|"ai_memory out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n12
  n6 -->|"main out 0 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n7
  n14 -->|"ai_tool out 0 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 1"| n10
  n7 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n11
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
