# n8n Subworkflow Dependency Graph & Auto-Tagging

This folder contains the **n8n Subworkflow Dependency Graph & Auto-Tagging** workflow. Its executable nodes use `aggregate`, `code`, `filter`, `httpRequest`, `if`, `merge`, `n8n`, `n8nTrigger`, `quickChart`, `respondToWebhook`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`workflow-dependency-graph.json`](workflow-dependency-graph.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `n8nApi`

**Entry nodes:** And every Sunday, When this workflow is activated, When viewed in a browser

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Update workflow tags | `httpRequest` | PUT |
| GET all workflows | `n8n` | Inspect parameters |
| List callers of subworkflows | `code` | Inspect parameters |
| Exclude uncalled workflows | `filter` | Inspect parameters |
| Exclude missing workflows | `filter` | Inspect parameters |
| And every Sunday | `scheduleTrigger` | Inspect parameters |
| When this workflow is activated | `n8nTrigger` | Inspect parameters |
| GET workflow(s) | `n8n` | get |
| Count callers and identify new callers | `set` | Inspect parameters |
| Loop through workflows | `splitInBatches` | Inspect parameters |
| GET all tags | `httpRequest` | Inspect parameters |
| Remove existing tags from new_callers list | `set` | Inspect parameters |
| If any new callers | `if` | Inspect parameters |
| Split out new callers as new tags | `splitOut` | Inspect parameters |
| Create new tags | `httpRequest` | POST |
| Return original pass through values | `code` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| GET all tags again | `httpRequest` | Inspect parameters |
| Create tag id:name dictionary | `set` | Inspect parameters |
| Retrieve tag ids and names from dictionary | `set` | Inspect parameters |
| Return dependency graph data | `set` | Inspect parameters |
| Combine dependency graph values into labels | `aggregate` | Inspect parameters |
| Visualize subworkflow dependency graph | `quickChart` | Inspect parameters |
| SET instance_url | `set` | Inspect parameters |
| When viewed in a browser | `webhook` | Inspect parameters |
| Format workflow relationship data for rendering | `code` | Inspect parameters |
| Visualize dependency graph with MermaidJS | `respondToWebhook` | Inspect parameters |

## Connection map

- Merge → GET all tags again (`main`, output 0, input 0)
- GET all tags → Remove existing tags from new_callers list (`main`, output 0, input 0)
- Create new tags → Return original pass through values (`main`, output 0, input 0)
- GET workflow(s) → Exclude missing workflows (`main`, output 0, input 0)
- And every Sunday → GET all workflows (`main`, output 0, input 0)
- SET instance_url → GET all tags (`main`, output 0, input 0)
- GET all workflows → List callers of subworkflows (`main`, output 0, input 0)
- GET all tags again → Create tag id:name dictionary (`main`, output 0, input 0)
- If any new callers → Split out new callers as new tags (`main`, output 0, input 0)
- If any new callers → Merge (`main`, output 1, input 1)
- Update workflow tags → Return dependency graph data (`main`, output 0, input 0)
- Loop through workflows → Combine dependency graph values into labels (`main`, output 0, input 0)
- Loop through workflows → Format workflow relationship data for rendering (`main`, output 0, input 0)
- Loop through workflows → SET instance_url (`main`, output 1, input 0)
- When viewed in a browser → GET all workflows (`main`, output 0, input 0)
- Exclude missing workflows → Count callers and identify new callers (`main`, output 0, input 0)
- Exclude uncalled workflows → GET workflow(s) (`main`, output 0, input 0)
- List callers of subworkflows → Exclude uncalled workflows (`main`, output 0, input 0)
- Return dependency graph data → Loop through workflows (`main`, output 0, input 0)
- Create tag id:name dictionary → Retrieve tag ids and names from dictionary (`main`, output 0, input 0)
- When this workflow is activated → GET all workflows (`main`, output 0, input 0)
- Split out new callers as new tags → Create new tags (`main`, output 0, input 0)
- Return original pass through values → Merge (`main`, output 0, input 0)
- Count callers and identify new callers → Loop through workflows (`main`, output 0, input 0)
- Remove existing tags from new_callers list → If any new callers (`main`, output 0, input 0)
- Retrieve tag ids and names from dictionary → Update workflow tags (`main`, output 0, input 0)
- Combine dependency graph values into labels → Visualize subworkflow dependency graph (`main`, output 0, input 0)
- Format workflow relationship data for rendering → Visualize dependency graph with MermaidJS (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1591_Splitout_Code_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/1591_Splitout_Code_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
