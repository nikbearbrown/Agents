# webhook and youtube transcripter and split out fddb0a51

This folder contains the **webhook and youtube transcripter and split out fddb0a51** workflow. Its executable nodes use `chainLlm`, `code`, `lmChatOpenAi`, `respondToWebhook`, `set`, `splitOut`, `summarize`, `telegram`, `webhook`, `youTube`, `youtubeTranscripter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`webhook-and-youtube-transcripter-and-split-out-fddb0a51.json`](webhook-and-youtube-transcripter-and-split-out-fddb0a51.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Webhook | `webhook` | Inspect parameters |
| YouTube Transcript | `youtubeTranscripter` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Respond to Webhook | `respondToWebhook` | Inspect parameters |
| Telegram | `telegram` | Inspect parameters |
| Get YouTube URL | `set` | Inspect parameters |
| YouTube Video ID | `code` | Inspect parameters |
| Get YouTube Video | `youTube` | video / get |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Summarize & Analyze Transcript | `chainLlm` | Inspect parameters |
| Concatenate | `summarize` | Inspect parameters |
| Response Object | `set` | Inspect parameters |

## Connection map

- Webhook → Get YouTube URL (`main`, output 0, input 0)
- Split Out → Concatenate (`main`, output 0, input 0)
- Concatenate → Summarize & Analyze Transcript (`main`, output 0, input 0)
- gpt-4o-mini → Summarize & Analyze Transcript (`ai_languageModel`, output 0, input 0)
- Get YouTube URL → YouTube Video ID (`main`, output 0, input 0)
- Response Object → Respond to Webhook (`main`, output 0, input 0)
- Response Object → Telegram (`main`, output 0, input 0)
- YouTube Video ID → Get YouTube Video (`main`, output 0, input 0)
- Summarize & Analyze Transcript → Response Object (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2040_Telegram_Splitout_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/2040_Telegram_Splitout_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
