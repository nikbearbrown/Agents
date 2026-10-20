# Unsubscribe Mautic contacts from automated unsubscribe emails

This folder contains the **Unsubscribe Mautic contacts from automated unsubscribe emails** workflow. Its executable nodes use `code`, `gmail`, `gmailTrigger`, `if`, `mautic`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`unsubscribe-mautic-contacts-from-automated-unsubscribe-emails.json`](unsubscribe-mautic-contacts-from-automated-unsubscribe-emails.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `mauticOAuth2Api`

**Entry nodes:** Gmail Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Gmail Trigger | `gmailTrigger` | Inspect parameters |
| Is automated unsubscribe? | `if` | Inspect parameters |
| Add to unsubscribed segment | `mautic` | contactSegment |
| Remove newsletter segment | `mautic` | contactSegment / remove |
| Reply Unsubscribe Message | `gmail` | reply |
| Add to Do Not Contact List | `mautic` | editDoNotContactList |
| Extract Email from 'From' Field | `code` | Inspect parameters |
| Extract Unique Email Addresses | `code` | Inspect parameters |
| Get Mautic Contact ID from Email Address | `mautic` | getAll |
| If Contact Exists in Mautic | `if` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |

## Connection map

- Edit Fields → Is automated unsubscribe? (`main`, output 0, input 0)
- Gmail Trigger → Edit Fields (`main`, output 0, input 0)
- Is automated unsubscribe? → Extract Email from 'From' Field (`main`, output 0, input 0)
- If Contact Exists in Mautic → Add to unsubscribed segment (`main`, output 0, input 0)
- If Contact Exists in Mautic → Remove newsletter segment (`main`, output 0, input 0)
- If Contact Exists in Mautic → Reply Unsubscribe Message (`main`, output 0, input 0)
- If Contact Exists in Mautic → Add to Do Not Contact List (`main`, output 0, input 0)
- If Contact Exists in Mautic → Reply Unsubscribe Message (`main`, output 1, input 0)
- Extract Unique Email Addresses → Get Mautic Contact ID from Email Address (`main`, output 0, input 0)
- Extract Email from 'From' Field → Extract Unique Email Addresses (`main`, output 0, input 0)
- Get Mautic Contact ID from Email Address → If Contact Exists in Mautic (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/0490_Mautic_Gmail_Send_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/0490_Mautic_Gmail_Send_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
