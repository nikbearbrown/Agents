# Email mailbox as Todoist tasks

Adapt the published “Email mailbox as Todoist tasks” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 21 executable nodes and 23 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Mark As Read"]
  n2["Star"]
  n3["Get Starred From Inbox"]
  n4["Get Unread From Inbox"]
  n5["If Task Not Exist"]
  n6["OpenAI Chat Model"]
  n7["Structure Output Todoist Ready"]
  n8["If AI responded properly"]
  n9["Create Todoist Task"]
  n10["Get Full Message"]
  n11["Summarize Message"]
  n12["Enrich Emails With Tasks"]
  n13["Enrich Tasks with Emails"]
  n14["If Email Unstarred #40;Not Exist#41;"]
  n15["Close Task"]
  n16["Email Trigger #40;IMAP#41;"]
  n17["Schedule Trigger"]
  n18["No Operation, do nothing"]
  n19["Merge Starred and Unread Messages"]
  n20["Get Open Tasks"]
  n1 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 0 to in 1"| n12
  n20 -->|"main out 0 to in 1"| n13
  n10 -->|"main out 0 to in 0"| n11
  n17 -->|"main out 0 to in 0"| n18
  n5 -->|"main out 0 to in 0"| n10
  n6 -->|"ai_languageModel out 0 to in 0"| n11
  n11 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n18
  n4 -->|"main out 0 to in 0"| n1
  n4 -->|"main out 0 to in 0"| n19
  n3 -->|"main out 0 to in 1"| n19
  n12 -->|"main out 0 to in 0"| n5
  n13 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 0 to in 0"| n9
  n18 -->|"main out 0 to in 0"| n4
  n18 -->|"main out 0 to in 0"| n3
  n18 -->|"main out 0 to in 0"| n20
  n14 -->|"main out 0 to in 0"| n15
  n7 -->|"ai_outputParser out 0 to in 0"| n11
  n19 -->|"main out 0 to in 0"| n12
  n19 -->|"main out 0 to in 0"| n13
  n0 -->|"main out 0 to in 0"| n18
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
