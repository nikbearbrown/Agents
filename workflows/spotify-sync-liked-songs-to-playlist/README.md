# Spotify Sync Liked Songs to Playlist

This folder contains the **Spotify Sync Liked Songs to Playlist** workflow. Its executable nodes use `compareDatasets`, `filter`, `gotify`, `manualTrigger`, `merge`, `noOp`, `scheduleTrigger`, `set`, `sort`, `splitInBatches`, `spotify`, `summarize`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`spotify-sync-liked-songs-to-playlist.json`](spotify-sync-liked-songs-to-playlist.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Start, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Start | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Sort first added to first item | `sort` | Inspect parameters |
| Gotify Send deleted n from x | `gotify` | Inspect parameters |
| Loop delete old | `splitInBatches` | Inspect parameters |
| Spotify delete old | `spotify` | playlist / delete |
| Edit set Vars | `set` | Inspect parameters |
| Edit success to del | `set` | Inspect parameters |
| Filter Playlist x | `filter` | Inspect parameters |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| count added | `summarize` | Inspect parameters |
| Loop add missing | `splitInBatches` | Inspect parameters |
| Spotify add Missing to x | `spotify` | playlist |
| Edit snapshot to added | `set` | Inspect parameters |
| Cound deleted | `summarize` | Inspect parameters |
| Sort | `sort` | Inspect parameters |
| Set pluri | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Gotify | `gotify` | Inspect parameters |
| Edit set intern vars | `set` | Inspect parameters |
| END | `noOp` | Inspect parameters |
| Spotify get Liked Songs | `spotify` | library |
| Spotify get all playlists | `spotify` | playlist / getUserPlaylists |
| Spotify get Tracks of X | `spotify` | playlist / getTracks |

## Connection map

- Sort → Compare Datasets (`main`, output 0, input 1)
- Merge → Compare Datasets (`main`, output 0, input 0)
- Start → Edit set Vars (`main`, output 0, input 0)
- Set pluri → Spotify get Tracks of X (`main`, output 0, input 0)
- Set pluri → Merge (`main`, output 0, input 1)
- count added → Gotify (`main`, output 0, input 0)
- Cound deleted → Gotify Send deleted n from x (`main`, output 0, input 0)
- Edit set Vars → Edit set intern vars (`main`, output 0, input 0)
- Loop delete old → Edit success to del (`main`, output 0, input 0)
- Loop delete old → Spotify delete old (`main`, output 1, input 0)
- Compare Datasets → Loop add missing (`main`, output 0, input 0)
- Compare Datasets → END (`main`, output 1, input 0)
- Compare Datasets → END (`main`, output 2, input 0)
- Compare Datasets → Loop delete old (`main`, output 3, input 0)
- Loop add missing → Edit snapshot to added (`main`, output 0, input 0)
- Loop add missing → Spotify add Missing to x (`main`, output 1, input 0)
- Schedule Trigger → Edit set Vars (`main`, output 0, input 0)
- Filter Playlist x → Set pluri (`main`, output 0, input 0)
- Spotify delete old → Loop delete old (`main`, output 0, input 0)
- Edit success to del → Cound deleted (`main`, output 0, input 0)
- Edit set intern vars → Spotify get Liked Songs (`main`, output 0, input 0)
- Edit set intern vars → Spotify get all playlists (`main`, output 0, input 0)
- Edit snapshot to added → count added (`main`, output 0, input 0)
- Spotify get Liked Songs → Sort first added to first item (`main`, output 0, input 0)
- Spotify get Tracks of X → Sort (`main`, output 0, input 0)
- Spotify add Missing to x → Loop add missing (`main`, output 0, input 0)
- Spotify get all playlists → Filter Playlist x (`main`, output 0, input 0)
- Sort first added to first item → Merge (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1867_Schedule_Filter_Sync_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/1867_Schedule_Filter_Sync_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
