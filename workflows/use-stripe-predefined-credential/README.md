# Use Stripe Predefined Credential

This folder contains the **Use Stripe Predefined Credential** workflow. Its executable nodes use `awsS3`, `httpRequest`, `if`, `manualTrigger`, `scheduleTrigger`, `set`, `splitOut`, `stopAndError`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`use-stripe-predefined-credential.json`](use-stripe-predefined-credential.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** When clicking ‘Test workflow’, Every Month the First Day of the Month

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| List Invoices | `splitOut` | Inspect parameters |
| Inject s3 Subpath | `set` | Inspect parameters |
| Set-Subpath | `set` | Inspect parameters |
| We do only Invoice Objects | `if` | Inspect parameters |
| It shouldn't be something else | `stopAndError` | Inspect parameters |
| ENV* | `set` | Inspect parameters |
| Download Invoice PDF from Stripe | `httpRequest` | Inspect parameters |
| Every Month the First Day of the Month | `scheduleTrigger` | Inspect parameters |
| Get all Invoices* | `httpRequest` | Inspect parameters |
| Upload to S3 Bucket* | `awsS3` | upload |
| Clean and Escape ENV | `set` | Inspect parameters |

## Connection map

- ENV* → Clean and Escape ENV (`main`, output 0, input 0)
- Set-Subpath → Upload to S3 Bucket* (`main`, output 0, input 0)
- List Invoices → We do only Invoice Objects (`main`, output 0, input 0)
- Get all Invoices* → List Invoices (`main`, output 0, input 0)
- Inject s3 Subpath → Set-Subpath (`main`, output 0, input 0)
- Clean and Escape ENV → Get all Invoices* (`main`, output 0, input 0)
- We do only Invoice Objects → Download Invoice PDF from Stripe (`main`, output 0, input 0)
- We do only Invoice Objects → It shouldn't be something else (`main`, output 1, input 0)
- Download Invoice PDF from Stripe → Inject s3 Subpath (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → ENV* (`main`, output 0, input 0)
- Every Month the First Day of the Month → ENV* (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0592_Stopanderror_Awss3_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/0592_Stopanderror_Awss3_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
