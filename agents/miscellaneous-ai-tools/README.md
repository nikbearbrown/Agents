# MISCELLANEOUS AI TOOLS

Adapt the published “MISCELLANEOUS AI TOOLS” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 97 executable nodes and 2 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["AI Agent"]
  n1["OpenAI"]
  n2["Basic LLM Chain"]
  n3["Information Extractor"]
  n4["Question and Answer Chain"]
  n5["Sentiment Analysis"]
  n6["Summarization Chain"]
  n7["Text Classifier"]
  n8["Chat Memory Manager"]
  n9["Bitly App"]
  n10["Dropbox App"]
  n11["Gmail App"]
  n12["Google Calendar App"]
  n13["Google Docs App"]
  n14["Google Sheets App"]
  n15["Pushbullet App"]
  n16["YouTube App"]
  n17["Bluesky App"]
  n18["Perplexity App"]
  n19["ElevenLabs App"]
  n20["Reddit App"]
  n21["Gmail Trigger App"]
  n22["Google Sheets Trigger App"]
  n23["Call n8n Workflow Tool"]
  n24["Code Tool"]
  n25["HTTP Request1"]
  n26["Calculator"]
  n27["Postgres"]
  n28["Redis"]
  n29["Send Email"]
  n30["SerpAPI"]
  n31["Wikipedia"]
  n32["Wolfram Alpha"]
  n33["gmailTool App"]
  n34["googleCalendarTool App"]
  n35["googleDocsTool App"]
  n36["googleSheetsTool App"]
  n37["Default Data Loader"]
  n38["Auto-fixing Output Parser"]
  n39["Answer questions with a vector store"]
  n40["In-Memory Vector Store"]
  n41["Pinecone Vector Store"]
  n42["Postgres PGVector Store"]
  n43["Supabase Vector Store"]
  n44["Anthropic Chat Model"]
  n45["Google Gemini Chat Model"]
  n46["OpenAI Chat Model"]
  n47["Window Buffer Memory"]
  n48["Postgres Chat Memory"]
  n49["Redis Chat Memory"]
  n50["Item List Output Parser"]
  n51["Structured Output Parser"]
  n52["Embeddings Google Gemini"]
  n53["Embeddings OpenAI"]
  n54["X"]
  n55["Calendly Trigger"]
  n56["Email Trigger #40;IMAP#41;"]
  n57["Google Drive Trigger"]
  n58["Gumroad Trigger"]
  n59["Local File Trigger"]
  n60["On form submission"]
  n61["Schedule Trigger"]
  n62["Webhook"]
  n63["When chat message received"]
  n64["When clicking #39;Test workflow#39;"]
  n65["Workflow Input Trigger"]
  n66["Gmail Trigger"]
  n67["Google Sheets Trigger"]
  n68["Code"]
  n69["Date #38; Time"]
  n70["Edit Fields"]
  n71["Filter"]
  n72["Limit"]
  n73["Remove Duplicates"]
  n74["Split Out"]
  n75["Aggregate"]
  n76["Merge"]
  n77["Summarize"]
  n78["Convert to File"]
  n79["Extract from File"]
  n80["HTML"]
  n81["Markdown"]
  n82["Rename Keys"]
  n83["Sort"]
  n84["If"]
  n85["Loop Over Items"]
  n86["Replace Me"]
  n87["Execute Workflow"]
  n88["Wait"]
  n89["Execute Command"]
  n90["HTTP Request"]
  n91["Execution Data"]
  n92["FTP"]
  n93["Respond to Webhook"]
  n94["RSS Read"]
  n95["AI Transform"]
  n96["MCP Client"]
  n86 -->|"main out 0 to in 0"| n85
  n85 -->|"main out 1 to in 0"| n86
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
