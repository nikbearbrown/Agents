# receive form events and completion form and enter date time

Adapt the published “receive form events and completion form and enter date time” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 17 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["n8n Form Trigger"]
  n1["Form End"]
  n2["Enter Date #38; Time"]
  n3["Get Form Values"]
  n4["Terms #38; Conditions"]
  n5["OpenAI Chat Model"]
  n6["Has Accepted#63;"]
  n7["Send Receipt"]
  n8["Wait for Approval"]
  n9["Has Approval#63;"]
  n10["OpenAI Chat Model1"]
  n11["Create Appointment"]
  n12["Send Rejection"]
  n13["Decline"]
  n14["Decline1"]
  n15["Trigger Approval Process"]
  n16["Execute Workflow Trigger"]
  n17["Summarise Enquiry"]
  n18["Enquiry Classifier"]
  n7 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 1 to in 0"| n14
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 1 to in 0"| n12
  n3 -->|"main out 0 to in 0"| n15
  n0 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n3
  n5 -->|"ai_languageModel out 0 to in 0"| n18
  n17 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n18 -->|"main out 0 to in 0"| n4
  n18 -->|"main out 1 to in 0"| n13
  n10 -->|"ai_languageModel out 0 to in 0"| n17
  n4 -->|"main out 0 to in 0"| n6
  n16 -->|"main out 0 to in 0"| n17
  n15 -->|"main out 0 to in 0"| n7
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
