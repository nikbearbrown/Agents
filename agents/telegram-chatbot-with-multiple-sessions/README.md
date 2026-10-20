# Telegram ChatBot with multiple sessions

Adapt the published “Telegram ChatBot with multiple sessions” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Simple Memory"]
  n2["Get message"]
  n3["Command or text#63;"]
  n4["Get session"]
  n5["Disable previous session"]
  n6["Set new session"]
  n7["Session activated"]
  n8["Send response"]
  n9["Update database"]
  n10["Summarization Chain"]
  n11["OpenAI Chat Model1"]
  n12["OpenAI Chat Model2"]
  n13["Basic LLM Chain"]
  n14["Get message1"]
  n15["Set to expire"]
  n16["Exist#63;"]
  n17["OK"]
  n18["KO"]
  n19["Trim resume"]
  n20["Get session1"]
  n21["Prompt #43; Resume"]
  n22["Send summary"]
  n23["Get message2"]
  n24["Trim question"]
  n25["Set new current session"]
  n26["Response #43; Text"]
  n27["fullText"]
  n28["Send answer"]
  n29["Send current session"]
  n30["Telegram Chatbot"]
  n16 -->|"main out 0 to in 0"| n18
  n16 -->|"main out 1 to in 0"| n17
  n27 -->|"main out 0 to in 0"| n13
  n2 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n3
  n19 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n19
  n23 -->|"main out 0 to in 0"| n24
  n20 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n9
  n15 -->|"main out 0 to in 0"| n25
  n1 -->|"ai_memory out 0 to in 0"| n30
  n24 -->|"main out 0 to in 0"| n26
  n13 -->|"main out 0 to in 0"| n28
  n21 -->|"main out 0 to in 0"| n10
  n26 -->|"main out 0 to in 0"| n27
  n6 -->|"main out 0 to in 0"| n7
  n3 -->|"main out 0 to in 0"| n5
  n3 -->|"main out 1 to in 0"| n29
  n3 -->|"main out 2 to in 0"| n14
  n3 -->|"main out 3 to in 0"| n20
  n3 -->|"main out 4 to in 0"| n23
  n3 -->|"main out 5 to in 0"| n30
  n30 -->|"main out 0 to in 0"| n8
  n0 -->|"ai_languageModel out 0 to in 0"| n30
  n11 -->|"ai_languageModel out 0 to in 0"| n10
  n12 -->|"ai_languageModel out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n22
  n25 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n6
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
