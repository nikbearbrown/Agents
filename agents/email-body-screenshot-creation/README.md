# Email Body Screenshot Creation

Adapt the published “Email Body Screenshot Creation” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 19 executable nodes and 19 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Gmail Trigger"]
  n1["Microsoft Outlook Trigger"]
  n2["Screenshot HTML"]
  n3["Retrieve Screenshot"]
  n4["Set Outlook Variables"]
  n5["Set Gmail Variables"]
  n6["Retrieve Headers of Email"]
  n7["Format Headers"]
  n8["Analyze Email with ChatGPT"]
  n9["Create Potentially Malicious Ticket"]
  n10["Create Potentially Benign Ticket"]
  n11["Rename Screenshot"]
  n12["Set Jira ID"]
  n13["Upload Screenshot of Email to Jira"]
  n14["Upload Email Body to Jira"]
  n15["Convert Email Body to File"]
  n16["Set Email Variables"]
  n17["Rename Email Body Screenshot"]
  n18["Check if Malicious"]
  n12 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n5
  n7 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 0 to in 0"| n3
  n11 -->|"main out 0 to in 0"| n13
  n18 -->|"main out 0 to in 0"| n9
  n18 -->|"main out 1 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n8
  n16 -->|"main out 0 to in 0"| n15
  n5 -->|"main out 0 to in 0"| n16
  n4 -->|"main out 0 to in 0"| n16
  n1 -->|"main out 0 to in 0"| n6
  n6 -->|"main out 0 to in 0"| n7
  n8 -->|"main out 0 to in 0"| n18
  n15 -->|"main out 0 to in 0"| n2
  n17 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 0 to in 0"| n12
  n13 -->|"main out 0 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n12
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
