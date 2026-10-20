# Auto-Tag Blog Posts in WordPress with AI

Adapt the published “Auto-Tag Blog Posts in WordPress with AI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Auto-fixing Output Parser"]
  n2["OpenAI Chat Model1"]
  n3["Structured Output Parser"]
  n4["RSS Feed Trigger"]
  n5["Return article details"]
  n6["Split Out"]
  n7["Loop over articles"]
  n8["SET initial record"]
  n9["GET WP tags"]
  n10["POST WP tags"]
  n11["GET updated WP tags"]
  n12["Keep matches"]
  n13["Combine tag_ids"]
  n14["Combine slugs"]
  n15["If"]
  n16["MOCK article"]
  n17["Return missing tags"]
  n18["Wordpress"]
  n19["Demo Usage in Another Workflow"]
  n20["Auto-Tag Posts in WordPress"]
  n21["Generate tags for article"]
  n15 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 1 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n17
  n13 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n21
  n0 -->|"ai_languageModel out 0 to in 0"| n21
  n7 -->|"main out 1 to in 0"| n8
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n8 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n18
  n3 -->|"ai_outputParser out 0 to in 0"| n1
  n1 -->|"ai_outputParser out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n16
  n20 -->|"main out 0 to in 0"| n5
  n19 -->|"main out 0 to in 0"| n7
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
