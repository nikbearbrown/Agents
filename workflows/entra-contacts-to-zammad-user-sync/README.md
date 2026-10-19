# Entra Contacts to Zammad User Sync

This folder contains the **Entra Contacts to Zammad User Sync** workflow. Its executable nodes use `compareDatasets`, `httpRequest`, `if`, `manualTrigger`, `merge`, `set`, `splitOut`, `zammad`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`entra-contacts-to-zammad-user-sync.json`](entra-contacts-to-zammad-user-sync.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftGraphSecurityOAuth2Api`, `microsoftOAuth2Api`, `zammadTokenAuthApi`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Zammad Univeral User Object | `set` | Inspect parameters |
| Get Zammad Users | `zammad` | getAll |
| Merge | `merge` | Inspect parameters |
| Find new Zammad Users | `compareDatasets` | Inspect parameters |
| Update Zammad User | `zammad` | update |
| Create Zammad User | `zammad` | Inspect parameters |
| Deactivate Zammad User | `zammad` | update |
| Find removed Users | `compareDatasets` | Inspect parameters |
| Get Contacts from Entra | `httpRequest` | Inspect parameters |
| Entra Contacts | `splitOut` | Inspect parameters |
| Filter contacts if needed | `if` | Inspect parameters |
| Filter if needed | `if` | Inspect parameters |

## Connection map

- Merge → Update Zammad User (`main`, output 0, input 0)
- Entra Contacts → Filter contacts if needed (`main`, output 0, input 0)
- Filter if needed → Merge (`main`, output 0, input 0)
- Filter if needed → Find new Zammad Users (`main`, output 0, input 0)
- Filter if needed → Find removed Users (`main`, output 0, input 0)
- Get Zammad Users → Filter if needed (`main`, output 0, input 0)
- Find removed Users → Deactivate Zammad User (`main`, output 0, input 0)
- Find new Zammad Users → Create Zammad User (`main`, output 3, input 0)
- Get Contacts from Entra → Entra Contacts (`main`, output 0, input 0)
- Filter contacts if needed → Zammad Univeral User Object (`main`, output 0, input 0)
- Zammad Univeral User Object → Merge (`main`, output 0, input 1)
- Zammad Univeral User Object → Find new Zammad Users (`main`, output 0, input 1)
- Zammad Univeral User Object → Find removed Users (`main`, output 0, input 1)
- When clicking ‘Test workflow’ → Get Zammad Users (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Contacts from Entra (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1889_Splitout_Comparedatasets_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1889_Splitout_Comparedatasets_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
