# Replace Storage name, database ID and credentials.

Adapt the published “Replace Storage name, database ID and credentials.” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get All files"]
  n1["Default Data Loader"]
  n2["Recursive Character Text Splitter"]
  n3["Extract Document PDF"]
  n4["Embeddings OpenAI"]
  n5["Create File record2"]
  n6["If"]
  n7["Get All Files"]
  n8["Download"]
  n9["Loop Over Items"]
  n10["When clicking #8216;Test workflow#8217;"]
  n11["Aggregate"]
  n12["When chat message received"]
  n13["OpenAI Chat Model1"]
  n14["Embeddings OpenAI2"]
  n15["OpenAI Chat Model2"]
  n16["Vector Store Tool1"]
  n17["Switch"]
  n18["Insert into Supabase Vectorstore"]
  n19["Merge"]
  n20["AI Agent"]
  n21["Supabase Vector Store"]
  n6 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 1 to in 0"| n9
  n19 -->|"main out 0 to in 0"| n5
  n17 -->|"main out 0 to in 0"| n19
  n17 -->|"main out 1 to in 0"| n3
  n8 -->|"main out 0 to in 0"| n17
  n11 -->|"main out 0 to in 0"| n0
  n7 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 1 to in 0"| n6
  n4 -->|"ai_embedding out 0 to in 0"| n18
  n14 -->|"ai_embedding out 0 to in 0"| n21
  n13 -->|"ai_languageModel out 0 to in 0"| n20
  n15 -->|"ai_languageModel out 0 to in 0"| n16
  n16 -->|"ai_tool out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n18
  n1 -->|"ai_document out 0 to in 0"| n18
  n3 -->|"main out 0 to in 1"| n19
  n21 -->|"ai_vectorStore out 0 to in 0"| n16
  n12 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n9
  n2 -->|"ai_textSplitter out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n7
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
