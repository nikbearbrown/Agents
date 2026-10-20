# Resume Screening &amp; Behavioral Interviews with Gemini, Elevenlabs, &amp; Notion ATS copy

Adapt the published “Resume Screening &amp; Behavioral Interviews with Gemini, Elevenlabs, &amp; Notion ATS copy” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 38 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Merge"]
  n1["Structured Output Parser"]
  n2["HR Expert"]
  n3["Upload CV"]
  n4["Extract Resume"]
  n5["Applicant Summary"]
  n6["Job Description Summary"]
  n7["Applicant Qualifications"]
  n8["Applicant Personal Data"]
  n9["Application Data"]
  n10["ElevenLabs Web Hook"]
  n11["ai_convo_items"]
  n12["Extract_Audio"]
  n13["Filter_Notion_db"]
  n14["AI Agent"]
  n15["Link Audio in Notion"]
  n16["Resume URL"]
  n17["Get Applicant Record"]
  n18["Embed Resume in Notion"]
  n19["Wait"]
  n20["Application Form 1 of 3"]
  n21["Application Form 2 of 3"]
  n22["Application form 3 of 3"]
  n23["Get Job Description"]
  n24["Job Description Mapping"]
  n25["Applicant Data Backup"]
  n26["Create Applicant Record"]
  n27["Upload Audio to Drive"]
  n28["Google Gemini"]
  n29["Evaluation Criteria"]
  n30["Applicant Record"]
  n31["Update_Applicant_Record"]
  n32["Google Gemini Model"]
  n19 -->|"main out 0 to in 0"| n17
  n0 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 0"| n30
  n2 -->|"main out 0 to in 0"| n25
  n3 -->|"main out 0 to in 0"| n16
  n16 -->|"main out 0 to in 0"| n19
  n12 -->|"main out 0 to in 0"| n27
  n28 -->|"ai_languageModel out 0 to in 0"| n5
  n28 -->|"ai_languageModel out 0 to in 0"| n7
  n28 -->|"ai_languageModel out 0 to in 0"| n2
  n28 -->|"ai_languageModel out 0 to in 0"| n8
  n28 -->|"ai_languageModel out 0 to in 0"| n6
  n4 -->|"main out 0 to in 0"| n7
  n4 -->|"main out 0 to in 0"| n8
  n11 -->|"main out 0 to in 0"| n14
  n30 -->|"main out 0 to in 0"| n13
  n9 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n31
  n5 -->|"main out 0 to in 0"| n23
  n10 -->|"main out 0 to in 0"| n11
  n29 -->|"ai_tool out 0 to in 0"| n14
  n23 -->|"main out 0 to in 0"| n6
  n32 -->|"ai_languageModel out 0 to in 0"| n14
  n17 -->|"main out 0 to in 0"| n18
  n25 -->|"main out 0 to in 0"| n26
  n27 -->|"main out 0 to in 0"| n15
  n8 -->|"main out 0 to in 0"| n0
  n20 -->|"main out 0 to in 0"| n3
  n20 -->|"main out 0 to in 0"| n9
  n21 -->|"main out 0 to in 0"| n3
  n21 -->|"main out 0 to in 0"| n9
  n22 -->|"main out 0 to in 0"| n3
  n22 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n2
  n6 -->|"main out 0 to in 0"| n24
  n31 -->|"main out 0 to in 0"| n12
  n7 -->|"main out 0 to in 1"| n0
  n1 -->|"ai_outputParser out 0 to in 0"| n2
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
