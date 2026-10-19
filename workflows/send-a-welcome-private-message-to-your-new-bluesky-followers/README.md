# Send a welcome private message to your new BlueSky followers

This folder contains the **Send a welcome private message to your new BlueSky followers** workflow. Its executable nodes use `code`, `convertToFile`, `extractFromFile`, `httpRequest`, `noOp`, `readWriteFile`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`send-a-welcome-private-message-to-your-new-bluesky-followers.json`](send-a-welcome-private-message-to-your-new-bluesky-followers.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Each 60 minutes

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Create Session | `httpRequest` | POST |
| List followers | `httpRequest` | Inspect parameters |
| Convert to File | `convertToFile` | toJson |
| Extract from File | `extractFromFile` | fromJson |
| Split Out | `splitOut` | Inspect parameters |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Find new followers | `code` | Inspect parameters |
| Read followers from file | `readWriteFile` | Inspect parameters |
| Save followers to file | `readWriteFile` | write |
| Define welcome message | `set` | Inspect parameters |
| Send message | `httpRequest` | POST |
| Get conversation ID | `httpRequest` | Inspect parameters |
| Each 60 minutes | `scheduleTrigger` | Inspect parameters |
| No Operation, do nothing | `noOp` | Inspect parameters |

## Connection map

- Wait → Convert to File (`main`, output 0, input 0)
- Split Out → Loop Over Items (`main`, output 0, input 0)
- Send message → Loop Over Items (`main`, output 0, input 0)
- Create Session → List followers (`main`, output 0, input 0)
- List followers → Read followers from file (`main`, output 0, input 0)
- List followers → Wait (`main`, output 0, input 0)
- Convert to File → Save followers to file (`main`, output 0, input 0)
- Each 60 minutes → Create Session (`main`, output 0, input 0)
- Loop Over Items → Define welcome message (`main`, output 1, input 0)
- Extract from File → Find new followers (`main`, output 0, input 0)
- Find new followers → Split Out (`main`, output 0, input 0)
- Get conversation ID → Send message (`main`, output 0, input 0)
- Define welcome message → Get conversation ID (`main`, output 0, input 0)
- Save followers to file → No Operation, do nothing (`main`, output 0, input 0)
- Read followers from file → Extract from File (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0640_Wait_Splitout_Create_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/0640_Wait_Splitout_Create_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
