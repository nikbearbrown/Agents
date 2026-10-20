# AI Talent Intelligence Agent

Adapt the published “AI Talent Intelligence Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["#9654;#65039; START - Run Complete Analysis"]
  n1["#128218; SOURCE 1: ArXiv Papers"]
  n2["#128240; SOURCE 2: News Search"]
  n3["#128260; Parse ArXiv Data"]
  n4["#128260; Parse News Data"]
  n5["#128269; FILTER: High Significance Only"]
  n6["#128202; AGGREGATE Statistics"]
  n7["#128203; Generate Intelligence Report"]
  n8["#128190; Save to Database"]
  n9["#128231; Format Email Report"]
  n10["#128236; Send Email Report"]
  n11["Code"]
  n12["Merge"]
  n13["When chat message received"]
  n14["Basic LLM Chain"]
  n15["Groq Chat Model"]
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n11
  n1 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n12
  n4 -->|"main out 0 to in 1"| n12
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 0 to in 2"| n12
  n12 -->|"main out 0 to in 0"| n14
  n15 -->|"ai_languageModel out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n5
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/nikbearbrown-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
