# Open Deep Research - AI-Powered Autonomous Research Workflow

Adapt the published “Open Deep Research - AI-Powered Autonomous Research Workflow” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Chat Message Trigger"]
  n1["Generate Search Queries using LLM"]
  n2["LLM Response Provider #40;OpenRouter#41;"]
  n3["Parse and Chunk JSON Data"]
  n4["Perform SerpAPI Search Request"]
  n5["Perform Jina AI Analysis Request"]
  n6["Format SerpAPI Organic Results"]
  n7["Extract Relevant Context via LLM"]
  n8["Generate Comprehensive Research Report"]
  n9["Split Data for SerpAPI Batching"]
  n10["Split Data for Jina AI Batching"]
  n11["LLM Memory Buffer #40;Input Context#41;"]
  n12["LLM Memory Buffer #40;Report Context#41;"]
  n13["Fetch Wikipedia Information"]
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n9
  n13 -->|"ai_tool out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n7
  n10 -->|"main out 1 to in 0"| n5
  n9 -->|"main out 0 to in 0"| n6
  n9 -->|"main out 1 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n3
  n11 -->|"ai_memory out 0 to in 0"| n7
  n12 -->|"ai_memory out 0 to in 0"| n8
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n2 -->|"ai_languageModel out 0 to in 0"| n7
  n2 -->|"ai_languageModel out 0 to in 0"| n8
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
