# Personalized AI Tech Newsletter Using RSS, OpenAI and Gmail

Adapt the published “Personalized AI Tech Newsletter Using RSS, OpenAI and Gmail” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split Out"]
  n1["Normalize Fields"]
  n2["Embeddings OpenAI"]
  n3["Default Data Loader"]
  n4["Recursive Character Text Splitter"]
  n5["OpenAI Chat Model"]
  n6["Get Articles Daily"]
  n7["Send Weekly Summary"]
  n8["News reader AI"]
  n9["Send Newsletter"]
  n10["Convert Response to an Email-Friendly Format"]
  n11["Your topics of interest"]
  n12["Store News Articles"]
  n13["Set Tech News RSS Feeds"]
  n14["Read RSS News Feeds"]
  n15["Get News Articles"]
  n16["Embeddings OpenAI2"]
  n0 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n12
  n2 -->|"ai_embedding out 0 to in 0"| n12
  n15 -->|"ai_tool out 0 to in 0"| n8
  n5 -->|"ai_languageModel out 0 to in 0"| n8
  n16 -->|"ai_embedding out 0 to in 0"| n15
  n6 -->|"main out 0 to in 0"| n13
  n3 -->|"ai_document out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n1
  n7 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n8
  n4 -->|"ai_textSplitter out 0 to in 0"| n3
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
