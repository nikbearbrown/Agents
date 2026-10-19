# My workflow

This folder contains the **My workflow** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `compression`, `convertToFile`, `googleDrive`, `httpRequest`, `if`, `lmChatAnthropic`, `reddit`, `scheduleTrigger`, `set`, `splitInBatches`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automatic-weekly-digital-pr-stories-suggestions.json`](automatic-weekly-digital-pr-stories-suggestions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Split Topics into Items | `code` | Inspect parameters |
| Search Posts | `reddit` | search |
| Upvotes Requirement Filtering | `if` | Inspect parameters |
| Set Reddit Posts | `set` | Inspect parameters |
| Remove Duplicates | `code` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Get Comments | `reddit` | postComment / getAll |
| Extract Top Comments | `code` | Inspect parameters |
| Format Comments | `code` | Inspect parameters |
| Set for Loop | `set` | Inspect parameters |
| Get News Content | `httpRequest` | Inspect parameters |
| Set Final Report | `set` | Inspect parameters |
| Convert to File | `convertToFile` | toText |
| Compress files | `compression` | compress |
| Merge Binary Files | `code` | Inspect parameters |
| Google Drive6 | `googleDrive` | Inspect parameters |
| Google Drive7 | `googleDrive` | share |
| Send files to Mattermost3 | `httpRequest` | POST |
| Aggregate | `aggregate` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Anthropic Chat Model1 | `lmChatAnthropic` | Inspect parameters |
| Keep Last | `code` | Inspect parameters |
| Anthropic Chat Model2 | `lmChatAnthropic` | Inspect parameters |
| Comments Analysis | `chainLlm` | Inspect parameters |
| News Analysis | `chainLlm` | Inspect parameters |
| Stories Report | `chainLlm` | Inspect parameters |
| Set Data | `set` | Inspect parameters |

## Connection map

- Set Data → Split Topics into Items (`main`, output 0, input 0)
- Aggregate → Merge Binary Files (`main`, output 0, input 0)
- Keep Last → News Analysis (`main`, output 0, input 0)
- Get Comments → Extract Top Comments (`main`, output 0, input 0)
- Search Posts → Upvotes Requirement Filtering (`main`, output 0, input 0)
- Set for Loop → Get Comments (`main`, output 0, input 0)
- Google Drive6 → Google Drive7 (`main`, output 0, input 0)
- Google Drive7 → Send files to Mattermost3 (`main`, output 0, input 0)
- News Analysis → Stories Report (`main`, output 0, input 0)
- Compress files → Google Drive6 (`main`, output 0, input 0)
- Stories Report → Set Final Report (`main`, output 0, input 0)
- Convert to File → Loop Over Items (`main`, output 0, input 0)
- Format Comments → Comments Analysis (`main`, output 0, input 0)
- Loop Over Items → Aggregate (`main`, output 0, input 0)
- Loop Over Items → Set for Loop (`main`, output 1, input 0)
- Get News Content → Keep Last (`main`, output 0, input 0)
- Schedule Trigger → Set Data (`main`, output 0, input 0)
- Set Final Report → Convert to File (`main`, output 0, input 0)
- Set Reddit Posts → Remove Duplicates (`main`, output 0, input 0)
- Comments Analysis → Get News Content (`main`, output 0, input 0)
- Remove Duplicates → Loop Over Items (`main`, output 0, input 0)
- Merge Binary Files → Compress files (`main`, output 0, input 0)
- Anthropic Chat Model → Comments Analysis (`ai_languageModel`, output 0, input 0)
- Extract Top Comments → Format Comments (`main`, output 0, input 0)
- Anthropic Chat Model1 → News Analysis (`ai_languageModel`, output 0, input 0)
- Anthropic Chat Model2 → Stories Report (`ai_languageModel`, output 0, input 0)
- Split Topics into Items → Search Posts (`main`, output 0, input 0)
- Upvotes Requirement Filtering → Set Reddit Posts (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1875_Code_Schedule_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/1875_Code_Schedule_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
