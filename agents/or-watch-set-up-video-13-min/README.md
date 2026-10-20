# ... or watch set up video &#91;13 min&#93;

Adapt the published “... or watch set up video &#91;13 min&#93;” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["get_channel_details"]
  n2["get_video_description"]
  n3["get_list_of_videos"]
  n4["get_list_of_comments"]
  n5["search"]
  n6["analyze_thumbnail"]
  n7["video_transcription"]
  n8["Postgres Chat Memory"]
  n9["AI Agent"]
  n10["When chat message received"]
  n11["Get Comments"]
  n12["Execute Workflow Trigger"]
  n13["Get Channel Details"]
  n14["Get Video Description"]
  n15["Edit Fields"]
  n16["Run Query"]
  n17["Get Videos by Channel"]
  n18["Response"]
  n19["Switch"]
  n20["Get Video Transcription"]
  n21["OpenAI"]
  n21 -->|"main out 0 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n13
  n19 -->|"main out 1 to in 0"| n14
  n19 -->|"main out 2 to in 0"| n11
  n19 -->|"main out 3 to in 0"| n16
  n19 -->|"main out 4 to in 0"| n17
  n19 -->|"main out 5 to in 0"| n21
  n19 -->|"main out 6 to in 0"| n20
  n5 -->|"ai_tool out 0 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n18
  n15 -->|"main out 0 to in 0"| n18
  n11 -->|"main out 0 to in 0"| n15
  n0 -->|"ai_languageModel out 0 to in 0"| n9
  n6 -->|"ai_tool out 0 to in 0"| n9
  n3 -->|"ai_tool out 0 to in 0"| n9
  n13 -->|"main out 0 to in 0"| n18
  n1 -->|"ai_tool out 0 to in 0"| n9
  n7 -->|"ai_tool out 0 to in 0"| n9
  n8 -->|"ai_memory out 0 to in 0"| n9
  n4 -->|"ai_tool out 0 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n18
  n2 -->|"ai_tool out 0 to in 0"| n9
  n20 -->|"main out 0 to in 0"| n18
  n12 -->|"main out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n9
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
