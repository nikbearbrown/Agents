# Embed your Vector Store

Adapt the published “Embed your Vector Store” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When chat message received"]
  n1["AI Agent"]
  n2["OpenAI Chat Model"]
  n3["Split Out"]
  n4["Embeddings OpenAI1"]
  n5["Default Data Loader"]
  n6["Token Splitter1"]
  n7["Window Buffer Memory"]
  n8["Embeddings OpenAI2"]
  n9["Extract from File"]
  n10["When clicking #8216;Test workflow#8217;"]
  n11["AI Agent1"]
  n12["OpenAI Chat Model1"]
  n13["Embeddings OpenAI"]
  n14["Loop Over Items"]
  n15["Structured Output Parser"]
  n16["Pull Mitre Data From Gdrive"]
  n17["Embed JSON in Qdrant Collection"]
  n18["Query Qdrant Vector Store"]
  n19["Qdrant Vector Store query"]
  n20["Get all Zendesk Tickets"]
  n21["Update Zendesk with Mitre Data"]
  n22["Move on to next ticket"]
  n11 -->|"main out 0 to in 0"| n21
  n3 -->|"main out 0 to in 0"| n17
  n14 -->|"main out 1 to in 0"| n11
  n6 -->|"ai_textSplitter out 0 to in 0"| n5
  n13 -->|"ai_embedding out 0 to in 0"| n19
  n9 -->|"main out 0 to in 0"| n3
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n4 -->|"ai_embedding out 0 to in 0"| n17
  n8 -->|"ai_embedding out 0 to in 0"| n18
  n12 -->|"ai_languageModel out 0 to in 0"| n11
  n5 -->|"ai_document out 0 to in 0"| n17
  n7 -->|"ai_memory out 0 to in 0"| n1
  n22 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n14
  n15 -->|"ai_outputParser out 0 to in 0"| n11
  n19 -->|"ai_tool out 0 to in 0"| n11
  n18 -->|"ai_tool out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n9
  n21 -->|"main out 0 to in 0"| n22
  n10 -->|"main out 0 to in 0"| n16
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
