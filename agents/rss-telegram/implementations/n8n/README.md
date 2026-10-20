# rss-telegram

This folder contains the **rss-telegram** workflow. Its executable nodes use `cron`, `function`, `if`, `manualTrigger`, `rssFeedRead`, `splitInBatches`, `telegram`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`rss-telegram.json`](rss-telegram.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `telegramApi`

**Entry nodes:** Cron1, test

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| SplitInBatches | `splitInBatches` | Inspect parameters |
| Function | `function` | Inspect parameters |
| Cron1 | `cron` | Inspect parameters |
| 是否重复 | `if` | Inspect parameters |
| 写入图片的属性 | `function` | Inspect parameters |
| 图片数量判断 | `if` | Inspect parameters |
| 一张图片 | `telegram` | sendPhoto |
| 其他状况 | `telegram` | Inspect parameters |
| NaN | `function` | Inspect parameters |
| SplitInBatches1 | `splitInBatches` | Inspect parameters |
| Function1 | `function` | Inspect parameters |
| IF | `if` | Inspect parameters |
| IF1 | `if` | Inspect parameters |
| send | `telegram` | sendPhoto |
| instagram rss | `rssFeedRead` | Inspect parameters |
| weibo rss | `rssFeedRead` | Inspect parameters |
| Telegram | `telegram` | sendPhoto |
| test | `manualTrigger` | Inspect parameters |

## Connection map

- IF → NaN (`main`, output 1, input 0)
- IF1 → send (`main`, output 0, input 0)
- IF1 → Telegram (`main`, output 1, input 0)
- NaN → IF1 (`main`, output 0, input 0)
- test → instagram rss (`main`, output 0, input 0)
- test → weibo rss (`main`, output 0, input 0)
- Cron1 → weibo rss (`main`, output 0, input 0)
- Cron1 → instagram rss (`main`, output 0, input 0)
- Function → 是否重复 (`main`, output 0, input 0)
- Function1 → IF (`main`, output 0, input 0)
- weibo rss → SplitInBatches (`main`, output 0, input 0)
- 是否重复 → 写入图片的属性 (`main`, output 1, input 0)
- instagram rss → SplitInBatches1 (`main`, output 0, input 0)
- SplitInBatches → Function (`main`, output 0, input 0)
- SplitInBatches1 → Function1 (`main`, output 0, input 0)
- 图片数量判断 → 一张图片 (`main`, output 0, input 0)
- 图片数量判断 → 其他状况 (`main`, output 1, input 0)
- 写入图片的属性 → 图片数量判断 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0944_Telegram_Rssfeedread_Automation_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Telegram/0944_Telegram_Rssfeedread_Automation_Scheduled.json). License: **MIT**; preserve [the notice](../../../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
