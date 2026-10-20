# receive form events and split out and open ai

Adapt the published “receive form events and split out and open ai” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On form submission"]
  n1["Split Out"]
  n2["OpenAI"]
  n3["Settings"]
  n4["Create post title and structure"]
  n5["Wikipedia"]
  n6["Check data consistency"]
  n7["Form"]
  n8["Merge chapters title and text"]
  n9["Final article text"]
  n10["Post on Wordpress"]
  n11["Generate featured image"]
  n12["Upload media"]
  n13["Set image ID for the post"]
  n14["Form1"]
  n2 -->|"main out 0 to in 0"| n8
  n3 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 1"| n8
  n5 -->|"ai_tool out 0 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 1 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 0 to in 0"| n6
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
