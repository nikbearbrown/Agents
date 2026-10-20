# Crypto News &amp; Sentiment

Adapt the published “Crypto News &amp; Sentiment” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 20 executable nodes and 27 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Set Query"]
  n2["Crypto News #38; Sentiment Agent"]
  n3["RSS Cointelegraph"]
  n4["RSS Bitcoinmagazine"]
  n5["RSS Coindesk"]
  n6["RSS Bitcoinist"]
  n7["RSS Newsbtc"]
  n8["RSS Cryptopotato"]
  n9["RSS 99bitcoins"]
  n10["RSS Cryptobriefing"]
  n11["RSS Crypto.news"]
  n12["Merge All Articles"]
  n13["Filter by Query"]
  n14["Build Prompt"]
  n15["Adds the sessionId"]
  n16["Summarize News #38; Sentiment #40;GPT-4o#41;"]
  n17["Prepare Telegram Message"]
  n18["Sends Response"]
  n19["Send Crypto or Company Name for Analysis"]
  n1 -->|"main out 0 to in 0"| n3
  n1 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n5
  n1 -->|"main out 0 to in 0"| n6
  n1 -->|"main out 0 to in 0"| n7
  n1 -->|"main out 0 to in 0"| n8
  n1 -->|"main out 0 to in 0"| n9
  n1 -->|"main out 0 to in 0"| n10
  n1 -->|"main out 0 to in 0"| n11
  n7 -->|"main out 0 to in 4"| n12
  n14 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 2"| n12
  n9 -->|"main out 0 to in 7"| n12
  n6 -->|"main out 0 to in 3"| n12
  n13 -->|"main out 0 to in 0"| n14
  n11 -->|"main out 0 to in 9"| n12
  n8 -->|"main out 0 to in 6"| n12
  n0 -->|"ai_languageModel out 0 to in 0"| n2
  n3 -->|"main out 0 to in 0"| n12
  n15 -->|"main out 0 to in 0"| n2
  n12 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 8"| n12
  n4 -->|"main out 0 to in 1"| n12
  n17 -->|"main out 0 to in 0"| n18
  n2 -->|"main out 0 to in 0"| n1
  n16 -->|"main out 0 to in 0"| n17
  n19 -->|"main out 0 to in 0"| n15
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
