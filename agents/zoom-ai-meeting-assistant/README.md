# Zoom AI Meeting Assistant

Adapt the published “Zoom AI Meeting Assistant” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["When clicking #8216;Test workflow#8217;"]
  n2["No Recording/Transcript available"]
  n3["Zoom: Get data of last meeting"]
  n4["Filter transcript URL"]
  n5["Filter: Only 1 item"]
  n6["Zoom: Get transcript file"]
  n7["Extract text from transcript file"]
  n8["Format transcript text"]
  n9["Zoom: Get participants data"]
  n10["Create meeting summary"]
  n11["Sort for mail delivery"]
  n12["Format to html"]
  n13["Send meeting summary"]
  n14["Create tasks"]
  n15["Create tasks and follow-up call"]
  n16["Create follow-up call"]
  n17["Filter: Last 24 hours"]
  n18["Execute Workflow Trigger"]
  n19["Split Out"]
  n20["ClickUp"]
  n21["Zoom: Get transcripts data"]
  n19 -->|"main out 0 to in 0"| n20
  n14 -->|"ai_tool out 0 to in 0"| n15
  n12 -->|"main out 0 to in 0"| n13
  n0 -->|"ai_languageModel out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 1 to in 0"| n6
  n16 -->|"ai_tool out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n21
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n19
  n6 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n4
  n21 -->|"main out 1 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n3
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
