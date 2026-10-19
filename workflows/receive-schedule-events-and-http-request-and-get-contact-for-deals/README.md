# receive schedule events and http request and get contact for deals

This folder contains the **receive schedule events and http request and get contact for deals** workflow. Its executable nodes use `filter`, `httpRequest`, `hubspot`, `scheduleTrigger`, `splitOut`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-http-request-and-get-contact-for-deals.json`](receive-schedule-events-and-http-request-and-get-contact-for-deals.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `hubspotOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Deals | `httpRequest` | Inspect parameters |
| Get contact for deals | `httpRequest` | Inspect parameters |
| Unassigned Deals | `filter` | Inspect parameters |
| Split out deals | `splitOut` | Inspect parameters |
| Assign by Region | `switch` | Inspect parameters |
| Assign deal to John | `hubspot` | deal / update |
| Assign to Max | `hubspot` | deal / update |
| Assign to Eeden | `hubspot` | deal / update |
| Assign to Peter | `hubspot` | deal / update |
| Get company of contact(s) | `httpRequest` | Inspect parameters |
| Assign US deals by company size | `switch` | Inspect parameters |
| Assign deal to Edward | `hubspot` | deal / update |
| Assign to Michael | `hubspot` | deal / update |
| Assign to Suka | `hubspot` | deal / update |
| Assign DE deals by company size | `switch` | Inspect parameters |

## Connection map

- Get Deals → Split out deals (`main`, output 0, input 0)
- Split out deals → Unassigned Deals (`main`, output 0, input 0)
- Assign by Region → Assign US deals by company size (`main`, output 0, input 0)
- Assign by Region → Assign DE deals by company size (`main`, output 1, input 0)
- Assign by Region → Assign to Peter (`main`, output 2, input 0)
- Schedule Trigger → Get Deals (`main`, output 0, input 0)
- Unassigned Deals → Get contact for deals (`main`, output 0, input 0)
- Get contact for deals → Get company of contact(s) (`main`, output 0, input 0)
- Get company of contact(s) → Assign by Region (`main`, output 0, input 0)
- Assign DE deals by company size → Assign deal to Edward (`main`, output 0, input 0)
- Assign DE deals by company size → Assign to Michael (`main`, output 1, input 0)
- Assign DE deals by company size → Assign to Suka (`main`, output 2, input 0)
- Assign US deals by company size → Assign deal to John (`main`, output 0, input 0)
- Assign US deals by company size → Assign to Max (`main`, output 1, input 0)
- Assign US deals by company size → Assign to Eeden (`main`, output 2, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0421_Splitout_Schedule_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0421_Splitout_Schedule_Import_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
