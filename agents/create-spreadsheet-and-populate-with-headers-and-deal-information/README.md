# Create spreadsheet and populate with headers and deal information

Adapt the published “Create spreadsheet and populate with headers and deal information” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 40 executable nodes and 42 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Generate reply"]
  n1["On email received"]
  n2["Only continue for specific emails"]
  n3["Configure"]
  n4["Send reply to recipient"]
  n5["Generate UUID"]
  n6["Thanks for your response#33;"]
  n7["Extract message content #40;advanced#41;"]
  n8["If spreadsheet doesn#39;t exist"]
  n9["Successfully created or updated row"]
  n10["Create spreadsheet"]
  n11["Store spreadsheet ID"]
  n12["Paste data"]
  n13["If no sheet IDs"]
  n14["Create or update rows"]
  n15["Get data from #96;Format data#96;"]
  n16["Get data from #96;Format data#96; node"]
  n17["Format data"]
  n18["Send email reply"]
  n19["On feedback given"]
  n20["Send feedback for fine-tuned data"]
  n21["Show HTML page"]
  n22["Get sheet IDs #35;1"]
  n23["If no spreadsheet in configuration #35;2"]
  n24["Store specific sheet IDs #35;2"]
  n25["Get sheet IDs #35;2"]
  n26["If no spreadsheet in configuration #35;1"]
  n27["Store specific sheet IDs #35;1"]
  n28["Email template"]
  n29["Record feedback"]
  n30["Fallback route"]
  n31["Identify trigger #35;2"]
  n32["Identify trigger #35;1"]
  n33["Do not send unfinished email reply"]
  n34["If reply is complete"]
  n35["Do not send email to this recipient"]
  n36["Send reply to database"]
  n37["Determine which trigger ran"]
  n38["Is text within token limit#63;"]
  n39["Do nothing"]
  n3 -->|"main out 0 to in 0"| n37
  n17 -->|"main out 0 to in 0"| n26
  n5 -->|"main out 0 to in 0"| n7
  n28 -->|"main out 0 to in 0"| n4
  n0 -->|"main out 0 to in 0"| n36
  n0 -->|"main out 0 to in 0"| n34
  n21 -->|"main out 0 to in 0"| n23
  n13 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 1 to in 0"| n15
  n29 -->|"main out 0 to in 0"| n6
  n22 -->|"main out 0 to in 0"| n13
  n25 -->|"main out 0 to in 0"| n20
  n18 -->|"main out 0 to in 0"| n28
  n1 -->|"main out 0 to in 0"| n32
  n19 -->|"main out 0 to in 0"| n31
  n10 -->|"main out 0 to in 0"| n11
  n32 -->|"main out 0 to in 0"| n3
  n31 -->|"main out 0 to in 0"| n3
  n34 -->|"main out 0 to in 0"| n18
  n34 -->|"main out 1 to in 0"| n33
  n11 -->|"main out 0 to in 0"| n16
  n14 -->|"main out 0 to in 0"| n8
  n36 -->|"main out 0 to in 0"| n17
  n6 -->|"main out 0 to in 0"| n21
  n37 -->|"main out 0 to in 0"| n2
  n37 -->|"main out 1 to in 0"| n29
  n37 -->|"main out 3 to in 0"| n30
  n15 -->|"main out 0 to in 0"| n14
  n38 -->|"main out 0 to in 0"| n0
  n38 -->|"main out 1 to in 0"| n39
  n27 -->|"main out 0 to in 0"| n13
  n24 -->|"main out 0 to in 0"| n20
  n8 -->|"main out 0 to in 0"| n10
  n8 -->|"main out 1 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n5
  n2 -->|"main out 1 to in 0"| n35
  n7 -->|"main out 0 to in 0"| n38
  n26 -->|"main out 0 to in 0"| n22
  n26 -->|"main out 1 to in 0"| n27
  n23 -->|"main out 0 to in 0"| n25
  n23 -->|"main out 1 to in 0"| n24
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
