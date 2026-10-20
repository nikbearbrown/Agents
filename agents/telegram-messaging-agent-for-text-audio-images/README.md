# 🤖 Telegram Messaging Agent for Text/Audio/Images

Adapt the published “🤖 Telegram Messaging Agent for Text/Audio/Images” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Check User #38; Chat ID"]
  n1["Error message"]
  n2["Listen for Telegram Events"]
  n3["Set Webhook Test URL"]
  n4["Get Telegram Webhook Info"]
  n5["Image Schema"]
  n6["gpt-4o-mini"]
  n7["Get Audio File"]
  n8["Get Image"]
  n9["Analyze Image"]
  n10["Transcribe Recording"]
  n11["gpt-4o-mini1"]
  n12["Test Webhook Status"]
  n13["Production Webhook Status"]
  n14["Set Webhook Production URL"]
  n15["Edit Fields"]
  n16["Audio Task Message"]
  n17["Audio Other Message"]
  n18["Text Task Message"]
  n19["Text Other Message"]
  n20["Image Message"]
  n21["Convert to Image File"]
  n22["Extract from File to Base64"]
  n23["Text Classifier Audio"]
  n24["Text Classifier"]
  n25["Telegram Token #38; Webhooks"]
  n26["Get Webhook Status"]
  n27["Validation"]
  n28["Message Router"]
  n8 -->|"main out 0 to in 0"| n22
  n27 -->|"main out 0 to in 0"| n0
  n15 -->|"main out 0 to in 0"| n24
  n6 -->|"ai_languageModel out 0 to in 0"| n23
  n5 -->|"main out 0 to in 0"| n8
  n11 -->|"ai_languageModel out 0 to in 0"| n24
  n9 -->|"main out 0 to in 0"| n20
  n7 -->|"main out 0 to in 0"| n10
  n28 -->|"main out 0 to in 0"| n7
  n28 -->|"main out 1 to in 0"| n15
  n28 -->|"main out 2 to in 0"| n5
  n28 -->|"main out 3 to in 0"| n1
  n24 -->|"main out 0 to in 0"| n18
  n24 -->|"main out 1 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n28
  n0 -->|"main out 1 to in 0"| n1
  n3 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n23
  n21 -->|"main out 0 to in 0"| n9
  n23 -->|"main out 0 to in 0"| n16
  n23 -->|"main out 1 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n26
  n25 -->|"main out 0 to in 0"| n14
  n25 -->|"main out 0 to in 0"| n3
  n25 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n27
  n14 -->|"main out 0 to in 0"| n13
  n22 -->|"main out 0 to in 0"| n21
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
