# delete google sheets and append google sheets and google sheets

This folder contains the **delete google sheets and append google sheets and google sheets** workflow. Its executable nodes use `discord`, `filter`, `googleSheets`, `if`, `manualTrigger`, `merge`, `noOp`, `respondToWebhook`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`delete-google-sheets-and-append-google-sheets-and-google-sheets.json`](delete-google-sheets-and-append-google-sheets-and-google-sheets.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordBotApi`, `googleSheetsOAuth2Api`

**Entry nodes:** When clicking "Test workflow", Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Delete ID | `googleSheets` | delete |
| SaveID | `googleSheets` | append |
| Get ID | `googleSheets` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Check if we have more members left | `if` | Inspect parameters |
| We're done | `noOp` | Inspect parameters |
| Check if we have an ID | `if` | Inspect parameters |
| Filter to only include members with role | `filter` | Inspect parameters |
| Get First 100 Members | `discord` | member |
| Get next 100 Members after last ID | `discord` | member |
| Setup: Edit this to get started | `set` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Send Response | `respondToWebhook` | Inspect parameters |

## Connection map

- Merge → Check if we have more members left (`main`, output 0, input 0)
- Merge → Filter to only include members with role (`main`, output 0, input 0)
- Get ID → Check if we have an ID (`main`, output 0, input 0)
- SaveID → Get ID (`main`, output 0, input 0)
- Webhook → Setup: Edit this to get started (`main`, output 0, input 0)
- Delete ID → SaveID (`main`, output 0, input 0)
- Get First 100 Members → Merge (`main`, output 0, input 1)
- Check if we have an ID → Get next 100 Members after last ID (`main`, output 0, input 0)
- Check if we have an ID → Get First 100 Members (`main`, output 1, input 0)
- When clicking "Test workflow" → Setup: Edit this to get started (`main`, output 0, input 0)
- Setup: Edit this to get started → Get ID (`main`, output 0, input 0)
- Check if we have more members left → We're done (`main`, output 0, input 0)
- Check if we have more members left → Delete ID (`main`, output 1, input 0)
- Get next 100 Members after last ID → Merge (`main`, output 0, input 0)
- Filter to only include members with role → Send Response (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0410_Webhook_Filter_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0410_Webhook_Filter_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
