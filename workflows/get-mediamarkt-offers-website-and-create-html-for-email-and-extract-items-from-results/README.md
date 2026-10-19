# get mediamarkt offers website and create html for email and extract items from results

This folder contains the **get mediamarkt offers website and create html for email and extract items from results** workflow. Its executable nodes use `brightData`, `documentGenerator`, `emailSend`, `form`, `formTrigger`, `html`, `openAi`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-mediamarkt-offers-website-and-create-html-for-email-and-extract-items-from-results.json`](get-mediamarkt-offers-website-and-create-html-for-email-and-extract-items-from-results.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `brightdataApi`, `openAiApi`, `smtp`

**Entry nodes:** When User Completes Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get MediaMarkt Offers Website | `brightData` | Inspect parameters |
| Create HTML for Email | `documentGenerator` | Inspect parameters |
| Extract items from results | `splitOut` | Inspect parameters |
| Notify End User by Email | `emailSend` | Inspect parameters |
| Show Form Results Page | `form` | completion |
| Extract Body and Title from Website | `html` | extractHtmlContent |
| Generate List of Deals by Category | `openAi` | Inspect parameters |
| When User Completes Form | `formTrigger` | Inspect parameters |

## Connection map

- Create HTML for Email → Notify End User by Email (`main`, output 0, input 0)
- Notify End User by Email → Show Form Results Page (`main`, output 0, input 0)
- When User Completes Form → Get MediaMarkt Offers Website (`main`, output 0, input 0)
- Extract items from results → Create HTML for Email (`main`, output 0, input 0)
- Get MediaMarkt Offers Website → Extract Body and Title from Website (`main`, output 0, input 0)
- Generate List of Deals by Category → Extract items from results (`main`, output 0, input 0)
- Extract Body and Title from Website → Generate List of Deals by Category (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0805_Form_Html_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0805_Form_Html_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
