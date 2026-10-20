# Search for all contacts that last contact date for is known

This folder contains the **Search for all contacts that last contact date for is known** workflow. Its executable nodes use `gmail`, `httpRequest`, `hubspot`, `if`, `scheduleTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-for-all-contacts-that-last-contact-date-for-is-known.json`](search-for-all-contacts-that-last-contact-date-for-is-known.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `hubspotOAuth2Api`

**Entry nodes:** Every day at 9 am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Every day at 9 am | `scheduleTrigger` | Inspect parameters |
| Send outreach email | `gmail` | Inspect parameters |
| Record engagement in HubSpot | `hubspot` | engagement |
| Get previously HubSpot contacts | `hubspot` | search |
| if last contacted before a month | `if` | Inspect parameters |
| Get Hubspot Contact to engagement | `httpRequest` | Inspect parameters |
| if there has been only one engagement | `if` | Inspect parameters |
| Set email keys | `set` | Inspect parameters |

## Connection map

- Set email keys → Record engagement in HubSpot (`main`, output 0, input 0)
- Set email keys → Send outreach email (`main`, output 0, input 0)
- Every day at 9 am → Get previously HubSpot contacts (`main`, output 0, input 0)
- Get previously HubSpot contacts → if last contacted before a month (`main`, output 0, input 0)
- if last contacted before a month → Get Hubspot Contact to engagement (`main`, output 0, input 0)
- Get Hubspot Contact to engagement → if there has been only one engagement (`main`, output 0, input 0)
- if there has been only one engagement → Set email keys (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0422_Schedule_HTTP_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0422_Schedule_HTTP_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
