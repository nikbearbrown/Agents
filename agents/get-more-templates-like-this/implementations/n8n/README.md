# Get More Templates Like This 👇

This folder contains the **Get More Templates Like This 👇** workflow. Its executable nodes use `airtable`, `code`, `googleSheets`, `html`, `httpRequest`, `manualTrigger`, `merge`, `nocoDb`, `openAi`, `scheduleTrigger`, `set`, `slack`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-more-templates-like-this.json`](get-more-templates-like-this.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableOAuth2Api`, `googleSheetsOAuth2Api`, `nocoDbApiToken`, `openAiApi`, `slackOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger Every Monday, @ 08:00am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get advice articles from a Google search | `httpRequest` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Merge data and keep unique google search results | `merge` | Inspect parameters |
| Extract Article links for LinkedIn advice articles | `code` | Inspect parameters |
| Split Out all links for LinkedIn advice articles | `splitOut` | Inspect parameters |
| Schedule Trigger Every Monday, @ 08:00am | `scheduleTrigger` | Inspect parameters |
| LinkedIn Contribution Writer | `openAi` | Inspect parameters |
| Post new LinkedIn contributions to NocoDB (CreateRows) | `nocoDb` | create |
| Post new LinkedIn contributions to Slack channel | `slack` | Inspect parameters |
| Get all LinkedIn contributions from database NocoDB (GetRows) | `nocoDb` | getAll |
| HTML extract LinkedIn article & other users contributions | `html` | extractHtmlContent |
| HTTP Request to get LinkedIn advice articles | `httpRequest` | Inspect parameters |
| Airtable | `airtable` | base |
| Google Sheets | `googleSheets` | Inspect parameters |
| Get all LinkedIn contributions from database NocoDB (GetRows)1 | `nocoDb` | getAll |
| Set Topic for Google search | `set` | Inspect parameters |

## Connection map

- Set Topic for Google search → Get advice articles from a Google search (`main`, output 0, input 0)
- LinkedIn Contribution Writer → Post new LinkedIn contributions to Slack channel (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get all LinkedIn contributions from database NocoDB (GetRows) (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set Topic for Google search (`main`, output 0, input 0)
- Get advice articles from a Google search → Extract Article links for LinkedIn advice articles (`main`, output 0, input 0)
- Schedule Trigger Every Monday, @ 08:00am → Get all LinkedIn contributions from database NocoDB (GetRows) (`main`, output 0, input 0)
- Schedule Trigger Every Monday, @ 08:00am → Set Topic for Google search (`main`, output 0, input 0)
- HTTP Request to get LinkedIn advice articles → HTML extract LinkedIn article & other users contributions (`main`, output 0, input 0)
- Merge data and keep unique google search results → HTTP Request to get LinkedIn advice articles (`main`, output 0, input 0)
- Post new LinkedIn contributions to Slack channel → Post new LinkedIn contributions to NocoDB (CreateRows) (`main`, output 0, input 0)
- Split Out all links for LinkedIn advice articles → Merge data and keep unique google search results (`main`, output 0, input 1)
- Extract Article links for LinkedIn advice articles → Split Out all links for LinkedIn advice articles (`main`, output 0, input 0)
- HTML extract LinkedIn article & other users contributions → LinkedIn Contribution Writer (`main`, output 0, input 0)
- Get all LinkedIn contributions from database NocoDB (GetRows) → Merge data and keep unique google search results (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0613_Splitout_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0613_Splitout_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
