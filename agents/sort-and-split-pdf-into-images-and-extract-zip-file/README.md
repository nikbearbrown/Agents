# sort and split pdf into images and extract zip file

Adapt the published “sort and split pdf into images and extract zip file” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 39 executable nodes and 37 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["When clicking #8216;Test workflow#8217;"]
  n1["Sort Pages"]
  n2["Split PDF into Images"]
  n3["Extract Zip File"]
  n4["Images To List"]
  n5["Resize Images For AI"]
  n6["Combine All Pages"]
  n7["Default Data Loader"]
  n8["Recursive Character Text Splitter"]
  n9["OpenAI Chat Model"]
  n10["OpenAI Chat Model2"]
  n11["Embeddings OpenAI"]
  n12["Delete Existing Vectors"]
  n13["Continue With Pages Only"]
  n14["Update Pitchdecks Table"]
  n15["Search Pending Rows"]
  n16["Get Row"]
  n17["Prequisites Met"]
  n18["Execute Workflow"]
  n19["No Operation, do nothing"]
  n20["Execute Workflow Trigger"]
  n21["Extract from File"]
  n22["Convert to File"]
  n23["OpenAI Chat Model1"]
  n24["Vector Store Tool"]
  n25["OpenAI Chat Model3"]
  n26["Embeddings OpenAI1"]
  n27["OpenAI Chat Model4"]
  n28["Generate Report"]
  n29["Download Deck From Airtable"]
  n30["Airtable Trigger For Pending Rows"]
  n31["Transcribe to Markdown"]
  n32["Identify Companies In Question"]
  n33["Qdrant Vector Store"]
  n34["Ask Questions About Pitchdecks"]
  n35["Window Buffer Memory"]
  n36["Check Pitch Deck Exists"]
  n37["When chat message received"]
  n38["Pitchdecks Vector Store"]
  n16 -->|"main out 0 to in 0"| n17
  n1 -->|"main out 0 to in 0"| n5
  n4 -->|"main out 0 to in 0"| n1
  n22 -->|"main out 0 to in 0"| n2
  n28 -->|"main out 0 to in 0"| n14
  n17 -->|"main out 0 to in 0"| n18
  n17 -->|"main out 1 to in 0"| n19
  n3 -->|"main out 0 to in 0"| n4
  n6 -->|"main out 0 to in 0"| n28
  n11 -->|"ai_embedding out 0 to in 0"| n38
  n21 -->|"main out 0 to in 0"| n22
  n9 -->|"ai_languageModel out 0 to in 0"| n34
  n24 -->|"ai_tool out 0 to in 0"| n34
  n26 -->|"ai_embedding out 0 to in 0"| n33
  n23 -->|"ai_languageModel out 0 to in 0"| n32
  n10 -->|"ai_languageModel out 0 to in 0"| n28
  n25 -->|"ai_languageModel out 0 to in 0"| n24
  n27 -->|"ai_languageModel out 0 to in 0"| n31
  n7 -->|"ai_document out 0 to in 0"| n38
  n33 -->|"ai_vectorStore out 0 to in 0"| n24
  n15 -->|"main out 0 to in 0"| n16
  n5 -->|"main out 0 to in 0"| n31
  n35 -->|"ai_memory out 0 to in 0"| n34
  n2 -->|"main out 0 to in 0"| n3
  n31 -->|"main out 0 to in 0"| n6
  n31 -->|"main out 0 to in 0"| n13
  n31 -->|"main out 0 to in 0"| n12
  n36 -->|"ai_tool out 0 to in 0"| n34
  n12 -->|"main out 0 to in 1"| n13
  n13 -->|"main out 0 to in 0"| n38
  n20 -->|"main out 0 to in 0"| n29
  n37 -->|"main out 0 to in 0"| n32
  n29 -->|"main out 0 to in 0"| n21
  n32 -->|"main out 0 to in 0"| n34
  n30 -->|"main out 0 to in 0"| n16
  n8 -->|"ai_textSplitter out 0 to in 0"| n7
  n0 -->|"main out 0 to in 0"| n15
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
