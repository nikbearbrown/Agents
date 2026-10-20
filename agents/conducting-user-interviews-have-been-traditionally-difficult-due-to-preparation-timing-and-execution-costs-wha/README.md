# Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?

Adapt the published “Conducting user interviews have been traditionally difficult due to preparation, timing and execution costs. What if we let an AI/LLM do it instead?” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Stop Interview#63;"]
  n1["Generate Row"]
  n2["Generate Row1"]
  n3["Clear For Next Interview"]
  n4["Send Reply To Agent"]
  n5["Start Interview"]
  n6["Get Answer"]
  n7["Set Interview Topic"]
  n8["UUID"]
  n9["Generate Row2"]
  n10["Create Session"]
  n11["Update Session"]
  n12["Update Session1"]
  n13["Update Session2"]
  n14["Valid Session#63;"]
  n15["Respond to Webhook"]
  n16["Window Buffer Memory2"]
  n17["Window Buffer Memory"]
  n18["Redirect to Completion Screen"]
  n19["Webhook"]
  n20["404 Not Found"]
  n21["AI Researcher"]
  n22["Parse Response"]
  n23["Groq Chat Model"]
  n24["Show Transcript"]
  n25["Save to Google Sheet"]
  n26["Session to List"]
  n27["Messages To JSON"]
  n28["Query By Session"]
  n29["Get Session"]
  n8 -->|"main out 0 to in 0"| n10
  n19 -->|"main out 0 to in 0"| n28
  n6 -->|"main out 0 to in 0"| n1
  n29 -->|"main out 0 to in 0"| n26
  n1 -->|"main out 0 to in 0"| n12
  n20 -->|"main out 0 to in 0"| n15
  n21 -->|"main out 0 to in 0"| n22
  n2 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n9
  n22 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 0"| n24
  n14 -->|"main out 1 to in 0"| n20
  n23 -->|"ai_languageModel out 0 to in 0"| n21
  n26 -->|"main out 0 to in 0"| n27
  n24 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 0 to in 0"| n2
  n0 -->|"main out 1 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n3
  n27 -->|"main out 0 to in 0"| n25
  n28 -->|"main out 0 to in 0"| n14
  n4 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n21
  n17 -->|"ai_memory out 0 to in 0"| n3
  n16 -->|"ai_memory out 0 to in 0"| n21
  n3 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n29
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
