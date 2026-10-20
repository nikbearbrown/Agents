# Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack

Adapt the published “Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 13 executable nodes and 13 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Schedule Trigger"]
  n1["Split out detections"]
  n2["Get recent detections from Crowdstrike"]
  n3["Get detection details"]
  n4["Split out behaviours"]
  n5["Look up SHA in Virustotal"]
  n6["Look up IOC in Virustotal"]
  n7["Split In Batches"]
  n8["Merge behaviour descriptions"]
  n9["Set behaviour descriptions"]
  n10["Create Jira issue"]
  n11["Post notification on Slack"]
  n12["Pause 1 second"]
  n12 -->|"main out 0 to in 0"| n5
  n0 -->|"main out 0 to in 0"| n2
  n7 -->|"main out 0 to in 0"| n4
  n10 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n12
  n1 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n7
  n6 -->|"main out 0 to in 0"| n9
  n5 -->|"main out 0 to in 0"| n6
  n11 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n10
  n2 -->|"main out 0 to in 0"| n1
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
