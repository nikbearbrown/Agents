# Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion

Adapt the published “Deep Research Report Generation Using Open Router, Google Search, Webhook/Telegram and Notion” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 37 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Telegram Trigger"]
  n1["Simple Memory"]
  n2["Structured Output Parser"]
  n3["Switch"]
  n4["Strategy Agent"]
  n5["Search Query Agent"]
  n6["Structured Output Parser1"]
  n7["Split Out"]
  n8["Loop Over Queries"]
  n9["HTTP Request"]
  n10["Edit Fields"]
  n11["OpenAI"]
  n12["HTTP Request1"]
  n13["Aggregate"]
  n14["AI Agent"]
  n15["OpenAI1"]
  n16["Notion"]
  n17["Notion1"]
  n18["HTTP Request2"]
  n19["Convert to HTML"]
  n20["HTML to Array"]
  n21["Tags to Items"]
  n22["Notion Block Generator"]
  n23["Google Gemini Chat Model"]
  n24["Parse JSON blocks"]
  n25["Valid Blocks"]
  n26["For Each Block..."]
  n27["Get Existing Row"]
  n28["Code"]
  n29["Aggregate1"]
  n30["OpenRouter Chat Model"]
  n31["OpenRouter Chat Model1"]
  n32["OpenRouter Chat Model2"]
  n33["Webhook"]
  n34["Respond to Webhook"]
  n35["Respond to Webhook1"]
  n36["HTTP Request3"]
  n1 -->|"ai_memory out 0 to in 0"| n4
  n2 -->|"ai_outputParser out 0 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n34
  n3 -->|"main out 1 to in 0"| n35
  n4 -->|"main out 0 to in 0"| n3
  n6 -->|"ai_outputParser out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n13
  n8 -->|"main out 1 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n10
  n10 -->|"main out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n12
  n12 -->|"main out 0 to in 0"| n8
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n27
  n15 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n36
  n19 -->|"main out 0 to in 0"| n20
  n20 -->|"main out 0 to in 0"| n21
  n21 -->|"main out 0 to in 0"| n22
  n23 -->|"ai_languageModel out 0 to in 0"| n22
  n22 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n26
  n26 -->|"main out 0 to in 0"| n29
  n26 -->|"main out 1 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n19
  n28 -->|"main out 0 to in 0"| n15
  n29 -->|"main out 0 to in 0"| n17
  n16 -->|"main out 0 to in 0"| n5
  n30 -->|"ai_languageModel out 0 to in 0"| n4
  n31 -->|"ai_languageModel out 0 to in 0"| n5
  n32 -->|"ai_languageModel out 0 to in 0"| n14
  n33 -->|"main out 0 to in 0"| n4
  n35 -->|"main out 0 to in 0"| n28
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
