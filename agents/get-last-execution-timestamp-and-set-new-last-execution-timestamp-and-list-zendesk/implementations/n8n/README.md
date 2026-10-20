# get last execution timestamp and set new last execution timestamp and list zendesk

This folder contains the **get last execution timestamp and set new last execution timestamp and list zendesk** workflow. Its executable nodes use `cron`, `functionItem`, `httpRequest`, `if`, `merge`, `pipedrive`, `set`, `zendesk`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-last-execution-timestamp-and-set-new-last-execution-timestamp-and-list-zendesk.json`](get-last-execution-timestamp-and-set-new-last-execution-timestamp-and-list-zendesk.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `pipedriveApi`, `zendeskApi`

**Entry nodes:** Every 5 minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get last execution timestamp | `functionItem` | Inspect parameters |
| Set new last execution timestamp | `functionItem` | Inspect parameters |
| Get tickets created after last execution | `zendesk` | getAll |
| Get requester information | `zendesk` | user / get |
| Keep only needed requester information | `set` | Inspect parameters |
| Keep only requester owner email | `set` | Inspect parameters |
| Every 5 minutes | `cron` | Inspect parameters |
| Add requester information to ticket data | `merge` | Inspect parameters |
| Search requester in pipedrive | `pipedrive` | person / search |
| Get owner information of Pipedrive contact | `httpRequest` | Inspect parameters |
| Get agents and admins | `zendesk` | user / getAll |
| Keep only email and Id | `set` | Inspect parameters |
| Add Pipedrive agent data to pipedrive contact information | `merge` | Inspect parameters |
| Add contact owner to ticket data | `merge` | Inspect parameters |
| Contact exists in Pipedrive | `if` | Inspect parameters |
| Change assignee to Pipedrive contact owner | `zendesk` | update |
| Add a note requester not found | `zendesk` | update |

## Connection map

- Every 5 minutes → Get last execution timestamp (`main`, output 0, input 0)
- Get agents and admins → Keep only email and Id (`main`, output 0, input 0)
- Keep only email and Id → Add Pipedrive agent data to pipedrive contact information (`main`, output 0, input 1)
- Get requester information → Keep only needed requester information (`main`, output 0, input 0)
- Contact exists in Pipedrive → Change assignee to Pipedrive contact owner (`main`, output 0, input 0)
- Contact exists in Pipedrive → Add a note requester not found (`main`, output 1, input 0)
- Get last execution timestamp → Get tickets created after last execution (`main`, output 0, input 0)
- Search requester in pipedrive → Get owner information of Pipedrive contact (`main`, output 0, input 0)
- Add a note requester not found → Set new last execution timestamp (`main`, output 0, input 0)
- Keep only requester owner email → Add Pipedrive agent data to pipedrive contact information (`main`, output 0, input 0)
- Add contact owner to ticket data → Contact exists in Pipedrive (`main`, output 0, input 0)
- Keep only needed requester information → Add requester information to ticket data (`main`, output 0, input 1)
- Add requester information to ticket data → Search requester in pipedrive (`main`, output 0, input 0)
- Add requester information to ticket data → Add contact owner to ticket data (`main`, output 0, input 0)
- Get tickets created after last execution → Add requester information to ticket data (`main`, output 0, input 0)
- Get tickets created after last execution → Get requester information (`main`, output 0, input 0)
- Change assignee to Pipedrive contact owner → Set new last execution timestamp (`main`, output 0, input 0)
- Get owner information of Pipedrive contact → Keep only requester owner email (`main`, output 0, input 0)
- Add Pipedrive agent data to pipedrive contact information → Add contact owner to ticket data (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0266_Functionitem_Zendesk_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0266_Functionitem_Zendesk_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
