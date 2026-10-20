# Material Issue Request and Approval

This folder contains the **Material Issue Request and Approval** workflow. Its executable nodes use `code`, `gmail`, `googleSheets`, `if`, `itemLists`, `merge`, `set`, `supabase`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`material-issue-request-and-approval.json`](material-issue-request-and-approval.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** None declared. HTTP requests or Code nodes may still require configuration.

**Entry nodes:** Get Approvals, Receive Issue Request, Receive Raw Materials Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Append Material Request | `googleSheets` | append |
| Get Approvals | `webhook` | Inspect parameters |
| Standardize Data | `set` | Inspect parameters |
| Update Stock | `code` | Inspect parameters |
| Receive Issue Request | `webhook` | Inspect parameters |
| Send Approval Request | `gmail` | Inspect parameters |
| Prepare Approval | `code` | Inspect parameters |
| Create Record Issue | `supabase` | Inspect parameters |
| Search Product ID | `supabase` | getAll |
| Searck Issues | `supabase` | getAll |
| Update Current Stck | `supabase` | update |
| Merge Lookups | `merge` | Inspect parameters |
| Update Current Stock1 | `googleSheets` | update |
| LookUp Current stock1 | `googleSheets` | Inspect parameters |
| Low stock Detection1 | `code` | Inspect parameters |
| Merge1 | `merge` | Inspect parameters |
| Append Raw Materials | `googleSheets` | append |
| Calculate Total Price | `code` | Inspect parameters |
| Calculate Updated Current Stock | `code` | Inspect parameters |
| Validate Quantity Received | `code` | Inspect parameters |
| Initialize New Product stock | `googleSheets` | append |
| Update Current Stock | `googleSheets` | update |
| LookUp Current stock | `googleSheets` | Inspect parameters |
| New Row Current Stock | `supabase` | Inspect parameters |
| Current Stock Update | `supabase` | update |
| Search Current Stock | `supabase` | getAll |
| Format response | `itemLists` | removeDuplicates |
| Merge | `merge` | Inspect parameters |
| Low stock Detection2 | `code` | Inspect parameters |
| Receive Raw Materials Webhook | `webhook` | Inspect parameters |
| Standardize Raw Material Data | `set` | Inspect parameters |
| Lookup Existing Stock | `googleSheets` | Inspect parameters |
| Check If Product ID Exists | `if` | Inspect parameters |
| New Record Row | `supabase` | Inspect parameters |
| Trigger Low Stock Alert | `if` | Inspect parameters |
| Send Low Stock Email Alert | `gmail` | Inspect parameters |
| Low Stock Email Alert | `gmail` | Inspect parameters |
| Validate Issue Request Data | `code` | Inspect parameters |
| Verify Requested Quantity | `code` | Inspect parameters |
| Check Available Stock for Issue | `googleSheets` | Inspect parameters |
| Format Approval Response | `set` | Inspect parameters |
| Verify Approval Data | `code` | Inspect parameters |
| Retrieve Issue Request Details | `googleSheets` | Inspect parameters |
| Process Approval Decision | `if` | Inspect parameters |
| Get Stock for Issue Update from Current | `googleSheets` | Inspect parameters |
| Update Stock After Issue | `googleSheets` | update |
| Materials Issue Table Update | `supabase` | update |
| Is Stock is Low | `if` | Inspect parameters |

## Connection map

- Merge → Check If Product ID Exists (`main`, output 0, input 0)
- Merge1 → Process Approval Decision (`main`, output 0, input 0)
- Update Stock → Update Current Stock1 (`main`, output 0, input 0)
- Update Stock → Update Current Stck (`main`, output 0, input 0)
- Get Approvals → Format Approval Response (`main`, output 0, input 0)
- Merge Lookups → Prepare Approval (`main`, output 0, input 0)
- Searck Issues → Merge1 (`main`, output 0, input 1)
- New Record Row → Search Current Stock (`main`, output 0, input 0)
- Format response → Initialize New Product stock (`main`, output 0, input 0)
- Format response → New Row Current Stock (`main`, output 0, input 0)
- Is Stock is Low → Low Stock Email Alert (`main`, output 0, input 0)
- Prepare Approval → Send Approval Request (`main`, output 0, input 0)
- Standardize Data → Validate Issue Request Data (`main`, output 0, input 0)
- Search Product ID → Merge Lookups (`main`, output 0, input 1)
- Create Record Issue → Search Product ID (`main`, output 0, input 0)
- Append Raw Materials → Validate Quantity Received (`main`, output 0, input 0)
- LookUp Current stock → Low stock Detection2 (`main`, output 0, input 0)
- Low stock Detection1 → Is Stock is Low (`main`, output 0, input 0)
- Low stock Detection2 → Trigger Low Stock Alert (`main`, output 0, input 0)
- Search Current Stock → Merge (`main`, output 0, input 0)
- Update Current Stock → LookUp Current stock (`main`, output 0, input 0)
- Verify Approval Data → Retrieve Issue Request Details (`main`, output 0, input 0)
- Verify Approval Data → Searck Issues (`main`, output 0, input 0)
- Calculate Total Price → Append Raw Materials (`main`, output 0, input 0)
- Calculate Total Price → New Record Row (`main`, output 0, input 0)
- LookUp Current stock1 → Low stock Detection1 (`main`, output 0, input 0)
- Lookup Existing Stock → Merge (`main`, output 0, input 0)
- Receive Issue Request → Standardize Data (`main`, output 0, input 0)
- Update Current Stock1 → LookUp Current stock1 (`main`, output 0, input 0)
- Append Material Request → Check Available Stock for Issue (`main`, output 0, input 0)
- Trigger Low Stock Alert → Send Low Stock Email Alert (`main`, output 0, input 0)
- Format Approval Response → Verify Approval Data (`main`, output 0, input 0)
- Process Approval Decision → Update Stock After Issue (`main`, output 0, input 0)
- Process Approval Decision → Materials Issue Table Update (`main`, output 0, input 0)
- Process Approval Decision → Get Stock for Issue Update from Current (`main`, output 0, input 0)
- Verify Requested Quantity → Append Material Request (`main`, output 0, input 0)
- Verify Requested Quantity → Create Record Issue (`main`, output 0, input 0)
- Check If Product ID Exists → Calculate Updated Current Stock (`main`, output 0, input 0)
- Check If Product ID Exists → Format response (`main`, output 1, input 0)
- Validate Quantity Received → Lookup Existing Stock (`main`, output 0, input 0)
- Validate Issue Request Data → Verify Requested Quantity (`main`, output 0, input 0)
- Receive Raw Materials Webhook → Standardize Raw Material Data (`main`, output 0, input 0)
- Standardize Raw Material Data → Calculate Total Price (`main`, output 0, input 0)
- Retrieve Issue Request Details → Merge1 (`main`, output 0, input 0)
- Calculate Updated Current Stock → Update Current Stock (`main`, output 0, input 0)
- Calculate Updated Current Stock → Current Stock Update (`main`, output 0, input 0)
- Check Available Stock for Issue → Merge Lookups (`main`, output 0, input 0)
- Get Stock for Issue Update from Current → Update Stock (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0926_Code_Webhook_Create_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0926_Code_Webhook_Create_Webhook.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
