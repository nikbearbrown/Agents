# fetch apple press releases1 and parse apple press xml1 and fetch google news rss1

Adapt the published “fetch apple press releases1 and parse apple press xml1 and fetch google news rss1” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 47 executable nodes and 52 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Fetch Apple Press Releases1"]
  n1["Parse Apple Press XML1"]
  n2["Extract Apple Press1"]
  n3["Fetch Google News RSS1"]
  n4["Parse Google News XML1"]
  n5["Extract Google News1"]
  n6["Merge All News2"]
  n7["Read Processed Links1"]
  n8["Combine Data1"]
  n9["Deduplicate with Sheets1"]
  n10["Multi-Brand Config1"]
  n11["Split In Batches1"]
  n12["Prepare Subreddits"]
  n13["Fetch Reddit Posts"]
  n14["Extract #38; Format Reddit Data"]
  n15["Split In Batches"]
  n16["Webhook Trigger"]
  n17["Parse XML1"]
  n18["Filter Source Type"]
  n19["Fetch Regulatory News1"]
  n20["Regulatory Sources Config1"]
  n21["Merge Data Streams"]
  n22["Save to Compliance Sheet"]
  n23["Extract Content1"]
  n24["Read Existing Articles1"]
  n25["Deduplicate Articles1"]
  n26["Check New Articles1"]
  n27["OpenAI Sentiment"]
  n28["Merge Analysis Results1"]
  n29["Calculate Baseline Metrics"]
  n30["Build Knowledge Graph"]
  n31["Multi-Brand Competitor Analysis"]
  n32["Detect Anomalies"]
  n33["Format Drift Metrics"]
  n34["Alert Trigger"]
  n35["Format Knowledge Graph for Sheets"]
  n36["Format Competitor Analysis for Sheets"]
  n37["Check New Items"]
  n38["OpenAI Sentiment2"]
  n39["Combine Data"]
  n40["Save Drift Metrics1"]
  n41["Save to Google Sheets"]
  n42["Create JSON1"]
  n43["Respond with JSON"]
  n44["Respond No New Items"]
  n45["Save Knowledge Graph to Sheets"]
  n46["Save Competitor Analysis to Sheets"]
  n0 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n2
  n2 -->|"main out 0 to in 0"| n6
  n3 -->|"main out 0 to in 0"| n4
  n4 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n11
  n6 -->|"main out 0 to in 0"| n8
  n6 -->|"main out 0 to in 0"| n7
  n7 -->|"main out 0 to in 1"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n37
  n10 -->|"main out 0 to in 0"| n11
  n10 -->|"main out 0 to in 0"| n15
  n10 -->|"main out 0 to in 0"| n0
  n11 -->|"main out 0 to in 1"| n6
  n11 -->|"main out 1 to in 0"| n3
  n12 -->|"main out 0 to in 0"| n13
  n13 -->|"main out 0 to in 0"| n14
  n14 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 1"| n6
  n15 -->|"main out 1 to in 0"| n12
  n16 -->|"main out 0 to in 0"| n20
  n16 -->|"main out 0 to in 0"| n24
  n16 -->|"main out 0 to in 0"| n10
  n17 -->|"main out 0 to in 0"| n23
  n18 -->|"main out 1 to in 0"| n19
  n19 -->|"main out 0 to in 0"| n17
  n20 -->|"main out 0 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n25
  n23 -->|"main out 0 to in 0"| n21
  n24 -->|"main out 0 to in 1"| n21
  n25 -->|"main out 0 to in 0"| n26
  n26 -->|"main out 0 to in 0"| n27
  n27 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n22
  n29 -->|"main out 0 to in 0"| n32
  n30 -->|"main out 0 to in 0"| n35
  n31 -->|"main out 0 to in 0"| n36
  n32 -->|"main out 0 to in 0"| n33
  n32 -->|"main out 0 to in 0"| n34
  n33 -->|"main out 0 to in 0"| n40
  n35 -->|"main out 0 to in 0"| n45
  n36 -->|"main out 0 to in 0"| n46
  n37 -->|"main out 0 to in 0"| n38
  n37 -->|"main out 1 to in 0"| n44
  n38 -->|"main out 0 to in 0"| n39
  n39 -->|"main out 0 to in 0"| n29
  n39 -->|"main out 0 to in 0"| n41
  n39 -->|"main out 0 to in 0"| n42
  n39 -->|"main out 0 to in 0"| n31
  n39 -->|"main out 0 to in 0"| n30
  n42 -->|"main out 0 to in 0"| n43
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

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/humanitariansai-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
