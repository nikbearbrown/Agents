# HDW Lead Geländewagen

This folder contains the **HDW Lead Geländewagen** workflow. Its executable nodes use `agent`, `aggregate`, `chatTrigger`, `code`, `googleSheets`, `hdwLinkedin`, `hdwLinkedinManagement`, `hdwWebParserTool`, `if`, `limit`, `lmChatOpenAi`, `manualTrigger`, `memoryBufferWindow`, `openAi`, `outputParserStructured`, `scheduleTrigger`, `sort`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`hdw-lead-gelandewagen.json`](hdw-lead-gelandewagen.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `hdwLinkedinApi`, `openAiApi`

**Entry nodes:** When chat message received, Schedule Trigger, Schedule Trigger1, When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Simple Memory | `memoryBufferWindow` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Google Sheets | `googleSheets` | appendOrUpdate |
| Google Sheets1 | `googleSheets` | Inspect parameters |
| Google Sheets2 | `googleSheets` | update |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| HDW LinkedIn SN | `hdwLinkedin` | search |
| HDW Get Company Website | `hdwLinkedin` | company |
| Google Sheets3 | `googleSheets` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Google Sheets4 | `googleSheets` | Inspect parameters |
| HDW Get User Posts | `hdwLinkedin` | getPosts |
| Aggregate | `aggregate` | Inspect parameters |
| Loop Over Items2 | `splitInBatches` | Inspect parameters |
| Google Sheets5 | `googleSheets` | update |
| Google Sheets6 | `googleSheets` | Inspect parameters |
| Aggregate1 | `aggregate` | Inspect parameters |
| Loop Over Items3 | `splitInBatches` | Inspect parameters |
| Google Sheets7 | `googleSheets` | update |
| Google Sheets8 | `googleSheets` | Inspect parameters |
| Aggregate2 | `aggregate` | Inspect parameters |
| Loop Over Items4 | `splitInBatches` | Inspect parameters |
| Google Sheets9 | `googleSheets` | update |
| HDW Get Company News | `hdwLinkedin` | google / googleSearch |
| HDW Get Company Posts | `hdwLinkedin` | company / getCompanyPosts |
| Loop Over Items5 | `splitInBatches` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Google Sheets10 | `googleSheets` | update |
| HDW Site-map | `hdwWebParserTool` | map |
| HDW Parser | `hdwWebParserTool` | Inspect parameters |
| Summarise user posts | `openAi` | Inspect parameters |
| Summarise company news | `openAi` | Inspect parameters |
| Summarise company posts | `openAi` | Inspect parameters |
| Summarise company website | `agent` | Inspect parameters |
| Google Sheets11 | `googleSheets` | Inspect parameters |
| Loop Over Items6 | `splitInBatches` | Inspect parameters |
| Google Sheets12 | `googleSheets` | update |
| Google Sheets13 | `googleSheets` | Inspect parameters |
| Sort | `sort` | Inspect parameters |
| If2 | `if` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Loop Over Items7 | `splitInBatches` | Inspect parameters |
| Google Sheets14 | `googleSheets` | update |
| Google Sheets15 | `googleSheets` | update |
| Google Sheets16 | `googleSheets` | Inspect parameters |
| Google Sheets17 | `googleSheets` | update |
| Loop Over Items8 | `splitInBatches` | Inspect parameters |
| HDW LinkedIn Send Message | `hdwLinkedinManagement` | chat |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| HDW Get LinkedIn Profile Connections | `hdwLinkedinManagement` | getConnections |
| HDW Send LinkedIn Connection | `hdwLinkedinManagement` | Inspect parameters |
| AI Agent: ICP -> LinkedIn search filters | `agent` | Inspect parameters |
| Company name is not empty | `if` | Inspect parameters |
| Website is not empty | `if` | Inspect parameters |
| Post summary is empty | `if` | Inspect parameters |
| Company news is empty | `if` | Inspect parameters |
| Company post is empty | `if` | Inspect parameters |
| Lead Score is empty | `if` | Inspect parameters |
| Company Score Analysis | `openAi` | Inspect parameters |
| Split LinkedIn connections to items | `code` | Inspect parameters |
| 5s | `wait` | Inspect parameters |
| Company name is not empty1 | `if` | Inspect parameters |
| Google Sheets18 | `googleSheets` | update |
| Loop Over Items9 | `splitInBatches` | Inspect parameters |
| HDW Get Company Website1 | `hdwLinkedin` | google / googleSearch |
| Google Sheets19 | `googleSheets` | Inspect parameters |

## Connection map

- 5s → HDW LinkedIn Send Message (`main`, output 0, input 0)
- If2 → Limit (`main`, output 0, input 0)
- Sort → If2 (`main`, output 0, input 0)
- Limit → Loop Over Items7 (`main`, output 0, input 0)
- Aggregate → Summarise user posts (`main`, output 0, input 0)
- Split Out → Loop Over Items5 (`main`, output 0, input 0)
- Aggregate1 → Summarise company news (`main`, output 0, input 0)
- Aggregate2 → Summarise company posts (`main`, output 0, input 0)
- HDW Parser → Summarise company website (`ai_tool`, output 0, input 0)
- HDW Site-map → Summarise company website (`ai_tool`, output 0, input 0)
- Google Sheets → Google Sheets1 (`main`, output 0, input 0)
- Simple Memory → AI Agent: ICP -> LinkedIn search filters (`ai_memory`, output 0, input 0)
- Google Sheets1 → Company name is not empty (`main`, output 0, input 0)
- Google Sheets2 → Loop Over Items (`main`, output 0, input 0)
- Google Sheets3 → Website is not empty (`main`, output 0, input 0)
- Google Sheets4 → Post summary is empty (`main`, output 0, input 0)
- Google Sheets5 → Loop Over Items2 (`main`, output 0, input 0)
- Google Sheets6 → Company news is empty (`main`, output 0, input 0)
- Google Sheets7 → Loop Over Items3 (`main`, output 0, input 0)
- Google Sheets8 → Company post is empty (`main`, output 0, input 0)
- Google Sheets9 → Loop Over Items4 (`main`, output 0, input 0)
- Google Sheets10 → Loop Over Items1 (`main`, output 0, input 0)
- Google Sheets11 → Lead Score is empty (`main`, output 0, input 0)
- Google Sheets12 → Loop Over Items6 (`main`, output 0, input 0)
- Google Sheets13 → Sort (`main`, output 0, input 0)
- Google Sheets14 → Loop Over Items7 (`main`, output 0, input 0)
- Google Sheets15 → Google Sheets16 (`main`, output 0, input 0)
- Google Sheets16 → Loop Over Items8 (`main`, output 0, input 0)
- Google Sheets17 → Loop Over Items8 (`main`, output 0, input 0)
- Google Sheets18 → Loop Over Items9 (`main`, output 0, input 0)
- Google Sheets19 → Company name is not empty1 (`main`, output 0, input 0)
- HDW LinkedIn SN → Loop Over Items5 (`main`, output 0, input 0)
- Loop Over Items → Google Sheets19 (`main`, output 0, input 0)
- Loop Over Items → HDW Get Company Website (`main`, output 1, input 0)
- Loop Over Items1 → Google Sheets4 (`main`, output 0, input 0)
- Loop Over Items1 → Summarise company website (`main`, output 1, input 0)
- Loop Over Items2 → Google Sheets6 (`main`, output 0, input 0)
- Loop Over Items2 → HDW Get User Posts (`main`, output 1, input 0)
- Loop Over Items3 → Google Sheets8 (`main`, output 0, input 0)
- Loop Over Items3 → HDW Get Company News (`main`, output 1, input 0)
- Loop Over Items4 → Google Sheets11 (`main`, output 0, input 0)
- Loop Over Items4 → HDW Get Company Posts (`main`, output 1, input 0)
- Loop Over Items5 → Google Sheets (`main`, output 0, input 0)
- Loop Over Items5 → HDW LinkedIn SN (`main`, output 1, input 0)
- Loop Over Items6 → Google Sheets13 (`main`, output 0, input 0)
- Loop Over Items6 → Company Score Analysis (`main`, output 1, input 0)
- Loop Over Items7 → HDW Send LinkedIn Connection (`main`, output 1, input 0)
- Loop Over Items8 → 5s (`main`, output 1, input 0)
- Loop Over Items9 → Google Sheets3 (`main`, output 0, input 0)
- Loop Over Items9 → HDW Get Company Website1 (`main`, output 1, input 0)
- Schedule Trigger → Google Sheets13 (`main`, output 0, input 0)
- OpenAI Chat Model → AI Agent: ICP -> LinkedIn search filters (`ai_languageModel`, output 0, input 0)
- Schedule Trigger1 → HDW Get LinkedIn Profile Connections (`main`, output 0, input 0)
- HDW Get User Posts → Aggregate (`main`, output 0, input 0)
- OpenAI Chat Model1 → Summarise company website (`ai_languageModel`, output 0, input 0)
- Lead Score is empty → Loop Over Items6 (`main`, output 0, input 0)
- HDW Get Company News → Aggregate1 (`main`, output 0, input 0)
- Summarise user posts → Google Sheets5 (`main`, output 0, input 0)
- Website is not empty → Loop Over Items1 (`main`, output 0, input 0)
- Company news is empty → Loop Over Items3 (`main`, output 0, input 0)
- Company post is empty → Loop Over Items4 (`main`, output 0, input 0)
- HDW Get Company Posts → Aggregate2 (`main`, output 0, input 0)
- Post summary is empty → Loop Over Items2 (`main`, output 0, input 0)
- Company Score Analysis → Google Sheets12 (`main`, output 0, input 0)
- Summarise company news → Google Sheets7 (`main`, output 0, input 0)
- HDW Get Company Website → Google Sheets2 (`main`, output 0, input 0)
- Summarise company posts → Google Sheets9 (`main`, output 0, input 0)
- HDW Get Company Website1 → Google Sheets18 (`main`, output 0, input 0)
- Structured Output Parser → AI Agent: ICP -> LinkedIn search filters (`ai_outputParser`, output 0, input 0)
- Company name is not empty → Loop Over Items (`main`, output 0, input 0)
- HDW LinkedIn Send Message → Google Sheets17 (`main`, output 0, input 0)
- Summarise company website → Google Sheets10 (`main`, output 0, input 0)
- Company name is not empty1 → Loop Over Items9 (`main`, output 0, input 0)
- When chat message received → AI Agent: ICP -> LinkedIn search filters (`main`, output 0, input 0)
- HDW Send LinkedIn Connection → Google Sheets14 (`main`, output 0, input 0)
- Split LinkedIn connections to items → Google Sheets15 (`main`, output 0, input 0)
- HDW Get LinkedIn Profile Connections → Split LinkedIn connections to items (`main`, output 0, input 0)
- AI Agent: ICP -> LinkedIn search filters → Split Out (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1955_Wait_Splitout_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1955_Wait_Splitout_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
