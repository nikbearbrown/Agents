# Generate Instagram Content from Top Trends with AI Image Generation

This folder contains the **Generate Instagram Content from Top Trends with AI Image Generation** workflow. Its executable nodes use `code`, `facebookGraphApi`, `httpRequest`, `if`, `merge`, `openAi`, `postgres`, `scheduleTrigger`, `set`, `splitInBatches`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`generate-instagram-content-from-top-trends-with-ai-image-generation.json`](generate-instagram-content-from-top-trends-with-ai-image-generation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `openAiApi`, `postgres`, `telegramApi`

**Entry nodes:** Schedule Trigger1

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If media status is finished | `if` | Inspect parameters |
| If media status is finished1 | `if` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Telegram1 | `telegram` | Inspect parameters |
| Telegram2 | `telegram` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Schedule Trigger1 | `scheduleTrigger` | Inspect parameters |
| Telegram Params | `set` | Inspect parameters |
| Instagram params | `set` | Inspect parameters |
| Rapid Api params | `set` | Inspect parameters |
| filter the image content | `code` | Inspect parameters |
| get  top trends on instagram #blender3d | `httpRequest` | Inspect parameters |
| get top trends on instagram #isometric | `httpRequest` | Inspect parameters |
| merge the array content | `merge` | Inspect parameters |
| Check Data on Database Is Exist | `postgres` | select |
| If Data is Exist | `if` | Inspect parameters |
| send error message to telegram | `telegram` | Inspect parameters |
| insert data on db | `postgres` | Inspect parameters |
| Analyze Image and give the content | `openAi` | image / analyze |
| Analyze Content And Generate Instagram Caption | `openAi` | Inspect parameters |
| Prepare data on Instagram | `facebookGraphApi` | Inspect parameters |
| Check Status Of Media Before Uploaded | `facebookGraphApi` | Inspect parameters |
| Publish Media on Instagram | `facebookGraphApi` | Inspect parameters |
| Check status of post  | `facebookGraphApi` | Inspect parameters |
| filter the image content-2 | `code` | Inspect parameters |
| Replicate params | `set` | Inspect parameters |
| Generate image on flux | `httpRequest` | POST |

## Connection map

- Loop Over Items → Check Data on Database Is Exist (`main`, output 1, input 0)
- Telegram Params → Rapid Api params (`main`, output 0, input 0)
- If Data is Exist → Loop Over Items (`main`, output 0, input 0)
- If Data is Exist → insert data on db (`main`, output 1, input 0)
- Instagram params → Telegram Params (`main`, output 0, input 0)
- Rapid Api params → get top trends on instagram #isometric (`main`, output 0, input 0)
- Rapid Api params → get  top trends on instagram #blender3d (`main`, output 0, input 0)
- Replicate params → Instagram params (`main`, output 0, input 0)
- Schedule Trigger1 → Replicate params (`main`, output 0, input 0)
- insert data on db → Analyze Image and give the content (`main`, output 0, input 0)
- Check status of post  → If media status is finished1 (`main`, output 0, input 0)
- Generate image on flux → Prepare data on Instagram (`main`, output 0, input 0)
- merge the array content → Loop Over Items (`main`, output 0, input 0)
- filter the image content → merge the array content (`main`, output 0, input 1)
- Prepare data on Instagram → Check Status Of Media Before Uploaded (`main`, output 0, input 0)
- Publish Media on Instagram → Check status of post  (`main`, output 0, input 0)
- filter the image content-2 → merge the array content (`main`, output 0, input 0)
- If media status is finished → Publish Media on Instagram (`main`, output 0, input 0)
- If media status is finished → Telegram (`main`, output 1, input 0)
- If media status is finished1 → Telegram1 (`main`, output 0, input 0)
- If media status is finished1 → Telegram2 (`main`, output 1, input 0)
- Check Data on Database Is Exist → If Data is Exist (`main`, output 0, input 0)
- Check Data on Database Is Exist → send error message to telegram (`main`, output 1, input 0)
- Analyze Image and give the content → Analyze Content And Generate Instagram Caption (`main`, output 0, input 0)
- Check Status Of Media Before Uploaded → If media status is finished (`main`, output 0, input 0)
- get top trends on instagram #isometric → filter the image content (`main`, output 0, input 0)
- get  top trends on instagram #blender3d → filter the image content-2 (`main`, output 0, input 0)
- Analyze Content And Generate Instagram Caption → Generate image on flux (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1482_Telegram_Code_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/1482_Telegram_Code_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
