# You only have to run this part once!

Adapt the published “You only have to run this part once!” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 18 executable nodes and 16 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["WhatsApp Trigger"]
  n1["OpenAI Chat Model"]
  n2["Window Buffer Memory"]
  n3["Vector Store Tool"]
  n4["Embeddings OpenAI"]
  n5["OpenAI Chat Model1"]
  n6["When clicking #8216;Test workflow#8217;"]
  n7["Embeddings OpenAI1"]
  n8["Default Data Loader"]
  n9["Recursive Character Text Splitter"]
  n10["Extract from File"]
  n11["get Product Brochure"]
  n12["Reply To User"]
  n13["Reply To User1"]
  n14["Product Catalogue"]
  n15["Create Product Catalogue"]
  n16["Handle Message Types"]
  n17["AI Sales Agent"]
  n17 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n16
  n4 -->|"ai_embedding out 0 to in 0"| n14
  n10 -->|"main out 0 to in 0"| n15
  n1 -->|"ai_languageModel out 0 to in 0"| n17
  n14 -->|"ai_vectorStore out 0 to in 0"| n3
  n3 -->|"ai_tool out 0 to in 0"| n17
  n7 -->|"ai_embedding out 0 to in 0"| n15
  n5 -->|"ai_languageModel out 0 to in 0"| n3
  n8 -->|"ai_document out 0 to in 0"| n15
  n16 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 1 to in 0"| n13
  n2 -->|"ai_memory out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n10
  n9 -->|"ai_textSplitter out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n11
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
