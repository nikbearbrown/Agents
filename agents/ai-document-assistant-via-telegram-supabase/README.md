# AI Document Assistant via Telegram + Supabase

Adapt the published “AI Document Assistant via Telegram + Supabase” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Google Gemini Chat Model"]
  n1["OpenWeatherMap"]
  n2["AI Agent"]
  n3["Telegram Trigger"]
  n4["Telegram"]
  n5["Think"]
  n6["Embeddings Google Gemini"]
  n7["Default Data Loader"]
  n8["Recursive Character Text Splitter"]
  n9["Extract from File"]
  n10["Answer questions with a vector store"]
  n11["Supabase Vector Store"]
  n12["Telegram - Embedding Complete"]
  n13["Supabase - Save Embeddings"]
  n14["Command Router"]
  n15["Telegram - Download file"]
  n16["Aggregate"]
  n17["Fallback- No formatting"]
  n18["Split Out"]
  n19["Simple Memory"]
  n20["Handle formatting and split"]
  n21["Manual Mapping"]
  n22["Unsupported message"]
  n23["Send processing document message"]
  n24["Send embedding Started message"]
  n5 -->|"ai_tool out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n20
  n4 -->|"main out 1 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n12
  n18 -->|"main out 0 to in 0"| n21
  n19 -->|"ai_memory out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n2
  n14 -->|"main out 2 to in 0"| n22
  n21 -->|"main out 0 to in 0"| n4
  n1 -->|"ai_tool out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n24
  n7 -->|"ai_document out 0 to in 0"| n13
  n11 -->|"ai_vectorStore out 0 to in 0"| n10
  n6 -->|"ai_embedding out 0 to in 0"| n13
  n6 -->|"ai_embedding out 0 to in 0"| n11
  n0 -->|"ai_languageModel out 0 to in 0"| n2
  n0 -->|"ai_languageModel out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n23
  n13 -->|"main out 0 to in 0"| n16
  n20 -->|"main out 0 to in 0"| n18
  n8 -->|"ai_textSplitter out 0 to in 0"| n7
  n10 -->|"ai_tool out 0 to in 0"| n2
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
