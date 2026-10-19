# reach out via email to new form submissions that meet a certain criteria

This folder contains the **reach out via email to new form submissions that meet a certain criteria** workflow. Its executable nodes use `clearbit`, `formTrigger`, `hubspot`, `hunter`, `if`, `noOp`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`reach-out-via-email-to-new-form-submissions-that-meet-a-certain-criteria.json`](reach-out-via-email-to-new-form-submissions-that-meet-a-certain-criteria.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `clearbitApi`, `hubspotOAuth2Api`, `hunterApi`

**Entry nodes:** n8n Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| n8n Form Trigger | `formTrigger` | Inspect parameters |
| Hunter | `hunter` | emailVerifier |
| Check if the email is valid | `if` | Inspect parameters |
| Enrich company | `clearbit` | Inspect parameters |
| Add lead to Hubspot | `hubspot` | Inspect parameters |
| Enrich person | `clearbit` | person |
| Email is not valid, do nothing | `noOp` | Inspect parameters |

## Connection map

- Hunter → Check if the email is valid (`main`, output 0, input 0)
- Enrich person → Enrich company (`main`, output 0, input 0)
- Enrich company → Add lead to Hubspot (`main`, output 0, input 0)
- n8n Form Trigger → Hunter (`main`, output 0, input 0)
- Check if the email is valid → Enrich person (`main`, output 0, input 0)
- Check if the email is valid → Email is not valid, do nothing (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hunter/0420_Hunter_Form_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Hunter/0420_Hunter_Form_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
