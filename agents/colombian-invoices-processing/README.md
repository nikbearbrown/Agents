# Colombian Invoices Processing

Adapt the published “Colombian Invoices Processing” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 22 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Loop Over Items"]
  n1["OpenAI Chat Model"]
  n2["Calculator"]
  n3["Structured Output Parser"]
  n4["On Email receipt"]
  n5["Get Filename and mimeType"]
  n6["Filter ZIP files only"]
  n7["Unzip Invoice"]
  n8["Just for style"]
  n9["Get filename and mimeType on extracted docs"]
  n10["Split XML and PDF"]
  n11["Extract PDF Data"]
  n12["Extract XML Data"]
  n13["Convert to JSON"]
  n14["Append both Docs"]
  n15["Aggregate all Data into 1 list"]
  n16["Extract Data from PDF and XML"]
  n17["Create initial PDF"]
  n18["Merge both flows"]
  n19["Update PDF with actual name"]
  n20["Get Current Date"]
  n21["Create or update row"]
  n2 -->|"ai_tool out 0 to in 0"| n16
  n7 -->|"main out 0 to in 0"| n0
  n13 -->|"main out 0 to in 1"| n14
  n0 -->|"main out 0 to in 0"| n8
  n0 -->|"main out 1 to in 0"| n9
  n14 -->|"main out 0 to in 0"| n15
  n11 -->|"main out 0 to in 0"| n14
  n12 -->|"main out 0 to in 0"| n13
  n20 -->|"main out 0 to in 0"| n21
  n18 -->|"main out 0 to in 0"| n19
  n4 -->|"main out 0 to in 0"| n5
  n1 -->|"ai_languageModel out 0 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n17
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 1 to in 0"| n12
  n17 -->|"main out 0 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n0
  n6 -->|"main out 0 to in 0"| n7
  n3 -->|"ai_outputParser out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 1"| n18
  n15 -->|"main out 0 to in 0"| n16
  n9 -->|"main out 0 to in 0"| n10
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
