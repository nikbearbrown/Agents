# receive schedule events and search airtable and gmail

Adapt the published “receive schedule events and search airtable and gmail” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 24 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Search daily"]
  n2["Search weekly"]
  n3["confirmation email1"]
  n4["Execute Workflow"]
  n5["Create Event"]
  n6["Execute Workflow Trigger"]
  n7["Unsubscribe Form"]
  n8["Set Email Vars"]
  n9["Log Last Sent"]
  n10["Search surprise"]
  n11["Should Send #61; True"]
  n12["Should Send#63;"]
  n13["Create Subscriber"]
  n14["Update Subscriber"]
  n15["Subscribe Form"]
  n16["Execution Data"]
  n17["Window Buffer Memory"]
  n18["Wikipedia"]
  n19["Content Generation Agent"]
  n20["Groq Chat Model"]
  n21["Generate Image"]
  n22["Resize Image"]
  n23["Send Message"]
  n18 -->|"ai_tool out 0 to in 0"| n19
  n5 -->|"main out 0 to in 0"| n4
  n22 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n5
  n23 -->|"main out 0 to in 0"| n9
  n12 -->|"main out 0 to in 0"| n11
  n2 -->|"main out 0 to in 0"| n5
  n16 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 0 to in 0"| n22
  n8 -->|"main out 0 to in 0"| n23
  n15 -->|"main out 0 to in 0"| n13
  n20 -->|"ai_languageModel out 0 to in 0"| n19
  n10 -->|"main out 0 to in 0"| n12
  n0 -->|"main out 0 to in 0"| n10
  n0 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n14
  n13 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n5
  n17 -->|"ai_memory out 0 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n21
  n6 -->|"main out 0 to in 0"| n16
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
