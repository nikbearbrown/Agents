# lemlist add lead to campaign and hubspot follow up task and lonescale new job intent

This folder contains the **lemlist add lead to campaign and hubspot follow up task and lonescale new job intent** workflow. Its executable nodes use `dropcontact`, `hubspot`, `if`, `lemlist`, `slack`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`lemlist-add-lead-to-campaign-and-hubspot-follow-up-task-and-lonescale-new-job-intent.json`](lemlist-add-lead-to-campaign-and-hubspot-follow-up-task-and-lonescale-new-job-intent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `dropcontactApi`, `hubspotOAuth2Api`, `lemlistApi`, `slackOAuth2Api`

**Entry nodes:** Lonescale - New  Job Intent

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Lemlist - Add lead to campaign | `lemlist` | lead |
| HubSpot - Follow up task | `hubspot` | engagement |
| Attempted to contact? | `if` | Inspect parameters |
| Lonescale - New  Job Intent | `webhook` | Inspect parameters |
| Dropcontact | `dropcontact` | Inspect parameters |
| HubSpot - Search company | `hubspot` | company / searchByDomain |
| New Company? | `if` | Inspect parameters |
| Is Customer? | `if` | Inspect parameters |
| Slack - Notify CS team on Slack1 | `slack` | Inspect parameters |
| HubSpot Update Account | `hubspot` | company / update |
| HubSpot | `hubspot` | contact / search |
| HubSpot Create Account | `hubspot` | company |
| Is Account in Hubspot | `if` | Inspect parameters |
| HubSpot - Create/Update Contact | `hubspot` | contact |
| Slack - Notify sales team on Slack | `slack` | Inspect parameters |
| Open Deal? | `if` | Inspect parameters |
| email found | `if` | Inspect parameters |
| HubSpot - Linkedin Outreach | `hubspot` | engagement |

## Connection map

- HubSpot → HubSpot - Create/Update Contact (`main`, output 0, input 0)
- Open Deal? → Slack - Notify sales team on Slack (`main`, output 0, input 0)
- Dropcontact → HubSpot - Search company (`main`, output 0, input 0)
- email found → Lemlist - Add lead to campaign (`main`, output 0, input 0)
- email found → HubSpot - Linkedin Outreach (`main`, output 1, input 0)
- Is Customer? → Slack - Notify CS team on Slack1 (`main`, output 0, input 0)
- New Company? → email found (`main`, output 0, input 0)
- Attempted to contact? → HubSpot - Follow up task (`main`, output 0, input 0)
- Is Account in Hubspot → HubSpot Update Account (`main`, output 0, input 0)
- Is Account in Hubspot → HubSpot Create Account (`main`, output 1, input 0)
- HubSpot Create Account → HubSpot (`main`, output 0, input 0)
- HubSpot Update Account → HubSpot (`main`, output 0, input 0)
- HubSpot - Search company → Is Account in Hubspot (`main`, output 0, input 0)
- Lonescale - New  Job Intent → Dropcontact (`main`, output 0, input 0)
- HubSpot - Create/Update Contact → New Company? (`main`, output 0, input 0)
- HubSpot - Create/Update Contact → Is Customer? (`main`, output 0, input 0)
- HubSpot - Create/Update Contact → Attempted to contact? (`main`, output 0, input 0)
- HubSpot - Create/Update Contact → Open Deal? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0295_Webhook_Dropcontact_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0295_Webhook_Dropcontact_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
