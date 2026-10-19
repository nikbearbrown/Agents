# receive schedule events and list channelmessage microsoft teams and team member weekly report agent

This folder contains the **receive schedule events and list channelmessage microsoft teams and team member weekly report agent** workflow. Its executable nodes use `aggregate`, `chainLlm`, `code`, `lmChatOpenAi`, `markdown`, `microsoftTeams`, `scheduleTrigger`, `set`, `splitOut`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-channelmessage-microsoft-teams-and-team-member-weekly-report-agent.json`](receive-schedule-events-and-list-channelmessage-microsoft-teams-and-team-member-weekly-report-agent.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `microsoftTeamsOAuth2Api`, `openAiApi`

**Entry nodes:** Schedule Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Fetch Latest Channel Messages | `microsoftTeams` | channelMessage / getAll |
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| Team Member Weekly Report Agent | `chainLlm` | Inspect parameters |
| Merge Report With User Data | `set` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| Reports to Single List | `aggregate` | Inspect parameters |
| Team Weekly Report Agent | `chainLlm` | Inspect parameters |
| Markdown to HTML | `markdown` | Inspect parameters |
| Send Report to Channel | `microsoftTeams` | channelMessage |
| Group Messages By UserId | `code` | Inspect parameters |
| Groups to Items | `splitOut` | Inspect parameters |

## Connection map

- Groups to Items → Team Member Weekly Report Agent (`main`, output 0, input 0)
- Markdown to HTML → Send Report to Channel (`main`, output 0, input 0)
- Schedule Trigger → Fetch Latest Channel Messages (`main`, output 0, input 0)
- OpenAI Chat Model → Team Member Weekly Report Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model1 → Team Weekly Report Agent (`ai_languageModel`, output 0, input 0)
- Reports to Single List → Team Weekly Report Agent (`main`, output 0, input 0)
- Group Messages By UserId → Groups to Items (`main`, output 0, input 0)
- Team Weekly Report Agent → Markdown to HTML (`main`, output 0, input 0)
- Merge Report With User Data → Reports to Single List (`main`, output 0, input 0)
- Fetch Latest Channel Messages → Group Messages By UserId (`main`, output 0, input 0)
- Team Member Weekly Report Agent → Merge Report With User Data (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0923_Splitout_Code_Send_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Splitout/0923_Splitout_Code_Send_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
