# Porxmox Custom AI Agent

Adapt the published “Porxmox Custom AI Agent” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["HTTP Request1"]
  n1["Proxmox API Documentation"]
  n2["Auto-fixing Output Parser"]
  n3["Google Gemini Chat Model1"]
  n4["Structured Output Parser"]
  n5["Proxmox"]
  n6["HTTP Request"]
  n7["Google Gemini Chat Model2"]
  n8["When chat message received"]
  n9["Telegram Trigger"]
  n10["Gmail Trigger"]
  n11["Webhook"]
  n12["Proxmox API Wiki"]
  n13["Structure Response"]
  n14["Structgure Response from Proxmox"]
  n15["Format Response and Hide Sensitive Data"]
  n16["If"]
  n17["HTTP Request2"]
  n18["Merge"]
  n19["HTTP Request3"]
  n20["Google Gemini Chat Model"]
  n21["AI Agent1"]
  n22["If1"]
  n23["HTTP Request4"]
  n24["Merge1"]
  n25["AI Agent"]
  n26["Switch"]
  n16 -->|"main out 0 to in 0"| n0
  n16 -->|"main out 1 to in 0"| n17
  n22 -->|"main out 0 to in 0"| n19
  n22 -->|"main out 1 to in 0"| n23
  n18 -->|"main out 0 to in 0"| n14
  n24 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n6
  n26 -->|"main out 1 to in 0"| n16
  n26 -->|"main out 4 to in 0"| n22
  n5 -->|"ai_tool out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n26
  n6 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 0 to in 1"| n18
  n19 -->|"main out 0 to in 0"| n24
  n23 -->|"main out 0 to in 1"| n24
  n12 -->|"ai_tool out 0 to in 0"| n25
  n13 -->|"main out 0 to in 0"| n21
  n20 -->|"ai_languageModel out 0 to in 0"| n25
  n4 -->|"ai_outputParser out 0 to in 0"| n2
  n2 -->|"ai_outputParser out 0 to in 0"| n25
  n3 -->|"ai_languageModel out 0 to in 0"| n2
  n7 -->|"ai_languageModel out 0 to in 0"| n21
  n1 -->|"ai_tool out 0 to in 0"| n25
  n8 -->|"main out 0 to in 0"| n25
  n14 -->|"main out 0 to in 0"| n15
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
