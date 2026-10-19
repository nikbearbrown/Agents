# DSP Certificate w/ Google Forms

This folder contains the **DSP Certificate w/ Google Forms** workflow. Its executable nodes use `gmail`, `googleDrive`, `googleSheetsTrigger`, `googleSlides`, `if`, `noOp`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`dsp-certificate-w-google-forms.json`](dsp-certificate-w-google-forms.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleDriveOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `googleSlidesOAuth2Api`

**Entry nodes:** Google Sheets Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Google Sheets Trigger | `googleSheetsTrigger` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Extract essential data | `set` | Inspect parameters |
| Score Checker | `if` | Inspect parameters |
| Copy from your template | `googleDrive` | copy |
| Replace text | `googleSlides` | replaceText |
| Convert to PDF | `googleDrive` | download |
| Send to user's email | `gmail` | Inspect parameters |

## Connection map

- Replace text → Convert to PDF (`main`, output 0, input 0)
- Score Checker → Copy from your template (`main`, output 0, input 0)
- Score Checker → No Operation, do nothing (`main`, output 1, input 0)
- Convert to PDF → Send to user's email (`main`, output 0, input 0)
- Google Sheets Trigger → Extract essential data (`main`, output 0, input 0)
- Extract essential data → Score Checker (`main`, output 0, input 0)
- Copy from your template → Replace text (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/0754_Googleslides_Noop_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Googleslides/0754_Googleslides_Noop_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
