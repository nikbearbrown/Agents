# 🧠 Give Your AI Agent Chatbot Long Term Memory Tools Router

Adapt the published “🧠 Give Your AI Agent Chatbot Long Term Memory Tools Router” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 20 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When Executed by Another Workflow"]
  n1["Save Long Term Memories"]
  n2["Saved response"]
  n3["Respond with long term memories"]
  n4["Retrieve Long Term Memories3"]
  n5["Send Success Message to Telegram"]
  n6["Email Workflow Stats"]
  n7["OpenAI Chat Model2"]
  n8["OpenAI Chat Model3"]
  n9["#128228;Send Memories to Telegram"]
  n10["#128235;Send Memories to Gmail"]
  n11["#129504;Save Memories"]
  n12["#128270;Retrieve Memories"]
  n13["#129327;Window Buffer Memory"]
  n14["#129504; AI Agent w/Long Term Memory"]
  n15["#129302;OpenAI Chat Model"]
  n16["#9410;#65039; When chat message received"]
  n17["Prepare Telegram Message"]
  n18["Prepare Gmail Message"]
  n19["Retrieve Long Term Memories"]
  n20["Memory Tool Router"]
  n21["Retrieve Long Term Memories2"]
  n11 -->|"ai_tool out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n1
  n20 -->|"main out 1 to in 0"| n19
  n20 -->|"main out 2 to in 0"| n21
  n20 -->|"main out 3 to in 0"| n4
  n7 -->|"ai_languageModel out 0 to in 0"| n17
  n8 -->|"ai_languageModel out 0 to in 0"| n18
  n18 -->|"main out 0 to in 0"| n6
  n12 -->|"ai_tool out 0 to in 0"| n14
  n15 -->|"ai_languageModel out 0 to in 0"| n14
  n1 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n5
  n13 -->|"ai_memory out 0 to in 0"| n14
  n10 -->|"ai_tool out 0 to in 0"| n14
  n19 -->|"main out 0 to in 0"| n3
  n21 -->|"main out 0 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n18
  n9 -->|"ai_tool out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 0"| n14
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
