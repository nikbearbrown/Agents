# Activate workflow to use!

Adapt the published “Activate workflow to use!” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["WhatsApp Trigger"]
  n1["Get Audio URL"]
  n2["Get Video URL"]
  n3["Get Image URL"]
  n4["Download Video"]
  n5["Download Audio"]
  n6["Download Image"]
  n7["Window Buffer Memory"]
  n8["Get User#39;s Message"]
  n9["Split Out Message Parts"]
  n10["Wikipedia"]
  n11["Redirect Message Types"]
  n12["Get Text"]
  n13["Respond to User"]
  n14["Image Explainer"]
  n15["Format Response"]
  n16["Google Gemini Chat Model"]
  n17["Google Gemini Audio"]
  n18["Google Gemini Video"]
  n19["Google Gemini Chat Model1"]
  n20["Google Gemini Chat Model2"]
  n21["Format Response1"]
  n22["Text Summarizer"]
  n23["AI Agent"]
  n23 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 0 to in 0"| n22
  n10 -->|"ai_tool out 0 to in 0"| n23
  n1 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n4
  n5 -->|"main out 0 to in 0"| n17
  n6 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n18
  n15 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n8
  n22 -->|"main out 0 to in 0"| n8
  n21 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n23
  n17 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n15
  n7 -->|"ai_memory out 0 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 1 to in 0"| n2
  n11 -->|"main out 2 to in 0"| n3
  n11 -->|"main out 3 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n11
  n16 -->|"ai_languageModel out 0 to in 0"| n23
  n19 -->|"ai_languageModel out 0 to in 0"| n14
  n20 -->|"ai_languageModel out 0 to in 0"| n22
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
