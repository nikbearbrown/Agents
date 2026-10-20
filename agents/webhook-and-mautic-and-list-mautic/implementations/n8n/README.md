# webhook and mautic and list mautic

This folder contains the **webhook and mautic and list mautic** workflow. Its executable nodes use `function`, `if`, `mautic`, `merge`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-mautic-and-list-mautic.json`](webhook-and-mautic-and-list-mautic.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mauticOAuth2Api`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Mautic | `mautic` | Inspect parameters |
| Find User | `mautic` | getAll |
| Update User | `mautic` | update |
| Tag User | `mautic` | update |
| Unsubscribe User | `mautic` | update |
| Split Full Name | `function` | Inspect parameters |
| If not found return -1 | `function` | Inspect parameters |
| @MAIN STUDENT DATA | `merge` | Inspect parameters |
| Remove unsubscribe | `mautic` | update |
| Find User To Tag Sale | `mautic` | getAll |
| Set userFound | `set` | Inspect parameters |
| Switch Webhook Types | `switch` | Inspect parameters |
| Set Webhook Request | `set` | Inspect parameters |
| IF NOT userFound | `if` | Inspect parameters |
| Switch User.type | `switch` | Inspect parameters |
| IF unsubscribe_from_marketing_emails | `if` | Inspect parameters |

## Connection map

- Webhook → Set Webhook Request (`main`, output 0, input 0)
- Find User → If not found return -1 (`main`, output 0, input 0)
- Update User → IF unsubscribe_from_marketing_emails (`main`, output 0, input 0)
- Set userFound → @MAIN STUDENT DATA (`main`, output 0, input 0)
- Split Full Name → @MAIN STUDENT DATA (`main`, output 0, input 1)
- IF NOT userFound → Mautic (`main`, output 0, input 0)
- IF NOT userFound → Switch User.type (`main`, output 1, input 0)
- Switch User.type → Update User (`main`, output 0, input 0)
- Switch User.type → Unsubscribe User (`main`, output 1, input 0)
- Switch User.type → Remove unsubscribe (`main`, output 2, input 0)
- @MAIN STUDENT DATA → IF NOT userFound (`main`, output 0, input 0)
- Set Webhook Request → Switch Webhook Types (`main`, output 0, input 0)
- Switch Webhook Types → Find User (`main`, output 0, input 0)
- Switch Webhook Types → Split Full Name (`main`, output 0, input 0)
- Switch Webhook Types → Find User To Tag Sale (`main`, output 1, input 0)
- Find User To Tag Sale → Tag User (`main`, output 0, input 0)
- If not found return -1 → Set userFound (`main`, output 0, input 0)
- IF unsubscribe_from_marketing_emails → Unsubscribe User (`main`, output 0, input 0)
- IF unsubscribe_from_marketing_emails → Remove unsubscribe (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/0963_Mautic_Webhook_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/0963_Mautic_Webhook_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
