# Dialpad to Syncro

This folder contains the **Dialpad to Syncro** workflow. Its executable nodes use `function`, `googleSheets`, `httpRequest`, `if`, `noOp`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dialpad-to-syncro.json`](dialpad-to-syncro.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleApi`, `httpHeaderAuth`

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| GetCustomer | `httpRequest` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| CreateTicket | `httpRequest` | Inspect parameters |
| GetTicket | `httpRequest` | Inspect parameters |
| IFMoreThanOne | `if` | Inspect parameters |
| Google Sheets | `googleSheets` | append |
| ForGoogle | `set` | Inspect parameters |
| UpdateTicket | `httpRequest` | Inspect parameters |
| ForGoogle1 | `set` | Inspect parameters |
| Google Sheets1 | `googleSheets` | append |
| NoOp | `noOp` | Inspect parameters |
| Contacts | `function` | Inspect parameters |
| IFContacts | `if` | Inspect parameters |
| Customers | `function` | Inspect parameters |
| IFCustomers | `if` | Inspect parameters |
| NoOp1 | `noOp` | Inspect parameters |
| CreateTicketForCustomer | `httpRequest` | Inspect parameters |
| ForGoogle2 | `set` | Inspect parameters |
| Google Sheets2 | `googleSheets` | append |
| EnvVariables | `set` | Inspect parameters |
| IF | `if` | Inspect parameters |
| NoOp2 | `noOp` | Inspect parameters |

## Connection map

- IF → EnvVariables (`main`, output 0, input 0)
- IF → NoOp2 (`main`, output 1, input 0)
- Webhook → IF (`main`, output 0, input 0)
- Contacts → IFContacts (`main`, output 0, input 0)
- Customers → IFCustomers (`main`, output 0, input 0)
- ForGoogle → Google Sheets (`main`, output 0, input 0)
- GetTicket → IFMoreThanOne (`main`, output 0, input 0)
- ForGoogle1 → Google Sheets1 (`main`, output 0, input 0)
- ForGoogle2 → Google Sheets2 (`main`, output 0, input 0)
- IFContacts → GetTicket (`main`, output 0, input 0)
- IFContacts → NoOp (`main`, output 1, input 0)
- GetCustomer → Contacts (`main`, output 0, input 0)
- GetCustomer → Customers (`main`, output 0, input 0)
- IFCustomers → CreateTicketForCustomer (`main`, output 0, input 0)
- IFCustomers → NoOp1 (`main`, output 1, input 0)
- CreateTicket → ForGoogle1 (`main`, output 0, input 0)
- EnvVariables → GetCustomer (`main`, output 0, input 0)
- UpdateTicket → ForGoogle (`main`, output 0, input 0)
- IFMoreThanOne → UpdateTicket (`main`, output 0, input 0)
- IFMoreThanOne → CreateTicket (`main`, output 1, input 0)
- CreateTicketForCustomer → ForGoogle2 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0347_HTTP_GoogleSheets_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0347_HTTP_GoogleSheets_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
