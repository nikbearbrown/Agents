# &#91;n8n&#93; Advanced URL Parsing and Shortening Workflow - Switchy.io Integration

Adapt the published “&#91;n8n&#93; Advanced URL Parsing and Shortening Workflow - Switchy.io Integration” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 47 executable nodes and 59 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Split In Batches"]
  n1["Get Headers"]
  n2["OpenGraph API"]
  n3["Meta tags Scraper - dub.sh"]
  n4["IF OpenGraph invaild"]
  n5["Parse headers"]
  n6["If - Enable ScreenShots #40;yes to enable#41;"]
  n7["API Auth"]
  n8["Method 1 - META"]
  n9["Convert to File"]
  n10["Final Data"]
  n11["CREATE"]
  n12["UPDATE"]
  n13["IF Slug available"]
  n14["Final Meta"]
  n15["Host Screenshot"]
  n16["Host OGImage"]
  n17["Host Favicon"]
  n18["Edit Fields"]
  n19["Download final OG"]
  n20["Download Favicon"]
  n21["Method 2 - META"]
  n22["Stop and Error"]
  n23["Method 3 - META1"]
  n24["Method 1 - SCR"]
  n25["Method 2 - SCR"]
  n26["Final SCR"]
  n27["Stop And Error"]
  n28["Shortened URL"]
  n29["n8n Form Trigger"]
  n30["Respond to Webhook"]
  n31["Scan URL #40;Community#41;"]
  n32["If"]
  n33["If1"]
  n34["Check Reviews #40;Community#41;"]
  n35["Norton"]
  n36["bitdefender"]
  n37["HTML"]
  n38["#40;Fraud Check#41;"]
  n39["#40;Others#41;"]
  n40["If2"]
  n41["set unsafe"]
  n42["If3"]
  n43["PhishTank"]
  n44["IF GH invaild"]
  n45["Method 4 - META"]
  n46["IF dub invaild"]
  n32 -->|"main out 0 to in 0"| n43
  n32 -->|"main out 1 to in 0"| n33
  n33 -->|"main out 0 to in 0"| n34
  n33 -->|"main out 1 to in 0"| n35
  n40 -->|"main out 0 to in 0"| n2
  n40 -->|"main out 1 to in 0"| n41
  n42 -->|"main out 0 to in 0"| n31
  n42 -->|"main out 1 to in 0"| n2
  n37 -->|"main out 0 to in 0"| n36
  n11 -->|"main out 0 to in 0"| n13
  n35 -->|"main out 0 to in 0"| n43
  n12 -->|"main out 0 to in 0"| n28
  n39 -->|"main out 0 to in 0"| n37
  n7 -->|"main out 0 to in 0"| n42
  n26 -->|"main out 0 to in 0"| n15
  n43 -->|"main out 0 to in 0"| n38
  n10 -->|"main out 0 to in 0"| n11
  n14 -->|"main out 0 to in 0"| n6
  n41 -->|"main out 0 to in 0"| n0
  n18 -->|"main out 0 to in 0"| n19
  n1 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 1 to in 0"| n3
  n36 -->|"main out 0 to in 0"| n40
  n17 -->|"main out 0 to in 0"| n10
  n16 -->|"main out 0 to in 0"| n20
  n38 -->|"main out 0 to in 0"| n39
  n44 -->|"main out 0 to in 0"| n3
  n44 -->|"main out 1 to in 0"| n14
  n2 -->|"main out 0 to in 0"| n4
  n2 -->|"main out 1 to in 0"| n1
  n5 -->|"main out 0 to in 0"| n21
  n28 -->|"main out 0 to in 0"| n0
  n46 -->|"main out 0 to in 0"| n45
  n46 -->|"main out 1 to in 0"| n23
  n24 -->|"main out 0 to in 0"| n26
  n24 -->|"main out 1 to in 0"| n25
  n25 -->|"main out 0 to in 0"| n9
  n25 -->|"main out 1 to in 0"| n27
  n9 -->|"main out 0 to in 0"| n26
  n15 -->|"main out 0 to in 0"| n18
  n8 -->|"main out 0 to in 0"| n14
  n21 -->|"main out 0 to in 0"| n44
  n45 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n17
  n23 -->|"main out 0 to in 0"| n14
  n0 -->|"main out 0 to in 0"| n7
  n0 -->|"main out 1 to in 0"| n30
  n29 -->|"main out 0 to in 0"| n0
  n19 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n28
  n13 -->|"main out 1 to in 0"| n12
  n4 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 1 to in 0"| n1
  n31 -->|"main out 0 to in 0"| n32
  n34 -->|"main out 0 to in 0"| n35
  n3 -->|"main out 0 to in 0"| n46
  n3 -->|"main out 1 to in 0"| n22
  n6 -->|"main out 0 to in 0"| n24
  n6 -->|"main out 1 to in 0"| n18
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
