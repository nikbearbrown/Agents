# 🙋‍♂️ Why not just use the built-in PDF convertor?

Adapt the published “🙋‍♂️ Why not just use the built-in PDF convertor?” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 17 executable nodes and 18 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Model"]
  n1["Structured Output Parser"]
  n2["Upload to LlamaParse"]
  n3["Receiving Invoices"]
  n4["Append to Reconciliation Sheet"]
  n5["Get Processing Status"]
  n6["Wait to stay within service limits"]
  n7["Is Job Ready#63;"]
  n8["Add #34;invoice synced#34; Label"]
  n9["Get Parsed Invoice Data"]
  n10["Map Output"]
  n11["Apply Data Extraction Rules"]
  n12["Should Process Email#63;"]
  n13["Split Out Labels"]
  n14["Get Labels Names"]
  n15["Combine Label Names"]
  n16["Email with Label Names"]
  n10 -->|"main out 0 to in 0"| n4
  n0 -->|"ai_languageModel out 0 to in 0"| n11
  n7 -->|"main out 0 to in 0"| n9
  n7 -->|"main out 3 to in 0"| n6
  n14 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 0"| n14
  n3 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 1"| n16
  n2 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n2
  n16 -->|"main out 0 to in 0"| n12
  n9 -->|"main out 0 to in 0"| n11
  n1 -->|"ai_outputParser out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n10
  n4 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n5
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
