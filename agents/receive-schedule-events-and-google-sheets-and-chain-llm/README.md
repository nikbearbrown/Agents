# receive schedule events and google sheets and chain llm

Adapt the published “receive schedule events and google sheets and chain llm” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Scheduled Start: Check for New Posts"]
  n1["1. Get Next Post Idea from Sheet"]
  n2["2. Prepare Input Variables #40;Topic, Audience, etc.#41;"]
  n3["3a. Generate Content Concept #40;Gemini#41;"]
  n4["#40;LLM Model for Concept#41;"]
  n5["#40;Parse Concept JSON#41;"]
  n6["3b. Generate Image Prompt Options #40;Gemini#41;"]
  n7["#40;LLM Model for Prompts#41;"]
  n8["#40;Parse Prompts JSON#41;"]
  n9["3c. Generate Post Caption #40;Gemini#41;"]
  n10["#40;LLM Model for Caption#41;"]
  n11["#40;Parse Caption JSON#41;"]
  n12["4. Generate Image using Prompt 1 #40;Replicate Flux#41;"]
  n13["5. Prepare Data for Instagram API"]
  n14["6a. Create Instagram Media Container"]
  n15["6b. Wait for Container Processing"]
  n16["6c. Publish Post to Instagram"]
  n17["7. Update Post Status in Sheet"]
  n11 -->|"ai_outputParser out 0 to in 0"| n9
  n5 -->|"ai_outputParser out 0 to in 0"| n3
  n8 -->|"ai_outputParser out 0 to in 0"| n6
  n10 -->|"ai_languageModel out 0 to in 0"| n9
  n4 -->|"ai_languageModel out 0 to in 0"| n3
  n7 -->|"ai_languageModel out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n17
  n1 -->|"main out 0 to in 0"| n2
  n13 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n3
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
