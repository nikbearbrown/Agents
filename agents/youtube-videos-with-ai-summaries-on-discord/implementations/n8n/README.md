# YouTube Videos with AI Summaries on Discord

This folder contains the **YouTube Videos with AI Summaries on Discord** workflow. Its executable nodes use `discord`, `extractFromFile`, `httpRequest`, `openAi`, `rssFeedReadTrigger`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-videos-with-ai-summaries-on-discord.json`](youtube-videos-with-ai-summaries-on-discord.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `discordWebhookApi`, `openAiApi`, `youTubeOAuth2Api`

**Entry nodes:** YouTube Video Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| YouTube Video Trigger | `rssFeedReadTrigger` | Inspect parameters |
| Retrieve Caption Data | `httpRequest` | Inspect parameters |
| Download Captions | `httpRequest` | Inspect parameters |
| Caption File Conversion | `extractFromFile` | text |
| Caption Summary with ChatGPT | `openAi` | Inspect parameters |
| Post to Discord | `discord` | Inspect parameters |
| Find English Captions | `set` | Inspect parameters |

## Connection map

- Download Captions → Caption File Conversion (`main`, output 0, input 0)
- Find English Captions → Download Captions (`main`, output 0, input 0)
- Retrieve Caption Data → Find English Captions (`main`, output 0, input 0)
- YouTube Video Trigger → Retrieve Caption Data (`main`, output 0, input 0)
- Caption File Conversion → Caption Summary with ChatGPT (`main`, output 0, input 0)
- Caption Summary with ChatGPT → Post to Discord (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1536_Rssfeedread_Extractfromfile_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Rssfeedread/1536_Rssfeedread_Extractfromfile_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
