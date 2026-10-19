# Adding to GSheet-List, Creating a OTP / Verification Code

This folder contains the **Adding to GSheet-List, Creating a OTP / Verification Code** workflow. Its executable nodes use `crypto`, `emailSend`, `form`, `formTrigger`, `googleSheets`, `if`, `merge`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`adding-to-gsheet-list-creating-a-otp-verification-code.json`](adding-to-gsheet-list-creating-a-otp-verification-code.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `smtp`

**Entry nodes:** Waitlist Form

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Add  to Waitlist Sheet | `googleSheets` | appendOrUpdate |
| Clean and Standardize | `set` | Inspect parameters |
| Send Verification Email | `emailSend` | Inspect parameters |
| Validate with Verification Code | `form` | Inspect parameters |
| Get all Data from the Prev Form + Current | `set` | Inspect parameters |
| Additional Data for the Sheet | `form` | Inspect parameters |
| Every Step Data | `set` | Inspect parameters |
| is the Code correct? | `if` | Inspect parameters |
| Let the User Reenter Code | `form` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Save Intend to List | `googleSheets` | appendOrUpdate |
| Save as Verified | `googleSheets` | appendOrUpdate |
| Generate Random Verification Code | `crypto` | Inspect parameters |
| Waitlist Form | `formTrigger` | Inspect parameters |

## Connection map

- Merge → Send Verification Email (`main`, output 0, input 0)
- Waitlist Form → Clean and Standardize (`main`, output 0, input 0)
- Every Step Data → Save Intend to List (`main`, output 0, input 0)
- Save as Verified → Additional Data for the Sheet (`main`, output 0, input 0)
- is the Code correct? → Save as Verified (`main`, output 0, input 0)
- is the Code correct? → Let the User Reenter Code (`main`, output 1, input 0)
- Clean and Standardize → Generate Random Verification Code (`main`, output 0, input 0)
- Add  to Waitlist Sheet → Merge (`main`, output 0, input 0)
- Send Verification Email → Validate with Verification Code (`main`, output 0, input 0)
- Let the User Reenter Code → Get all Data from the Prev Form + Current (`main`, output 0, input 0)
- Additional Data for the Sheet → Every Step Data (`main`, output 0, input 0)
- Validate with Verification Code → Get all Data from the Prev Form + Current (`main`, output 0, input 0)
- Generate Random Verification Code → Add  to Waitlist Sheet (`main`, output 0, input 0)
- Generate Random Verification Code → Merge (`main`, output 0, input 1)
- Get all Data from the Prev Form + Current → is the Code correct? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0633_Form_GoogleSheets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Form/0633_Form_GoogleSheets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
