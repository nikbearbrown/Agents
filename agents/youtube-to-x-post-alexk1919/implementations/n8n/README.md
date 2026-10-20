# YouTube to X Post- AlexK1919

This folder contains the **YouTube to X Post- AlexK1919** workflow. Its executable nodes use `discord`, `gmail`, `googleSheets`, `if`, `manualTrigger`, `openAi`, `removeDuplicates`, `scheduleTrigger`, `set`, `slack`, `toolCalculator`, `toolWikipedia`, `twitter`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`youtube-to-x-post-alexk1919.json`](youtube-to-x-post-alexk1919.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `googleSheetsOAuth2Api`, `openAiApi`, `twitterOAuth2Api`, `youTubeOAuth2Api`

**Entry nodes:** Check Every 2 Hours, When clicking "Test workflow"

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Post to X | `twitter` | Inspect parameters |
| Fetch Latest Videos | `youTube` | video |
| Calculator | `toolCalculator` | Inspect parameters |
| Wikipedia | `toolWikipedia` | Inspect parameters |
| Check Every 2 Hours | `scheduleTrigger` | Inspect parameters |
| Calculator2 | `toolCalculator` | Inspect parameters |
| GS - Add Tweet | `googleSheets` | append |
| GS - Update Tweet | `googleSheets` | appendOrUpdate |
| When clicking "Test workflow" | `manualTrigger` | Inspect parameters |
| Discord | `discord` | Inspect parameters |
| Remove Duplicates | `removeDuplicates` | removeItemsSeenInPreviousExecutions |
| Generate X Post | `openAi` | Inspect parameters |
| Set Fields | `set` | Inspect parameters |
| Wikipedia1 | `toolWikipedia` | Inspect parameters |
| Rewrite X Post to 220 Characters | `openAi` | Inspect parameters |
| Verify character limit constraints | `if` | Inspect parameters |
| Slack | `slack` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Set Final Fields | `set` | Inspect parameters |
| If Array is empty? | `if` | Inspect parameters |

## Connection map

- Post to X → GS - Update Tweet (`main`, output 0, input 0)
- Wikipedia → Generate X Post (`ai_tool`, output 0, input 0)
- Calculator → Generate X Post (`ai_tool`, output 0, input 0)
- Set Fields → Remove Duplicates (`main`, output 0, input 0)
- Wikipedia1 → Rewrite X Post to 220 Characters (`ai_tool`, output 0, input 0)
- Calculator2 → Rewrite X Post to 220 Characters (`ai_tool`, output 0, input 0)
- GS - Add Tweet → Post to X (`main`, output 0, input 0)
- Generate X Post → Verify character limit constraints (`main`, output 0, input 0)
- Set Final Fields → GS - Add Tweet (`main`, output 0, input 0)
- Remove Duplicates → If Array is empty? (`main`, output 0, input 0)
- If Array is empty? → Generate X Post (`main`, output 1, input 0)
- Fetch Latest Videos → Set Fields (`main`, output 0, input 0)
- When clicking "Test workflow" → Fetch Latest Videos (`main`, output 0, input 0)
- Rewrite X Post to 220 Characters → Verify character limit constraints (`main`, output 0, input 0)
- Verify character limit constraints → Rewrite X Post to 220 Characters (`main`, output 0, input 0)
- Verify character limit constraints → Set Final Fields (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 1}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1345_Schedule_Discord_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1345_Schedule_Discord_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
