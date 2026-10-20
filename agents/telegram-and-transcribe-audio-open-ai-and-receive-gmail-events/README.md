# telegram and transcribe audio open ai and receive gmail events

Adapt the published “telegram and transcribe audio open ai and receive gmail events” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Structured Output Parser"]
  n1["OpenAI Chat Model"]
  n2["Text Email"]
  n3["OpenAI"]
  n4["New Email Received"]
  n5["In the Inbox#63;"]
  n6["Needs a response#63;"]
  n7["Telegram Bot Message Received"]
  n8["It needs to be an audio message #43; a reply#33;"]
  n9["Get Audio File"]
  n10["Create Email Draft"]
  n11["Direct to Draft"]
  n12["Does Email Need a Response#63;"]
  n13["Is Type Audio Message #43; Reply#63;"]
  n14["OpenAI Chat Model1"]
  n15["Write Polished Reply"]
  n16["Set Chat ID"]
  n3 -->|"main out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n2
  n5 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n16
  n1 -->|"ai_languageModel out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n5
  n14 -->|"ai_languageModel out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n10
  n0 -->|"ai_outputParser out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n6
  n7 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n9
  n13 -->|"main out 1 to in 0"| n8
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
