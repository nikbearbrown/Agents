# MiniBear Webhook

Adapt the published “MiniBear Webhook” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 26 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Line Webhook"]
  n1["Line Loading Animation"]
  n2["Switch"]
  n3["Get Image"]
  n4["Line Reply #40;image#41;"]
  n5["Line Reply #40;Text#41;"]
  n6["Line Reply #40;Not Supported 2#41;"]
  n7["Line Reply #40;Not Supported 1#41;"]
  n8["OpenRouter Chat Model"]
  n9["Image Router"]
  n10["Microsoft Teams"]
  n11["Microsoft To Do"]
  n12["Line Reply #40;Text#41;1"]
  n13["If namecard"]
  n14["Other Images"]
  n15["Microsoft Teams1"]
  n16["OpenRouter Chat Model2"]
  n17["Microsoft OneDrive"]
  n18["Microsoft OneDrive1"]
  n19["Get Image2"]
  n20["Microsoft To Do1"]
  n21["HTTP Request"]
  n22["OpenRouter Chat Model3"]
  n23["NamecardExtract"]
  n24["Structured Output Parser"]
  n25["Line Reply Namecard"]
  n26["Get Image3"]
  n2 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 1 to in 0"| n10
  n2 -->|"main out 2 to in 0"| n3
  n2 -->|"main out 3 to in 0"| n7
  n2 -->|"main out 4 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n9
  n19 -->|"main out 0 to in 0"| n14
  n26 -->|"main out 0 to in 0"| n23
  n13 -->|"main out 0 to in 0"| n26
  n13 -->|"main out 1 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n5
  n11 -->|"main out 0 to in 0"| n12
  n23 -->|"main out 0 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n4
  n20 -->|"main out 0 to in 0"| n25
  n17 -->|"main out 0 to in 0"| n18
  n25 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n19
  n8 -->|"ai_languageModel out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n2
  n16 -->|"ai_languageModel out 0 to in 0"| n14
  n22 -->|"ai_languageModel out 0 to in 0"| n23
  n24 -->|"ai_outputParser out 0 to in 0"| n23
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
