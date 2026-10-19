# New WooCommerce Customer to Mautic

This folder contains the **New WooCommerce Customer to Mautic** workflow. Its executable nodes use `if`, `mautic`, `wooCommerceTrigger`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`new-woocommerce-customer-to-mautic.json`](new-woocommerce-customer-to-mautic.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `mauticOAuth2Api`, `wooCommerceApi`

**Entry nodes:** Customer Created or Updated

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Check for Existing | `mautic` | getAll |
| If New | `if` | Inspect parameters |
| Create Contact | `mautic` | Inspect parameters |
| Update Contact | `mautic` | update |
| Customer Created or Updated | `wooCommerceTrigger` | Inspect parameters |

## Connection map

- If New → Create Contact (`main`, output 0, input 0)
- If New → Update Contact (`main`, output 1, input 0)
- Check for Existing → If New (`main`, output 0, input 0)
- Customer Created or Updated → Check for Existing (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/1160_Mautic_Woocommerce_Create_Triggered.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Mautic/1160_Mautic_Woocommerce_Create_Triggered.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
