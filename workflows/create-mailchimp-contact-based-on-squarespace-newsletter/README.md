# Create Mailchimp contact based on Squarespace newsletter

This folder contains the **Create Mailchimp contact based on Squarespace newsletter** workflow. Its executable nodes use `googleSheets`, `mailchimp`, `manualTrigger`, `scheduleTrigger`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-mailchimp-contact-based-on-squarespace-newsletter.json`](create-mailchimp-contact-based-on-squarespace-newsletter.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `mailchimpApi`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Squarespace newsletter submissions | `googleSheets` | Inspect parameters |
| Loop Over each item | `splitInBatches` | Inspect parameters |
| Add new member to Mailchimp | `mailchimp` | Inspect parameters |

## Connection map

- Schedule Trigger → Squarespace newsletter submissions (`main`, output 0, input 0)
- Loop Over each item → Add new member to Mailchimp (`main`, output 1, input 0)
- Add new member to Mailchimp → Loop Over each item (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Squarespace newsletter submissions (`main`, output 0, input 0)
- Squarespace newsletter submissions → Loop Over each item (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0795_Schedule_Mailchimp_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0795_Schedule_Mailchimp_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
