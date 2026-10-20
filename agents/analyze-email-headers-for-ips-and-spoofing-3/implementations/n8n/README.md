# Analyze_email_headers_for_IPs_and_spoofing__3

This folder contains the **Analyze_email_headers_for_IPs_and_spoofing__3** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `itemLists`, `merge`, `respondToWebhook`, `set`, `switch`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`analyze-email-headers-for-ips-and-spoofing-3.json`](analyze-email-headers-for-ips-and-spoofing-3.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Receive Headers

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Receive Headers | `webhook` | Inspect parameters |
| Fraud Score | `code` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Explode Email Header | `code` | Inspect parameters |
| Split Out IPs | `itemLists` | Inspect parameters |
| Extract IPs from "received" | `code` | Inspect parameters |
| IP Quality Score | `httpRequest` | Inspect parameters |
| IP-API | `httpRequest` | POST |
| Collect interesting data | `set` | Inspect parameters |
| SPF/DKIM/DMARC from "authentication-results" | `code` | Inspect parameters |
| SPF from "received-spf" | `code` | Inspect parameters |
| DKIM from "dkim-signature" | `code` | Inspect parameters |
| DMARC from "received-dmarc" | `code` | Inspect parameters |
| DKIM | `switch` | Inspect parameters |
| Extract Email Header from webhook | `set` | Inspect parameters |
| Received Headers Present? | `if` | Inspect parameters |
| Authentication Results Present? | `if` | Inspect parameters |
| Aggregate Authentication Data | `set` | Inspect parameters |
| IP Data Merge | `merge` | Inspect parameters |
| Merge Security Data | `merge` | Inspect parameters |
| Join IP Analysis into one JSON object | `itemLists` | concatenateItems |
| Join results into one JSON object | `itemLists` | concatenateItems |
| SPF Authentication Checker | `switch` | Inspect parameters |
| Set SPF Pass Status | `set` | Inspect parameters |
| Set SPF Fail Status | `set` | Inspect parameters |
| Set SPF Neutral Status | `set` | Inspect parameters |
| Set SPF UnknownStatus | `set` | Inspect parameters |

## Connection map

- IP-API → Fraud Score (`main`, output 0, input 0)
- Fraud Score → Collect interesting data (`main`, output 0, input 0)
- IP Data Merge → Join IP Analysis into one JSON object (`main`, output 0, input 0)
- Split Out IPs → IP Quality Score (`main`, output 0, input 0)
- Receive Headers → Extract Email Header from webhook (`main`, output 0, input 0)
- IP Quality Score → IP-API (`main`, output 0, input 0)
- Merge Security Data → Join results into one JSON object (`main`, output 0, input 0)
- Set SPF Fail Status → DKIM (`main`, output 0, input 0)
- Set SPF Pass Status → DKIM (`main`, output 0, input 0)
- Explode Email Header → Received Headers Present? (`main`, output 0, input 0)
- Explode Email Header → Authentication Results Present? (`main`, output 0, input 0)
- Set SPF UnknownStatus → DKIM (`main`, output 0, input 0)
- Set SPF Neutral Status → DKIM (`main`, output 0, input 0)
- SPF from "received-spf" → DKIM from "dkim-signature" (`main`, output 0, input 0)
- Collect interesting data → IP Data Merge (`main`, output 0, input 0)
- Received Headers Present? → Extract IPs from "received" (`main`, output 0, input 0)
- Received Headers Present? → IP Data Merge (`main`, output 1, input 1)
- DKIM from "dkim-signature" → DMARC from "received-dmarc" (`main`, output 0, input 0)
- SPF Authentication Checker → Set SPF Pass Status (`main`, output 0, input 0)
- SPF Authentication Checker → Set SPF Fail Status (`main`, output 1, input 0)
- SPF Authentication Checker → Set SPF Neutral Status (`main`, output 2, input 0)
- SPF Authentication Checker → Set SPF UnknownStatus (`main`, output 3, input 0)
- DMARC from "received-dmarc" → Aggregate Authentication Data (`main`, output 0, input 0)
- Extract IPs from "received" → Split Out IPs (`main`, output 0, input 0)
- Aggregate Authentication Data → Merge Security Data (`main`, output 0, input 1)
- Authentication Results Present? → SPF/DKIM/DMARC from "authentication-results" (`main`, output 0, input 0)
- Authentication Results Present? → SPF Authentication Checker (`main`, output 0, input 0)
- Authentication Results Present? → SPF from "received-spf" (`main`, output 1, input 0)
- Extract Email Header from webhook → Explode Email Header (`main`, output 0, input 0)
- Join results into one JSON object → Respond to Webhook (`main`, output 0, input 0)
- Join IP Analysis into one JSON object → Merge Security Data (`main`, output 0, input 0)
- SPF/DKIM/DMARC from "authentication-results" → Merge Security Data (`main`, output 0, input 1)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0946_Code_Webhook_Send_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0946_Code_Webhook_Send_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
