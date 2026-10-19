# Monthly Spotify Track Archiving and Playlist Classification

This folder contains the **Monthly Spotify Track Archiving and Playlist Classification** workflow. Its executable nodes use `chainLlm`, `code`, `filter`, `googleSheets`, `httpRequest`, `limit`, `lmChatAnthropic`, `merge`, `noOp`, `outputParserStructured`, `scheduleTrigger`, `set`, `splitOut`, `spotify`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`monthly-spotify-track-archiving-and-playlist-classification.json`](monthly-spotify-track-archiving-and-playlist-classification.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `anthropicApi`, `googleSheetsOAuth2Api`, `spotifyOAuth2Api`

**Entry nodes:** Monthly Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Retrieve relevant info | `set` | Inspect parameters |
| Batch preparation | `code` | Inspect parameters |
| Get Track details | `httpRequest` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Anthropic Chat Model | `lmChatAnthropic` | Inspect parameters |
| Get Playlist | `spotify` | playlist / getUserPlaylists |
| Get Tracks | `spotify` | library |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Playlists informations | `set` | Inspect parameters |
| Filter my playlist | `filter` | Inspect parameters |
| Split Out1 | `splitOut` | Inspect parameters |
| Batch preparation1 | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Simplify Tracks informations | `set` | Inspect parameters |
| Limit | `limit` | Inspect parameters |
| Get logged tracks | `googleSheets` | Inspect parameters |
| Excluding logged tracks | `merge` | Inspect parameters |
| Filter | `filter` | Inspect parameters |
| Split Out2 | `splitOut` | Inspect parameters |
| Manual Verification | `merge` | Inspect parameters |
| Spotify | `spotify` | playlist |
| Aggregate by 200 tracks | `code` | Inspect parameters |
| Monthly Trigger | `scheduleTrigger` | Inspect parameters |
| Get logged playlists | `googleSheets` | Inspect parameters |
| Log new tracks | `googleSheets` | append |
| Log new playlists | `googleSheets` | append |
| Excluding logged playlists | `merge` | Inspect parameters |
| Limit2 | `limit` | Inspect parameters |
| Classify new tracks | `noOp` | Inspect parameters |
| Basic LLM Chain - AI Classification | `chainLlm` | Inspect parameters |

## Connection map

- Limit → Get logged tracks (`main`, output 0, input 0)
- Merge → Simplify Tracks informations (`main`, output 0, input 0)
- Filter → Batch preparation1 (`main`, output 0, input 0)
- Limit2 → Get logged playlists (`main`, output 0, input 0)
- Split Out → Merge (`main`, output 0, input 0)
- Get Tracks → Retrieve relevant info (`main`, output 0, input 0)
- Split Out1 → Split Out2 (`main`, output 0, input 0)
- Split Out1 → Filter (`main`, output 0, input 0)
- Split Out2 → Manual Verification (`main`, output 0, input 1)
- Get Playlist → Filter my playlist (`main`, output 0, input 0)
- Monthly Trigger → Get Playlist (`main`, output 0, input 0)
- Monthly Trigger → Get Tracks (`main`, output 0, input 0)
- Batch preparation → Get Track details (`main`, output 0, input 0)
- Get Track details → Split Out (`main`, output 0, input 0)
- Get logged tracks → Excluding logged tracks (`main`, output 0, input 0)
- Batch preparation1 → Spotify (`main`, output 0, input 0)
- Filter my playlist → Playlists informations (`main`, output 0, input 0)
- Classify new tracks → Aggregate by 200 tracks (`main`, output 0, input 0)
- Classify new tracks → Manual Verification (`main`, output 0, input 0)
- Anthropic Chat Model → Basic LLM Chain - AI Classification (`ai_languageModel`, output 0, input 0)
- Get logged playlists → Excluding logged playlists (`main`, output 0, input 0)
- Playlists informations → Excluding logged playlists (`main`, output 0, input 1)
- Playlists informations → Limit2 (`main`, output 0, input 0)
- Retrieve relevant info → Batch preparation (`main`, output 0, input 0)
- Retrieve relevant info → Merge (`main`, output 0, input 1)
- Aggregate by 200 tracks → Basic LLM Chain - AI Classification (`main`, output 0, input 0)
- Excluding logged tracks → Log new tracks (`main`, output 0, input 0)
- Excluding logged tracks → Classify new tracks (`main`, output 0, input 0)
- Structured Output Parser → Basic LLM Chain - AI Classification (`ai_outputParser`, output 0, input 0)
- Excluding logged playlists → Log new playlists (`main`, output 0, input 0)
- Simplify Tracks informations → Limit (`main`, output 0, input 0)
- Simplify Tracks informations → Excluding logged tracks (`main`, output 0, input 1)
- Basic LLM Chain - AI Classification → Split Out1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 7 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0618_Splitout_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0618_Splitout_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
