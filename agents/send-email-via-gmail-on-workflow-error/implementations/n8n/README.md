# send email via gmail on workflow error

This folder contains the **send email via gmail on workflow error** workflow. Its executable nodes use `if`, `merge`, `scheduleTrigger`, `spotify`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-email-via-gmail-on-workflow-error.json`](send-email-via-gmail-on-workflow-error.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `spotifyOAuth2Api`

**Entry nodes:** CRON

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| CRON | `scheduleTrigger` | Inspect parameters |
| Get User's Playlists | `spotify` | playlist / getUserPlaylists |
| Switch | `switch` | Inspect parameters |
| Get Discover Tracks | `spotify` | playlist / getTracks |
| Get Archive Tracks | `spotify` | playlist / getTracks |
| Merge | `merge` | Inspect parameters |
| Check if tracks to add is NOT empty | `if` | Inspect parameters |
| Add tracks to Archive playlist | `spotify` | playlist |

## Connection map

- CRON → Get User's Playlists (`main`, output 0, input 0)
- Merge → Check if tracks to add is NOT empty (`main`, output 0, input 0)
- Switch → Get Discover Tracks (`main`, output 0, input 0)
- Switch → Get Archive Tracks (`main`, output 1, input 0)
- Get Archive Tracks → Merge (`main`, output 0, input 1)
- Get Discover Tracks → Merge (`main`, output 0, input 0)
- Get User's Playlists → Switch (`main`, output 0, input 0)
- Check if tracks to add is NOT empty → Add tracks to Archive playlist (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0382_Schedule_Spotify_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Schedule/0382_Schedule_Spotify_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
