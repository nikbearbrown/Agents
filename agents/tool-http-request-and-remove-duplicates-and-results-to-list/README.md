# tool http request and remove duplicates and results to list

Adapt the published “tool http request and remove duplicates and results to list” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 30 executable nodes and 30 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["OpenAI Chat Model1"]
  n2["Search Crunchbase"]
  n3["Search WellFound"]
  n4["Search LinkedIn"]
  n5["Structured Output Parser1"]
  n6["Webscraper Tool1"]
  n7["Remove Duplicates"]
  n8["Extract Domain"]
  n9["Results to List"]
  n10["Check Company Profiles Exist"]
  n11["Webscraper Tool"]
  n12["Search Company Website"]
  n13["Structured Output Parser"]
  n14["OpenAI Chat Model"]
  n15["Search Product Review Sites"]
  n16["Webscraper Tool2"]
  n17["Structured Output Parser2"]
  n18["OpenAI Chat Model2"]
  n19["Insert Into Notion"]
  n20["Limit"]
  n21["Loop Over Items"]
  n22["Competitor Search via Exa.ai"]
  n23["Get Company News"]
  n24["Set Source Company"]
  n25["Collect Results"]
  n26["2sec"]
  n27["Company Overview Agent"]
  n28["Company Product Offering Agent"]
  n29["Company Product Reviews Agent"]
  n26 -->|"main out 0 to in 0"| n21
  n20 -->|"main out 0 to in 0"| n21
  n8 -->|"main out 0 to in 0"| n7
  n25 -->|"main out 0 to in 0"| n19
  n21 -->|"main out 1 to in 0"| n27
  n9 -->|"main out 0 to in 0"| n8
  n4 -->|"ai_tool out 0 to in 0"| n27
  n11 -->|"ai_tool out 0 to in 0"| n28
  n23 -->|"ai_tool out 0 to in 0"| n27
  n3 -->|"ai_tool out 0 to in 0"| n27
  n6 -->|"ai_tool out 0 to in 0"| n27
  n16 -->|"ai_tool out 0 to in 0"| n29
  n14 -->|"ai_languageModel out 0 to in 0"| n28
  n7 -->|"main out 0 to in 0"| n20
  n2 -->|"ai_tool out 0 to in 0"| n27
  n19 -->|"main out 0 to in 0"| n26
  n1 -->|"ai_languageModel out 0 to in 0"| n27
  n18 -->|"ai_languageModel out 0 to in 0"| n29
  n24 -->|"main out 0 to in 0"| n22
  n27 -->|"main out 0 to in 0"| n28
  n12 -->|"ai_tool out 0 to in 0"| n28
  n13 -->|"ai_outputParser out 0 to in 0"| n28
  n5 -->|"ai_outputParser out 0 to in 0"| n27
  n17 -->|"ai_outputParser out 0 to in 0"| n29
  n15 -->|"ai_tool out 0 to in 0"| n29
  n10 -->|"ai_tool out 0 to in 0"| n27
  n22 -->|"main out 0 to in 0"| n9
  n29 -->|"main out 0 to in 0"| n25
  n28 -->|"main out 0 to in 0"| n29
  n0 -->|"main out 0 to in 0"| n24
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
