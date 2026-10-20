# Effortless Email Management with AI

Adapt the published “Effortless Email Management with AI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Email Trigger #40;IMAP#41;"]
  n1["Markdown"]
  n2["Send Email"]
  n3["Qdrant Vector Store"]
  n4["Embeddings OpenAI"]
  n5["Email Summarization Chain"]
  n6["Write email"]
  n7["OpenAI"]
  n8["Gmail"]
  n9["Text Classifier"]
  n10["Edit Fields"]
  n11["When clicking #8216;Test workflow#8217;"]
  n12["Create collection"]
  n13["Refresh collection"]
  n14["Get folder"]
  n15["Download Files"]
  n16["Default Data Loader"]
  n17["Token Splitter"]
  n18["Qdrant Vector Store1"]
  n19["Embeddings OpenAI1"]
  n20["DeepSeek Chat Model"]
  n21["Email Reviewer"]
  n8 -->|"main out 0 to in 0"| n9
  n7 -->|"ai_languageModel out 0 to in 0"| n6
  n7 -->|"ai_languageModel out 0 to in 0"| n21
  n7 -->|"ai_languageModel out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n10
  n15 -->|"main out 0 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n10
  n17 -->|"ai_textSplitter out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 1 to in 0"| n21
  n4 -->|"ai_embedding out 0 to in 0"| n3
  n19 -->|"ai_embedding out 0 to in 0"| n18
  n13 -->|"main out 0 to in 0"| n14
  n20 -->|"ai_languageModel out 0 to in 0"| n5
  n16 -->|"ai_document out 0 to in 0"| n18
  n3 -->|"ai_tool out 0 to in 0"| n6
  n3 -->|"ai_tool out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n12
  n11 -->|"main out 0 to in 0"| n13
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
