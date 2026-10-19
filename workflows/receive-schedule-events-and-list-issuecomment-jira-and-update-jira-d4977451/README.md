# receive schedule events and list issuecomment jira and update jira d4977451

This folder contains the **receive schedule events and list issuecomment jira and update jira d4977451** workflow. Its executable nodes use `agent`, `aggregate`, `chainLlm`, `executeWorkflow`, `executeWorkflowTrigger`, `if`, `jira`, `jiraTool`, `lmChatOpenAi`, `notionTool`, `outputParserStructured`, `scheduleTrigger`, `sentimentAnalysis`, `set`, `slack`, `textClassifier`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`receive-schedule-events-and-list-issuecomment-jira-and-update-jira-d4977451.json`](receive-schedule-events-and-list-issuecomment-jira-and-update-jira-d4977451.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `jiraSoftwareCloudApi`, `notionApi`, `openAiApi`, `slackApi`

**Entry nodes:** Schedule Trigger, Execute Workflow Trigger

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| OpenAI Chat Model | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model1 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model3 | `lmChatOpenAi` | Inspect parameters |
| OpenAI Chat Model4 | `lmChatOpenAi` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Get Issue Comments | `jira` | issueComment / getAll |
| Close Issue | `jira` | update |
| Send Reminder | `jira` | issueComment |
| Join Comments | `aggregate` | Inspect parameters |
| Add Autoclose Message | `jira` | issueComment |
| Ask For Feedback Message | `jira` | issueComment |
| Simplify Thread For AI | `set` | Inspect parameters |
| Solution Found? | `if` | Inspect parameters |
| Reply to Issue | `jira` | issueComment |
| Last Message is Not Bot | `if` | Inspect parameters |
| Structured Output Parser | `outputParserStructured` | Inspect parameters |
| Get Issue Metadata | `set` | Inspect parameters |
| Notify Slack Channel | `slack` | Inspect parameters |
| Close Issue2 | `jira` | update |
| Get List of Unresolved Long Lived Issues | `jira` | getAll |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Customer Satisfaction Agent | `sentimentAnalysis` | Inspect parameters |
| KnowledgeBase Agent | `agent` | Inspect parameters |
| Issue Reminder Agent | `chainLlm` | Inspect parameters |
| Find Simlar Issues | `jiraTool` | getAll |
| Query KnowledgeBase | `notionTool` | search |
| Report Unhappy Resolution | `slack` | Inspect parameters |
| Classify Current Issue State | `textClassifier` | Inspect parameters |

## Connection map

- Join Comments → Simplify Thread For AI (`main`, output 0, input 0)
- Reply to Issue → Close Issue2 (`main`, output 0, input 0)
- Solution Found? → Reply to Issue (`main`, output 0, input 0)
- Solution Found? → Notify Slack Channel (`main`, output 1, input 0)
- Schedule Trigger → Get List of Unresolved Long Lived Issues (`main`, output 0, input 0)
- OpenAI Chat Model → Classify Current Issue State (`ai_languageModel`, output 0, input 0)
- Find Simlar Issues → KnowledgeBase Agent (`ai_tool`, output 0, input 0)
- Get Issue Comments → Join Comments (`main`, output 0, input 0)
- Get Issue Metadata → Get Issue Comments (`main`, output 0, input 0)
- OpenAI Chat Model1 → KnowledgeBase Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model3 → Issue Reminder Agent (`ai_languageModel`, output 0, input 0)
- OpenAI Chat Model4 → Customer Satisfaction Agent (`ai_languageModel`, output 0, input 0)
- KnowledgeBase Agent → Solution Found? (`main`, output 0, input 0)
- Query KnowledgeBase → KnowledgeBase Agent (`ai_tool`, output 0, input 0)
- Issue Reminder Agent → Send Reminder (`main`, output 0, input 0)
- Notify Slack Channel → Reply to Issue (`main`, output 0, input 0)
- Add Autoclose Message → Close Issue (`main`, output 0, input 0)
- Simplify Thread For AI → Classify Current Issue State (`main`, output 0, input 0)
- Last Message is Not Bot → Issue Reminder Agent (`main`, output 0, input 0)
- Ask For Feedback Message → Close Issue (`main`, output 0, input 0)
- Execute Workflow Trigger → Get Issue Metadata (`main`, output 0, input 0)
- Structured Output Parser → KnowledgeBase Agent (`ai_outputParser`, output 0, input 0)
- Customer Satisfaction Agent → Ask For Feedback Message (`main`, output 0, input 0)
- Customer Satisfaction Agent → Add Autoclose Message (`main`, output 1, input 0)
- Customer Satisfaction Agent → Report Unhappy Resolution (`main`, output 2, input 0)
- Classify Current Issue State → Customer Satisfaction Agent (`main`, output 0, input 0)
- Classify Current Issue State → Last Message is Not Bot (`main`, output 1, input 0)
- Classify Current Issue State → KnowledgeBase Agent (`main`, output 2, input 0)
- Get List of Unresolved Long Lived Issues → Execute Workflow (`main`, output 0, input 0)

## Verification and provenance

Selected from 3 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Jiratool/1328_Jiratool_Schedule_Automate_Scheduled.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Jiratool/1328_Jiratool_Schedule_Automate_Scheduled.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
