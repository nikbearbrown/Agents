# Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini &amp; Pinecone

Adapt the published “Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini &amp; Pinecone” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 16 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["AI Agent"]
  n2["Pinecone Vector Store"]
  n3["Embeddings Google Gemini"]
  n4["Default Data Loader"]
  n5["Recursive Character Text Splitter"]
  n6["Google Gemini Chat Model1"]
  n7["Google Gemini Chat Model2"]
  n8["Google Gemini Chat Model"]
  n9["Structured Output Parser"]
  n10["Set Fields - URL and Webhook URL"]
  n11["Make a web request"]
  n12["Structured JSON Data Formatter"]
  n13["Webhook for structured data"]
  n14["Webhook for structured AI agent response"]
  n15["Information Extractor with Data Formatter"]
  n1 -->|"main out 0 to in 0"| n2
  n1 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n15
  n4 -->|"ai_document out 0 to in 0"| n2
  n3 -->|"ai_embedding out 0 to in 0"| n2
  n8 -->|"ai_languageModel out 0 to in 0"| n15
  n9 -->|"ai_outputParser out 0 to in 0"| n1
  n6 -->|"ai_languageModel out 0 to in 0"| n1
  n7 -->|"ai_languageModel out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n14
  n5 -->|"ai_textSplitter out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n1
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
