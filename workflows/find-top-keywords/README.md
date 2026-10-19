# Find Top Keywords

This folder contains the **Find Top Keywords** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `if`, `manualTrigger`, `nocoDb`, `scheduleTrigger`, `splitInBatches`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`find-top-keywords.json`](find-top-keywords.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `httpBasicAuth`, `httpHeaderAuth`, `nocoDbApiToken`

**Entry nodes:** When clicking ‘Test workflow’, Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking ‘Test workflow’ | `manualTrigger` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Gen Time | `code` | Inspect parameters |
| NocoDB | `nocoDb` | getAll |
| Second Order Google Autocomplete Keywords | `httpRequest` | Inspect parameters |
| Google Search Volume | `httpRequest` | POST |
| Split Out Google Search | `splitOut` | Inspect parameters |
| YouTube Search Volume | `httpRequest` | POST |
| Second Order YouTube Autocomplete Keywords | `httpRequest` | Inspect parameters |
| Split Out YT Search | `splitOut` | Inspect parameters |
| Google Filter | `filter` | Inspect parameters |
| YT Filter | `filter` | Inspect parameters |
| Add Second Tier YT Keyword Data | `nocoDb` | create |
| Add Second Tier G Keyword Data | `nocoDb` | create |
| Format G Data | `code` | Inspect parameters |
| Format YT Data | `code` | Inspect parameters |
| Bulk Import G Monthly Search Volume | `httpRequest` | POST |
| Bulk Import YT Monthly Search Volume | `httpRequest` | POST |
| Is Google Keyword Available | `if` | Inspect parameters |
| Is YT Keyword Avaliable | `if` | Inspect parameters |
| Check for Google Keyword | `httpRequest` | Inspect parameters |
| Check for YT Keyword | `httpRequest` | Inspect parameters |
| Loop Over YT Keywords | `splitInBatches` | Inspect parameters |
| Update Second Tier G Keyword Data | `nocoDb` | update |
| Update Second Tier YT Keyword Data | `nocoDb` | update |
| Loop Over Google Keywords | `splitInBatches` | Inspect parameters |
| Combine G Keywords and Filter | `code` | Inspect parameters |
| Combine YT Keywords and Filter | `code` | Inspect parameters |

## Connection map

- NocoDB → Second Order YouTube Autocomplete Keywords (`main`, output 0, input 0)
- NocoDB → Second Order Google Autocomplete Keywords (`main`, output 0, input 0)
- Gen Time → NocoDB (`main`, output 0, input 0)
- YT Filter → Loop Over YT Keywords (`main`, output 0, input 0)
- Format G Data → Bulk Import G Monthly Search Volume (`main`, output 0, input 0)
- Google Filter → Loop Over Google Keywords (`main`, output 0, input 0)
- Format YT Data → Bulk Import YT Monthly Search Volume (`main`, output 0, input 0)
- Schedule Trigger → Gen Time (`main`, output 0, input 0)
- Split Out YT Search → YT Filter (`main`, output 0, input 0)
- Check for YT Keyword → Is YT Keyword Avaliable (`main`, output 0, input 0)
- Google Search Volume → Split Out Google Search (`main`, output 0, input 0)
- Loop Over YT Keywords → Check for YT Keyword (`main`, output 1, input 0)
- YouTube Search Volume → Split Out YT Search (`main`, output 0, input 0)
- Is YT Keyword Avaliable → Add Second Tier YT Keyword Data (`main`, output 0, input 0)
- Is YT Keyword Avaliable → Update Second Tier YT Keyword Data (`main`, output 1, input 0)
- Split Out Google Search → Google Filter (`main`, output 0, input 0)
- Check for Google Keyword → Is Google Keyword Available (`main`, output 0, input 0)
- Loop Over Google Keywords → Check for Google Keyword (`main`, output 1, input 0)
- Is Google Keyword Available → Add Second Tier G Keyword Data (`main`, output 0, input 0)
- Is Google Keyword Available → Update Second Tier G Keyword Data (`main`, output 1, input 0)
- Combine G Keywords and Filter → Google Search Volume (`main`, output 0, input 0)
- Add Second Tier G Keyword Data → Format G Data (`main`, output 0, input 0)
- Combine YT Keywords and Filter → YouTube Search Volume (`main`, output 0, input 0)
- Add Second Tier YT Keyword Data → Format YT Data (`main`, output 0, input 0)
- Update Second Tier G Keyword Data → Loop Over Google Keywords (`main`, output 0, input 0)
- When clicking ‘Test workflow’ → Gen Time (`main`, output 0, input 0)
- Update Second Tier YT Keyword Data → Loop Over YT Keywords (`main`, output 0, input 0)
- Bulk Import G Monthly Search Volume → Loop Over Google Keywords (`main`, output 0, input 0)
- Bulk Import YT Monthly Search Volume → Loop Over YT Keywords (`main`, output 0, input 0)
- Second Order Google Autocomplete Keywords → Combine G Keywords and Filter (`main`, output 0, input 0)
- Second Order YouTube Autocomplete Keywords → Combine YT Keywords and Filter (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1642_Splitout_Code_Automation_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1642_Splitout_Code_Automation_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
