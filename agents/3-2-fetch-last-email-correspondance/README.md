# 3.2: Fetch Last Email Correspondance

Adapt the published “3.2: Fetch Last Email Correspondance” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 47 executable nodes and 47 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get Message Contents"]
  n1["Simplify Emails"]
  n2["Check For Upcoming Meetings"]
  n3["OpenAI Chat Model2"]
  n4["Extract Attendee Information"]
  n5["Execute Workflow Trigger"]
  n6["OpenAI Chat Model"]
  n7["Get Last Correspondence"]
  n8["OpenAI Chat Model1"]
  n9["OpenAI Chat Model3"]
  n10["WhatsApp Business Cloud"]
  n11["Schedule Trigger"]
  n12["Return LinkedIn Success"]
  n13["Return LinkedIn Error"]
  n14["Return Email Error"]
  n15["Return Email Success"]
  n16["Set Route Email"]
  n17["Set Route Linkedin"]
  n18["Router"]
  n19["Return LinkedIn Error1"]
  n20["Has Emails#63;"]
  n21["Return Email Error1"]
  n22["Sections To List"]
  n23["Set LinkedIn Cookie"]
  n24["Attendees to List"]
  n25["Merge Attendee with Summaries"]
  n26["Has Email Address#63;"]
  n27["Has LinkedIn URL#63;"]
  n28["Get Correspondance"]
  n29["Merge"]
  n30["Aggregate Attendees"]
  n31["Activities To Array"]
  n32["Extract Profile Metadata"]
  n33["Activities To List"]
  n34["APIFY Web Scraper"]
  n35["Get Activity Details"]
  n36["Get Sections"]
  n37["Get About Section"]
  n38["Get Activity Section"]
  n39["Extract Activities"]
  n40["Merge1"]
  n41["Is Scrape Successful#63;"]
  n42["Extract About"]
  n43["Get LinkedIn Profile #38; Activity"]
  n44["Correspondance Recap Agent"]
  n45["Attendee Research Agent"]
  n46["LinkedIn Summarizer Agent"]
  n29 -->|"main out 0 to in 0"| n25
  n40 -->|"main out 0 to in 0"| n46
  n18 -->|"main out 0 to in 0"| n26
  n18 -->|"main out 1 to in 0"| n27
  n20 -->|"main out 0 to in 0"| n0
  n20 -->|"main out 1 to in 0"| n14
  n36 -->|"main out 0 to in 0"| n37
  n36 -->|"main out 0 to in 0"| n38
  n42 -->|"main out 0 to in 0"| n40
  n16 -->|"main out 0 to in 0"| n28
  n1 -->|"main out 0 to in 0"| n44
  n11 -->|"main out 0 to in 0"| n2
  n22 -->|"main out 0 to in 0"| n36
  n34 -->|"main out 0 to in 0"| n41
  n24 -->|"main out 0 to in 0"| n16
  n24 -->|"main out 0 to in 0"| n17
  n37 -->|"main out 0 to in 0"| n42
  n27 -->|"main out 0 to in 0"| n23
  n27 -->|"main out 1 to in 0"| n19
  n6 -->|"ai_languageModel out 0 to in 0"| n44
  n33 -->|"main out 0 to in 0"| n35
  n39 -->|"main out 0 to in 0"| n33
  n28 -->|"main out 0 to in 0"| n29
  n26 -->|"main out 0 to in 0"| n7
  n26 -->|"main out 1 to in 0"| n21
  n8 -->|"ai_languageModel out 0 to in 0"| n46
  n3 -->|"ai_languageModel out 0 to in 0"| n4
  n9 -->|"ai_languageModel out 0 to in 0"| n45
  n17 -->|"main out 0 to in 0"| n43
  n31 -->|"main out 0 to in 1"| n40
  n30 -->|"main out 0 to in 0"| n45
  n23 -->|"main out 0 to in 0"| n34
  n35 -->|"main out 0 to in 0"| n31
  n38 -->|"main out 0 to in 0"| n39
  n0 -->|"main out 0 to in 0"| n1
  n41 -->|"main out 0 to in 0"| n32
  n41 -->|"main out 1 to in 0"| n13
  n45 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n20
  n5 -->|"main out 0 to in 0"| n18
  n32 -->|"main out 0 to in 0"| n22
  n46 -->|"main out 0 to in 0"| n12
  n44 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n24
  n25 -->|"main out 0 to in 0"| n30
  n43 -->|"main out 0 to in 1"| n29
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
