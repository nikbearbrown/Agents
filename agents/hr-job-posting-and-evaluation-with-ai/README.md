# HR Job Posting and Evaluation with AI

Adapt the published “HR Job Posting and Evaluation with AI” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["On form submission"]
  n1["Airtable"]
  n2["Upload CV to google drive"]
  n3["applicant details"]
  n4["download CV"]
  n5["Extract from File"]
  n6["AI Agent"]
  n7["OpenAI Chat Model"]
  n8["Airtable1"]
  n9["Structured Output Parser"]
  n10["shortlisted#63;"]
  n11["Rejected"]
  n12["Potential Hire"]
  n13["Airtable2"]
  n14["generate questionnaires"]
  n15["questionnaires"]
  n16["update questionnaires"]
  n17["job_posting"]
  n18["candidate_insights"]
  n19["Personalize email"]
  n20["Edit Fields"]
  n21["Send Email"]
  n22["Book Meeting"]
  n23["Google Calendar"]
  n24["update phone meeting time"]
  n25["Screening Questions"]
  n26["job_posting1"]
  n27["candidate_insights1"]
  n28["screening questions"]
  n29["Edit Fields1"]
  n6 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n4
  n8 -->|"ai_tool out 0 to in 0"| n6
  n13 -->|"ai_tool out 0 to in 0"| n14
  n21 -->|"main out 0 to in 0"| n22
  n20 -->|"main out 0 to in 0"| n21
  n4 -->|"main out 0 to in 0"| n5
  n17 -->|"ai_tool out 0 to in 0"| n19
  n22 -->|"main out 0 to in 0"| n24
  n29 -->|"main out 0 to in 0"| n28
  n26 -->|"ai_tool out 0 to in 0"| n25
  n10 -->|"main out 0 to in 0"| n12
  n10 -->|"main out 1 to in 0"| n11
  n12 -->|"main out 0 to in 0"| n14
  n15 -->|"main out 0 to in 0"| n16
  n23 -->|"ai_tool out 0 to in 0"| n22
  n5 -->|"main out 0 to in 0"| n6
  n7 -->|"ai_languageModel out 0 to in 0"| n6
  n19 -->|"main out 0 to in 0"| n20
  n3 -->|"main out 0 to in 0"| n1
  n0 -->|"main out 0 to in 0"| n2
  n18 -->|"ai_tool out 0 to in 0"| n19
  n25 -->|"main out 0 to in 0"| n29
  n27 -->|"ai_tool out 0 to in 0"| n25
  n16 -->|"main out 0 to in 0"| n19
  n14 -->|"main out 0 to in 0"| n15
  n9 -->|"ai_outputParser out 0 to in 0"| n6
  n2 -->|"main out 0 to in 0"| n3
  n24 -->|"main out 0 to in 0"| n25
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
