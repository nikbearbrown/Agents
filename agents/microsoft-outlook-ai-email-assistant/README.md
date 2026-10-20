# Microsoft Outlook AI Email Assistant

Adapt the published “Microsoft Outlook AI Email Assistant” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Microsoft Outlook23"]
  n2["OpenAI Chat Model"]
  n3["Set Category"]
  n4["Structured Output Parser"]
  n5["If"]
  n6["Set Importance"]
  n7["AI: Analyse Email"]
  n8["Check Mail Schedule Trigger"]
  n9["Update Contacts Schedule Trigger"]
  n10["Monday.com - Get Contacts"]
  n11["Airtable - Contacts"]
  n12["Convert to Markdown"]
  n13["Email Messages"]
  n14["Rules"]
  n15["Categories"]
  n16["Delete Rules"]
  n17["Contact"]
  n18["Loop Over Items"]
  n19["Merge"]
  n5 -->|"main out 0 to in 0"| n6
  n5 -->|"main out 1 to in 0"| n18
  n19 -->|"main out 0 to in 0"| n7
  n14 -->|"main out 0 to in 1"| n19
  n17 -->|"main out 0 to in 0"| n19
  n15 -->|"main out 0 to in 2"| n19
  n16 -->|"main out 0 to in 3"| n19
  n3 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n18
  n6 -->|"main out 0 to in 0"| n18
  n18 -->|"main out 1 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n3
  n2 -->|"ai_languageModel out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n13
  n1 -->|"main out 0 to in 0"| n12
  n4 -->|"ai_outputParser out 0 to in 0"| n7
  n10 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n1
  n9 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n16
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
