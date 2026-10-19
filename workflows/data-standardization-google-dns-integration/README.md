# Data Standardization & Google DNS Integration

This folder contains the **Data Standardization & Google DNS Integration** workflow. Its executable nodes use `code`, `filter`, `formTrigger`, `gmail`, `httpRequest`, `if`, `itemLists`, `merge`, `set`, `slack`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`data-standardization-google-dns-integration.json`](data-standardization-google-dns-integration.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook, Form Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| VirusTotal result | `httpRequest` | Inspect parameters |
| DNS Lookup | `httpRequest` | Inspect parameters |
| Set IP From Lookup | `code` | Inspect parameters |
| Set IP | `set` | Inspect parameters |
| Merge VirusTotal & Greynoise results | `merge` | Inspect parameters |
| Is IP? | `if` | Inspect parameters |
| Start VirusTotal Scan | `httpRequest` | POST |
| VirusTotal Summary | `set` | Inspect parameters |
| VirusTotal ready? | `if` | Inspect parameters |
| Wait 5s | `wait` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Get List of URLs | `itemLists` | Inspect parameters |
| Set Email | `set` | Inspect parameters |
| Merge Greynoise results | `merge` | Inspect parameters |
| Send Report Slack | `slack` | Inspect parameters |
| Send Report Email | `gmail` | Inspect parameters |
| Greynoise Summary | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Combine looped items | `code` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| GreyNoise RIOT lookup | `httpRequest` | Inspect parameters |
| GreyNoise IP Check | `httpRequest` | Inspect parameters |
| Form Trigger | `formTrigger` | Inspect parameters |

## Connection map

- Merge → Start VirusTotal Scan (`main`, output 0, input 0)
- Merge → GreyNoise IP Check (`main`, output 0, input 0)
- Merge → GreyNoise RIOT lookup (`main`, output 0, input 0)
- Filter → VirusTotal ready? (`main`, output 0, input 0)
- Is IP? → Set IP (`main`, output 0, input 0)
- Is IP? → DNS Lookup (`main`, output 1, input 0)
- Set IP → Merge (`main`, output 0, input 0)
- Wait 5s → VirusTotal result (`main`, output 0, input 0)
- Webhook → Get List of URLs (`main`, output 0, input 0)
- Set Email → Is IP? (`main`, output 0, input 0)
- DNS Lookup → Set IP From Lookup (`main`, output 0, input 0)
- Form Trigger → Is IP? (`main`, output 0, input 0)
- Get List of URLs → Set Email (`main`, output 0, input 0)
- Greynoise Summary → Merge VirusTotal & Greynoise results (`main`, output 0, input 0)
- VirusTotal ready? → Combine looped items (`main`, output 0, input 0)
- VirusTotal ready? → Wait 5s (`main`, output 1, input 0)
- VirusTotal result → Filter (`main`, output 0, input 0)
- GreyNoise IP Check → Merge Greynoise results (`main`, output 0, input 1)
- Set IP From Lookup → Merge (`main`, output 0, input 1)
- VirusTotal Summary → Merge VirusTotal & Greynoise results (`main`, output 0, input 1)
- Combine looped items → VirusTotal Summary (`main`, output 0, input 0)
- GreyNoise RIOT lookup → Merge Greynoise results (`main`, output 0, input 0)
- Start VirusTotal Scan → Wait 5s (`main`, output 0, input 0)
- Merge Greynoise results → Greynoise Summary (`main`, output 0, input 0)
- Merge VirusTotal & Greynoise results → Send Report Slack (`main`, output 0, input 0)
- Merge VirusTotal & Greynoise results → Send Report Email (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0330_Wait_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0330_Wait_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
