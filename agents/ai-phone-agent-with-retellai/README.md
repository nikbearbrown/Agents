# AI Phone Agent with RetellAI

Adapt the published “AI Phone Agent with RetellAI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Filter"]
  n1["OpenAI Chat Model"]
  n2["Structured Output Parser"]
  n3["n8n_rag_function"]
  n4["Retrive Qdrant Vector Store"]
  n5["Embeddings OpenAI2"]
  n6["RAG"]
  n7["OpenAI Chat Model2"]
  n8["Respond to Webhook"]
  n9["OpenAI Chat Model1"]
  n10["Telegram"]
  n11["Google Calendar"]
  n12["OpenAI Chat Model3"]
  n13["Structured Output Parser1"]
  n14["n8n_call"]
  n15["n8n_check_available"]
  n16["When clicking #8216;Test workflow#8217;"]
  n17["Qdrant Vector Store"]
  n18["Create collection"]
  n19["Refresh collection"]
  n20["Get folder"]
  n21["Download Files"]
  n22["Embeddings OpenAI"]
  n23["Default Data Loader"]
  n24["Token Splitter"]
  n25["Set call fields"]
  n26["Extract key points"]
  n27["Concert start date"]
  n28["Retrive Agent"]
  n6 -->|"ai_tool out 0 to in 0"| n28
  n0 -->|"main out 0 to in 0"| n25
  n14 -->|"main out 0 to in 0"| n0
  n20 -->|"main out 0 to in 0"| n21
  n28 -->|"main out 0 to in 0"| n8
  n21 -->|"main out 0 to in 0"| n17
  n24 -->|"ai_textSplitter out 0 to in 0"| n23
  n25 -->|"main out 0 to in 0"| n26
  n3 -->|"main out 0 to in 0"| n28
  n22 -->|"ai_embedding out 0 to in 0"| n17
  n1 -->|"ai_languageModel out 0 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n11
  n5 -->|"ai_embedding out 0 to in 0"| n4
  n26 -->|"main out 0 to in 0"| n10
  n9 -->|"ai_languageModel out 0 to in 0"| n6
  n7 -->|"ai_languageModel out 0 to in 0"| n28
  n12 -->|"ai_languageModel out 0 to in 0"| n27
  n19 -->|"main out 0 to in 0"| n20
  n23 -->|"ai_document out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n27
  n2 -->|"ai_outputParser out 0 to in 0"| n26
  n13 -->|"ai_outputParser out 0 to in 0"| n27
  n4 -->|"ai_vectorStore out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 0 to in 0"| n19
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
