# TechCrunch & VentureBeat

This folder contains the **TechCrunch & VentureBeat** workflow. Its executable nodes use `airtable`, `chainLlm`, `executeWorkflow`, `executeWorkflowTrigger`, `filter`, `html`, `httpRequest`, `informationExtractor`, `lmChatAnthropic`, `lmChatOpenRouter`, `manualTrigger`, `merge`, `outputParserAutofixing`, `outputParserStructured`, `set`, `splitOut`, `xml`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`techcrunch-venturebeat.json`](techcrunch-venturebeat.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `anthropicApi`, `httpHeaderAuth`, `openRouterApi`

**Entry nodes:** When clicking ‘Test workflow’, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Perplexity | `lmChatOpenRouter` | Inspect parameters |
| Filter1 | `filter` | Inspect parameters |
| Extract Structured Data  | `informationExtractor` | Inspect parameters |
| Research URL | `chainLlm` | Inspect parameters |
| Extract URL | `chainLlm` | Inspect parameters |
| Merge Extracted Data | `merge` | Inspect parameters |
| Split TC Articles | `splitOut` | Inspect parameters |
| TC HTML Parser | `html` | extractHtmlContent |
| Split VB Articles | `splitOut` | Inspect parameters |
| VB HTML Parser | `html` | extractHtmlContent |
| Venturebeat (VB) | `httpRequest` | Inspect parameters |
| Techcrunch (TC) | `httpRequest` | Inspect parameters |
| Claude 3.5 Sonnet | `lmChatAnthropic` | Inspect parameters |
| Claude 3.5 Haiku | `lmChatAnthropic` | Inspect parameters |
| Collect Data | `set` | Inspect parameters |
| Airtable | `airtable` | create |
| Auto-fixing Output Parser | `outputParserAutofixing` | Inspect parameters |
| Extract Structured JSON  | `outputParserStructured` | Inspect parameters |
| Prompts | `set` | Inspect parameters |
| Deep Research | `httpRequest` | POST |
| Pick data (Perplexity) | `set` | Inspect parameters |
| Pick data (jina) | `set` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| JINA Deep Search | `httpRequest` | POST |
| Write Results to Airtable | `airtable` | create |
| Extract Structured Data | `chainLlm` | Inspect parameters |
| Route to Deep Research | `executeWorkflow` | Inspect parameters |
| Parse TC XML | `xml` | Inspect parameters |
| Parse VB XML | `xml` | Inspect parameters |
| Claude  3.5 Sonnet | `lmChatAnthropic` | Inspect parameters |
| Get Funding Article HTML for scraping (TC) | `httpRequest` | Inspect parameters |
| Get Funding Article HTML for scraping (VB) | `httpRequest` | Inspect parameters |

## Connection map

- Filter → Get Funding Article HTML for scraping (TC) (`main`, output 0, input 0)
- Filter1 → Get Funding Article HTML for scraping (VB) (`main`, output 0, input 0)
- Prompts → Deep Research (`main`, output 0, input 0)
- Perplexity → Research URL (`ai_languageModel`, output 0, input 0)
- Extract URL → Collect Data (`main`, output 0, input 0)
- Collect Data → Route to Deep Research (`main`, output 0, input 0)
- Collect Data → Airtable (`main`, output 0, input 0)
- Parse TC XML → Split TC Articles (`main`, output 0, input 0)
- Parse VB XML → Split VB Articles (`main`, output 0, input 0)
- Research URL → Extract URL (`main`, output 0, input 0)
- Deep Research → Pick data (Perplexity) (`main`, output 0, input 0)
- TC HTML Parser → Merge Extracted Data (`main`, output 0, input 0)
- VB HTML Parser → Merge Extracted Data (`main`, output 0, input 1)
- Techcrunch (TC) → Parse TC XML (`main`, output 0, input 0)
- Claude 3.5 Haiku → Extract URL (`ai_languageModel`, output 0, input 0)
- JINA Deep Search → Pick data (jina) (`main`, output 0, input 0)
- Venturebeat (VB) → Parse VB XML (`main`, output 0, input 0)
- Claude 3.5 Sonnet → Extract Structured Data  (`ai_languageModel`, output 0, input 0)
- Split TC Articles → Filter (`main`, output 0, input 0)
- Split VB Articles → Filter1 (`main`, output 0, input 0)
- Claude  3.5 Sonnet → Extract Structured Data (`ai_languageModel`, output 0, input 0)
- Claude  3.5 Sonnet → Auto-fixing Output Parser (`ai_languageModel`, output 0, input 0)
- Merge Extracted Data → Extract Structured Data  (`main`, output 0, input 0)
- Pick data (Perplexity) → Extract Structured Data (`main`, output 0, input 0)
- Extract Structured Data → Write Results to Airtable (`main`, output 0, input 0)
- Extract Structured Data  → Research URL (`main`, output 0, input 0)
- Extract Structured JSON  → Auto-fixing Output Parser (`ai_outputParser`, output 0, input 0)
- Structured Output Parser → Extract URL (`ai_outputParser`, output 0, input 0)
- Auto-fixing Output Parser → Extract Structured Data (`ai_outputParser`, output 0, input 0)
- When Executed by Another Workflow → Prompts (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Techcrunch (TC) (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Venturebeat (VB) (`main`, output 0, input 0)
- Get Funding Article HTML for scraping (TC) → TC HTML Parser (`main`, output 0, input 0)
- Get Funding Article HTML for scraping (VB) → VB HTML Parser (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0780_Splitout_Filter_Process_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0780_Splitout_Filter_Process_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
