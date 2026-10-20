# Write a WordPress post with AI (starting from a few keywords)

Adapt the published “Write a WordPress post with AI (starting from a few keywords)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Form"]
  n1["Settings"]
  n2["Check data consistency"]
  n3["Split out chapters"]
  n4["Merge chapters title and text"]
  n5["Final article text"]
  n6["Post on Wordpress"]
  n7["Upload media"]
  n8["Set image ID for the post"]
  n9["Respond: Success"]
  n10["Respond: Error"]
  n11["Generate featured image"]
  n12["Wikipedia"]
  n13["Create post title and structure"]
  n14["Create chapters text"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n13
  n12 -->|"ai_tool out 0 to in 0"| n13
  n7 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n11
  n5 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 1"| n4
  n3 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n3
  n2 -->|"main out 1 to in 0"| n10
  n11 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n2
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
