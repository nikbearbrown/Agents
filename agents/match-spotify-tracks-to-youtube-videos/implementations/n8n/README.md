# Match Spotify Tracks to YouTube Videos

This folder contains the **Match Spotify Tracks to YouTube Videos** workflow. Its executable nodes use `aggregate`, `compareDatasets`, `discord`, `if`, `noOp`, `removeDuplicates`, `scheduleTrigger`, `set`, `splitInBatches`, `spotify`, `supabase`, `wait`, `youTube`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`match-spotify-tracks-to-youtube-videos.json`](match-spotify-tracks-to-youtube-videos.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Every day at noon, Every day at noon + 1mn, Every hour, Every day at midnight, Every month

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get playlist snapshot | `spotify` | playlist / get |
| Get playlist snapshot1 | `spotify` | playlist / get |
| If different snapshot | `if` | Inspect parameters |
| Get all musics | `supabase` | getAll |
| Update to_delete to true | `supabase` | update |
| Add music | `supabase` | Inspect parameters |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Spotify | `spotify` | playlist / getTracks |
| No Operation, do nothing | `noOp` | Inspect parameters |
| Get all musics not in youtube playlist | `supabase` | getAll |
| Every day at noon | `scheduleTrigger` | Inspect parameters |
| Every day at noon + 1mn | `scheduleTrigger` | Inspect parameters |
| Every hour | `scheduleTrigger` | Inspect parameters |
| Wait 1 hour | `wait` | Inspect parameters |
| variables | `set` | Inspect parameters |
| Search video | `youTube` | video |
| Get video duration | `youTube` | video / get |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| If video duration ~= music duration | `if` | Inspect parameters |
| Add music to playlist | `youTube` | playlistItem |
| Add youtube id to row | `supabase` | update |
| Discord | `discord` | Inspect parameters |
| Discord1 | `discord` | Inspect parameters |
| Set youtube id to NOTFOUND if no matching | `supabase` | update |
| Aggregate | `aggregate` | Inspect parameters |
| If no result | `if` | Inspect parameters |
| data | `set` | Inspect parameters |
| variables2 | `set` | Inspect parameters |
| variables1 | `set` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| data1 | `set` | Inspect parameters |
| Get playlist items | `youTube` | playlistItem / getAll |
| Playlist items to be deleted | `compareDatasets` | Inspect parameters |
| Get all musics that should be in playlist | `supabase` | getAll |
| Remove Duplicates | `removeDuplicates` | Inspect parameters |
| Remove video from playlist | `youTube` | playlistItem / delete |
| Check for deleted videos | `compareDatasets` | Inspect parameters |
| Set youtube_video_id to null | `supabase` | update |
| Get all musics to be deleted | `supabase` | getAll |
| Delete music | `supabase` | delete |
| Every day at midnight | `scheduleTrigger` | Inspect parameters |
| variables3 | `set` | Inspect parameters |
| Reset NOTFOUND id to NULL | `supabase` | update |
| variables4 | `set` | Inspect parameters |
| Every month | `scheduleTrigger` | Inspect parameters |

## Connection map

- data → Loop Over Items1 (`main`, output 0, input 0)
- data1 → Search video (`main`, output 0, input 0)
- Spotify → Compare Datasets (`main`, output 0, input 0)
- Add music → data (`main`, output 0, input 0)
- Aggregate → Set youtube id to NOTFOUND if no matching (`main`, output 0, input 0)
- variables → Get playlist snapshot (`main`, output 0, input 0)
- Every hour → variables (`main`, output 0, input 0)
- variables1 → Get all musics not in youtube playlist (`main`, output 0, input 0)
- variables2 → Spotify (`main`, output 0, input 0)
- variables2 → Get all musics (`main`, output 0, input 0)
- variables3 → Get all musics that should be in playlist (`main`, output 0, input 0)
- variables3 → Get playlist items (`main`, output 0, input 0)
- variables3 → Get all musics to be deleted (`main`, output 0, input 0)
- variables4 → Reset NOTFOUND id to NULL (`main`, output 0, input 0)
- Every month → variables4 (`main`, output 0, input 0)
- Wait 1 hour → Get playlist snapshot1 (`main`, output 0, input 0)
- If no result → Aggregate (`main`, output 0, input 0)
- If no result → Loop Over Items (`main`, output 1, input 0)
- Search video → If no result (`main`, output 0, input 0)
- Get all musics → Compare Datasets (`main`, output 0, input 1)
- Loop Over Items → Aggregate (`main`, output 0, input 0)
- Loop Over Items → Get video duration (`main`, output 1, input 0)
- Compare Datasets → Add music (`main`, output 0, input 0)
- Compare Datasets → Update to_delete to true (`main`, output 3, input 0)
- Loop Over Items1 → data1 (`main`, output 1, input 0)
- Every day at noon → variables2 (`main`, output 0, input 0)
- Remove Duplicates → Remove video from playlist (`main`, output 0, input 0)
- Get playlist items → Playlist items to be deleted (`main`, output 0, input 0)
- Get playlist items → Check for deleted videos (`main`, output 0, input 1)
- Get video duration → If video duration ~= music duration (`main`, output 0, input 0)
- Add music to playlist → Add youtube id to row (`main`, output 0, input 0)
- Add youtube id to row → Loop Over Items1 (`main`, output 0, input 0)
- Add youtube id to row → Discord (`main`, output 0, input 0)
- Every day at midnight → variables3 (`main`, output 0, input 0)
- Get playlist snapshot → Wait 1 hour (`main`, output 0, input 0)
- If different snapshot → Spotify (`main`, output 0, input 0)
- If different snapshot → Get all musics (`main`, output 0, input 0)
- If different snapshot → No Operation, do nothing (`main`, output 1, input 0)
- Get playlist snapshot1 → If different snapshot (`main`, output 0, input 0)
- Every day at noon + 1mn → variables1 (`main`, output 0, input 0)
- Check for deleted videos → Set youtube_video_id to null (`main`, output 0, input 0)
- Remove video from playlist → Delete music (`main`, output 0, input 0)
- Get all musics to be deleted → Playlist items to be deleted (`main`, output 0, input 1)
- Playlist items to be deleted → Remove Duplicates (`main`, output 2, input 0)
- If video duration ~= music duration → Add music to playlist (`main`, output 0, input 0)
- If video duration ~= music duration → Loop Over Items (`main`, output 1, input 0)
- Get all musics not in youtube playlist → data (`main`, output 0, input 0)
- Get all musics that should be in playlist → Check for deleted videos (`main`, output 0, input 0)
- Set youtube id to NOTFOUND if no matching → Loop Over Items1 (`main`, output 0, input 0)
- Set youtube id to NOTFOUND if no matching → Discord1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0715_Wait_Schedule_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0715_Wait_Schedule_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
