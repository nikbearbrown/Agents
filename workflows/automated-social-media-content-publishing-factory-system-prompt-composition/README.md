# ✨🩷Automated Social Media Content Publishing Factory + System Prompt Composition

This folder contains the **✨🩷Automated Social Media Content Publishing Factory + System Prompt Composition** workflow. Its executable nodes use `agent`, `chatTrigger`, `code`, `executeWorkflowTrigger`, `extractFromFile`, `facebookGraphApi`, `gmail`, `googleDocs`, `googleDrive`, `httpRequest`, `if`, `linkedIn`, `lmChatOpenAi`, `memoryBufferWindow`, `merge`, `noOp`, `set`, `switch`, `telegram`, `toolSerpApi`, `toolWorkflow`, `twitter`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`automated-social-media-content-publishing-factory-system-prompt-composition.json`](automated-social-media-content-publishing-factory-system-prompt-composition.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `facebookGraphApi`, `gmailOAuth2`, `googleDocsOAuth2Api`, `googleDriveOAuth2Api`, `linkedInOAuth2Api`, `openAiApi`, `serpApi`, `telegramApi`, `twitterOAuth2Api`

**Entry nodes:** When chat message received, When Executed by Another Workflow

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| When chat message received | `chatTrigger` | Inspect parameters |
| X-Twiter | `toolWorkflow` | Inspect parameters |
| Instagram | `toolWorkflow` | Inspect parameters |
| Window Buffer Memory | `memoryBufferWindow` | Inspect parameters |
| When Executed by Another Workflow | `executeWorkflowTrigger` | Inspect parameters |
| Facebook | `toolWorkflow` | Inspect parameters |
| LinkedIn | `toolWorkflow` | Inspect parameters |
| Short | `toolWorkflow` | Inspect parameters |
| YouTube Short | `toolWorkflow` | Inspect parameters |
| pollinations.ai1 | `httpRequest` | Inspect parameters |
| Save Image to imgbb.com | `httpRequest` | POST |
| Gmail | `gmail` | Inspect parameters |
| Social Media Schema | `googleDocs` | get |
| Social Media System Prompt | `googleDocs` | get |
| gpt-40-mini | `lmChatOpenAi` | Inspect parameters |
| Instagram Image | `httpRequest` | POST |
| X Post | `twitter` | Inspect parameters |
| Instragram Post | `facebookGraphApi` | Inspect parameters |
| Facebook Post | `facebookGraphApi` | Inspect parameters |
| LinkedIn Post | `linkedIn` | Inspect parameters |
| Gmail User for Approval | `gmail` | sendAndWait |
| Get Social Post Image | `httpRequest` | Inspect parameters |
| gpt-40-mini1 | `lmChatOpenAi` | Inspect parameters |
| gpt-4o-mini | `lmChatOpenAi` | Inspect parameters |
| Schema | `set` | Inspect parameters |
| System Prompt | `set` | Inspect parameters |
| Parse Schema | `code` | Inspect parameters |
| Parse System Prompt | `code` | Inspect parameters |
| Compose Prompt & Schema | `set` | Inspect parameters |
| Social Media Content Creator | `agent` | Inspect parameters |
| Merge Prompts and Schema | `merge` | Inspect parameters |
| Social Content | `set` | Inspect parameters |
| Save Image to Google Drive | `googleDrive` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Save Social Post to Google Drive | `googleDrive` | createFromText |
| Google Drive Image Meta | `set` | Inspect parameters |
| Social Post JSON | `set` | Inspect parameters |
| Respond with Google Drive Id | `set` | Inspect parameters |
| Telegram Success Message (Optional) | `telegram` | Inspect parameters |
| Telegram Error Message (Optional) | `telegram` | Inspect parameters |
| Social Media Publishing Router | `switch` | Inspect parameters |
| Prepare Email Contents | `agent` | Inspect parameters |
| Is Approved? | `if` | Inspect parameters |
| File Id | `set` | Inspect parameters |
| Get Social Post from Google Drive | `googleDrive` | download |
| Extract as JSON | `extractFromFile` | fromJson |
| Merge Image and Post Contents | `merge` | Inspect parameters |
| Implement Threads Here | `noOp` | Inspect parameters |
| Implement YouTube Shorts Here | `noOp` | Inspect parameters |
| X Response | `set` | Inspect parameters |
| Instagram Response | `set` | Inspect parameters |
| Facebook Response | `set` | Inspect parameters |
| LinkedIn Response | `set` | Inspect parameters |
| 🤖Social Media Router Agent | `agent` | Inspect parameters |
| SerpAPI | `toolSerpApi` | Inspect parameters |
| Prepare Social Media Email Contents | `agent` | Inspect parameters |
| gpt-4o | `lmChatOpenAi` | Inspect parameters |

## Connection map

- Merge → Prepare Social Media Email Contents (`main`, output 0, input 0)
- Merge → Google Drive Image Meta (`main`, output 0, input 0)
- Short → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- Schema → Parse Schema (`main`, output 0, input 0)
- X Post → X Response (`main`, output 0, input 0)
- gpt-4o → 🤖Social Media Router Agent (`ai_languageModel`, output 0, input 0)
- File Id → Get Social Post from Google Drive (`main`, output 0, input 0)
- SerpAPI → Social Media Content Creator (`ai_tool`, output 0, input 0)
- Facebook → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- LinkedIn → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- X-Twiter → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- Instagram → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- gpt-40-mini → Prepare Social Media Email Contents (`ai_languageModel`, output 0, input 0)
- gpt-4o-mini → Social Media Content Creator (`ai_languageModel`, output 0, input 0)
- Is Approved? → Get Social Post Image (`main`, output 0, input 0)
- Parse Schema → Merge Prompts and Schema (`main`, output 0, input 0)
- gpt-40-mini1 → Prepare Email Contents (`ai_languageModel`, output 0, input 0)
- Facebook Post → Facebook Response (`main`, output 0, input 0)
- LinkedIn Post → LinkedIn Response (`main`, output 0, input 0)
- System Prompt → Parse System Prompt (`main`, output 0, input 0)
- YouTube Short → 🤖Social Media Router Agent (`ai_tool`, output 0, input 0)
- Social Content → pollinations.ai1 (`main`, output 0, input 0)
- Extract as JSON → Merge Image and Post Contents (`main`, output 0, input 0)
- Extract as JSON → Prepare Email Contents (`main`, output 0, input 0)
- Instagram Image → Instragram Post (`main`, output 0, input 0)
- Instragram Post → Instagram Response (`main`, output 0, input 0)
- Social Post JSON → Save Social Post to Google Drive (`main`, output 0, input 0)
- pollinations.ai1 → Telegram Success Message (Optional) (`main`, output 0, input 0)
- pollinations.ai1 → Save Image to imgbb.com (`main`, output 0, input 0)
- pollinations.ai1 → Save Image to Google Drive (`main`, output 0, input 0)
- pollinations.ai1 → Merge (`main`, output 0, input 1)
- pollinations.ai1 → Telegram Error Message (Optional) (`main`, output 1, input 0)
- Parse System Prompt → Merge Prompts and Schema (`main`, output 0, input 2)
- Social Media Schema → Schema (`main`, output 0, input 0)
- Window Buffer Memory → 🤖Social Media Router Agent (`ai_memory`, output 0, input 0)
- Get Social Post Image → Merge Image and Post Contents (`main`, output 0, input 1)
- Prepare Email Contents → Gmail User for Approval (`main`, output 0, input 0)
- Compose Prompt & Schema → Social Media Content Creator (`main`, output 0, input 0)
- Gmail User for Approval → Is Approved? (`main`, output 0, input 0)
- Google Drive Image Meta → Social Post JSON (`main`, output 0, input 0)
- Save Image to imgbb.com → Merge (`main`, output 0, input 0)
- Merge Prompts and Schema → Compose Prompt & Schema (`main`, output 0, input 0)
- Save Image to Google Drive → Merge (`main`, output 0, input 2)
- Social Media System Prompt → System Prompt (`main`, output 0, input 0)
- When chat message received → 🤖Social Media Router Agent (`main`, output 0, input 0)
- Social Media Content Creator → Social Content (`main`, output 0, input 0)
- Merge Image and Post Contents → Social Media Publishing Router (`main`, output 0, input 0)
- 🤖Social Media Router Agent → File Id (`main`, output 0, input 0)
- Social Media Publishing Router → X Post (`main`, output 0, input 0)
- Social Media Publishing Router → Instagram Image (`main`, output 1, input 0)
- Social Media Publishing Router → Facebook Post (`main`, output 2, input 0)
- Social Media Publishing Router → LinkedIn Post (`main`, output 3, input 0)
- Social Media Publishing Router → Implement Threads Here (`main`, output 4, input 0)
- Social Media Publishing Router → Implement YouTube Shorts Here (`main`, output 5, input 0)
- Save Social Post to Google Drive → Respond with Google Drive Id (`main`, output 0, input 0)
- Get Social Post from Google Drive → Extract as JSON (`main`, output 0, input 0)
- When Executed by Another Workflow → Social Media System Prompt (`main`, output 0, input 0)
- When Executed by Another Workflow → Social Media Schema (`main`, output 0, input 0)
- When Executed by Another Workflow → Merge Prompts and Schema (`main`, output 0, input 1)
- Prepare Social Media Email Contents → Gmail (`main`, output 0, input 0)

## Verification and provenance

Selected from 8 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1342_Linkedin_Telegram_Automate_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Linkedin/1342_Linkedin_Telegram_Automate_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
