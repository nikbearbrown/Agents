# Scenario 1 - AI Agent

Adapt the published “Scenario 1 - AI Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Window Buffer Memory"]
  n1["Get Chart"]
  n2["AI Agent"]
  n3["Telegram Trigger"]
  n4["Send Analysis"]
  n5["Workflow Input Trigger"]
  n6["response"]
  n7["Download Chart"]
  n8["Get Chart URL"]
  n9["Send Chart"]
  n10["OpenAI Chat Model"]
  n11["Switch"]
  n12["Transcribe"]
  n13["Download File"]
  n14["Set Text"]
  n15["Set Values"]
  n16["Technical Analysis"]
  n17["Webhook"]
  n18["Set Text1"]
  n19["Save Ticker"]
  n20["Loop Over Items"]
  n21["Schedule Trigger"]
  n22["Run Agent"]
  n23["Get tokens"]
  n11 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 1 to in 0"| n14
  n17 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n4
  n14 -->|"main out 0 to in 0"| n2
  n1 -->|"ai_tool out 0 to in 0"| n2
  n22 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n2
  n23 -->|"main out 0 to in 0"| n20
  n9 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n2
  n19 -->|"ai_tool out 0 to in 0"| n2
  n13 -->|"main out 0 to in 0"| n12
  n8 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n16
  n20 -->|"main out 1 to in 0"| n22
  n21 -->|"main out 0 to in 0"| n23
  n3 -->|"main out 0 to in 0"| n11
  n10 -->|"ai_languageModel out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n9
  n0 -->|"ai_memory out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n15
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
