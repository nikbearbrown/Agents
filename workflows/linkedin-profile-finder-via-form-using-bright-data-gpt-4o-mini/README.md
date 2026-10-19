# LinkedIn Profile Finder via Form using Bright Data & GPT-4o-mini

This folder contains the **LinkedIn Profile Finder via Form using Bright Data & GPT-4o-mini** workflow. Its executable nodes use `brightData`, `emailSend`, `filter`, `form`, `formTrigger`, `html`, `if`, `limit`, `merge`, `openAi`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`linkedin-profile-finder-via-form-using-bright-data-gpt-4o-mini.json`](linkedin-profile-finder-via-form-using-bright-data-gpt-4o-mini.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `brightdataApi`, `openAiApi`, `smtp`

**Entry nodes:** When User Completes Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Extract Body and Title from Website | `html` | extractHtmlContent |
| When User Completes Form | `formTrigger` | Inspect parameters |
| Get LinkedIn Entry on Google | `brightData` | Inspect parameters |
| Parse Google Results | `openAi` | Inspect parameters |
| Form Not Found | `form` | completion |
| Get only Matching Profiles | `filter` | Inspect parameters |
| Limit to 1 Profile | `limit` | Inspect parameters |
| Extract Parsed Results | `splitOut` | Inspect parameters |
| LinkedIn Profile is Found? | `if` | Inspect parameters |
| Edit Url LinkedIn | `set` | Inspect parameters |
| Edit Company Search | `set` | Inspect parameters |
| Extract Body and Title from Website1 | `html` | extractHtmlContent |
| Get Company on Google | `brightData` | Inspect parameters |
| Parse Google Results for Company | `openAi` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Create a Followup for Company and Person | `openAi` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| Form Email Sent | `form` | completion |

## Connection map

- Merge → Create a Followup for Company and Person (`main`, output 0, input 0)
- Split Out → Merge (`main`, output 0, input 1)
- Send Email → Form Email Sent (`main`, output 0, input 0)
- Edit Url LinkedIn → Get LinkedIn Entry on Google (`main`, output 0, input 0)
- Limit to 1 Profile → LinkedIn Profile is Found? (`main`, output 0, input 0)
- Edit Company Search → Get Company on Google (`main`, output 0, input 0)
- Parse Google Results → Extract Parsed Results (`main`, output 0, input 0)
- Get Company on Google → Extract Body and Title from Website1 (`main`, output 0, input 0)
- Extract Parsed Results → Get only Matching Profiles (`main`, output 0, input 0)
- When User Completes Form → Edit Url LinkedIn (`main`, output 0, input 0)
- When User Completes Form → Edit Company Search (`main`, output 0, input 0)
- Get only Matching Profiles → Limit to 1 Profile (`main`, output 0, input 0)
- LinkedIn Profile is Found? → Merge (`main`, output 0, input 0)
- LinkedIn Profile is Found? → Form Not Found (`main`, output 1, input 0)
- Get LinkedIn Entry on Google → Extract Body and Title from Website (`main`, output 0, input 0)
- Parse Google Results for Company → Split Out (`main`, output 0, input 0)
- Extract Body and Title from Website → Parse Google Results (`main`, output 0, input 0)
- Extract Body and Title from Website1 → Parse Google Results for Company (`main`, output 0, input 0)
- Create a Followup for Company and Person → Send Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1937_Splitout_Limit_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1937_Splitout_Limit_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
