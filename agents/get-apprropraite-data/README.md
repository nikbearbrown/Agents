# Get Apprropraite Data

Adapt the published “Get Apprropraite Data” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 23 executable nodes and 22 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Code"]
  n1["ApplicantData"]
  n2["ERPNext - Reject if Resume not Attached"]
  n3["Applied Against Job"]
  n4["ERPNext - Hold Applicant"]
  n5["Get Job Opening"]
  n6["Google Gemini Chat Model"]
  n7["Convert to Fields"]
  n8["If score less than 80"]
  n9["Reject Applicant"]
  n10["Update Applicant Data"]
  n11["Reume Attachment Link"]
  n12["Resume Link Provided"]
  n13["Accept Applicant"]
  n14["Webhook"]
  n15["File Type"]
  n16["Download PDF Resume"]
  n17["PDF to Text"]
  n18["Txt File to Text #40;Example#41;"]
  n19["Merge1"]
  n20["Recruitment AI Agent"]
  n21["Microsoft Outlook"]
  n22["WhatsApp Business Cloud"]
  n0 -->|"main out 0 to in 0"| n1
  n19 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n0
  n15 -->|"main out 0 to in 0"| n16
  n17 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n12
  n5 -->|"main out 0 to in 0"| n20
  n13 -->|"main out 0 to in 0"| n22
  n9 -->|"main out 0 to in 0"| n21
  n7 -->|"main out 0 to in 0"| n10
  n3 -->|"main out 0 to in 0"| n11
  n3 -->|"main out 1 to in 0"| n4
  n16 -->|"main out 0 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n7
  n12 -->|"main out 0 to in 0"| n3
  n12 -->|"main out 1 to in 0"| n2
  n8 -->|"main out 0 to in 0"| n9
  n8 -->|"main out 1 to in 0"| n13
  n11 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n8
  n6 -->|"ai_languageModel out 0 to in 0"| n20
  n18 -->|"main out 0 to in 1"| n19
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
