# 🙋‍♀️What's the difference?

Adapt the published “🙋‍♀️What's the difference?” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Embeddings Mistral Cloud"]
  n2["Default Data Loader"]
  n3["Recursive Character Text Splitter"]
  n4["Get Tax Code Zip File"]
  n5["Extract Zip Files"]
  n6["Files as Items"]
  n7["Extract PDF Contents"]
  n8["Extract From Chapter"]
  n9["Map To Sections"]
  n10["Execute Workflow Trigger"]
  n11["Get Mistral Embeddings"]
  n12["Content Chunking #64; 50k Chars"]
  n13["Split Out Chunks"]
  n14["For Each Section..."]
  n15["Sections To List"]
  n16["Only Valid Sections"]
  n17["Use Qdrant Search API1"]
  n18["Use Qdrant Scroll API"]
  n19["Get Search Response"]
  n20["Qdrant Vector Store"]
  n21["AI Agent"]
  n22["Window Buffer Memory"]
  n23["When chat message received"]
  n24["Window Buffer Memory1"]
  n25["OpenAI Chat Model"]
  n26["1sec"]
  n27["Ask Tool"]
  n28["Search Tool"]
  n29["Switch"]
  n30["Get Ask Response"]
  n26 -->|"main out 0 to in 0"| n14
  n29 -->|"main out 0 to in 0"| n11
  n29 -->|"main out 1 to in 0"| n18
  n27 -->|"ai_tool out 0 to in 0"| n21
  n28 -->|"ai_tool out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n6
  n25 -->|"ai_languageModel out 0 to in 0"| n21
  n2 -->|"ai_document out 0 to in 0"| n20
  n14 -->|"main out 1 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n26
  n8 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 0 to in 0"| n8
  n22 -->|"ai_memory out 0 to in 0"| n21
  n4 -->|"main out 0 to in 0"| n5
  n18 -->|"main out 0 to in 0"| n19
  n24 -->|"ai_memory out 0 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n30
  n1 -->|"ai_embedding out 0 to in 0"| n20
  n10 -->|"main out 0 to in 0"| n29
  n23 -->|"main out 0 to in 0"| n21
  n12 -->|"main out 0 to in 0"| n13
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
  n0 -->|"main out 0 to in 0"| n4
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
