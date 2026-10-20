# Podcast Digest

Adapt the published “Podcast Digest” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 15 executable nodes and 14 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Execute Workflow#34;"]
  n1["Podcast Episode Transcript"]
  n2["Workflow Input to JSON Document"]
  n3["Recursive Character Text Splitter"]
  n4["Topics"]
  n5["Summarize Transcript"]
  n6["GPT 4 - Extract"]
  n7["Wikipedia1"]
  n8["Send Digest"]
  n9["Format topic text #38; title"]
  n10["Structured Output Parser"]
  n11["Extract Topics #38; Questions"]
  n12["GPT3.5 - Research"]
  n13["GPT3.5 - Summarize"]
  n14["Research #38; Explain Topics"]
  n4 -->|"main out 0 to in 0"| n14
  n7 -->|"ai_tool out 0 to in 0"| n14
  n6 -->|"ai_languageModel out 0 to in 0"| n11
  n12 -->|"ai_languageModel out 0 to in 0"| n14
  n13 -->|"ai_languageModel out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n11
  n10 -->|"ai_outputParser out 0 to in 0"| n11
  n9 -->|"main out 0 to in 0"| n8
  n14 -->|"main out 0 to in 0"| n9
  n11 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n5
  n2 -->|"ai_document out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n1
  n3 -->|"ai_textSplitter out 0 to in 0"| n2
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
