# Qualify new leads in Google Sheets via OpenAI's GPT-4

This folder contains the **Qualify new leads in Google Sheets via OpenAI's GPT-4** workflow. Its executable nodes use `googleSheets`, `googleSheetsTrigger`, `merge`, `openAi`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`qualify-new-leads-in-google-sheets-via-openai-s-gpt-4.json`](qualify-new-leads-in-google-sheets-via-openai-s-gpt-4.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googleSheetsOAuth2Api`, `googleSheetsTriggerOAuth2Api`, `openAiApi`

**Entry nodes:** Check for new entries

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Merge | `merge` | Inspect parameters |
| Update lead status | `googleSheets` | update |
| Extract JSON reply | `set` | Inspect parameters |
| Qualify leads with GPT | `openAi` | chat |
| Check for new entries | `googleSheetsTrigger` | Inspect parameters |

## Connection map

- Merge → Update lead status (`main`, output 0, input 0)
- Extract JSON reply → Merge (`main`, output 0, input 1)
- Check for new entries → Merge (`main`, output 0, input 0)
- Check for new entries → Qualify leads with GPT (`main`, output 0, input 0)
- Qualify leads with GPT → Extract JSON reply (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/1618_Openai_GoogleSheets_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Openai/1618_Openai_GoogleSheets_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
