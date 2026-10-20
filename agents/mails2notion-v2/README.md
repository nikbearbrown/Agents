# mails2notion V2

Adapt the published “mails2notion V2” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 25 executable nodes and 24 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Calculator"]
  n2["Structured Output Parser"]
  n3["Add Label #34;Processed#34;"]
  n4["Active Routes Only"]
  n5["Extract Route ID"]
  n6["Deactivate Route"]
  n7["Add Label #34;Error#34;"]
  n8["Send notification about deactivated route"]
  n9["Send notification about missing route"]
  n10["Get Route by ID"]
  n11["Create Notion Page"]
  n12["Gmail Trigger"]
  n13["Filter for unprocessed mails"]
  n14["When clicking #8216;Test workflow#8217;"]
  n15["Required labels"]
  n16["Globals"]
  n17["No Operation, do nothing"]
  n18["Format Notion Page Blocks"]
  n19["Get all labels"]
  n20["Structured Output Parser1"]
  n21["Calculator1"]
  n22["OpenAI Chat Model1"]
  n23["Generate Actionable Task"]
  n24["Get Summary #38; Meta Data"]
  n16 -->|"main out 0 to in 0"| n13
  n1 -->|"ai_tool out 0 to in 0"| n24
  n21 -->|"ai_tool out 0 to in 0"| n23
  n12 -->|"main out 0 to in 0"| n16
  n19 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 1 to in 0"| n17
  n6 -->|"main out 0 to in 0"| n8
  n5 -->|"main out 0 to in 0"| n10
  n0 -->|"ai_languageModel out 0 to in 0"| n24
  n4 -->|"main out 0 to in 0"| n23
  n11 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 1 to in 0"| n6
  n22 -->|"ai_languageModel out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n18
  n23 -->|"main out 0 to in 0"| n24
  n17 -->|"main out 0 to in 0"| n9
  n2 -->|"ai_outputParser out 0 to in 0"| n24
  n18 -->|"main out 0 to in 0"| n11
  n20 -->|"ai_outputParser out 0 to in 0"| n23
  n13 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n19
  n9 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n7
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
