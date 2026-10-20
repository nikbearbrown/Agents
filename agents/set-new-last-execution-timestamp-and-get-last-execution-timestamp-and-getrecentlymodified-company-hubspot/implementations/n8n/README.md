# set new last execution timestamp and get last execution timestamp and getrecentlymodified company hubspot

This folder contains the **set new last execution timestamp and get last execution timestamp and getrecentlymodified company hubspot** workflow. Its executable nodes use `cron`, `functionItem`, `hubspot`, `if`, `merge`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`set-new-last-execution-timestamp-and-get-last-execution-timestamp-and-getrecentlymodified-company-hubspot.json`](set-new-last-execution-timestamp-and-get-last-execution-timestamp-and-getrecentlymodified-company-hubspot.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotAppToken`, `zendeskApi`

**Entry nodes:** Every 5 minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Add Zendesk company data to Hubspot data | `merge` | Inspect parameters |
| Set new last execution timestamp | `functionItem` | Inspect parameters |
| Get last execution timestamp | `functionItem` | Inspect parameters |
| Get modified companies | `hubspot` | company / getRecentlyModified |
| Get all Zendesk organisations | `zendesk` | organization / getAll |
| Company exists in Zendesk | `if` | Inspect parameters |
| Create organisation | `zendesk` | organization |
| Update organisation | `zendesk` | organization / update |
| Every 5 minutes | `cron` | Inspect parameters |

## Connection map

- Every 5 minutes → Get last execution timestamp (`main`, output 0, input 0)
- Create organisation → Set new last execution timestamp (`main`, output 0, input 0)
- Update organisation → Set new last execution timestamp (`main`, output 0, input 0)
- Get modified companies → Get all Zendesk organisations (`main`, output 0, input 0)
- Get modified companies → Add Zendesk company data to Hubspot data (`main`, output 0, input 0)
- Company exists in Zendesk → Update organisation (`main`, output 0, input 0)
- Company exists in Zendesk → Create organisation (`main`, output 1, input 0)
- Get last execution timestamp → Get modified companies (`main`, output 0, input 0)
- Get all Zendesk organisations → Add Zendesk company data to Hubspot data (`main`, output 0, input 1)
- Add Zendesk company data to Hubspot data → Company exists in Zendesk (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Zendesk/0285_Zendesk_HubSpot_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Zendesk/0285_Zendesk_HubSpot_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
