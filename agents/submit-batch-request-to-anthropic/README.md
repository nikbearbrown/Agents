# Submit batch request to Anthropic

Adapt the published “Submit batch request to Anthropic” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Submit batch"]
  n1["Check batch status"]
  n2["When Executed by Another Workflow"]
  n3["Get results"]
  n4["Parse response"]
  n5["If ended processing"]
  n6["Batch Status Poll Interval"]
  n7["Run example"]
  n8["One query example"]
  n9["Delete original properties"]
  n10["Construct #39;requests#39; array"]
  n11["Set desired #39;anthropic-version#39;"]
  n12["Execute Workflow #39;Process Multiple Prompts in Parallel with Anthropic Claude Batch API#39;"]
  n13["Build batch #39;request#39; object for single query"]
  n14["Simple Memory Store"]
  n15["Fill Chat Memory with example data"]
  n16["Build batch #39;request#39; object from Chat Memory and execution data"]
  n17["Load Chat Memory Data"]
  n18["First Prompt Result"]
  n19["Second Prompt Result"]
  n20["Split Out Parsed Results"]
  n21["Filter Second Prompt Results"]
  n22["Filter First Prompt Results"]
  n23["Join two example requests into array"]
  n24["Append execution data for single query example"]
  n25["Append execution data for chat memory example"]
  n26["Truncate Chat Memory"]
  n3 -->|"main out 0 to in 0"| n4
  n7 -->|"main out 0 to in 0"| n8
  n7 -->|"main out 0 to in 0"| n26
  n0 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n20
  n8 -->|"main out 0 to in 0"| n24
  n1 -->|"main out 0 to in 0"| n5
  n5 -->|"main out 0 to in 0"| n3
  n5 -->|"main out 1 to in 0"| n6
  n14 -->|"ai_memory out 0 to in 0"| n17
  n14 -->|"ai_memory out 0 to in 0"| n15
  n14 -->|"ai_memory out 0 to in 0"| n26
  n26 -->|"main out 0 to in 0"| n15
  n17 -->|"main out 0 to in 0"| n25
  n6 -->|"main out 0 to in 0"| n1
  n10 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 0 to in 1"| n23
  n22 -->|"main out 0 to in 0"| n18
  n21 -->|"main out 0 to in 0"| n19
  n11 -->|"main out 0 to in 0"| n12
  n2 -->|"main out 0 to in 0"| n0
  n15 -->|"main out 0 to in 0"| n17
  n23 -->|"main out 0 to in 0"| n10
  n25 -->|"main out 0 to in 0"| n16
  n13 -->|"main out 0 to in 0"| n9
  n24 -->|"main out 0 to in 0"| n13
  n16 -->|"main out 0 to in 0"| n23
  n12 -->|"main out 0 to in 0"| n22
  n12 -->|"main out 0 to in 0"| n21
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
