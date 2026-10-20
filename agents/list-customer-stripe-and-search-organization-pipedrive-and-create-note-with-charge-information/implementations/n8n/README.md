# list customer stripe and search organization pipedrive and create note with charge information

This folder contains the **list customer stripe and search organization pipedrive and create note with charge information** workflow. Its executable nodes use `cron`, `functionItem`, `httpRequest`, `itemLists`, `merge`, `pipedrive`, `set`, `stripe`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`list-customer-stripe-and-search-organization-pipedrive-and-create-note-with-charge-information.json`](list-customer-stripe-and-search-organization-pipedrive-and-create-note-with-charge-information.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `pipedriveApi`, `stripeApi`

**Entry nodes:** Every day at 8 am

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get customers | `stripe` | customer / getAll |
| Rename fields and keep only needed fields | `set` | Inspect parameters |
| Add customer name to charge data | `merge` | Inspect parameters |
| Search organisation | `pipedrive` | organization / search |
| Add organisation Information to charge data | `merge` | Inspect parameters |
| Create note with charge information | `pipedrive` | note |
| Get last execution timestamp | `functionItem` | Inspect parameters |
| Set new last execution timestamp | `functionItem` | Inspect parameters |
| Split array of charges to items | `itemLists` | Inspect parameters |
| Search for charges in Stripe | `httpRequest` | Inspect parameters |
| Every day at 8 am | `cron` | Inspect parameters |

## Connection map

- Get customers → Rename fields and keep only needed fields (`main`, output 0, input 0)
- Every day at 8 am → Get last execution timestamp (`main`, output 0, input 0)
- Search organisation → Add organisation Information to charge data (`main`, output 0, input 1)
- Get last execution timestamp → Search for charges in Stripe (`main`, output 0, input 0)
- Search for charges in Stripe → Split array of charges to items (`main`, output 0, input 0)
- Split array of charges to items → Add customer name to charge data (`main`, output 0, input 0)
- Add customer name to charge data → Search organisation (`main`, output 0, input 0)
- Add customer name to charge data → Add organisation Information to charge data (`main`, output 0, input 0)
- Create note with charge information → Set new last execution timestamp (`main`, output 0, input 0)
- Rename fields and keep only needed fields → Add customer name to charge data (`main`, output 0, input 1)
- Add organisation Information to charge data → Create note with charge information (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0246_Functionitem_Pipedrive_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Functionitem/0246_Functionitem_Pipedrive_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
