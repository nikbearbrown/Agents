# agente

Adapt the published “agente” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model1"]
  n1["Assistente clinica interno"]
  n2["Google Tasks"]
  n3["MCP Google Calendar"]
  n4["Receber Mensagem Telegram"]
  n5["Postgres Chat Memory"]
  n6["OpenAI Chat Model"]
  n7["Assistente Clínica"]
  n8["Enviar alerta de cancelamento"]
  n9["Gatilho diário"]
  n10["Assistente de confirmação"]
  n11["AI Agent"]
  n12["Postgres Chat Memory1"]
  n13["MCP Google Calendar2"]
  n14["MCP GMAIL"]
  n15["MCP CALENDAR"]
  n16["Telegram"]
  n17["OpenRouter Chat Model1"]
  n18["Webhook1"]
  n19["Edit Fields1"]
  n20["Switch"]
  n21["OpenAI"]
  n22["Evolution API"]
  n23["Convert to File"]
  n24["OpenAI1"]
  n25["AI Agent2"]
  n26["OpenRouter Chat Model2"]
  n27["Evolution API2"]
  n28["CallToHuman"]
  n29["OpenAI Chat Model2"]
  n30["REMINDER"]
  n21 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 0 to in 0"| n7
  n20 -->|"main out 1 to in 0"| n24
  n20 -->|"main out 2 to in 0"| n22
  n24 -->|"main out 0 to in 0"| n25
  n11 -->|"main out 0 to in 0"| n27
  n18 -->|"main out 0 to in 0"| n19
  n25 -->|"main out 0 to in 0"| n7
  n14 -->|"ai_tool out 0 to in 0"| n10
  n28 -->|"ai_tool out 0 to in 0"| n7
  n19 -->|"main out 0 to in 0"| n20
  n2 -->|"ai_tool out 0 to in 0"| n1
  n15 -->|"ai_tool out 0 to in 0"| n10
  n22 -->|"main out 0 to in 0"| n23
  n23 -->|"main out 0 to in 0"| n21
  n9 -->|"main out 0 to in 0"| n10
  n6 -->|"ai_languageModel out 0 to in 0"| n7
  n0 -->|"ai_languageModel out 0 to in 0"| n1
  n29 -->|"ai_languageModel out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n11
  n3 -->|"ai_tool out 0 to in 0"| n1
  n13 -->|"ai_tool out 0 to in 0"| n7
  n5 -->|"ai_memory out 0 to in 0"| n1
  n12 -->|"ai_memory out 0 to in 0"| n7
  n17 -->|"ai_languageModel out 0 to in 0"| n11
  n26 -->|"ai_languageModel out 0 to in 0"| n25
  n4 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n30
  n8 -->|"ai_tool out 0 to in 0"| n7
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
