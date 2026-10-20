# create playlist spotify and get liked tracks and aggregate

This folder contains the **create playlist spotify and get liked tracks and aggregate** workflow. Its executable nodes use `aggregate`, `code`, `filter`, `if`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `spotify`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`create-playlist-spotify-and-get-liked-tracks-and-aggregate.json`](create-playlist-spotify-and-get-liked-tracks-and-aggregate.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `spotifyOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| If no playlist | `if` | Inspect parameters |
| Create Downloads Playlist | `spotify` | playlist / create |
| Get Liked Tracks | `spotify` | library |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Split Out | `splitOut` | Inspect parameters |
| Add tracks to Downloads | `spotify` | playlist |
| Get Downloads Playlist | `spotify` | playlist / get |
| Filter out new tracks | `code` | Inspect parameters |
| Get tracks to remove | `code` | Inspect parameters |
| Remove oldest tracks from Downloads | `spotify` | playlist / delete |
| Filter out Downloads Playlist | `filter` | Inspect parameters |
| Get Updated Downloads Playlist | `spotify` | playlist / get |
| Get all Playlists | `spotify` | playlist / getUserPlaylists |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| If no Downloads Playlist found | `if` | Inspect parameters |
| Globals | `set` | Inspect parameters |

## Connection map

- Globals → Get all Playlists (`main`, output 0, input 0)
- Aggregate → If no Downloads Playlist found (`main`, output 0, input 0)
- Split Out → Filter out Downloads Playlist (`main`, output 0, input 0)
- If no playlist → Create Downloads Playlist (`main`, output 0, input 0)
- If no playlist → Aggregate (`main`, output 1, input 0)
- Loop Over Items → Get Updated Downloads Playlist (`main`, output 0, input 0)
- Loop Over Items → Add tracks to Downloads (`main`, output 1, input 0)
- Get Liked Tracks → Filter out new tracks (`main`, output 0, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- Get all Playlists → If no playlist (`main`, output 0, input 0)
- Get tracks to remove → Remove oldest tracks from Downloads (`main`, output 0, input 0)
- Filter out new tracks → Loop Over Items (`main`, output 0, input 0)
- Get Downloads Playlist → Get Liked Tracks (`main`, output 0, input 0)
- Add tracks to Downloads → Loop Over Items (`main`, output 0, input 0)
- Create Downloads Playlist → Get all Playlists (`main`, output 0, input 0)
- Filter out Downloads Playlist → Get Downloads Playlist (`main`, output 0, input 0)
- Get Updated Downloads Playlist → Get tracks to remove (`main`, output 0, input 0)
- If no Downloads Playlist found → Create Downloads Playlist (`main`, output 0, input 0)
- If no Downloads Playlist found → Split Out (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0503_Splitout_Code_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0503_Splitout_Code_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
