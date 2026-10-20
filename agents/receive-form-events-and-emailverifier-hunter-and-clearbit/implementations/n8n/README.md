# receive form events and emailverifier hunter and clearbit

This folder contains the **receive form events and emailverifier hunter and clearbit** workflow. Its executable nodes use `clearbit`, `formTrigger`, `hunter`, `if`, `noOp`, `pipedrive`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-form-events-and-emailverifier-hunter-and-clearbit.json`](receive-form-events-and-emailverifier-hunter-and-clearbit.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clearbitApi`, `hunterApi`, `pipedriveApi`

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Check if the email is valid | `if` | Inspect parameters |
| Email is not valid, do nothing | `noOp` | Inspect parameters |
| Verify email with Hunter | `hunter` | emailVerifier |
| Clearbit | `clearbit` | person |
| Person already exists in Pipedrive, do nothing | `noOp` | Inspect parameters |
| Is this a new person? | `if` | Inspect parameters |
| Search for person in Pipedrive | `pipedrive` | person / search |
| Is this a new organization? | `if` | Inspect parameters |
| Create Organization | `pipedrive` | organization |
| Search for organization in Pipedrive | `pipedrive` | organization / search |
| Create Person | `pipedrive` | person |
| Create lead | `pipedrive` | lead |

## Connection map

- Clearbit → Search for organization in Pipedrive (`main`, output 0, input 0)
- Create Person → Create lead (`main`, output 0, input 0)
- n8n Form Trigger → Verify email with Hunter (`main`, output 0, input 0)
- Create Organization → Create Person (`main`, output 0, input 0)
- Is this a new person? → Clearbit (`main`, output 0, input 0)
- Is this a new person? → Person already exists in Pipedrive, do nothing (`main`, output 1, input 0)
- Verify email with Hunter → Check if the email is valid (`main`, output 0, input 0)
- Check if the email is valid → Search for person in Pipedrive (`main`, output 0, input 0)
- Check if the email is valid → Email is not valid, do nothing (`main`, output 1, input 0)
- Is this a new organization? → Create Organization (`main`, output 0, input 0)
- Is this a new organization? → Create Person (`main`, output 1, input 0)
- Search for person in Pipedrive → Is this a new person? (`main`, output 0, input 0)
- Search for organization in Pipedrive → Is this a new organization? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hunter/0436_Hunter_Pipedrive_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hunter/0436_Hunter_Pipedrive_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
