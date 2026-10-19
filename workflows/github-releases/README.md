# Github Releases

This folder contains the **Github Releases** workflow. Its executable nodes use `code`, `dateTime`, `if`, `informationExtractor`, `limit`, `lmChatGoogleGemini`, `redis`, `rssFeedRead`, `scheduleTrigger`, `set`, `slack`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`github-releases.json`](github-releases.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `redis`, `slackApi`

**Entry nodes:** Cron Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Limit | `limit` | Inspect parameters |
| Loop | `splitInBatches` | Inspect parameters |
| Edit Fields | `set` | Inspect parameters |
| Cron Trigger | `scheduleTrigger` | Inspect parameters |
| GitHub Config | `code` | Inspect parameters |
| If No Error | `if` | Inspect parameters |
| If New | `if` | Inspect parameters |
| Null | `set` | Inspect parameters |
| Send Error | `slack` | Inspect parameters |
| If Not Empty | `if` | Inspect parameters |
| Date Format | `dateTime` | formatDate |
| Information Extractor | `informationExtractor` | Inspect parameters |
| Send Message | `slack` | Inspect parameters |
| Gemini | `lmChatGoogleGemini` | Inspect parameters |
| Redis Set Id | `redis` | set |
| Code for Slack Tpl | `code` | Inspect parameters |
| RSS for Release | `rssFeedRead` | Inspect parameters |
| Redis Get | `redis` | get |

## Connection map

- Loop → If Not Empty (`main`, output 0, input 0)
- Loop → RSS for Release (`main`, output 1, input 0)
- Null → Loop (`main`, output 0, input 0)
- Limit → Redis Get (`main`, output 0, input 0)
- Gemini → Information Extractor (`ai_languageModel`, output 0, input 0)
- If New → Edit Fields (`main`, output 0, input 0)
- If New → Null (`main`, output 1, input 0)
- Redis Get → If New (`main`, output 0, input 0)
- Date Format → Code for Slack Tpl (`main`, output 0, input 0)
- Edit Fields → Loop (`main`, output 0, input 0)
- If No Error → Limit (`main`, output 0, input 0)
- If No Error → Send Error (`main`, output 1, input 0)
- If No Error → Null (`main`, output 1, input 0)
- Cron Trigger → GitHub Config (`main`, output 0, input 0)
- If Not Empty → Information Extractor (`main`, output 0, input 0)
- Send Message → Redis Set Id (`main`, output 0, input 0)
- GitHub Config → Loop (`main`, output 0, input 0)
- RSS for Release → If No Error (`main`, output 0, input 0)
- Code for Slack Tpl → Send Message (`main`, output 0, input 0)
- Information Extractor → Date Format (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1695_Limit_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Limit/1695_Limit_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
