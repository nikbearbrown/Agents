# nl2sql

Adapt the published “nl2sql” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["DeepSeek Chat Model"]
  n2["Return Final Response"]
  n3["Webhook"]
  n4["Format Success Result"]
  n5["Chat Memory Manager"]
  n6["Format History"]
  n7["DeepSeek Chat Model1"]
  n8["Format Charts"]
  n9["Charts Agent"]
  n10["Loop Entry"]
  n11["If Can Retry"]
  n12["Format Error Prompt"]
  n13["If Error"]
  n14["Search Memory"]
  n15["Extract User Input"]
  n16["Get DB Schema"]
  n17["Format Schema"]
  n18["Prepare Initial Prompt"]
  n19["Execute Generated SQL"]
  n20["Insert Memory"]
  n21["If Charts"]
  n22["If Ai Error"]
  n23["Google Gemini Chat Model"]
  n0 -->|"main out 0 to in 0"| n22
  n3 -->|"main out 0 to in 0"| n15
  n4 -->|"main out 0 to in 0"| n21
  n5 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n16
  n1 -->|"ai_languageModel out 0 to in 0"| n0
  n7 -->|"ai_languageModel out 0 to in 0"| n9
  n8 -->|"main out 0 to in 0"| n2
  n9 -->|"main out 0 to in 0"| n8
  n10 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n10
  n11 -->|"main out 1 to in 0"| n4
  n12 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 1 to in 0"| n4
  n14 -->|"ai_memory out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n5
  n16 -->|"main out 0 to in 0"| n17
  n17 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n10
  n19 -->|"main out 0 to in 0"| n13
  n20 -->|"ai_memory out 0 to in 0"| n0
  n21 -->|"main out 0 to in 0"| n8
  n21 -->|"main out 1 to in 0"| n9
  n22 -->|"main out 0 to in 0"| n19
  n22 -->|"main out 1 to in 0"| n8
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/Wilsonoonn--n8n_nl2sql.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
