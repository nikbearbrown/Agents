# Analyze_email_headers_for_IPs_and_spoofing__3

Adapt the published “Analyze_email_headers_for_IPs_and_spoofing__3” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 27 executable nodes and 32 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Receive Headers"]
  n1["Fraud Score"]
  n2["Respond to Webhook"]
  n3["Explode Email Header"]
  n4["Split Out IPs"]
  n5["Extract IPs from #34;received#34;"]
  n6["IP Quality Score"]
  n7["IP-API"]
  n8["Collect interesting data"]
  n9["SPF/DKIM/DMARC from #34;authentication-results#34;"]
  n10["SPF from #34;received-spf#34;"]
  n11["DKIM from #34;dkim-signature#34;"]
  n12["DMARC from #34;received-dmarc#34;"]
  n13["DKIM"]
  n14["Extract Email Header from webhook"]
  n15["Received Headers Present#63;"]
  n16["Authentication Results Present#63;"]
  n17["Aggregate Authentication Data"]
  n18["IP Data Merge"]
  n19["Merge Security Data"]
  n20["Join IP Analysis into one JSON object"]
  n21["Join results into one JSON object"]
  n22["SPF Authentication Checker"]
  n23["Set SPF Pass Status"]
  n24["Set SPF Fail Status"]
  n25["Set SPF Neutral Status"]
  n26["Set SPF UnknownStatus"]
  n7 -->|"main out 0 to in 0"| n1
  n1 -->|"main out 0 to in 0"| n8
  n18 -->|"main out 0 to in 0"| n20
  n4 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n14
  n6 -->|"main out 0 to in 0"| n7
  n19 -->|"main out 0 to in 0"| n21
  n24 -->|"main out 0 to in 0"| n13
  n23 -->|"main out 0 to in 0"| n13
  n3 -->|"main out 0 to in 0"| n15
  n3 -->|"main out 0 to in 0"| n16
  n26 -->|"main out 0 to in 0"| n13
  n25 -->|"main out 0 to in 0"| n13
  n10 -->|"main out 0 to in 0"| n11
  n8 -->|"main out 0 to in 0"| n18
  n15 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 1 to in 1"| n18
  n11 -->|"main out 0 to in 0"| n12
  n22 -->|"main out 0 to in 0"| n23
  n22 -->|"main out 1 to in 0"| n24
  n22 -->|"main out 2 to in 0"| n25
  n22 -->|"main out 3 to in 0"| n26
  n12 -->|"main out 0 to in 0"| n17
  n5 -->|"main out 0 to in 0"| n4
  n17 -->|"main out 0 to in 1"| n19
  n16 -->|"main out 0 to in 0"| n9
  n16 -->|"main out 0 to in 0"| n22
  n16 -->|"main out 1 to in 0"| n10
  n14 -->|"main out 0 to in 0"| n3
  n21 -->|"main out 0 to in 0"| n2
  n20 -->|"main out 0 to in 0"| n19
  n9 -->|"main out 0 to in 1"| n19
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
