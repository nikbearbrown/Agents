# Find WooCommerce User-ID

Adapt the published “Find WooCommerce User-ID” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 31 executable nodes and 29 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["No email provided"]
  n1["If email provided"]
  n2["If user found"]
  n3["No customer found"]
  n4["If contains DHL data"]
  n5["Extract Tracking Data"]
  n6["Merge Orders"]
  n7["Merge Order and Tracking Data"]
  n8["Split Out"]
  n9["Aggregate"]
  n10["Merge Tracking Data"]
  n11["Window Buffer Memory"]
  n12["Execute Workflow Trigger"]
  n13["WooCommerce - Get User"]
  n14["If order found"]
  n15["WooCommerce Get Orders"]
  n16["No order found"]
  n17["Add Error Information"]
  n18["DHL"]
  n19["Send Response"]
  n20["OpenAI Chat Model"]
  n21["WooCommerce_Tool"]
  n22["Chat Trigger"]
  n23["Respond to Webhook"]
  n24["Webhook Example Page"]
  n25["Decrypt email"]
  n26["Encrypt email"]
  n27["Example encrypted email"]
  n28["Decrypt email address"]
  n29["AI Agent"]
  n30["Mock Data"]
  n18 -->|"main out 0 to in 0"| n10
  n18 -->|"main out 1 to in 0"| n17
  n9 -->|"main out 0 to in 0"| n6
  n30 -->|"main out 0 to in 0"| n29
  n8 -->|"main out 0 to in 0"| n18
  n22 -->|"main out 0 to in 0"| n28
  n6 -->|"main out 0 to in 0"| n7
  n2 -->|"main out 0 to in 0"| n15
  n2 -->|"main out 1 to in 0"| n3
  n14 -->|"main out 0 to in 0"| n5
  n14 -->|"main out 0 to in 1"| n7
  n14 -->|"main out 1 to in 0"| n16
  n21 -->|"ai_tool out 0 to in 0"| n29
  n1 -->|"main out 0 to in 0"| n13
  n1 -->|"main out 1 to in 0"| n0
  n20 -->|"ai_languageModel out 0 to in 0"| n29
  n10 -->|"main out 0 to in 0"| n9
  n4 -->|"main out 0 to in 0"| n8
  n4 -->|"main out 1 to in 1"| n6
  n24 -->|"main out 0 to in 0"| n23
  n11 -->|"ai_memory out 0 to in 0"| n29
  n17 -->|"main out 0 to in 1"| n10
  n28 -->|"main out 0 to in 0"| n30
  n5 -->|"main out 0 to in 0"| n4
  n13 -->|"main out 0 to in 0"| n2
  n15 -->|"main out 0 to in 0"| n14
  n27 -->|"main out 0 to in 0"| n25
  n12 -->|"main out 0 to in 0"| n1
  n7 -->|"main out 0 to in 0"| n19
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
