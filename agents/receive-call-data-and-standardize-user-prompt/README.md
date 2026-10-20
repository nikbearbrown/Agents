# Receive Call Data and standardize User Prompt

Adapt the published “Receive Call Data and standardize User Prompt” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Execute Workflow Trigger"]
  n1["Structured Output Parser1"]
  n2["Marketing AI Agent Processor"]
  n3["Structured Output Parser2"]
  n4["Product AI Agent Processor"]
  n5["Sales Data Processor"]
  n6["Marketing Data Processor"]
  n7["Product AI Data Processor"]
  n8["Data Recall Sales"]
  n9["Data Recall Marketing"]
  n10["Data Recall Product"]
  n11["SF Sales Data Processor"]
  n12["Azure OpenAI Chat Model"]
  n13["Azure OpenAI Chat Model1"]
  n14["Azure OpenAI Chat Model2"]
  n15["Create User Prompt"]
  n16["Success Status Generated"]
  n17["AI Agent"]
  n18["Structured Output Parser3"]
  n19["Merge all processed data"]
  n20["Bundle processed Data"]
  n17 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n5
  n8 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n4
  n15 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n19
  n20 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n6
  n12 -->|"ai_languageModel out 0 to in 0"| n17
  n13 -->|"ai_languageModel out 0 to in 0"| n2
  n14 -->|"ai_languageModel out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n15
  n6 -->|"main out 0 to in 1"| n19
  n19 -->|"main out 0 to in 0"| n20
  n7 -->|"main out 0 to in 2"| n19
  n1 -->|"ai_outputParser out 0 to in 0"| n2
  n3 -->|"ai_outputParser out 0 to in 0"| n4
  n18 -->|"ai_outputParser out 0 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n9
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
