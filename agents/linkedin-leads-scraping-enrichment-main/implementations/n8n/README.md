# LinkedIn Leads Scraping & Enrichment (Main)

This folder contains the **LinkedIn Leads Scraping & Enrichment (Main)** workflow. Its executable nodes use `code`, `formTrigger`, `googleSheets`, `googleSheetsTrigger`, `httpRequest`, `if`, `merge`, `openAi`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-leads-scraping-enrichment-main.json`](linkedin-leads-scraping-enrichment-main.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `openAiApi`

**Entry nodes:** On form submission, Google Sheets Trigger, Google Sheets Trigger2, Schedule Trigger, Google Sheets Trigger3, Google Sheets Trigger4, Google Sheets Trigger5, Schedule Trigger2, Schedule Trigger3, Google Sheets Trigger6

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On form submission | `formTrigger` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| OpenAI1 | `openAi` | Inspect parameters |
| Google Sheets Trigger2 | `googleSheetsTrigger` | Inspect parameters |
| Clean Data | `set` | Inspect parameters |
| Add Leads to Google Sheet | `googleSheets` | append |
| Add Linkedin Username | `googleSheets` | update |
| Get Pending Username Row | `googleSheets` | Inspect parameters |
| Add Email Address | `googleSheets` | update |
| Mark Invalid Email | `googleSheets` | update |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Email from Apollo | `httpRequest` | POST |
| Confirm Email Validity | `httpRequest` | Inspect parameters |
| Get Pending Email Statuses | `googleSheets` | Inspect parameters |
| Google Sheets Trigger3 | `googleSheetsTrigger` | Inspect parameters |
| Get Profile Posts | `httpRequest` | Inspect parameters |
| Get About Profile | `httpRequest` | Inspect parameters |
| Get Pending About and Posts Rows | `googleSheets` | Inspect parameters |
| Clean Profile Data | `code` | Inspect parameters |
| Google Sheets Trigger4 | `googleSheetsTrigger` | Inspect parameters |
| Get Pending About and Posts Rows1 | `googleSheets` | Inspect parameters |
| Clean Posts Data | `code` | Inspect parameters |
| Google Sheets Trigger5 | `googleSheetsTrigger` | Inspect parameters |
| Schedule Trigger2 | `scheduleTrigger` | Inspect parameters |
| get invalid email rows | `googleSheets` | Inspect parameters |
| update_to_pending | `googleSheets` | update |
| get_failed_profile_summary_rows | `googleSheets` | Inspect parameters |
| update_to_pending1 | `googleSheets` | update |
| Schedule Trigger3 | `scheduleTrigger` | Inspect parameters |
| get_failed_posts_summary_rows1 | `googleSheets` | Inspect parameters |
| Posts AI Summarizer | `openAi` | Inspect parameters |
| AI Profile Summarizer | `openAi` | Inspect parameters |
| Update Profile Summary | `googleSheets` | update |
| Update Posts Summary | `googleSheets` | update |
| Get Completely Enriched Profiles | `googleSheets` | Inspect parameters |
| update_to_unscraped | `googleSheets` | update |
| Append to Enriched Leads Database | `googleSheets` | appendOrUpdate |
| update status to failed | `googleSheets` | update |
| Google Sheets | `googleSheets` | update |
| Stringify Profile Data1 | `code` | Inspect parameters |
| Stringify Posts Data | `code` | Inspect parameters |
| Generate Leads with Apollo.io | `httpRequest` | POST |
| Google Sheets Trigger6 | `googleSheetsTrigger` | Inspect parameters |
| Get Pending About and Posts Rows2 | `googleSheets` | Inspect parameters |
| Clean Profile Data1 | `code` | Inspect parameters |
| Stringify Data2 | `code` | Inspect parameters |
| AI Profile Summarizer1 | `openAi` | Inspect parameters |
| Update Profile Summary1 | `googleSheets` | update |
| Stringify Data3 | `code` | Inspect parameters |
| Posts AI Summarizer1 | `openAi` | Inspect parameters |
| Get About Profile2 | `httpRequest` | Inspect parameters |
| Clean Profile Data2 | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| update status to failed1 | `googleSheets` | update |
| If email is valid | `if` | Inspect parameters |

## Connection map

- Merge → Update Profile Summary1 (`main`, output 0, input 0)
- OpenAI1 → Add Linkedin Username (`main`, output 0, input 0)
- Split Out → Clean Data (`main`, output 0, input 0)
- Clean Data → Add Leads to Google Sheet (`main`, output 0, input 0)
- Stringify Data2 → AI Profile Summarizer1 (`main`, output 0, input 0)
- Stringify Data3 → Posts AI Summarizer1 (`main`, output 0, input 0)
- Clean Posts Data → Stringify Posts Data (`main`, output 0, input 0)
- Clean Posts Data → Google Sheets (`main`, output 1, input 0)
- Schedule Trigger → get invalid email rows (`main`, output 0, input 0)
- Get About Profile → Clean Profile Data (`main`, output 0, input 0)
- Get Profile Posts → Clean Posts Data (`main`, output 0, input 0)
- If email is valid → Add Email Address (`main`, output 0, input 0)
- If email is valid → Mark Invalid Email (`main`, output 1, input 0)
- Schedule Trigger2 → get_failed_profile_summary_rows (`main`, output 0, input 0)
- Schedule Trigger3 → get_failed_posts_summary_rows1 (`main`, output 0, input 0)
- Clean Profile Data → Stringify Profile Data1 (`main`, output 0, input 0)
- Clean Profile Data → update status to failed (`main`, output 1, input 0)
- Get About Profile2 → Clean Profile Data1 (`main`, output 0, input 0)
- Get About Profile2 → Clean Profile Data2 (`main`, output 0, input 0)
- Get About Profile2 → update status to failed1 (`main`, output 1, input 0)
- On form submission → Generate Leads with Apollo.io (`main`, output 0, input 0)
- Clean Profile Data1 → Stringify Data2 (`main`, output 0, input 0)
- Clean Profile Data2 → Stringify Data3 (`main`, output 0, input 0)
- Posts AI Summarizer → Update Posts Summary (`main`, output 0, input 0)
- Posts AI Summarizer1 → Merge (`main`, output 0, input 1)
- Stringify Posts Data → Posts AI Summarizer (`main`, output 0, input 0)
- AI Profile Summarizer → Update Profile Summary (`main`, output 0, input 0)
- Get Email from Apollo → Confirm Email Validity (`main`, output 0, input 0)
- Google Sheets Trigger → Get Pending Username Row (`main`, output 0, input 0)
- AI Profile Summarizer1 → Merge (`main`, output 0, input 0)
- Confirm Email Validity → If email is valid (`main`, output 0, input 0)
- Google Sheets Trigger2 → Get Pending Email Statuses (`main`, output 0, input 0)
- Google Sheets Trigger3 → Get Pending About and Posts Rows (`main`, output 0, input 0)
- Google Sheets Trigger4 → Get Pending About and Posts Rows1 (`main`, output 0, input 0)
- Google Sheets Trigger5 → Get Completely Enriched Profiles (`main`, output 0, input 0)
- Google Sheets Trigger6 → Get Pending About and Posts Rows2 (`main`, output 0, input 0)
- get invalid email rows → update_to_pending (`main`, output 0, input 0)
- Stringify Profile Data1 → AI Profile Summarizer (`main`, output 0, input 0)
- Get Pending Username Row → OpenAI1 (`main`, output 0, input 0)
- Get Pending Email Statuses → Get Email from Apollo (`main`, output 0, input 0)
- Generate Leads with Apollo.io → Split Out (`main`, output 0, input 0)
- get_failed_posts_summary_rows1 → update_to_unscraped (`main`, output 0, input 0)
- get_failed_profile_summary_rows → update_to_pending1 (`main`, output 0, input 0)
- Get Completely Enriched Profiles → Append to Enriched Leads Database (`main`, output 0, input 0)
- Get Pending About and Posts Rows → Get About Profile (`main`, output 0, input 0)
- Get Pending About and Posts Rows1 → Get Profile Posts (`main`, output 0, input 0)
- Get Pending About and Posts Rows2 → Get About Profile2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1146_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1146_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
