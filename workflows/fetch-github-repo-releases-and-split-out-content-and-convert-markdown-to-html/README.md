# fetch github repo releases and split out content and convert markdown to html

This folder contains the **fetch github repo releases and split out content and convert markdown to html** workflow. Its executable nodes use `emailSend`, `httpRequest`, `if`, `markdown`, `scheduleTrigger`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`fetch-github-repo-releases-and-split-out-content-and-convert-markdown-to-html.json`](fetch-github-repo-releases-and-split-out-content-and-convert-markdown-to-html.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `smtp`

**Entry nodes:** Daily Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Fetch Github Repo Releases | `httpRequest` | Inspect parameters |
| Split Out Content | `splitOut` | Inspect parameters |
| Convert Markdown to HTML | `markdown` | Inspect parameters |
| Daily Trigger | `scheduleTrigger` | Inspect parameters |
| Send Email | `emailSend` | Inspect parameters |
| If new release in the last day | `if` | Inspect parameters |

## Connection map

- Daily Trigger → Fetch Github Repo Releases (`main`, output 0, input 0)
- Split Out Content → Convert Markdown to HTML (`main`, output 0, input 0)
- Convert Markdown to HTML → Send Email (`main`, output 0, input 0)
- Fetch Github Repo Releases → If new release in the last day (`main`, output 0, input 0)
- If new release in the last day → Split Out Content (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0652_Splitout_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0652_Splitout_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
