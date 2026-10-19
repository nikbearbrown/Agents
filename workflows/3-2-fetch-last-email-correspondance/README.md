# 3.2: Fetch Last Email Correspondance

This folder contains the **3.2: Fetch Last Email Correspondance** workflow. Its executable nodes use `aggregate`, `chainLlm`, `executeWorkflow`, `executeWorkflowTrigger`, `gmail`, `googleCalendar`, `html`, `httpRequest`, `if`, `informationExtractor`, `lmChatOpenAi`, `merge`, `scheduleTrigger`, `set`, `splitOut`, `switch`, `whatsApp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`3-2-fetch-last-email-correspondance.json`](3-2-fetch-last-email-correspondance.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleCalendarOAuth2Api`, `httpQueryAuth`, `openAiApi`, `whatsAppApi`

**Entry nodes:** Execute Workflow Trigger, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get Message Contents | `gmail` | get |
| Simplify Emails | `set` | Inspect parameters |
| Check For Upcoming Meetings | `googleCalendar` | getAll |
| OpenAI Chat Model2 | `lmChatOpenAi` | Inspect parameters |
| Extract Attendee Information | `informationExtractor` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Get Last Correspondence | `gmail` | getAll |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| WhatsApp Business Cloud | `whatsApp` | send |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Return LinkedIn Success | `set` | Inspect parameters |
| Return LinkedIn Error | `set` | Inspect parameters |
| Return Email Error | `set` | Inspect parameters |
| Return Email Success | `set` | Inspect parameters |
| Set Route Email | `set` | Inspect parameters |
| Set Route Linkedin | `set` | Inspect parameters |
| Router | `switch` | Inspect parameters |
| Return LinkedIn Error1 | `set` | Inspect parameters |
| Has Emails? | `if` | Inspect parameters |
| Return Email Error1 | `set` | Inspect parameters |
| Sections To List | `splitOut` | Inspect parameters |
| Set LinkedIn Cookie | `set` | Inspect parameters |
| Attendees to List | `splitOut` | Inspect parameters |
| Merge Attendee with Summaries | `set` | Inspect parameters |
| Has Email Address? | `if` | Inspect parameters |
| Has LinkedIn URL? | `if` | Inspect parameters |
| Get Correspondance | `executeWorkflow` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Aggregate Attendees | `aggregate` | Inspect parameters |
| Activities To Array | `aggregate` | Inspect parameters |
| Extract Profile Metadata | `html` | extractHtmlContent |
| Activities To List | `splitOut` | Inspect parameters |
| APIFY Web Scraper | `httpRequest` | Inspect parameters |
| Get Activity Details | `html` | extractHtmlContent |
| Get Sections | `html` | extractHtmlContent |
| Get About Section | `set` | Inspect parameters |
| Get Activity Section | `set` | Inspect parameters |
| Extract Activities | `html` | extractHtmlContent |
| Merge1 | `merge` | Inspect parameters |
| Is Scrape Successful? | `if` | Inspect parameters |
| Extract About | `html` | extractHtmlContent |
| Get LinkedIn Profile & Activity | `executeWorkflow` | Inspect parameters |
| Correspondance Recap Agent | `chainLlm` | Inspect parameters |
| Attendee Research Agent | `chainLlm` | Inspect parameters |
| LinkedIn Summarizer Agent | `chainLlm` | Inspect parameters |

## Connection map

- Merge → Merge Attendee with Summaries (`main`, output 0, input 0)
- Merge1 → LinkedIn Summarizer Agent (`main`, output 0, input 0)
- Router → Has Email Address? (`main`, output 0, input 0)
- Router → Has LinkedIn URL? (`main`, output 1, input 0)
- Has Emails? → Get Message Contents (`main`, output 0, input 0)
- Has Emails? → Return Email Error (`main`, output 1, input 0)
- Get Sections → Get About Section (`main`, output 0, input 0)
- Get Sections → Get Activity Section (`main`, output 0, input 0)
- Extract About → Merge1 (`main`, output 0, input 0)
- Set Route Email → Get Correspondance (`main`, output 0, input 0)
- Simplify Emails → Correspondance Recap Agent (`main`, output 0, input 0)
- Schedule Trigger → Check For Upcoming Meetings (`main`, output 0, input 0)
- Sections To List → Get Sections (`main`, output 0, input 0)
- APIFY Web Scraper → Is Scrape Successful? (`main`, output 0, input 0)
- Attendees to List → Set Route Email (`main`, output 0, input 0)
- Attendees to List → Set Route Linkedin (`main`, output 0, input 0)
- Get About Section → Extract About (`main`, output 0, input 0)
- Has LinkedIn URL? → Set LinkedIn Cookie (`main`, output 0, input 0)
- Has LinkedIn URL? → Return LinkedIn Error1 (`main`, output 1, input 0)
- OpenAI Chat Model → Correspondance Recap Agent (`ai_languageModel`, output 0, input 0)
- Activities To List → Get Activity Details (`main`, output 0, input 0)
- Extract Activities → Activities To List (`main`, output 0, input 0)
- Get Correspondance → Merge (`main`, output 0, input 0)
- Has Email Address? → Get Last Correspondence (`main`, output 0, input 0)
- Has Email Address? → Return Email Error1 (`main`, output 1, input 0)
- OpenAI Chat Model1 → LinkedIn Summarizer Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model2 → Extract Attendee Information (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Attendee Research Agent (`ai_languageModel`, output 0, input 0)
- Set Route Linkedin → Get LinkedIn Profile & Activity (`main`, output 0, input 0)
- Activities To Array → Merge1 (`main`, output 0, input 1)
- Aggregate Attendees → Attendee Research Agent (`main`, output 0, input 0)
- Set LinkedIn Cookie → APIFY Web Scraper (`main`, output 0, input 0)
- Get Activity Details → Activities To Array (`main`, output 0, input 0)
- Get Activity Section → Extract Activities (`main`, output 0, input 0)
- Get Message Contents → Simplify Emails (`main`, output 0, input 0)
- Is Scrape Successful? → Extract Profile Metadata (`main`, output 0, input 0)
- Is Scrape Successful? → Return LinkedIn Error (`main`, output 1, input 0)
- Attendee Research Agent → WhatsApp Business Cloud (`main`, output 0, input 0)
- Get Last Correspondence → Has Emails? (`main`, output 0, input 0)
- Execute Workflow Trigger → Router (`main`, output 0, input 0)
- Extract Profile Metadata → Sections To List (`main`, output 0, input 0)
- LinkedIn Summarizer Agent → Return LinkedIn Success (`main`, output 0, input 0)
- Correspondance Recap Agent → Return Email Success (`main`, output 0, input 0)
- Check For Upcoming Meetings → Extract Attendee Information (`main`, output 0, input 0)
- Extract Attendee Information → Attendees to List (`main`, output 0, input 0)
- Merge Attendee with Summaries → Aggregate Attendees (`main`, output 0, input 0)
- Get LinkedIn Profile & Activity → Merge (`main`, output 0, input 1)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 2}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0649_Splitout_GoogleCalendar_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0649_Splitout_GoogleCalendar_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
