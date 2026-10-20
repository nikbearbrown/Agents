# Auto WordPress Blog Generator (GPT + Postgres + WP Media)

Adapt the published “Auto WordPress Blog Generator (GPT + Postgres + WP Media)” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 25 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["OpenAI Chat Model"]
  n2["Download Image"]
  n3["Prepare Post JSON"]
  n4["Merge"]
  n5["OpenAI Chat Model1"]
  n6["Load Categories"]
  n7["Category Filter"]
  n8["Selecting recent"]
  n9["Picks Less Used"]
  n10["10 latest headlines"]
  n11["New article title"]
  n12["AI Agent SEO Headings"]
  n13["AI Agent SEO writer"]
  n14["Merge heading"]
  n15["Combines full post meta"]
  n16["Updating posts DB"]
  n17["Extracting output"]
  n18["Placeholder creator"]
  n19["Media Upload to WP"]
  n20["Post to WP"]
  n21["No Operation, do nothing"]
  n22["Config"]
  n4 -->|"main out 0 to in 0"| n3
  n22 -->|"main out 0 to in 0"| n6
  n20 -->|"main out 0 to in 0"| n21
  n14 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n19
  n7 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n10
  n9 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n9
  n17 -->|"main out 0 to in 1"| n4
  n11 -->|"main out 0 to in 1"| n14
  n1 -->|"ai_languageModel out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n4
  n19 -->|"main out 0 to in 2"| n4
  n5 -->|"ai_languageModel out 0 to in 0"| n12
  n10 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n18
  n13 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n11
  n15 -->|"main out 0 to in 0"| n16
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
