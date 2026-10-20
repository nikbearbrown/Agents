# search salesforce accounts and removeduplicates item lists and set account id for existing accounts 353b61b9

This folder contains the **search salesforce accounts and removeduplicates item lists and set account id for existing accounts 353b61b9** workflow. Its executable nodes use `if`, `itemLists`, `manualTrigger`, `merge`, `microsoftExcel`, `renameKeys`, `salesforce`, `set`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`search-salesforce-accounts-and-removeduplicates-item-lists-and-set-account-id-for-existing-accounts-353b61b9.json`](search-salesforce-accounts-and-removeduplicates-item-lists-and-set-account-id-for-existing-accounts-353b61b9.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftExcelOAuth2Api`, `salesforceOAuth2Api`

**Entry nodes:** On clicking 'execute'

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| On clicking 'execute' | `manualTrigger` | Inspect parameters |
| Search Salesforce accounts | `salesforce` | search |
| Keep new companies | `merge` | Inspect parameters |
| Merge existing account data | `merge` | Inspect parameters |
| Account found? | `if` | Inspect parameters |
| Remove duplicate companies | `itemLists` | removeDuplicates |
| Set Account ID for existing accounts | `renameKeys` | Inspect parameters |
| Retrieve new company contacts | `merge` | Inspect parameters |
| Set new account name | `set` | Inspect parameters |
| Create Salesforce account | `salesforce` | account |
| Create Salesforce contact | `salesforce` | contact / upsert |
| Microsoft Excel | `microsoftExcel` | worksheet / getContent |

## Connection map

- Account found? → Set Account ID for existing accounts (`main`, output 0, input 0)
- Microsoft Excel → Keep new companies (`main`, output 0, input 0)
- Microsoft Excel → Search Salesforce accounts (`main`, output 0, input 0)
- Microsoft Excel → Merge existing account data (`main`, output 0, input 0)
- Keep new companies → Remove duplicate companies (`main`, output 0, input 0)
- Keep new companies → Retrieve new company contacts (`main`, output 0, input 0)
- Set new account name → Retrieve new company contacts (`main`, output 0, input 1)
- On clicking 'execute' → Microsoft Excel (`main`, output 0, input 0)
- Create Salesforce account → Set new account name (`main`, output 0, input 0)
- Remove duplicate companies → Create Salesforce account (`main`, output 0, input 0)
- Search Salesforce accounts → Keep new companies (`main`, output 0, input 1)
- Search Salesforce accounts → Merge existing account data (`main`, output 0, input 1)
- Merge existing account data → Account found? (`main`, output 0, input 0)
- Retrieve new company contacts → Create Salesforce contact (`main`, output 0, input 0)
- Set Account ID for existing accounts → Create Salesforce contact (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftexcel/0258_Microsoftexcel_Manual_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Microsoftexcel/0258_Microsoftexcel_Manual_Create_Triggered.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
