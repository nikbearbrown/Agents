# 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠

Adapt the published “🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Check User #38; Chat ID"]
  n1["Error message"]
  n2["Listen for Telegram Events"]
  n3["Validation"]
  n4["Message Router"]
  n5["AI Agent"]
  n6["Merge"]
  n7["Window Buffer Memory"]
  n8["When chat message received"]
  n9["Telegram Response"]
  n10["Save Long Term Memories"]
  n11["Retrieve Long Term Memories"]
  n12["Response Error message"]
  n13["DeepSeek-R1 Reasoning"]
  n14["DeepSeek-V3 Chat"]
  n6 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 1 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n0
  n4 -->|"main out 1 to in 0"| n6
  n4 -->|"main out 1 to in 0"| n11
  n4 -->|"main out 3 to in 0"| n1
  n14 -->|"ai_languageModel out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 1 to in 0"| n1
  n10 -->|"ai_tool out 0 to in 0"| n5
  n2 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 1"| n6
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
