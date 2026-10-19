# Get companies from database

This folder contains the **Get companies from database** workflow. Its executable nodes use `agent`, `aggregate`, `filter`, `html`, `httpRequest`, `lmChatOpenAi`, `manualTrigger`, `markdown`, `merge`, `outputParserStructured`, `removeDuplicates`, `set`, `splitOut`, `supabase`, `toolWorkflow`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-companies-from-database.json`](get-companies-from-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `openAiApi`, `supabaseApi`

**Entry nodes:** Execute workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Text | `toolWorkflow` | Inspect parameters |
| URLs | `toolWorkflow` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| JSON Parser | `outputParserStructured` | Inspect parameters |
| Map company name and website | `set` | Inspect parameters |
| Execute workflow | `manualTrigger` | Inspect parameters |
| Get companies | `supabase` | getAll |
| Select company name and website | `set` | Inspect parameters |
| Set social media array | `set` | Inspect parameters |
| Merge all data | `merge` | Inspect parameters |
| Insert new row | `supabase` | Inspect parameters |
| Convert HTML to Markdown | `markdown` | Inspect parameters |
| Retrieve URLs | `html` | extractHtmlContent |
| Split out URLs | `splitOut` | Inspect parameters |
| Remove duplicated | `removeDuplicates` | Inspect parameters |
| Set domain to path | `set` | Inspect parameters |
| Filter out invalid URLs | `filter` | Inspect parameters |
| Aggregate URLs | `aggregate` | Inspect parameters |
| Filter out empty hrefs | `filter` | Inspect parameters |
| Set domain (text) | `set` | Inspect parameters |
| Add protocool to domain (text) | `set` | Inspect parameters |
| Get website (text) | `httpRequest` | Inspect parameters |
| Set response (text) | `set` | Inspect parameters |
| Set domain (URL) | `set` | Inspect parameters |
| Get website (URL) | `httpRequest` | Inspect parameters |
| Set response (URL) | `set` | Inspect parameters |
| Add protocool to domain (URL) | `set` | Inspect parameters |
| Crawl website | `agent` | Inspect parameters |

## Connection map

- Text → Crawl website (`ai_tool`, output 0, input 0)
- URLs → Crawl website (`ai_tool`, output 0, input 0)
- JSON Parser → Crawl website (`ai_outputParser`, output 0, input 0)
- Crawl website → Set social media array (`main`, output 0, input 0)
- Get companies → Select company name and website (`main`, output 0, input 0)
- Retrieve URLs → Split out URLs (`main`, output 0, input 0)
- Aggregate URLs → Set response (URL) (`main`, output 0, input 0)
- Merge all data → Insert new row (`main`, output 0, input 0)
- Split out URLs → Filter out empty hrefs (`main`, output 0, input 0)
- Execute workflow → Get companies (`main`, output 0, input 0)
- Set domain (URL) → Add protocool to domain (URL) (`main`, output 0, input 0)
- Get website (URL) → Retrieve URLs (`main`, output 0, input 0)
- OpenAI Chat Model → Crawl website (`ai_languageModel`, output 0, input 0)
- Remove duplicated → Set domain to path (`main`, output 0, input 0)
- Set domain (text) → Add protocool to domain (text) (`main`, output 0, input 0)
- Get website (text) → Convert HTML to Markdown (`main`, output 0, input 0)
- Set domain to path → Filter out invalid URLs (`main`, output 0, input 0)
- Filter out empty hrefs → Remove duplicated (`main`, output 0, input 0)
- Set social media array → Merge all data (`main`, output 0, input 1)
- Filter out invalid URLs → Aggregate URLs (`main`, output 0, input 0)
- Convert HTML to Markdown → Set response (text) (`main`, output 0, input 0)
- Map company name and website → Merge all data (`main`, output 0, input 0)
- Add protocool to domain (URL) → Get website (URL) (`main`, output 0, input 0)
- Add protocool to domain (text) → Get website (text) (`main`, output 0, input 0)
- Select company name and website → Crawl website (`main`, output 0, input 0)
- Select company name and website → Map company name and website (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0520_Splitout_Filter_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0520_Splitout_Filter_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
