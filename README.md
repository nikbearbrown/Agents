# N8N workflow collection

A documented collection of **1,900 canonical workflow folders**, consolidated from 8,070 snapshots. **1,900 workflow JSON files** have redistribution evidence and are included; all 1,900 selected workflow files are included. Start with the [searchable JSON catalog](catalog.json) or [linked workflow index](CATALOG.md).

## What is in this repository?

Each folder under `workflows/` represents one selected workflow family. Its README describes the configured nodes, credential types, setup, connection map, verification limits, and attribution. `provenance.json` records source and publication hashes; `configuration.json` records removed configuration locations without exposing values.

Published workflows include an overview sticky note. It describes observed structure and setup requirements; it is not a claim that the workflow has been executed. The original inputs and redundant snapshots are preserved outside this repository, not uploaded.

## Original workflows (not part of the 1,900)

[`lectern-job-search/`](lectern-job-search/README.md) holds five workflows written and tested for a course, not collected from elsewhere: collect, filter, delta, post to Discord and a daily runner, which rebuild a Python job-search pipeline as native n8n nodes. Each is tested against the Python's output (the filter agrees on 2,465 real postings), run headless in a disposable n8n 1.113.3 profile. The Discord node has not sent a message from n8n, and SmartRecruiters is not read live; the folder's README lists what is and is not tested. The counts and checks in this repository's other sections do not cover this folder.

## Use a workflow

1. Choose a folder in [CATALOG.md](CATALOG.md) and read its README.
2. Import its JSON into an isolated n8n instance and leave it inactive.
3. Connect your own credentials using n8n's credential store. Replace `REPLACE_WITH_*` configuration placeholders.
4. Review outbound actions, URLs, code, SQL and file access. Test with synthetic data before enabling schedules, webhooks, messages, or other writes.

## What the checks mean

- **Deduplicated:** a canonical source was selected using structure, lineage and known defects. It does not mean the newest export was provable.
- **Sanitized:** credential bindings, pinned/runtime data, scanner findings and selected personal/resource identifiers were removed from publication copies. Secret scanning is not a guarantee against every possible encoding or identifier.
- **Documented:** node inventory and connection-map descriptions are generated from actual JSON. They do not certify business logic.
- **Runtime-tested:** only explicitly identified classroom teaching references have passed synthetic headless tests. The bulk catalog has not passed service-level testing.

## Scope and counts

The local cleanup selected 1,900 families from 8,070 snapshots, archiving 6,167 noncanonical copies and quarantining 3 malformed files. This repository retains one documented folder per family. See [publication-report.json](publication-report.json) for excluded JSON files and current counts.

## Licensing and attribution

This is a curated collection, not a claim of authorship over all workflows. Preserve per-folder attribution and the notices in [licenses/](licenses/). There is no blanket license overriding individual sources. Workflows with unresolved redistribution rights are withheld. MIT and Apache notices remain with their respective sources. Availability here does not authorize reposting someone else's work to the n8n Creator Portal as your own.

## Annotation

The initial overview notes are generated locally without model calls. The official n8n annotation tool can add richer notes after review; keep renaming disabled until reference rewriting is proven safe. Compare executable nodes and all connections before and after annotation. See [ANNOTATION.md](ANNOTATION.md).

## Contributing

Keep folder names descriptive and lowercase kebab-case. Include provenance and a README. Do not commit credentials, execution payloads or personal sample data. Validate JSON, scan for secrets, and document actual test evidence separately from proposed behavior.
