# Add your company details here!

This folder contains the **Add your company details here!** workflow. Its executable nodes use `airtable`, `gmail`, `html`, `httpRequest`, `informationExtractor`, `lmChatOpenAi`, `merge`, `removeDuplicates`, `scheduleTrigger`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`add-your-company-details-here.json`](add-your-company-details-here.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableTokenApi`, `gmailOAuth2`, `openAiApi`

**Entry nodes:** Everyday @ 9am, Everyday @ 8.30am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Grants to List | `splitOut` | Inspect parameters |
| Get Grant Details | `httpRequest` | POST |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Summarize Synopsis | `informationExtractor` | Inspect parameters |
| Eligibility Factors | `informationExtractor` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Save to Tracker | `airtable` | create |
| Only New Grants | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| AI Grants since Yesterday | `httpRequest` | POST |
| Get New Eligible Grants Today | `airtable` | search |
| Generate Email | `html` | Inspect parameters |
| Everyday @ 9am | `scheduleTrigger` | Inspect parameters |
| Everyday @ 8.30am | `scheduleTrigger` | Inspect parameters |
| Get Subscribers | `airtable` | search |
| Send Subscriber Email | `gmail` | Inspect parameters |

## Connection map

- Merge → Save to Tracker (`main`, output 0, input 0)
- Everyday @ 9am → Get New Eligible Grants Today (`main`, output 0, input 0)
- Generate Email → Get Subscribers (`main`, output 0, input 0)
- Grants to List → Only New Grants (`main`, output 0, input 0)
- Get Subscribers → Send Subscriber Email (`main`, output 0, input 0)
- Only New Grants → Get Grant Details (`main`, output 0, input 0)
- Everyday @ 8.30am → AI Grants since Yesterday (`main`, output 0, input 0)
- Get Grant Details → Summarize Synopsis (`main`, output 0, input 0)
- Get Grant Details → Eligibility Factors (`main`, output 0, input 0)
- OpenAI Chat Model → Summarize Synopsis (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Eligibility Factors (`ai_languageModel`, output 0, input 0)
- Summarize Synopsis → Merge (`main`, output 0, input 0)
- Eligibility Factors → Merge (`main`, output 0, input 1)
- AI Grants since Yesterday → Grants to List (`main`, output 0, input 0)
- Get New Eligible Grants Today → Generate Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0659_Splitout_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0659_Splitout_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
