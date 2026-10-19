# split out and http request and receive form events

This folder contains the **split out and http request and receive form events** workflow. Its executable nodes use `convertToFile`, `extractFromFile`, `form`, `formTrigger`, `gmail`, `html`, `httpRequest`, `if`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`split-out-and-http-request-and-receive-form-events.json`](split-out-and-http-request-and-receive-form-events.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googlePalmApi`, `httpQueryAuth`

**Entry nodes:** On form submission

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Out | `splitOut` | Inspect parameters |
| Imagen 3.0 | `httpRequest` | POST |
| Variables | `set` | Inspect parameters |
| Download Image | `httpRequest` | Inspect parameters |
| On form submission | `formTrigger` | Inspect parameters |
| Form Validation | `if` | Inspect parameters |
| Retry Form | `form` | Inspect parameters |
| Upload to Cloudinary | `httpRequest` | POST |
| Convert to File1 | `convertToFile` | toText |
| Generate HTML | `html` | Inspect parameters |
| Convert to File | `convertToFile` | toBinary |
| Form Ending | `form` | completion |
| Has Email? | `if` | Inspect parameters |
| Send Results to Email | `gmail` | Inspect parameters |
| Image to Base64 | `extractFromFile` | binaryToPropery |
| Gemini 2.0 | `httpRequest` | POST |

## Connection map

- Split Out → Convert to File (`main`, output 0, input 0)
- Variables → Download Image (`main`, output 0, input 0)
- Gemini 2.0 → Imagen 3.0 (`main`, output 0, input 0)
- Has Email? → Send Results to Email (`main`, output 0, input 0)
- Imagen 3.0 → Split Out (`main`, output 0, input 0)
- Retry Form → Form Validation (`main`, output 0, input 0)
- Generate HTML → Convert to File1 (`main`, output 0, input 0)
- Generate HTML → Has Email? (`main`, output 0, input 0)
- Download Image → Image to Base64 (`main`, output 0, input 0)
- Convert to File → Upload to Cloudinary (`main`, output 0, input 0)
- Form Validation → Variables (`main`, output 0, input 0)
- Form Validation → Retry Form (`main`, output 1, input 0)
- Image to Base64 → Gemini 2.0 (`main`, output 0, input 0)
- Convert to File1 → Form Ending (`main`, output 0, input 0)
- On form submission → Form Validation (`main`, output 0, input 0)
- Upload to Cloudinary → Generate HTML (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0919_Splitout_Extractfromfile_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0919_Splitout_Extractfromfile_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
