# ✍️🌄 Your First Wordpress Content Creator - Quick Start

Adapt the published “✍️🌄 Your First Wordpress Content Creator - Quick Start” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 28 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["gpt-4o-mini"]
  n2["Structured Output - JSON"]
  n3["Separate Title #38; Content"]
  n4["gpt-4o-mini1"]
  n5["If1"]
  n6["gpt-4o-mini2"]
  n7["If2"]
  n8["gpt-4o-mini3"]
  n9["If3"]
  n10["Rewrite for Grade 5 Reading Level"]
  n11["Rewrite for Grade 2 Reading Level"]
  n12["Rewrite for Grade 9 Reading Level"]
  n13["Create Structured Blog Post"]
  n14["DeepSeek"]
  n15["Google Drive"]
  n16["Set Blog Topic"]
  n17["pollinations.ai"]
  n18["Create Wordpress Post"]
  n19["Upload Image to Wordpress"]
  n20["Set Image on Wordpress Post"]
  n21["HTML to Markdown"]
  n22["Tiltle #38; Content Exist#63;"]
  n23["Send Error Message"]
  n24["Send Error Message1"]
  n25["Send Error Message2"]
  n26["Send Error Message3"]
  n27["Send Success Message"]
  n5 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 1 to in 0"| n24
  n7 -->|"main out 1 to in 0"| n25
  n9 -->|"main out 1 to in 0"| n26
  n1 -->|"ai_languageModel out 0 to in 0"| n13
  n4 -->|"ai_languageModel out 0 to in 0"| n12
  n6 -->|"ai_languageModel out 0 to in 0"| n10
  n8 -->|"ai_languageModel out 0 to in 0"| n11
  n16 -->|"main out 0 to in 0"| n13
  n17 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n12
  n21 -->|"main out 0 to in 0"| n15
  n18 -->|"main out 0 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n21
  n22 -->|"main out 1 to in 0"| n23
  n3 -->|"main out 0 to in 0"| n22
  n2 -->|"ai_outputParser out 0 to in 0"| n13
  n19 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n3
  n20 -->|"main out 0 to in 0"| n27
  n11 -->|"main out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n16
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
