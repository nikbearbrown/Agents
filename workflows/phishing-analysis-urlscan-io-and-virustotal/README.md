# Phishing_analysis__URLScan_io_and_Virustotal_

This folder contains the **Phishing_analysis__URLScan_io_and_Virustotal_** workflow. Its executable nodes use `code`, `filter`, `httpRequest`, `if`, `manualTrigger`, `merge`, `microsoftOutlook`, `scheduleTrigger`, `slack`, `splitInBatches`, `urlScanIo`, `wait`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`phishing-analysis-urlscan-io-and-virustotal.json`](phishing-analysis-urlscan-io-and-virustotal.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftOutlookOAuth2Api`, `slackApi`, `urlScanIoApi`, `virusTotalApi`

**Entry nodes:** When clicking "Execute Workflow", Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When clicking "Execute Workflow" | `manualTrigger` | Inspect parameters |
| sends slack message | `slack` | Inspect parameters |
| Split In Batches | `splitInBatches` | Inspect parameters |
| Mark as read | `microsoftOutlook` | update |
| VirusTotal: Scan URL | `httpRequest` | POST |
| VirusTotal: Get report | `httpRequest` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Find indicators of compromise | `code` | Inspect parameters |
| URLScan: Get report | `urlScanIo` | get |
| URLScan: Scan URL | `urlScanIo` | Inspect parameters |
| Has URL? | `if` | Inspect parameters |
| No error? | `if` | Inspect parameters |
| Not empty? | `filter` | Inspect parameters |
| Wait 1 Minute | `wait` | Inspect parameters |
| Get all unread messages | `microsoftOutlook` | getAll |
| Merge Reports | `merge` | Inspect parameters |

## Connection map

- Has URL? → URLScan: Scan URL (`main`, output 0, input 0)
- Has URL? → VirusTotal: Scan URL (`main`, output 0, input 0)
- Has URL? → Split In Batches (`main`, output 1, input 0)
- No error? → Merge Reports (`main`, output 0, input 0)
- No error? → Wait 1 Minute (`main`, output 1, input 0)
- Not empty? → sends slack message (`main`, output 0, input 0)
- Mark as read → Split In Batches (`main`, output 0, input 0)
- Merge Reports → Split In Batches (`main`, output 0, input 0)
- Wait 1 Minute → URLScan: Get report (`main`, output 0, input 0)
- Schedule Trigger → Get all unread messages (`main`, output 0, input 0)
- Split In Batches → Find indicators of compromise (`main`, output 0, input 0)
- Split In Batches → Not empty? (`main`, output 1, input 0)
- URLScan: Scan URL → No error? (`main`, output 0, input 0)
- URLScan: Get report → Merge Reports (`main`, output 0, input 0)
- VirusTotal: Scan URL → VirusTotal: Get report (`main`, output 0, input 0)
- VirusTotal: Get report → Merge Reports (`main`, output 0, input 1)
- Get all unread messages → Mark as read (`main`, output 0, input 0)
- Find indicators of compromise → Has URL? (`main`, output 0, input 0)
- When clicking "Execute Workflow" → Get all unread messages (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{"stale_literal_reference": 5}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1600_Wait_Code_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Wait/1600_Wait_Code_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
