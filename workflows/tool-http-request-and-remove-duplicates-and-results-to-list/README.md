# tool http request and remove duplicates and results to list

This folder contains the **tool http request and remove duplicates and results to list** workflow. Its executable nodes use `agent`, `httpRequest`, `limit`, `lmChatOpenAi`, `manualTrigger`, `notion`, `outputParserStructured`, `removeDuplicates`, `set`, `splitInBatches`, `splitOut`, `toolHttpRequest`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`tool-http-request-and-remove-duplicates-and-results-to-list.json`](tool-http-request-and-remove-duplicates-and-results-to-list.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `notionApi`, `openAiApi`, `serpApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Search Crunchbase | `toolHttpRequest` | POST |
| Search WellFound | `toolHttpRequest` | POST |
| Search LinkedIn | `toolHttpRequest` | POST |
| Structured Output Parser1 | `outputParserStructured` | Inspect parameters |
| Webscraper Tool1 | `toolHttpRequest` | POST |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Extract Domain | `set` | Inspect parameters |
| Results to List | `splitOut` | Inspect parameters |
| Check Company Profiles Exist | `toolHttpRequest` | Inspect parameters |
| Webscraper Tool | `toolHttpRequest` | POST |
| Search Company Website | `toolHttpRequest` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Search Product Review Sites | `toolHttpRequest` | Inspect parameters |
| Webscraper Tool2 | `toolHttpRequest` | POST |
| Structured Output Parser2 | `outputParserStructured` | Inspect parameters |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Insert Into Notion | `notion` | databasePage |
| Limit | `limit` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Competitor Search via Exa.ai | `httpRequest` | POST |
| Get Company News | `toolHttpRequest` | Inspect parameters |
| Set Source Company | `set` | Inspect parameters |
| Collect Results | `set` | Inspect parameters |
| 2sec | `wait` | Inspect parameters |
| Company Overview Agent | `agent` | Inspect parameters |
| Company Product Offering Agent | `agent` | Inspect parameters |
| Company Product Reviews Agent | `agent` | Inspect parameters |

## Connection map

- 2sec → Loop Over Items (`main`, output 0, input 0)
- Limit → Loop Over Items (`main`, output 0, input 0)
- Extract Domain → Remove Duplicates (`main`, output 0, input 0)
- Collect Results → Insert Into Notion (`main`, output 0, input 0)
- Loop Over Items → Company Overview Agent (`main`, output 1, input 0)
- Results to List → Extract Domain (`main`, output 0, input 0)
- Search LinkedIn → Company Overview Agent (`ai_tool`, output 0, input 0)
- Webscraper Tool → Company Product Offering Agent (`ai_tool`, output 0, input 0)
- Get Company News → Company Overview Agent (`ai_tool`, output 0, input 0)
- Search WellFound → Company Overview Agent (`ai_tool`, output 0, input 0)
- Webscraper Tool1 → Company Overview Agent (`ai_tool`, output 0, input 0)
- Webscraper Tool2 → Company Product Reviews Agent (`ai_tool`, output 0, input 0)
- OpenAI Chat Model → Company Product Offering Agent (`ai_languageModel`, output 0, input 0)
- Remove Duplicates → Limit (`main`, output 0, input 0)
- Search Crunchbase → Company Overview Agent (`ai_tool`, output 0, input 0)
- Insert Into Notion → 2sec (`main`, output 0, input 0)
- OpenAI Chat Model1 → Company Overview Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Company Product Reviews Agent (`ai_languageModel`, output 0, input 0)
- Set Source Company → Competitor Search via Exa.ai (`main`, output 0, input 0)
- Company Overview Agent → Company Product Offering Agent (`main`, output 0, input 0)
- Search Company Website → Company Product Offering Agent (`ai_tool`, output 0, input 0)
- Structured Output Parser → Company Product Offering Agent (`ai_outputParser`, output 0, input 0)
- Structured Output Parser1 → Company Overview Agent (`ai_outputParser`, output 0, input 0)
- Structured Output Parser2 → Company Product Reviews Agent (`ai_outputParser`, output 0, input 0)
- Search Product Review Sites → Company Product Reviews Agent (`ai_tool`, output 0, input 0)
- Check Company Profiles Exist → Company Overview Agent (`ai_tool`, output 0, input 0)
- Competitor Search via Exa.ai → Results to List (`main`, output 0, input 0)
- Company Product Reviews Agent → Collect Results (`main`, output 0, input 0)
- Company Product Offering Agent → Company Product Reviews Agent (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Source Company (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0547_Wait_Splitout_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0547_Wait_Splitout_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
