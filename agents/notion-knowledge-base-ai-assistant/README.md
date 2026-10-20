# notion knowledge base ai assistant

Adapt the published “notion knowledge base ai assistant” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Notion"]
  n1["Return success to chat"]
  n2["Auto-fixing Output Parser"]
  n3["Anthropic Chat Model"]
  n4["Set schema for eval"]
  n5["Return error to chat"]
  n6["Anthropic Chat Model1"]
  n7["standardize schema"]
  n8["Simplify properties object"]
  n9["Structured Output Parser"]
  n10["Set input data"]
  n11["Set schem for rerun"]
  n12["Add feedback prompt"]
  n13["Check for WF JSON errors"]
  n14["Generate Workflow Agent"]
  n15["Anthropic Chat Model2"]
  n16["When chat message received"]
  n17["Valid n8n workflow JSON#63;"]
  n0 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 1 to in 0"| n5
  n10 -->|"main out 0 to in 0"| n14
  n7 -->|"main out 0 to in 0"| n8
  n12 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n13
  n3 -->|"ai_languageModel out 0 to in 0"| n14
  n6 -->|"ai_languageModel out 0 to in 0"| n2
  n15 -->|"ai_languageModel out 0 to in 0"| n17
  n14 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 1 to in 0"| n17
  n9 -->|"ai_outputParser out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 1 to in 0"| n1
  n2 -->|"ai_outputParser out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n10
  n16 -->|"main out 0 to in 0"| n0
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
