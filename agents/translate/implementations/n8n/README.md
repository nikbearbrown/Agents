# Translate

This folder contains the **Translate** workflow. Its executable nodes use `aggregate`, `code`, `convertToFile`, `extractFromFile`, `form`, `formTrigger`, `googleTranslate`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`translate.json`](translate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleTranslateOAuth2Api`

**Entry nodes:** Receive SRT File to Translate

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Google Translate | `googleTranslate` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Split SRT Lines | `code` | Inspect parameters |
| Generate Binary | `code` | Inspect parameters |
| Prep Parts for Translate | `code` | Inspect parameters |
| Clean Translations & Group Titles | `code` | Inspect parameters |
| Join completed text with double new line | `code` | Inspect parameters |
| Respond with file | `form` | completion |
| Receive SRT File to Translate | `formTrigger` | Inspect parameters |
| Extract text from Binary File | `extractFromFile` | text |
| Expose Binary | `code` | Inspect parameters |

## Connection map

- Aggregate → Join completed text with double new line (`main`, output 0, input 0)
- Split Out → Prep Parts for Translate (`main`, output 0, input 0)
- Edit Fields → Generate Binary (`main`, output 0, input 0)
- Expose Binary → Extract text from Binary File (`main`, output 0, input 0)
- Convert to File → Respond with file (`main`, output 0, input 0)
- Generate Binary → Convert to File (`main`, output 0, input 0)
- Split SRT Lines → Split Out (`main`, output 0, input 0)
- Google Translate → Clean Translations & Group Titles (`main`, output 0, input 0)
- Prep Parts for Translate → Google Translate (`main`, output 0, input 0)
- Extract text from Binary File → Split SRT Lines (`main`, output 0, input 0)
- Receive SRT File to Translate → Expose Binary (`main`, output 0, input 0)
- Clean Translations & Group Titles → Aggregate (`main`, output 0, input 0)
- Join completed text with double new line → Edit Fields (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1993_Splitout_Code_Automation_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1993_Splitout_Code_Automation_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
