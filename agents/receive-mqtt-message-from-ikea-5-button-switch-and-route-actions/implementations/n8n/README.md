# Receive MQTT message from IKEA 5-button Switch, and route actions.

This folder contains the **Receive MQTT message from IKEA 5-button Switch, and route actions.** workflow. Its executable nodes use `filter`, `httpRequest`, `if`, `mqttTrigger`, `noOp`, `set`, `splitOut`, `spotify`, `switch`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-mqtt-message-from-ikea-5-button-switch-and-route-actions.json`](receive-mqtt-message-from-ikea-5-button-switch-and-route-actions.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mqtt`, `spotifyOAuth2Api`

**Entry nodes:** MQTT Trigger - Remote Switch

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Spotify Next | `spotify` | nextSong |
| Spotify Resume | `spotify` | resume |
| Spotify Pause | `spotify` | pause |
| Spotify API - Volume up 5pct | `httpRequest` | PUT |
| Spotify API - Volume down 5pct | `httpRequest` | PUT |
| Spotify API - Get Available Devices | `httpRequest` | Inspect parameters |
| Extract Individual Devices | `splitOut` | Inspect parameters |
| Select Device by Name to get device_id | `filter` | Inspect parameters |
| Custom Function 1 - P1 | `httpRequest` | PUT |
| Custom Function 2 - P2 | `spotify` | Inspect parameters |
| Custom Function 1 - P3 | `spotify` | nextSong |
| Spotify API - Activate Target Playback Device | `httpRequest` | PUT |
| Route to Requested Function | `switch` | Inspect parameters |
| Custom Function 2 - P1 | `spotify` | playlist / getUserPlaylists |
| Filter | `filter` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Custom Function 2 - P3 | `spotify` | startMusic |
| Oops. How was this reached? | `noOp` | Inspect parameters |
| Spotify API - Get Device Status | `httpRequest` | Inspect parameters |
| Already playing on Target Device? | `if` | Inspect parameters |
| Is Playing? | `if` | Inspect parameters |
| Spotify Prev | `spotify` | previousSong |
| MQTT Trigger - Remote Switch | `mqttTrigger` | Inspect parameters |
| Remote Action -> Function Router | `switch` | Inspect parameters |

## Connection map

- Filter → Custom Function 2 - P3 (`main`, output 0, input 0)
- Globals → Remote Action -> Function Router (`main`, output 0, input 0)
- Is Playing? → Spotify Pause (`main`, output 0, input 0)
- Is Playing? → Spotify Resume (`main`, output 1, input 0)
- Custom Function 1 - P1 → Custom Function 2 - P2 (`main`, output 0, input 0)
- Custom Function 2 - P1 → Filter (`main`, output 0, input 0)
- Custom Function 2 - P2 → Custom Function 1 - P3 (`main`, output 0, input 0)
- Extract Individual Devices → Select Device by Name to get device_id (`main`, output 0, input 0)
- Route to Requested Function → Spotify API - Volume up 5pct (`main`, output 0, input 0)
- Route to Requested Function → Spotify API - Volume down 5pct (`main`, output 1, input 0)
- Route to Requested Function → Is Playing? (`main`, output 2, input 0)
- Route to Requested Function → Custom Function 1 - P1 (`main`, output 3, input 0)
- Route to Requested Function → Custom Function 2 - P1 (`main`, output 4, input 0)
- Route to Requested Function → Oops. How was this reached? (`main`, output 5, input 0)
- Spotify API - Get Device Status → Already playing on Target Device? (`main`, output 0, input 0)
- Remote Action -> Function Router → Spotify Prev (`main`, output 0, input 0)
- Remote Action -> Function Router → Spotify Next (`main`, output 1, input 0)
- Remote Action -> Function Router → Spotify API - Get Device Status (`main`, output 2, input 0)
- Remote Action -> Function Router → Spotify API - Get Device Status (`main`, output 3, input 0)
- Remote Action -> Function Router → Spotify API - Get Device Status (`main`, output 4, input 0)
- Remote Action -> Function Router → Spotify API - Get Device Status (`main`, output 5, input 0)
- Remote Action -> Function Router → Spotify API - Get Device Status (`main`, output 6, input 0)
- Already playing on Target Device? → Route to Requested Function (`main`, output 0, input 0)
- Already playing on Target Device? → Spotify API - Get Available Devices (`main`, output 1, input 0)
- MQTT Trigger - Ikea Remote Switch → Globals (`main`, output 0, input 0)
- Spotify API - Get Available Devices → Extract Individual Devices (`main`, output 0, input 0)
- Select Device by Name to get device_id → Spotify API - Activate Target Playback Device (`main`, output 0, input 0)
- Spotify API - Activate Target Playback Device → Route to Requested Function (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"missing_connection_source": 1, "stale_literal_reference": 6}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0560_Splitout_Filter_Import_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0560_Splitout_Filter_Import_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
