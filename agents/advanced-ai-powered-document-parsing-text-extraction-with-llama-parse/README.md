# ✨🔪 Advanced AI Powered Document Parsing &amp; Text Extraction with Llama Parse

Adapt the published “✨🔪 Advanced AI Powered Document Parsing &amp; Text Extraction with Llama Parse” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 36 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Webhook"]
  n1["Gmail"]
  n2["Gmail Trigger"]
  n3["Limit"]
  n4["Get Message"]
  n5["Parse Document with LlamaParse"]
  n6["Summarize Email"]
  n7["gpt-4o-mini"]
  n8["Save LlamaParse ID and Summary to Google Sheets"]
  n9["Save Document to Google Drive"]
  n10["Extract Invoice Details as JSON"]
  n11["gpt-4o-mini1"]
  n12["gpt-4o-mini2"]
  n13["Update Google Sheet by LlamaParse ID"]
  n14["Invoice Details"]
  n15["Prepare Message"]
  n16["Send Invoice Details as Telegram Message"]
  n17["gpt-4o-mini3"]
  n18["Send Error Message 2"]
  n19["Send Error Message 1"]
  n20["Send Document Summary as Telegram Message"]
  n21["Summarize Document"]
  n22["Classify Parsed Document"]
  n23["Get Parsed Markdown"]
  n24["Prepare Data"]
  n25["HTTP Request"]
  n26["Is there an Email Attachement"]
  n27["Aggregate"]
  n28["Edit Fields"]
  n29["Merge Email Processing"]
  n30["Merge"]
  n31["If Supported File Extensions"]
  n32["No Operation, do nothing"]
  n33["No Operation, do nothing1"]
  n34["Save Summarized Document to Google Drive"]
  n35["Save Parsed Document to Google Drive"]
  n1 -->|"main out 0 to in 0"| n3
  n3 -->|"main out 0 to in 0"| n4
  n30 -->|"main out 0 to in 0"| n5
  n30 -->|"main out 0 to in 0"| n9
  n30 -->|"main out 0 to in 0"| n6
  n0 -->|"main out 0 to in 0"| n23
  n27 -->|"main out 0 to in 0"| n28
  n28 -->|"main out 0 to in 0"| n31
  n4 -->|"main out 0 to in 0"| n26
  n7 -->|"ai_languageModel out 0 to in 0"| n6
  n25 -->|"main out 0 to in 0"| n27
  n24 -->|"main out 0 to in 1"| n29
  n11 -->|"ai_languageModel out 0 to in 0"| n22
  n12 -->|"ai_languageModel out 0 to in 0"| n10
  n17 -->|"ai_languageModel out 0 to in 0"| n21
  n2 -->|"main out 0 to in 0"| n1
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 0 to in 0"| n13
  n15 -->|"main out 0 to in 0"| n16
  n6 -->|"main out 0 to in 2"| n29
  n21 -->|"main out 0 to in 0"| n20
  n21 -->|"main out 0 to in 0"| n34
  n21 -->|"main out 1 to in 0"| n19
  n23 -->|"main out 0 to in 0"| n22
  n23 -->|"main out 0 to in 0"| n35
  n29 -->|"main out 0 to in 0"| n8
  n22 -->|"main out 0 to in 0"| n21
  n22 -->|"main out 1 to in 0"| n10
  n31 -->|"main out 0 to in 1"| n30
  n31 -->|"main out 1 to in 0"| n33
  n26 -->|"main out 0 to in 0"| n25
  n26 -->|"main out 0 to in 0"| n30
  n26 -->|"main out 1 to in 0"| n32
  n9 -->|"main out 0 to in 0"| n24
  n5 -->|"main out 0 to in 0"| n29
  n10 -->|"main out 0 to in 0"| n14
  n10 -->|"main out 1 to in 0"| n18
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
