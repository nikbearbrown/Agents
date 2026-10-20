# DSP Agent

Adapt the published “DSP Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Switch"]
  n2["Edit Fields"]
  n3["Telegram"]
  n4["OpenAI"]
  n5["AI Agent"]
  n6["Google Gemini Chat Model"]
  n7["Telegram1"]
  n8["Calculator"]
  n9["Wikipedia"]
  n10["Airtable"]
  n11["Aggregate"]
  n12["Merge"]
  n13["Simple Memory"]
  n14["OpenAI Chat Model"]
  n15["memory_tool"]
  n16["contentCreatorAgent"]
  n0 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 1 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 0 to in 0"| n7
  n8 -->|"ai_tool out 0 to in 0"| n5
  n9 -->|"ai_tool out 0 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 1"| n12
  n12 -->|"main out 0 to in 0"| n5
  n13 -->|"ai_memory out 0 to in 0"| n5
  n14 -->|"ai_languageModel out 0 to in 0"| n5
  n15 -->|"ai_tool out 0 to in 0"| n5
  n16 -->|"ai_tool out 0 to in 0"| n5
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
