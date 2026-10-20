# Send a Telegram message

Adapt the published “Send a Telegram message” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["OpenAI Chat Model"]
  n2["Structured Output Parser"]
  n3["Get Audio File"]
  n4["Transcribe Recording"]
  n5["Limit"]
  n6["Receive Telegram message"]
  n7["If it#39;s a voice message"]
  n8["Set chatInput from message"]
  n9["Set chatInput from voice"]
  n10["List of Ingredients and nutrients"]
  n11["Explode the list"]
  n12["Add date"]
  n13["Store in sheet"]
  n14["Respond message"]
  n5 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n12
  n1 -->|"ai_languageModel out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n3
  n7 -->|"main out 1 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n10
  n2 -->|"ai_outputParser out 0 to in 0"| n10
  n8 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n10
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
