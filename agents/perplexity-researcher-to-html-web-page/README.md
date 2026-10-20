# 🔍🛠️Perplexity Researcher to HTML Web Page

Adapt the published “🔍🛠️Perplexity Researcher to HTML Web Page” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 38 executable nodes and 36 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["gpt-4o-mini"]
  n1["gpt-4o-mini1"]
  n2["Structured Output Parser1"]
  n3["gpt-4o-mini2"]
  n4["Webhook"]
  n5["Respond to Webhook"]
  n6["Telegram"]
  n7["gpt-4o-mini5"]
  n8["Basic LLM Chain"]
  n9["Do Nothing1"]
  n10["gpt-4o-mini3"]
  n11["If2"]
  n12["Prompts"]
  n13["Execute Workflow Trigger"]
  n14["Telegram2"]
  n15["If"]
  n16["No Operation, do nothing"]
  n17["Perplexity Topic Agent"]
  n18["Call Perplexity Researcher"]
  n19["Do Nothing"]
  n20["Do Nothing2"]
  n21["Do Nothing3"]
  n22["Do Nothing4"]
  n23["Get Topic"]
  n24["If Topic Exists"]
  n25["Improve Users Topic"]
  n26["If Topic"]
  n27["Chat Id"]
  n28["Article"]
  n29["Extract JSON"]
  n30["If Article"]
  n31["Create HTML Article"]
  n32["If HTML"]
  n33["Contents"]
  n34["Chat Id1"]
  n35["Success Response"]
  n36["Error Response"]
  n37["Perplexity"]
  n15 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 1 to in 0"| n16
  n11 -->|"main out 0 to in 0"| n29
  n11 -->|"main out 1 to in 0"| n19
  n28 -->|"main out 0 to in 0"| n30
  n27 -->|"main out 0 to in 0"| n6
  n32 -->|"main out 0 to in 0"| n33
  n32 -->|"main out 1 to in 0"| n21
  n12 -->|"main out 0 to in 0"| n37
  n4 -->|"main out 0 to in 0"| n23
  n34 -->|"main out 0 to in 0"| n14
  n33 -->|"main out 0 to in 0"| n8
  n26 -->|"main out 0 to in 0"| n17
  n26 -->|"main out 1 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n24
  n14 -->|"main out 0 to in 0"| n15
  n30 -->|"main out 0 to in 0"| n31
  n30 -->|"main out 1 to in 0"| n20
  n37 -->|"main out 0 to in 0"| n35
  n0 -->|"ai_languageModel out 0 to in 0"| n31
  n29 -->|"main out 0 to in 0"| n28
  n1 -->|"ai_languageModel out 0 to in 0"| n17
  n3 -->|"ai_languageModel out 0 to in 0"| n29
  n10 -->|"ai_languageModel out 0 to in 0"| n25
  n7 -->|"ai_languageModel out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n5
  n24 -->|"main out 0 to in 0"| n25
  n24 -->|"main out 1 to in 0"| n9
  n31 -->|"main out 0 to in 0"| n32
  n25 -->|"main out 0 to in 0"| n26
  n17 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n27
  n13 -->|"main out 0 to in 0"| n34
  n16 -->|"main out 0 to in 0"| n36
  n2 -->|"ai_outputParser out 0 to in 0"| n29
  n18 -->|"ai_tool out 0 to in 0"| n17
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
