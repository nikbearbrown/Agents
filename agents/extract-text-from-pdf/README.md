# Extract text from PDF

Adapt the published “Extract text from PDF” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 33 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["OpenAI Chat Model"]
  n1["Convert education to HTML"]
  n2["Auto-fixing Output Parser"]
  n3["OpenAI Chat Model1"]
  n4["Structured Output Parser"]
  n5["Convert employment history to HTML"]
  n6["Convert projects to HTML"]
  n7["Convert volunteering to HTML"]
  n8["Telegram trigger"]
  n9["Auth"]
  n10["No operation #40;unauthorized#41;"]
  n11["Check if start message"]
  n12["No operation #40;start message#41;"]
  n13["Get file"]
  n14["Extract text from PDF"]
  n15["Set parsed fileds"]
  n16["Personal info"]
  n17["Technologies"]
  n18["Employment history"]
  n19["Education"]
  n20["Projects"]
  n21["Volunteering"]
  n22["Merge education and employment history"]
  n23["Merge projects and volunteering"]
  n24["Merge personal info and technologies"]
  n25["Merge all"]
  n26["Set final data"]
  n27["Convert raw to base64"]
  n28["Convert to HTML"]
  n29["Generate plain PDF doc"]
  n30["Send PDF to the user"]
  n31["Parse resume data"]
  n32["Merge other data"]
  n9 -->|"main out 0 to in 0"| n11
  n9 -->|"main out 1 to in 0"| n10
  n13 -->|"main out 0 to in 0"| n14
  n20 -->|"main out 0 to in 0"| n23
  n19 -->|"main out 0 to in 1"| n22
  n25 -->|"main out 0 to in 0"| n26
  n17 -->|"main out 0 to in 1"| n24
  n21 -->|"main out 0 to in 1"| n23
  n16 -->|"main out 0 to in 0"| n24
  n26 -->|"main out 0 to in 0"| n27
  n28 -->|"main out 0 to in 0"| n29
  n32 -->|"main out 0 to in 1"| n25
  n8 -->|"main out 0 to in 0"| n9
  n0 -->|"ai_languageModel out 0 to in 0"| n31
  n31 -->|"main out 0 to in 0"| n15
  n15 -->|"main out 0 to in 0"| n5
  n15 -->|"main out 0 to in 0"| n1
  n15 -->|"main out 0 to in 0"| n6
  n15 -->|"main out 0 to in 0"| n16
  n15 -->|"main out 0 to in 0"| n7
  n15 -->|"main out 0 to in 0"| n17
  n18 -->|"main out 0 to in 0"| n22
  n3 -->|"ai_languageModel out 0 to in 0"| n2
  n27 -->|"main out 0 to in 0"| n28
  n14 -->|"main out 0 to in 0"| n31
  n11 -->|"main out 0 to in 0"| n13
  n11 -->|"main out 1 to in 0"| n12
  n29 -->|"main out 0 to in 0"| n30
  n6 -->|"main out 0 to in 0"| n20
  n4 -->|"ai_outputParser out 0 to in 0"| n2
  n2 -->|"ai_outputParser out 0 to in 0"| n31
  n1 -->|"main out 0 to in 0"| n19
  n7 -->|"main out 0 to in 0"| n21
  n23 -->|"main out 0 to in 1"| n32
  n5 -->|"main out 0 to in 0"| n18
  n24 -->|"main out 0 to in 0"| n25
  n22 -->|"main out 0 to in 0"| n32
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
