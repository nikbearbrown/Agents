# Scenario 1: Transcribe Call with AssemblyAI

This folder contains the **Scenario 1: Transcribe Call with AssemblyAI** workflow. Its executable nodes use `httpRequest`, `if`, `manualTrigger`, `set`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`scenario-1-transcribe-call-with-assemblyai.json`](scenario-1-transcribe-call-with-assemblyai.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpHeaderAuth`, `openAiApi`, `supabaseApi`

**Entry nodes:** When clicking ‘Test workflow’, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Set link to audio | `set` | Inspect parameters |
| AssemblyAI - Transcribe | `httpRequest` | POST |
| If | `if` | Inspect parameters |
| AssemblyAI - Get transcription | `httpRequest` | Inspect parameters |
| OpenAI - Analyze call | `httpRequest` | POST |
| Set vars | `set` | Inspect parameters |
| Create record | `supabase` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |

## Connection map

- If → AssemblyAI - Get transcription (`main`, output 0, input 0)
- Webhook → Set vars (`main`, output 0, input 0)
- Set vars → If (`main`, output 0, input 0)
- Set link to audio → AssemblyAI - Transcribe (`main`, output 0, input 0)
- OpenAI - Analyze call → Create record (`main`, output 0, input 0)
- AssemblyAI - Get transcription → OpenAI - Analyze call (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Set link to audio (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0632_Webhook_Manual_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/0632_Webhook_Manual_Create_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
