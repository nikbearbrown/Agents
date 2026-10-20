# n8n Graphic Design Team

Adapt the published “n8n Graphic Design Team” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Google Sheets"]
  n1["SetImageData"]
  n2["Google Drive"]
  n3["Download Image3"]
  n4["ideogram Remix"]
  n5["Set Upload Fields1"]
  n6["Structured Output Parser1"]
  n7["Switch1"]
  n8["Image Reviewer"]
  n9["OpenAI Chat Model1"]
  n10["Google Drive Remix Image"]
  n11["Google Sheets - Add Remix"]
  n12["genImageURL1"]
  n13["genImageURL2"]
  n14["Download Image"]
  n15["TheImageURL"]
  n16["Gmail"]
  n17["creative brief"]
  n18["Ideogram Image generator"]
  n19["GET image"]
  n20["RE creative brief"]
  n21["Get Remixed Image"]
  n22["When clicking #8216;Test workflow#8217;"]
  n23["Convert to File"]
  n24["Spreadsheet"]
  n25["Google Drive - Create Folder"]
  n26["Google Drive - Create Generations Folder"]
  n27["Google Drive - Upload Spreadsheet"]
  n28["Gmail - Send Setup Details"]
  n29["On form submission"]
  n7 -->|"main out 0 to in 0"| n16
  n7 -->|"main out 1 to in 0"| n20
  n19 -->|"main out 0 to in 0"| n2
  n24 -->|"main out 0 to in 0"| n23
  n15 -->|"main out 0 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n0
  n1 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n15
  n13 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n12
  n14 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n7
  n17 -->|"main out 0 to in 0"| n18
  n4 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n27
  n3 -->|"main out 0 to in 0"| n4
  n21 -->|"main out 0 to in 0"| n10
  n20 -->|"main out 0 to in 0"| n3
  n29 -->|"main out 0 to in 0"| n17
  n9 -->|"ai_languageModel out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n21
  n10 -->|"main out 0 to in 0"| n11
  n18 -->|"main out 0 to in 0"| n1
  n11 -->|"main out 0 to in 0"| n13
  n6 -->|"ai_outputParser out 0 to in 0"| n8
  n25 -->|"main out 0 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n28
  n22 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n24
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
