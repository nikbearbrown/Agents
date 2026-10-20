# Email AI Auto-responder. Summerize and send email

Adapt the published “Email AI Auto-responder. Summerize and send email” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Email Trigger #40;IMAP#41;"]
  n1["Markdown"]
  n2["DeepSeek R1"]
  n3["Send Email"]
  n4["Qdrant Vector Store"]
  n5["Embeddings OpenAI"]
  n6["Email Classifier"]
  n7["Email Summarization Chain"]
  n8["Write email"]
  n9["Review email"]
  n10["When clicking #8216;Test workflow#8217;"]
  n11["Create collection"]
  n12["Refresh collection"]
  n13["Get folder"]
  n14["Download Files"]
  n15["Default Data Loader"]
  n16["Token Splitter"]
  n17["Qdrant Vector Store1"]
  n18["Embeddings OpenAI1"]
  n19["Do nothing"]
  n20["OpenAI"]
  n21["DeepSeek"]
  n22["OpenAI 4-o-mini"]
  n20 -->|"ai_languageModel out 0 to in 0"| n8
  n21 -->|"ai_languageModel out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n7
  n13 -->|"main out 0 to in 0"| n14
  n2 -->|"ai_languageModel out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n17
  n16 -->|"ai_textSplitter out 0 to in 0"| n15
  n22 -->|"ai_languageModel out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 1 to in 0"| n19
  n5 -->|"ai_embedding out 0 to in 0"| n4
  n18 -->|"ai_embedding out 0 to in 0"| n17
  n12 -->|"main out 0 to in 0"| n13
  n15 -->|"ai_document out 0 to in 0"| n17
  n4 -->|"ai_tool out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n1
  n7 -->|"main out 0 to in 0"| n6
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n12
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
