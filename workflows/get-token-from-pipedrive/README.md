# 2. Refresh Pipedrive tokens

This folder contains the **2. Refresh Pipedrive tokens** workflow. Its executable nodes use `code`, `httpRequest`, `if`, `respondToWebhook`, `set`, `stopAndError`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`get-token-from-pipedrive.json`](get-token-from-pipedrive.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `supabaseApi`

**Entry nodes:** Webhook, Receive request, catch Auth code

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Stop and Error | `stopAndError` | Inspect parameters |
| Insert | `supabase` | Inspect parameters |
| Get Pipedrive Token | `supabase` | get |
| Get contact from Pipedrive | `httpRequest` | Inspect parameters |
| Access Token Invalid | `if` | Inspect parameters |
| Success | `respondToWebhook` | Inspect parameters |
| Refresh Access Token | `httpRequest` | POST |
| convert clientId and secret to base64 | `code` | Inspect parameters |
| Generate Refresh Token from authcode | `httpRequest` | POST |
| Look for the related record in Supabase | `supabase` | get |
| IF rec not found | `if` | Inspect parameters |
| Update tokns in the record | `supabase` | update |
| Supabase- look for the record | `supabase` | get |
| combine client id and secret | `set` | Inspect parameters |
| Get Pipedrive acess token | `httpRequest` | POST |
| IF success | `if` | Inspect parameters |
| Update thr row with new access token | `supabase` | update |
| Webhook | `webhook` | Inspect parameters |
| Receive request | `webhook` | Inspect parameters |
| catch Auth code | `webhook` | Inspect parameters |

## Connection map

- Webhook → Supabase- look for the record (`main`, output 0, input 0)
- IF success → Update thr row with new access token (`main`, output 0, input 0)
- IF success → Stop and Error (`main`, output 1, input 0)
- Receive request → Get Pipedrive Token (`main`, output 0, input 0)
- catch Auth code → convert clientId and secret to base64 (`main`, output 0, input 0)
- IF rec not found → Insert (`main`, output 0, input 0)
- IF rec not found → Update tokns in the record (`main`, output 1, input 0)
- Get Pipedrive Token → Get contact from Pipedrive (`main`, output 0, input 0)
- Access Token Invalid → Refresh Access Token (`main`, output 0, input 0)
- Access Token Invalid → Success (`main`, output 1, input 0)
- Refresh Access Token → Get Pipedrive Token (`main`, output 0, input 0)
- Get Pipedrive acess token → IF success (`main`, output 0, input 0)
- Get contact from Pipedrive → Access Token Invalid (`main`, output 0, input 0)
- combine client id and secret → Get Pipedrive acess token (`main`, output 0, input 0)
- Supabase- look for the record → combine client id and secret (`main`, output 0, input 0)
- Generate Refresh Token from authcode → Look for the related record in Supabase (`main`, output 0, input 0)
- convert clientId and secret to base64 → Generate Refresh Token from authcode (`main`, output 0, input 0)
- Look for the related record in Supabase → IF rec not found (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1504_Stopanderror_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Stopanderror/1504_Stopanderror_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
