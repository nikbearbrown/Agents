# receive schedule events and list issuecomment jira and update jira

Adapt the published “receive schedule events and list issuecomment jira and update jira” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 29 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["OpenAI Chat Model1"]
  n2["OpenAI Chat Model3"]
  n3["OpenAI Chat Model4"]
  n4["Schedule Trigger"]
  n5["Get Issue Comments"]
  n6["Close Issue"]
  n7["Send Reminder"]
  n8["Join Comments"]
  n9["Add Autoclose Message"]
  n10["Ask For Feedback Message"]
  n11["Simplify Thread For AI"]
  n12["Solution Found#63;"]
  n13["Reply to Issue"]
  n14["Last Message is Not Bot"]
  n15["Structured Output Parser"]
  n16["Get Issue Metadata"]
  n17["Notify Slack Channel"]
  n18["Close Issue2"]
  n19["Get List of Unresolved Long Lived Issues"]
  n20["Execute Workflow"]
  n21["Execute Workflow Trigger"]
  n22["Customer Satisfaction Agent"]
  n23["KnowledgeBase Agent"]
  n24["Issue Reminder Agent"]
  n25["Find Simlar Issues"]
  n26["Query KnowledgeBase"]
  n27["Report Unhappy Resolution"]
  n28["Classify Current Issue State"]
  n8 -->|"main out 0 to in 0"| n11
  n13 -->|"main out 0 to in 0"| n18
  n12 -->|"main out 0 to in 0"| n13
  n12 -->|"main out 1 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n19
  n0 -->|"ai_languageModel out 0 to in 0"| n28
  n25 -->|"ai_tool out 0 to in 0"| n23
  n5 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n5
  n1 -->|"ai_languageModel out 0 to in 0"| n23
  n2 -->|"ai_languageModel out 0 to in 0"| n24
  n3 -->|"ai_languageModel out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n12
  n26 -->|"ai_tool out 0 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n7
  n17 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n24
  n10 -->|"main out 0 to in 0"| n6
  n21 -->|"main out 0 to in 0"| n16
  n15 -->|"ai_outputParser out 0 to in 0"| n23
  n22 -->|"main out 0 to in 0"| n10
  n22 -->|"main out 1 to in 0"| n9
  n22 -->|"main out 2 to in 0"| n27
  n28 -->|"main out 0 to in 0"| n22
  n28 -->|"main out 1 to in 0"| n14
  n28 -->|"main out 2 to in 0"| n23
  n19 -->|"main out 0 to in 0"| n20
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
