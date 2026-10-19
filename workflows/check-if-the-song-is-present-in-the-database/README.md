# Check if the song is present in the database

This folder contains the **Check if the song is present in the database** workflow. Its executable nodes use `code`, `filter`, `if`, `merge`, `noOp`, `nocoDb`, `scheduleTrigger`, `splitInBatches`, `spotify`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`check-if-the-song-is-present-in-the-database.json`](check-if-the-song-is-present-in-the-database.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `nocoDbApiToken`, `spotifyOAuth2Api`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get current date | `code` | Inspect parameters |
| Get last 10 liked tracks | `spotify` | library |
| Check if track is saved | `nocoDb` | getAll |
| Is not saved | `if` | Inspect parameters |
| Create song entry | `nocoDb` | create |
| Get all user playlist | `spotify` | playlist / getUserPlaylists |
| Get monthly playlist | `filter` | Inspect parameters |
| Get playlist in DB | `nocoDb` | getAll |
| Monthly playlist exist in Spotify ? | `if` | Inspect parameters |
| Playlist exist  in DB ? | `if` | Inspect parameters |
| Create playlist in Spotify | `spotify` | playlist / create |
| Create playlist in DB1 | `nocoDb` | create |
| Create playlist in DB | `nocoDb` | create |
| Merge | `merge` | Inspect parameters |
| Clean op | `noOp` | Inspect parameters |
| Clean op2 | `noOp` | Inspect parameters |
| Get this month playlist in DB | `nocoDb` | getAll |
| Get this month tracks in DB | `nocoDb` | getAll |
| Add song to the playlist | `spotify` | playlist |
| For each tracks in liked song | `splitInBatches` | Inspect parameters |
| For each monthly tracks in DB | `splitInBatches` | Inspect parameters |
| Get this month tracks in Spotify | `spotify` | playlist / getTracks |
| Filter1 | `filter` | Inspect parameters |
| Song is not present in the playlist ? | `if` | Inspect parameters |
| Clean op1 | `noOp` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| End | `noOp` | Inspect parameters |

## Connection map

- Merge → Get this month playlist in DB (`main`, output 0, input 0)
- Filter1 → Song is not present in the playlist ? (`main`, output 0, input 0)
- Clean op → Merge (`main`, output 0, input 0)
- Clean op1 → For each monthly tracks in DB (`main`, output 0, input 0)
- Clean op2 → For each tracks in liked song (`main`, output 0, input 0)
- Is not saved → Create song entry (`main`, output 0, input 0)
- Is not saved → Clean op2 (`main`, output 1, input 0)
- Get current date → Get all user playlist (`main`, output 0, input 0)
- Get current date → Get last 10 liked tracks (`main`, output 0, input 0)
- Schedule Trigger → Get current date (`main`, output 0, input 0)
- Create song entry → Clean op2 (`main`, output 0, input 0)
- Get playlist in DB → Playlist exist  in DB ? (`main`, output 0, input 0)
- Get monthly playlist → Monthly playlist exist in Spotify ? (`main`, output 0, input 0)
- Create playlist in DB → Clean op (`main`, output 0, input 0)
- Get all user playlist → Get monthly playlist (`main`, output 0, input 0)
- Create playlist in DB1 → Clean op (`main`, output 0, input 0)
- Check if track is saved → Is not saved (`main`, output 0, input 0)
- Playlist exist  in DB ? → Clean op (`main`, output 0, input 0)
- Playlist exist  in DB ? → Create playlist in DB (`main`, output 1, input 0)
- Add song to the playlist → Clean op1 (`main`, output 0, input 0)
- Get last 10 liked tracks → For each tracks in liked song (`main`, output 0, input 0)
- Create playlist in Spotify → Create playlist in DB1 (`main`, output 0, input 0)
- Get this month tracks in DB → For each monthly tracks in DB (`main`, output 0, input 0)
- For each monthly tracks in DB → End (`main`, output 0, input 0)
- For each monthly tracks in DB → Get this month tracks in Spotify (`main`, output 1, input 0)
- For each tracks in liked song → Merge (`main`, output 0, input 1)
- For each tracks in liked song → Check if track is saved (`main`, output 1, input 0)
- Get this month playlist in DB → Get this month tracks in DB (`main`, output 0, input 0)
- Get this month tracks in Spotify → Filter1 (`main`, output 0, input 0)
- Monthly playlist exist in Spotify ? → Get playlist in DB (`main`, output 0, input 0)
- Monthly playlist exist in Spotify ? → Create playlist in Spotify (`main`, output 1, input 0)
- Song is not present in the playlist ? → Add song to the playlist (`main`, output 0, input 0)
- Song is not present in the playlist ? → Clean op1 (`main`, output 1, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0034_Code_Filter_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0034_Code_Filter_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
