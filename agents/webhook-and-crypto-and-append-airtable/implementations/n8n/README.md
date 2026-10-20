# webhook and crypto and append airtable

This folder contains the **webhook and crypto and append airtable** workflow. Its executable nodes use `airtable`, `crypto`, `function`, `if`, `set`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-crypto-and-append-airtable.json`](webhook-and-crypto-and-append-airtable.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `airtableApi`

**Entry nodes:** Webhook, Webhook1, Webhook2

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| Extract URL | `set` | Inspect parameters |
| Check URL | `if` | Inspect parameters |
| Crypto | `crypto` | Inspect parameters |
| Airtable | `airtable` | append |
| Set ID,shortUrl,longUrl | `set` | Inspect parameters |
| Find by ID | `airtable` | list |
| Already exists ? | `if` | Inspect parameters |
| Set Output | `set` | Inspect parameters |
| Set Error output | `set` | Inspect parameters |
| Set Output1 | `set` | Inspect parameters |
| Set input | `set` | Inspect parameters |
| Webhook1 | `webhook` | Inspect parameters |
| Set Error output1 | `set` | Inspect parameters |
| Check Id | `if` | Inspect parameters |
| Find by ID1 | `airtable` | list |
| Already exists ?1 | `if` | Inspect parameters |
| Set Output2 | `set` | Inspect parameters |
| Extract Id | `set` | Inspect parameters |
| 404 Error | `set` | Inspect parameters |
| Update clicks | `airtable` | update |
| Prepare clicks count | `set` | Inspect parameters |
| Webhook2 | `webhook` | Inspect parameters |
| Find by ID2 | `airtable` | list |
| Extract stats | `function` | Inspect parameters |
| Set dashboard | `set` | Inspect parameters |

## Connection map

- Crypto → Set ID,shortUrl,longUrl (`main`, output 0, input 0)
- Webhook → Check URL (`main`, output 0, input 0)
- Airtable → Set Output1 (`main`, output 0, input 0)
- Check Id → Extract Id (`main`, output 0, input 0)
- Check Id → Set Error output1 (`main`, output 1, input 0)
- Webhook1 → Check Id (`main`, output 0, input 0)
- Webhook2 → Find by ID2 (`main`, output 0, input 0)
- Check URL → Extract URL (`main`, output 0, input 0)
- Check URL → Set Error output (`main`, output 1, input 0)
- Set input → Airtable (`main`, output 0, input 0)
- Extract Id → Find by ID1 (`main`, output 0, input 0)
- Find by ID → Already exists ? (`main`, output 0, input 0)
- Extract URL → Crypto (`main`, output 0, input 0)
- Find by ID1 → Already exists ?1 (`main`, output 0, input 0)
- Find by ID2 → Extract stats (`main`, output 0, input 0)
- Extract stats → Set dashboard (`main`, output 0, input 0)
- Update clicks → Set Output2 (`main`, output 0, input 0)
- Already exists ? → Set Output (`main`, output 0, input 0)
- Already exists ? → Set input (`main`, output 1, input 0)
- Already exists ?1 → Prepare clicks count (`main`, output 0, input 0)
- Already exists ?1 → 404 Error (`main`, output 1, input 0)
- Prepare clicks count → Update clicks (`main`, output 0, input 0)
- Set ID,shortUrl,longUrl → Find by ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Crypto/0042_Crypto_Airtable_Update_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Crypto/0042_Crypto_Airtable_Update_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
