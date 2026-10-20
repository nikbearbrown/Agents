# Main Function to Receive and Send Telegram Messages

Adapt the published “Main Function to Receive and Send Telegram Messages” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Incoming Message"]
  n1["MCP Server Trigger"]
  n2["AI Agent"]
  n3["MCP Client"]
  n4["OpenAI Chat Model"]
  n5["Simple Memory"]
  n6["chatInput"]
  n7["create_todays_task"]
  n8["chatOutput"]
  n9["sendMessage"]
  n10["create_upcoming_task"]
  n11["complete_task"]
  n12["get_todays_tasks"]
  n13["get_upcoming_tasks"]
  n14["Switch"]
  n15["audio_id"]
  n16["download_audio"]
  n17["transcribeAudio"]
  n18["audioInput"]
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n8
  n15 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n2
  n3 -->|"ai_tool out 0 to in 0"| n2
  n18 -->|"main out 0 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n9
  n5 -->|"ai_memory out 0 to in 0"| n2
  n11 -->|"ai_tool out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n0 -->|"main out 0 to in 0"| n14
  n12 -->|"ai_tool out 0 to in 0"| n1
  n4 -->|"ai_languageModel out 0 to in 0"| n2
  n7 -->|"ai_tool out 0 to in 0"| n1
  n13 -->|"ai_tool out 0 to in 0"| n1
  n10 -->|"ai_tool out 0 to in 0"| n1
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
