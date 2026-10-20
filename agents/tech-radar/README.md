# Tech Radar

Adapt the published “Tech Radar” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 37 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Download Doc File From Google Drive"]
  n1["Doc File Data Loader"]
  n2["Cron"]
  n3["MySQL -delete all data"]
  n4["MySQL - insert all from sheets"]
  n5["Google Sheets - Tech Radar"]
  n6["Code - Transform table into rows"]
  n7["Google Docs - Update GDoc"]
  n8["Google Drive - Doc File Updated"]
  n9["Content - Recursive Character Text Splitter"]
  n10["Google Sheets - Read TechRadar"]
  n11["Code - Simplify Mapping to Original Query"]
  n12["Codes - Simplify Mapping to Original Query"]
  n13["Execute Workflow - Sql Agent"]
  n14["Execute Workflow - RAG Agent"]
  n15["AI Agent - Output Guardrail"]
  n16["LLM - Determine - Agent Input Router"]
  n17["When Executed by Another Workflow"]
  n18["1_Get DB Schema and Tables List"]
  n19["2_Get Table Definition"]
  n20["3_Execute actual query"]
  n21["AI Agent -DB Sql Agent"]
  n22["Pinecone Vector Store #40;Retrieval#41;"]
  n23["4_RagTool"]
  n24["AI Agent - RAG"]
  n25["Embeddings - Tech Radar Data Embedding"]
  n26["Pinecone - Vector Store for Embedding Content"]
  n27["Retrieve Embeddings - Tech Radar Vector DB"]
  n28["AI Agent - Retrieval"]
  n29["AI Chat Model - Claude 3.5 Sonnet"]
  n30["AI Chat Model - QwQ 32b"]
  n31["AI Chatmodel - Deepseek 32B"]
  n32["AI Chat Model - llama3-8b"]
  n33["API Response - Respond to Webhook"]
  n34["API Request - Webhook"]
  n35["Determine if is #39;RAG#39;"]
  n36["User Conversation history"]
  n2 -->|"main out 0 to in 0"| n3
  n23 -->|"ai_tool out 0 to in 0"| n24
  n28 -->|"ai_languageModel out 0 to in 0"| n23
  n1 -->|"ai_document out 0 to in 0"| n26
  n34 -->|"main out 0 to in 0"| n16
  n19 -->|"ai_tool out 0 to in 0"| n21
  n20 -->|"ai_tool out 0 to in 0"| n21
  n35 -->|"main out 0 to in 0"| n11
  n35 -->|"main out 1 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n10
  n30 -->|"ai_languageModel out 0 to in 0"| n24
  n32 -->|"ai_languageModel out 0 to in 0"| n15
  n36 -->|"ai_memory out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n33
  n31 -->|"ai_languageModel out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n4
  n18 -->|"ai_tool out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n7
  n29 -->|"ai_languageModel out 0 to in 0"| n21
  n22 -->|"ai_vectorStore out 0 to in 0"| n23
  n17 -->|"main out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n26
  n16 -->|"main out 0 to in 0"| n35
  n25 -->|"ai_embedding out 0 to in 0"| n26
  n11 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n13
  n27 -->|"ai_embedding out 0 to in 0"| n22
  n9 -->|"ai_textSplitter out 0 to in 0"| n1
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
