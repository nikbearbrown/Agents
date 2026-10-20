# Youtube_Automation

This folder contains the **Youtube_Automation** workflow. Its executable nodes use `agent`, `code`, `httpRequest`, `if`, `lmChatGoogleGemini`, `manualTrigger`, `openAi`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`, `wait`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-automation.json`](youtube-automation.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `googlePalmApi`, `openAiApi`, `youTubeOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’, Every Day

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Fetch Latest Videos | `youTube` | video |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| YT Title | `openAi` | Inspect parameters |
| Create Description | `openAi` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| 2.5FlashPrev | `lmChatGoogleGemini` | Inspect parameters |
| YT Tags | `agent` | Inspect parameters |
| 3s | `wait` | Inspect parameters |
| gettitle | `youTube` | video / get |
| Set Publish Date | `youTube` | video / update |
| Every Day | `scheduleTrigger` | Inspect parameters |
| Get Videos to reschedule | `youTube` | video |
| Get video Ids seperated | `code` | Inspect parameters |
| Loop over Video IDs | `splitInBatches` | Inspect parameters |
| Get Video Data | `youTube` | video / get |
| Return Private Videos | `code` | Inspect parameters |
| 4s | `wait` | Inspect parameters |
| Loop over All Videos not Published | `splitInBatches` | Inspect parameters |
| get video id | `set` | Inspect parameters |
| Remove Duplicates from previous Runs | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| new video? | `if` | Inspect parameters |
| getLatestVideoID | `youTube` | video / get |
| Get Transcript | `httpRequest` | POST |
| Adjust Transcript Format | `code` | Inspect parameters |
| Update Video's Metadata | `youTube` | video / update |

## Connection map

- 3s → Loop Over Items (`main`, output 0, input 0)
- 4s → Fetch Latest Videos (`main`, output 0, input 0)
- YT Tags → Update Video's Metadata (`main`, output 0, input 0)
- gettitle → Set Publish Date (`main`, output 0, input 0)
- Every Day → Get Videos to reschedule (`main`, output 0, input 0)
- new video? → getLatestVideoID (`main`, output 1, input 0)
- 2.5FlashPrev → YT Tags (`ai_languageModel`, output 0, input 0)
- get video id → Remove Duplicates from previous Runs (`main`, output 0, input 0)
- Get Transcript → Adjust Transcript Format (`main`, output 0, input 0)
- Get Video Data → Loop over Video IDs (`main`, output 0, input 0)
- Loop Over Items → get video id (`main`, output 1, input 0)
- Set Publish Date → Loop over All Videos not Published (`main`, output 0, input 0)
- getLatestVideoID → Get Transcript (`main`, output 0, input 0)
- Create Description → YT Tags (`main`, output 0, input 0)
- Create Description → YT Title (`main`, output 0, input 0)
- Fetch Latest Videos → Loop Over Items (`main`, output 0, input 0)
- Loop over Video IDs → Return Private Videos (`main`, output 0, input 0)
- Loop over Video IDs → Get Video Data (`main`, output 1, input 0)
- Return Private Videos → Loop over All Videos not Published (`main`, output 0, input 0)
- Get video Ids seperated → Loop over Video IDs (`main`, output 0, input 0)
- Update Video's Metadata → 3s (`main`, output 0, input 0)
- Adjust Transcript Format → Create Description (`main`, output 0, input 0)
- Get Videos to reschedule → Get video Ids seperated (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get Videos to reschedule (`main`, output 0, input 0)
- Loop over All Videos not Published → 4s (`main`, output 0, input 0)
- Loop over All Videos not Published → gettitle (`main`, output 1, input 0)
- Remove Duplicates from previous Runs → new video? (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/2000_Wait_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/2000_Wait_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
