# LLM Chaining examples

Adapt the published “LLM Chaining examples” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 31 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["HTTP Request"]
  n2["Markdown"]
  n3["Anthropic Chat Model"]
  n4["Anthropic Chat Model1"]
  n5["Anthropic Chat Model2"]
  n6["Anthropic Chat Model3"]
  n7["Merge"]
  n8["Simple Memory"]
  n9["Clean memory"]
  n10["Initial prompts"]
  n11["Split Out"]
  n12["Reshape"]
  n13["Anthropic Chat Model4"]
  n14["Merge2"]
  n15["Basic LLM Chain4"]
  n16["Split Out1"]
  n17["Anthropic Chat Model5"]
  n18["Webhook"]
  n19["CONNECT ME"]
  n20["CONNECT ME1"]
  n21["CONNECT ME2"]
  n22["Initial prompts1"]
  n23["LLM Chain - Step 1"]
  n24["LLM Chain - Step 2"]
  n25["LLM Chain - Step 3"]
  n26["LLM Chain - Step 4"]
  n27["All LLM steps here - sequentially"]
  n28["LLM steps - parallel"]
  n29["Merge output with initial prompts"]
  n30["Merge output with initial prompts1"]
  n7 -->|"main out 0 to in 0"| n27
  n7 -->|"main out 0 to in 0"| n30
  n14 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n29
  n12 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 1"| n7
  n19 -->|"main out 0 to in 0"| n23
  n16 -->|"main out 0 to in 1"| n14
  n20 -->|"main out 0 to in 0"| n9
  n20 -->|"main out 0 to in 0"| n7
  n21 -->|"main out 0 to in 0"| n22
  n21 -->|"main out 0 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n2
  n8 -->|"ai_memory out 0 to in 0"| n27
  n8 -->|"ai_memory out 0 to in 0"| n9
  n10 -->|"main out 0 to in 0"| n12
  n22 -->|"main out 0 to in 0"| n16
  n23 -->|"main out 0 to in 0"| n24
  n24 -->|"main out 0 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n26
  n3 -->|"ai_languageModel out 0 to in 0"| n23
  n28 -->|"main out 0 to in 1"| n29
  n4 -->|"ai_languageModel out 0 to in 0"| n24
  n5 -->|"ai_languageModel out 0 to in 0"| n25
  n6 -->|"ai_languageModel out 0 to in 0"| n26
  n13 -->|"ai_languageModel out 0 to in 0"| n27
  n17 -->|"ai_languageModel out 0 to in 0"| n15
  n27 -->|"main out 0 to in 1"| n30
  n0 -->|"main out 0 to in 0"| n1
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
