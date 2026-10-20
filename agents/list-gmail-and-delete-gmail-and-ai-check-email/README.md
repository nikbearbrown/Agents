# list gmail and delete gmail and ai check email

Adapt the published “list gmail and delete gmail and ai check email” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Gmail Get Email"]
  n1["When clicking #8216;Test workflow#8217;"]
  n2["Google Gemini Chat Model"]
  n3["GmailDeleteEmail"]
  n4["AI Check Email"]
  n5["Unwanted Email Output Parser"]
  n6["If Unwanted Marketing or Spam"]
  n7["Telegram Sent Email Deleted Notification"]
  n8["Telegram Sent Email Not Deleted Notification"]
  n9["Telegram Sent AI Error Notification"]
  n10["Telegram Sent Delete Email Failed Notification"]
  n11["Success"]
  n12["Increment Loop Var"]
  n13["Forward Prev Page Num"]
  n14["Initialize Loop Vars"]
  n15["Aggregate"]
  n16["Gmail"]
  n16 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n6
  n4 -->|"main out 1 to in 0"| n9
  n0 -->|"main out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 1 to in 0"| n10
  n12 -->|"main out 0 to in 0"| n0
  n14 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n14
  n2 -->|"ai_languageModel out 0 to in 0"| n4
  n5 -->|"ai_outputParser out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n3
  n6 -->|"main out 1 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 1 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 1 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 1 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n11
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
