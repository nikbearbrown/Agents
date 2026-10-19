# Delete NM of KV (By Name Serach)

This folder contains the **Delete NM of KV (By Name Serach)** workflow. Its executable nodes use `httpRequest`, `manualTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`delete-nm-of-kv-by-name-serach.json`](delete-nm-of-kv-by-name-serach.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Manual Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Delete KV | `httpRequest` | DELETE |
| Delete KV1 | `httpRequest` | PUT |
| KV to Rename | `set` | Inspect parameters |
| Account Path | `set` | Inspect parameters |
| Delete KVs inside NM | `httpRequest` | DELETE |
| Create KV-NM | `httpRequest` | POST |
| Write KVs inside NM | `httpRequest` | PUT |
| -Get Keys inside NM | `httpRequest` | Inspect parameters |
| Delete KV inside NM | `httpRequest` | DELETE |
| Read Value Of KV In NM | `httpRequest` | Inspect parameters |
| Manual Trigger | `manualTrigger` | Inspect parameters |
| List KV-NMs (1) | `httpRequest` | Inspect parameters |
| Set KV-NM Name (2) | `set` | Inspect parameters |
| Set KV-NM Name (1) | `set` | Inspect parameters |
| Set KV-NM Name (3) | `set` | Inspect parameters |
| List KV-NMs (2) | `httpRequest` | Inspect parameters |
| List KV-NMs (3) | `httpRequest` | Inspect parameters |
| Set KV-NM Name (4) | `set` | Inspect parameters |
| Write V & MD of KV In NM | `httpRequest` | PUT |
| Set KV-NM Name (5) | `set` | Inspect parameters |
| Set KV-NM Name (6) | `set` | Inspect parameters |
| List KV-NMs (4) | `httpRequest` | Inspect parameters |
| List KV-NMs (5) | `httpRequest` | Inspect parameters |
| List KV-NMs (6) | `httpRequest` | Inspect parameters |
| List KV-NMs (7) | `httpRequest` | Inspect parameters |
| List KV-NMs (8) | `httpRequest` | Inspect parameters |
| List KV-NMs (9) | `httpRequest` | Inspect parameters |
| List KV-NMs (10) | `httpRequest` | Inspect parameters |
| Set KV-NM Name (7) | `set` | Inspect parameters |
| Set KV-NM Name (8) | `set` | Inspect parameters |
| Read MD from Key | `httpRequest` | Inspect parameters |

## Connection map

- Account Path → Set KV-NM Name (1) (`main`, output 0, input 0)
- Account Path → Create KV-NM (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (6) (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (2) (`main`, output 0, input 0)
- Account Path → KV to Rename (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (7) (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (3) (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (5) (`main`, output 0, input 0)
- Account Path → Set KV-NM Name (8) (`main`, output 0, input 0)
- KV to Rename → List KV-NMs (5) (`main`, output 0, input 0)
- Manual Trigger → Account Path (`main`, output 0, input 0)
- List KV-NMs (1) → Delete KV inside NM (`main`, output 0, input 0)
- List KV-NMs (2) → Delete KV (`main`, output 0, input 0)
- List KV-NMs (3) → Delete KVs inside NM (`main`, output 0, input 0)
- List KV-NMs (4) → Write V & MD of KV In NM (`main`, output 0, input 0)
- List KV-NMs (5) → Delete KV1 (`main`, output 0, input 0)
- List KV-NMs (6) → Write KVs inside NM (`main`, output 0, input 0)
- List KV-NMs (7) → Read Value Of KV In NM (`main`, output 0, input 0)
- List KV-NMs (8) → Read MD from Key (`main`, output 0, input 0)
- List KV-NMs (9) → -Get Keys inside NM (`main`, output 0, input 0)
- Set KV-NM Name (1) → List KV-NMs (1) (`main`, output 0, input 0)
- Set KV-NM Name (2) → List KV-NMs (2) (`main`, output 0, input 0)
- Set KV-NM Name (3) → List KV-NMs (3) (`main`, output 0, input 0)
- Set KV-NM Name (4) → List KV-NMs (4) (`main`, output 0, input 0)
- Set KV-NM Name (5) → List KV-NMs (6) (`main`, output 0, input 0)
- Set KV-NM Name (6) → List KV-NMs (7) (`main`, output 0, input 0)
- Set KV-NM Name (7) → List KV-NMs (8) (`main`, output 0, input 0)
- Set KV-NM Name (8) → List KV-NMs (9) (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0384_HTTP_Manual_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Http/0384_HTTP_Manual_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
