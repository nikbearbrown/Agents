# 🎦💌Advanced YouTube RSS Feed Buddy for Your Favorite Channels

Adapt the published “🎦💌Advanced YouTube RSS Feed Buddy for Your Favorite Channels” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 28 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On form submission"]
  n1["Create RSS Feed URLs1"]
  n2["Get Channel Ids"]
  n3["Create YouTube API URL"]
  n4["Get YouTube Video Details"]
  n5["Workflow Variables"]
  n6["OpenAI Chat Model"]
  n7["Merge"]
  n8["OpenAI Chat Model1"]
  n9["Default YouTube Channel Ids"]
  n10["YouTube Channel Ids"]
  n11["RSS Read - Max 15 Latest Videos per Channel"]
  n12["Label New Videos"]
  n13["Get New Videos"]
  n14["Prepare For Telegram Message"]
  n15["One List Object"]
  n16["Prepare YouTube Data"]
  n17["Create List of Channel Ids"]
  n18["Every Day"]
  n19["Multiple Emails"]
  n20["Single Email"]
  n21["Create Email per Video"]
  n22["Create One Email for All Videos"]
  n23["Telegram"]
  n24["Create RSS Feed URLs"]
  n25["RSS Read - Max 15 Latest Videos per Channel1"]
  n26["Create List of Channel Ids1"]
  n27["When clicking #8216;Test workflow#8217;"]
  n28["YouTube Channel Ids1"]
  n7 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n15
  n7 -->|"main out 0 to in 0"| n14
  n18 -->|"main out 0 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 1"| n7
  n2 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n22
  n12 -->|"main out 0 to in 0"| n13
  n6 -->|"ai_languageModel out 0 to in 0"| n21
  n0 -->|"main out 0 to in 0"| n9
  n8 -->|"ai_languageModel out 0 to in 0"| n22
  n5 -->|"main out 0 to in 0"| n3
  n10 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n25
  n16 -->|"main out 0 to in 0"| n7
  n28 -->|"main out 0 to in 0"| n26
  n1 -->|"main out 0 to in 0"| n11
  n21 -->|"main out 0 to in 0"| n19
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n1
  n26 -->|"main out 0 to in 0"| n24
  n9 -->|"main out 0 to in 0"| n2
  n14 -->|"main out 0 to in 0"| n23
  n22 -->|"main out 0 to in 0"| n20
  n27 -->|"main out 0 to in 0"| n28
  n11 -->|"main out 0 to in 0"| n12
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
