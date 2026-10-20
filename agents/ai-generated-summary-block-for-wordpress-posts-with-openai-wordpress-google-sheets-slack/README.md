# AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets &amp; Slack

Adapt the published “AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets &amp; Slack” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 21 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Text Classifier"]
  n2["OpenAI Chat Model"]
  n3["Loop Over Items"]
  n4["If"]
  n5["Webhook"]
  n6["Schedule Trigger"]
  n7["Wordpress - Update Post"]
  n8["Google Sheets - Get rows"]
  n9["HTML to Markdown"]
  n10["OpenAI"]
  n11["Google Sheets - Add Row"]
  n12["Slack - Notify Channel"]
  n13["Set fields - From Webhook input"]
  n14["Date #38; Time - Substract"]
  n15["Set fields - Prepare data for Gsheets #38; Slack"]
  n16["WordPress - Get Post2"]
  n17["No Operation, do nothing"]
  n18["WordPress - Get Last Posts"]
  n19["WordPress - Get Post1"]
  n20["WordPress - Get All Posts"]
  n4 -->|"main out 0 to in 0"| n3
  n4 -->|"main out 1 to in 0"| n16
  n10 -->|"main out 0 to in 0"| n7
  n5 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n17
  n3 -->|"main out 1 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 1 to in 0"| n3
  n9 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n14
  n2 -->|"ai_languageModel out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n18
  n11 -->|"main out 0 to in 0"| n12
  n7 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n4
  n20 -->|"main out 0 to in 0"| n3
  n13 -->|"main out 0 to in 0"| n19
  n0 -->|"main out 0 to in 0"| n20
  n15 -->|"main out 0 to in 0"| n11
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
