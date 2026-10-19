# Retrieve the playlists you want to synchronise

This folder contains the **Retrieve the playlists you want to synchronise** workflow. Its executable nodes use `compareDatasets`, `manualTrigger`, `set`, `splitInBatches`, `spotify`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`retrieve-the-playlists-you-want-to-synchronise.json`](retrieve-the-playlists-you-want-to-synchronise.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `spotifyOAuth2Api`, `youTubeOAuth2Api`

**Entry nodes:** When clicking ‘Test workflow’

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Compare the two Datasets | `compareDatasets` | Inspect parameters |
| Extract the spotify track ID | `set` | Inspect parameters |
| Extract the Spotify Track ID | `set` | Inspect parameters |
| Find the returned tracks on Spotify | `spotify` | track / search |
| Get my tracks inside my playlist | `youTube` | playlistItem / getAll |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Get tracks inside the Spotify Playlist | `spotify` | playlist / getTracks |
| Add tracks not already in playlist | `spotify` | playlist |

## Connection map

- Loop Over Items → Extract the Spotify Track ID (`main`, output 0, input 0)
- Loop Over Items → Find the returned tracks on Spotify (`main`, output 1, input 0)
- Compare the two Datasets → Add tracks not already in playlist (`main`, output 3, input 0)
- Extract the Spotify Track ID → Compare the two Datasets (`main`, output 0, input 1)
- Extract the spotify track ID → Compare the two Datasets (`main`, output 0, input 0)
- Get my tracks inside my playlist → Loop Over Items (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get my tracks inside my playlist (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Get tracks inside the Spotify Playlist (`main`, output 0, input 0)
- Find the returned tracks on Spotify → Loop Over Items (`main`, output 0, input 0)
- Get tracks inside the Spotify Playlist → Extract the spotify track ID (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Comparedatasets/0623_Comparedatasets_Manual_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Comparedatasets/0623_Comparedatasets_Manual_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
