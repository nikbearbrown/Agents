# get rows to enrich and basic llm chain ice breaker and http request

Adapt the published “get rows to enrich and basic llm chain ice breaker and http request” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 14 executable nodes and 15 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #34;Test workflow#34;"]
  n1["Get rows to enrich"]
  n2["Anthropic Chat Model"]
  n3["Basic LLM Chain- Ice Breaker"]
  n4["BrightData_Get_Linkedin"]
  n5["Adjust_input_for_loop"]
  n6["HTTP_Request_Post_Request_BrightData"]
  n7["Wait_For_API_Call_Results"]
  n8["API_Call_Snapshot_Progress"]
  n9["IF-Checking_Status_API_Call"]
  n10["Google Sheets - Update Row with data From API"]
  n11["Google Sheets - Update Row with Ice Breaker"]
  n12["Run Workflow on a certain Schedule"]
  n13["Loop Over Items- All Prospects"]
  n1 -->|"main out 0 to in 0"| n5
  n2 -->|"ai_languageModel out 0 to in 0"| n3
  n5 -->|"main out 0 to in 0"| n13
  n4 -->|"main out 0 to in 0"| n10
  n7 -->|"main out 0 to in 0"| n8
  n8 -->|"main out 0 to in 0"| n9
  n9 -->|"main out 0 to in 0"| n7
  n9 -->|"main out 1 to in 0"| n4
  n3 -->|"main out 0 to in 0"| n11
  n0 -->|"main out 0 to in 0"| n1
  n13 -->|"main out 1 to in 0"| n6
  n12 -->|"main out 0 to in 0"| n1
  n6 -->|"main out 0 to in 0"| n7
  n11 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n3
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
