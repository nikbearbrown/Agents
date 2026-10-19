# Realtime Notion Todoist 2-way Sync Template

This folder contains the **Realtime Notion Todoist 2-way Sync Template** workflow. Its executable nodes use `aggregate`, `code`, `compareDatasets`, `crypto`, `executeWorkflow`, `executeWorkflowTrigger`, `executionData`, `filter`, `form`, `formTrigger`, `gmail`, `html`, `httpRequest`, `if`, `merge`, `noOp`, `notion`, `redis`, `respondToWebhook`, `scheduleTrigger`, `set`, `splitInBatches`, `splitOut`, `stopAndError`, `switch`, `todoist`, `wait`, `webhook`. The table and connection map below are derived from the JSON, not an inferred guarantee of behavior.

**Status:** Published sanitized source; not runtime-tested.

## Files

- [`realtime-notion-todoist-2-way-sync-template.json`](realtime-notion-todoist-2-way-sync-template.json): sanitized, inactive import copy with an overview sticky note.
- [`provenance.json`](provenance.json): source attribution, original and publication hashes, selection and license evidence.
- [`configuration.json`](configuration.json): credential types and redacted configuration locations; no credential values.

## Setup

1. Import the JSON into an isolated n8n instance, leaving it inactive.
2. Create your own credentials in n8n and select them in the relevant nodes. Never paste secrets into a public workflow export.
3. Replace `REPLACE_WITH_*` values with your own resource identifiers. Inspect URLs, webhook paths, destinations, file paths, database queries, and Code nodes before execution.
4. Confirm required node packages and versions are available. Test with synthetic data and harmless destinations before enabling triggers or any external writes.

**Credential types referenced by the source:** `gmailOAuth2`, `notionApi`, `redis`, `todoistApi`

**Entry nodes:** OAuth redirect, Notion-Todoist Sync Setup Helper, Todoist Webhook Setup Helper, Schedule Trigger, Execute Workflow Trigger, Notion Webhook, Todoist Webhook, Webhook

## Configured nodes

| Node | Type | Resource / operation |
|---|---|---|
| Get projects | `httpRequest` | Inspect parameters |
| Get sections | `httpRequest` | Inspect parameters |
| Get Notion Databases | `notion` | database / getAll |
| Prep Dropdown | `code` | Inspect parameters |
| Prep Dropdown1 | `code` | Inspect parameters |
| Generate config | `code` | Inspect parameters |
| Choose Notion Database | `form` | Inspect parameters |
| Choose Todoist Project | `form` | Inspect parameters |
| Verify security token | `if` | Inspect parameters |
| Generate security token | `crypto` | Inspect parameters |
| Store variables | `code` | Inspect parameters |
| Get variables | `code` | Inspect parameters |
| Redirect to Auth Page | `form` | completion |
| OAuth redirect | `webhook` | Inspect parameters |
| Exchange Tokens | `httpRequest` | POST |
| Respond with success | `respondToWebhook` | Inspect parameters |
| Respond with error | `respondToWebhook` | Inspect parameters |
| Get Notion Database ID | `code` | Inspect parameters |
| Get Todoist Project ID | `code` | Inspect parameters |
| Notion-Todoist Sync Setup Helper | `formTrigger` | Inspect parameters |
| Todoist Webhook Setup Helper | `formTrigger` | Inspect parameters |
| Return config JSON | `form` | completion |
| Todoist | `todoist` | getAll |
| Notion | `notion` | databasePage / getAll |
| Compare Datasets | `compareDatasets` | Inspect parameters |
| Exists/Completed in Notion | `if` | Inspect parameters |
| Get Todoist Task | `todoist` | get |
| If Todoist ID exists | `if` | Inspect parameters |
| Store Todoist ID | `notion` | databasePage / update |
| Mark as Incomplete in Todoist | `todoist` | reopen |
| Mark as Completed in Todoist | `todoist` | close |
| Delete Task in Todoist | `todoist` | delete |
| Loop Over Items | `splitInBatches` | Inspect parameters |
| Get Notion Task | `notion` | databasePage / getAll |
| Update Task in Todoist | `httpRequest` | POST |
| Pick Todoist Fields | `set` | Inspect parameters |
| Map Notion to Todoist | `code` | Inspect parameters |
| Update task in Todoist before closing | `httpRequest` | POST |
| Map Notion to Todoist1 | `code` | Inspect parameters |
| Handle empty dates | `code` | Inspect parameters |
| Handle empty dates1 | `code` | Inspect parameters |
| Handle empty dates2 | `code` | Inspect parameters |
| Create task in Todoist | `httpRequest` | POST |
| Add project ID | `set` | Inspect parameters |
| Lock Todoist ID | `redis` | set |
| Generate UUID | `crypto` | Inspect parameters |
| Update section (Sync API) | `httpRequest` | POST |
| Status changed | `filter` | Inspect parameters |
| Aggregate | `aggregate` | Inspect parameters |
| Prepare Batching Items | `set` | Inspect parameters |
| Loop Over Items1 | `splitInBatches` | Inspect parameters |
| Status is Done | `if` | Inspect parameters |
| Lock Todoist ID1 | `redis` | set |
| Lock Todoist ID2 | `redis` | set |
| Update task in Todoist | `httpRequest` | POST |
| Get mapped item | `set` | Inspect parameters |
| Get mapped item1 | `set` | Inspect parameters |
| Schedule Trigger | `scheduleTrigger` | Inspect parameters |
| Prepare summary data | `set` | Inspect parameters |
| Prepare summary data1 | `set` | Inspect parameters |
| Merge | `merge` | Inspect parameters |
| Prepare summary data2 | `set` | Inspect parameters |
| Filter out status changes | `filter` | Inspect parameters |
| Map Todoist to Notion | `code` | Inspect parameters |
| Map summary fields | `set` | Inspect parameters |
| Convert to HTML Table | `html` | convertToHtmlTable |
| Generate email body | `html` | Inspect parameters |
| Get mapped item2 | `set` | Inspect parameters |
| Gmail | `gmail` | Inspect parameters |
| Merge summary | `merge` | Inspect parameters |
| Globals | `set` | Inspect parameters |
| Execute Workflow Trigger | `executeWorkflowTrigger` | Inspect parameters |
| Differences exist1 | `filter` | Inspect parameters |
| Requires completion change1 | `filter` | Inspect parameters |
| Create task in Notion | `notion` | databasePage |
| Update task in Notion | `notion` | databasePage / update |
| Mark as Done in Notion | `notion` | databasePage / update |
| Mark as Obsolete in Notion | `notion` | databasePage / update |
| Mark as In Progress in Notion | `notion` | databasePage / update |
| Only continue if not locked | `filter` | Inspect parameters |
| Lock Notion ID | `redis` | set |
| Check if Todoist ID is locked | `redis` | get |
| Update Description in Todoist | `todoist` | update |
| Description has changed in Todoist | `filter` | Inspect parameters |
| Update Description in Todoist1 | `todoist` | update |
| Generate UUID1 | `crypto` | Inspect parameters |
| Update section (Sync API)1 | `httpRequest` | POST |
| Get Backlog Section ID | `code` | Inspect parameters |
| Notion Task not found | `if` | Inspect parameters |
| Check if creating flag exists1 | `redis` | get |
| Only continue if flag does not exist1 | `filter` | Inspect parameters |
| Set creating flag1 | `redis` | set |
| Neither focussed nor planned1 | `filter` | Inspect parameters |
| Mark as Focussed in Notion | `notion` | databasePage / update |
| Todoist trigger reference | `noOp` | Inspect parameters |
| Get Notion Task2 | `notion` | databasePage / getAll |
| Notion Task found1 | `filter` | Inspect parameters |
| Switch by Event | `switch` | Inspect parameters |
| If event is not :deleted | `if` | Inspect parameters |
| Execution Data | `executionData` | Inspect parameters |
| Execution Data1 | `executionData` | Inspect parameters |
| Execution Data2 | `executionData` | Inspect parameters |
| Execution Data3 | `executionData` | Inspect parameters |
| Execution Data4 | `executionData` | Inspect parameters |
| Globals1 | `set` | Inspect parameters |
| Map Todoist to Notion1 | `code` | Inspect parameters |
| Get Todoist Task1 | `todoist` | get |
| Get Notion Task1 | `notion` | databasePage / getAll |
| Requires completion change | `filter` | Inspect parameters |
| Has been completed? | `if` | Inspect parameters |
| Differences exist | `filter` | Inspect parameters |
| Only continue if not locked1 | `filter` | Inspect parameters |
| Check if Notion ID is locked | `redis` | get |
| Get Notion task | `notion` | databasePage / get |
| Check if creating flag exists | `redis` | get |
| Only continue if flag does not exist | `filter` | Inspect parameters |
| Set creating flag | `redis` | set |
| Todoist ID exists? | `if` | Inspect parameters |
| Get todoist ID | `set` | Inspect parameters |
| Todoist ID exists | `filter` | Inspect parameters |
| Get todoist ID1 | `set` | Inspect parameters |
| Status changed but not empty | `filter` | Inspect parameters |
| Status is Obsolete? | `if` | Inspect parameters |
| Status is not Done | `filter` | Inspect parameters |
| Neither focussed nor planned | `if` | Inspect parameters |
| Notion trigger reference | `noOp` | Inspect parameters |
| Notion Webhook | `webhook` | Inspect parameters |
| Store Todoist ID1 | `notion` | databasePage / update |
| Mark as Completed in Todoist1 | `todoist` | close |
| Update task in Todoist1 | `httpRequest` | POST |
| Globals2 | `set` | Inspect parameters |
| Mark as Incomplete in Todoist1 | `todoist` | reopen |
| Generate UUID2 | `crypto` | Inspect parameters |
| Update section (Sync API)2 | `httpRequest` | POST |
| Lock Todoist ID4 | `redis` | set |
| Delete Task in Todoist2 | `todoist` | delete |
| Map Notion to Todoist2 | `code` | Inspect parameters |
| Get Todoist Task2 | `todoist` | get |
| Create task in Todoist1 | `httpRequest` | POST |
| Execution Data5 | `executionData` | Inspect parameters |
| Execution Data6 | `executionData` | Inspect parameters |
| Todoist Webhook | `webhook` | Inspect parameters |
| Execute Workflow | `executeWorkflow` | Inspect parameters |
| Extract IDs | `set` | Inspect parameters |
| Split out Notion changes | `splitOut` | Inspect parameters |
| Body is array? | `if` | Inspect parameters |
| Switch by project | `switch` | Inspect parameters |
| Webhook | `webhook` | Inspect parameters |
| Switch | `switch` | Inspect parameters |
| Execute Workflow1 | `executeWorkflow` | Inspect parameters |
| Due date empty | `filter` | Inspect parameters |
| Has not been completed? | `if` | Inspect parameters |
| End here | `noOp` | Inspect parameters |
| Retry limit reached | `stopAndError` | Inspect parameters |
| Set tries | `set` | Inspect parameters |
| Update tries | `set` | Inspect parameters |
| Wait | `wait` | Inspect parameters |
| Catch known error | `if` | Inspect parameters |
| If tries left | `if` | Inspect parameters |
| Retry limit reached1 | `stopAndError` | Inspect parameters |
| Set tries1 | `set` | Inspect parameters |
| Update tries1 | `set` | Inspect parameters |
| Wait1 | `wait` | Inspect parameters |
| Catch known error1 | `if` | Inspect parameters |
| If tries left1 | `if` | Inspect parameters |
| Set tries2 | `set` | Inspect parameters |
| Update tries2 | `set` | Inspect parameters |
| Wait2 | `wait` | Inspect parameters |
| Catch known error2 | `if` | Inspect parameters |
| If tries left2 | `if` | Inspect parameters |
| Retry limit reached2 | `stopAndError` | Inspect parameters |
| Turn Markdown into Notion Blocks | `code` | Inspect parameters |
| Handle each block separately | `splitOut` | Inspect parameters |
| Append Notion Block | `notion` | block |

## Connection map

- Wait → Update tries (`main`, output 0, input 0)
- Merge → Loop Over Items1 (`main`, output 0, input 0)
- Merge → Merge summary (`main`, output 0, input 0)
- Wait1 → Update tries1 (`main`, output 0, input 0)
- Wait2 → Update tries2 (`main`, output 0, input 0)
- Notion → Map Notion to Todoist (`main`, output 0, input 0)
- Switch → Execute Workflow (`main`, output 0, input 0)
- Switch → Execute Workflow1 (`main`, output 1, input 0)
- Todoist → Pick Todoist Fields (`main`, output 0, input 0)
- Webhook → Switch (`main`, output 0, input 0)
- Aggregate → Update section (Sync API) (`main`, output 0, input 0)
- Set tries → Get Todoist Task (`main`, output 0, input 0)
- Set tries1 → Get Todoist Task2 (`main`, output 0, input 0)
- Set tries2 → Get Todoist Task1 (`main`, output 0, input 0)
- Extract IDs → Notion trigger reference (`main`, output 0, input 0)
- Get projects → Prep Dropdown1 (`main`, output 0, input 0)
- Get sections → Generate config (`main`, output 0, input 0)
- Update tries → If tries left (`main`, output 0, input 0)
- Generate UUID → Prepare Batching Items (`main`, output 0, input 0)
- Get variables → Verify security token (`main`, output 0, input 0)
- If tries left → Set tries (`main`, output 0, input 0)
- If tries left → Retry limit reached (`main`, output 1, input 0)
- Merge summary → Filter out status changes (`main`, output 0, input 0)
- Prep Dropdown → Choose Notion Database (`main`, output 0, input 0)
- Update tries1 → If tries left1 (`main`, output 0, input 0)
- Update tries2 → If tries left2 (`main`, output 0, input 0)
- Add project ID → If Todoist ID exists (`main`, output 0, input 0)
- Body is array? → Split out Notion changes (`main`, output 0, input 0)
- Body is array? → Notion trigger reference (`main`, output 1, input 0)
- Due date empty → Mark as Focussed in Notion (`main`, output 0, input 0)
- Execution Data → Check if Todoist ID is locked (`main`, output 0, input 0)
- Generate UUID1 → Update section (Sync API)1 (`main`, output 0, input 0)
- Generate UUID2 → Update section (Sync API)2 (`main`, output 0, input 0)
- Get todoist ID → Lock Todoist ID4 (`main`, output 0, input 0)
- If tries left1 → Set tries1 (`main`, output 0, input 0)
- If tries left1 → Retry limit reached1 (`main`, output 1, input 0)
- If tries left2 → Set tries2 (`main`, output 0, input 0)
- If tries left2 → Retry limit reached2 (`main`, output 1, input 0)
- Notion Webhook → Body is array? (`main`, output 0, input 0)
- OAuth redirect → Get variables (`main`, output 0, input 0)
- Prep Dropdown1 → Choose Todoist Project (`main`, output 0, input 0)
- Status changed → Get mapped item1 (`main`, output 0, input 0)
- Status is Done → Mark as Completed in Todoist (`main`, output 0, input 0)
- Status is Done → Delete Task in Todoist (`main`, output 1, input 0)
- Exchange Tokens → Respond with success (`main`, output 0, input 0)
- Exchange Tokens → Respond with error (`main`, output 1, input 0)
- Execution Data1 → Get Notion Task1 (`main`, output 0, input 0)
- Execution Data2 → Update Description in Todoist (`main`, output 0, input 0)
- Execution Data2 → Lock Notion ID (`main`, output 0, input 0)
- Execution Data3 → Switch by Event (`main`, output 0, input 0)
- Execution Data4 → Mark as Obsolete in Notion (`main`, output 0, input 0)
- Execution Data5 → Check if Notion ID is locked (`main`, output 0, input 0)
- Execution Data6 → Status is Obsolete? (`main`, output 0, input 0)
- Generate config → Return config JSON (`main`, output 0, input 0)
- Get Notion Task → Loop Over Items (`main`, output 0, input 0)
- Get Notion task → Map Notion to Todoist2 (`main`, output 0, input 0)
- Get mapped item → Merge (`main`, output 0, input 0)
- Get todoist ID1 → Lock Todoist ID4 (`main`, output 0, input 0)
- Loop Over Items → Exists/Completed in Notion (`main`, output 0, input 0)
- Loop Over Items → Get Notion Task (`main`, output 1, input 0)
- Store variables → Redirect to Auth Page (`main`, output 0, input 0)
- Switch by Event → Differences exist1 (`main`, output 0, input 0)
- Switch by Event → Description has changed in Todoist (`main`, output 0, input 0)
- Switch by Event → Requires completion change1 (`main`, output 1, input 0)
- Switch by Event → Requires completion change1 (`main`, output 2, input 0)
- Todoist Webhook → Switch by project (`main`, output 0, input 0)
- Compare Datasets → Handle empty dates2 (`main`, output 0, input 0)
- Compare Datasets → Handle empty dates (`main`, output 2, input 0)
- Compare Datasets → Loop Over Items (`main`, output 3, input 0)
- Get Notion Task1 → Notion Task not found (`main`, output 0, input 0)
- Get Notion Task2 → Notion Task found1 (`main`, output 0, input 0)
- Get Todoist Task → Mark as Incomplete in Todoist (`main`, output 0, input 0)
- Get Todoist Task → Catch known error (`main`, output 1, input 0)
- Get mapped item1 → Merge (`main`, output 0, input 1)
- Get mapped item2 → Merge summary (`main`, output 0, input 1)
- Loop Over Items1 → Generate UUID (`main`, output 1, input 0)
- Schedule Trigger → Notion (`main`, output 0, input 0)
- Schedule Trigger → Todoist (`main`, output 0, input 0)
- Schedule Trigger → Globals (`main`, output 0, input 0)
- Store Todoist ID → Get mapped item2 (`main`, output 0, input 0)
- Catch known error → Create task in Todoist (`main`, output 0, input 0)
- Catch known error → Wait (`main`, output 1, input 0)
- Differences exist → Update task in Todoist1 (`main`, output 0, input 0)
- Get Todoist Task1 → Map Todoist to Notion1 (`main`, output 0, input 0)
- Get Todoist Task1 → Catch known error2 (`main`, output 1, input 0)
- Get Todoist Task2 → Differences exist (`main`, output 0, input 0)
- Get Todoist Task2 → Requires completion change (`main`, output 0, input 0)
- Get Todoist Task2 → Status changed but not empty (`main`, output 0, input 0)
- Get Todoist Task2 → Catch known error1 (`main`, output 1, input 0)
- Set creating flag → Create task in Todoist1 (`main`, output 0, input 0)
- Switch by project → Todoist trigger reference (`main`, output 0, input 0)
- Todoist ID exists → Delete Task in Todoist2 (`main`, output 0, input 0)
- Catch known error1 → Status is not Done (`main`, output 0, input 0)
- Catch known error1 → Wait1 (`main`, output 1, input 0)
- Catch known error2 → End here (`main`, output 0, input 0)
- Catch known error2 → Wait2 (`main`, output 1, input 0)
- Differences exist1 → Update task in Notion (`main`, output 0, input 0)
- Differences exist1 → Due date empty (`main`, output 0, input 0)
- Handle empty dates → Update Task in Todoist (`main`, output 0, input 0)
- Map summary fields → Convert to HTML Table (`main`, output 0, input 0)
- Notion Task found1 → Execution Data4 (`main`, output 0, input 0)
- Set creating flag1 → Get Backlog Section ID (`main`, output 0, input 0)
- Status is not Done → Check if creating flag exists (`main`, output 0, input 0)
- Todoist ID exists? → Set tries1 (`main`, output 0, input 0)
- Todoist ID exists? → Check if creating flag exists (`main`, output 1, input 0)
- Append Notion Block → Lock Notion ID (`main`, output 0, input 0)
- Generate email body → Gmail (`main`, output 0, input 0)
- Handle empty dates1 → Update task in Todoist before closing (`main`, output 0, input 0)
- Handle empty dates2 → Add project ID (`main`, output 0, input 0)
- Has been completed? → Mark as Completed in Todoist1 (`main`, output 0, input 0)
- Has been completed? → Mark as Incomplete in Todoist1 (`main`, output 1, input 0)
- Pick Todoist Fields → Compare Datasets (`main`, output 0, input 1)
- Status is Obsolete? → Todoist ID exists (`main`, output 0, input 0)
- Status is Obsolete? → Neither focussed nor planned (`main`, output 1, input 0)
- Get Notion Databases → Prep Dropdown (`main`, output 0, input 0)
- If Todoist ID exists → Set tries (`main`, output 0, input 0)
- If Todoist ID exists → Create task in Todoist (`main`, output 1, input 0)
- Prepare summary data → Merge summary (`main`, output 0, input 2)
- Convert to HTML Table → Generate email body (`main`, output 0, input 0)
- Create task in Notion → Execution Data2 (`main`, output 0, input 0)
- Create task in Notion → Turn Markdown into Notion Blocks (`main`, output 0, input 0)
- Map Notion to Todoist → Compare Datasets (`main`, output 0, input 0)
- Map Todoist to Notion → Map summary fields (`main`, output 0, input 0)
- Notion Task not found → Check if creating flag exists1 (`main`, output 0, input 0)
- Notion Task not found → Execution Data3 (`main`, output 1, input 0)
- Prepare summary data1 → Merge summary (`main`, output 0, input 3)
- Prepare summary data2 → Merge summary (`main`, output 0, input 4)
- Update task in Notion → Lock Notion ID (`main`, output 0, input 0)
- Verify security token → Exchange Tokens (`main`, output 0, input 0)
- Verify security token → Respond with error (`main`, output 1, input 0)
- Choose Notion Database → Get Notion Database ID (`main`, output 0, input 0)
- Choose Todoist Project → Get Todoist Project ID (`main`, output 0, input 0)
- Create task in Todoist → Store Todoist ID (`main`, output 0, input 0)
- Create task in Todoist → Lock Todoist ID (`main`, output 0, input 0)
- Delete Task in Todoist → Prepare summary data2 (`main`, output 0, input 0)
- Get Backlog Section ID → Generate UUID1 (`main`, output 0, input 0)
- Get Backlog Section ID → Create task in Notion (`main`, output 0, input 0)
- Get Notion Database ID → Get projects (`main`, output 0, input 0)
- Get Todoist Project ID → Get sections (`main`, output 0, input 0)
- Map Notion to Todoist1 → Handle empty dates1 (`main`, output 0, input 0)
- Map Notion to Todoist2 → Execution Data6 (`main`, output 0, input 0)
- Map Todoist to Notion1 → Execution Data1 (`main`, output 0, input 0)
- Mark as Done in Notion → Lock Notion ID (`main`, output 0, input 0)
- Prepare Batching Items → Aggregate (`main`, output 0, input 0)
- Update Task in Todoist → Status changed (`main`, output 0, input 0)
- Update Task in Todoist → Lock Todoist ID2 (`main`, output 0, input 0)
- Update Task in Todoist → Prepare summary data (`main`, output 0, input 0)
- Update task in Todoist → Get mapped item (`main`, output 0, input 0)
- Create task in Todoist1 → Store Todoist ID1 (`main`, output 0, input 0)
- Create task in Todoist1 → Lock Todoist ID4 (`main`, output 0, input 0)
- Delete Task in Todoist2 → Get todoist ID1 (`main`, output 0, input 0)
- Generate security token → Store variables (`main`, output 0, input 0)
- Has not been completed? → Mark as In Progress in Notion (`main`, output 0, input 0)
- Has not been completed? → Neither focussed nor planned1 (`main`, output 0, input 0)
- Has not been completed? → Mark as Done in Notion (`main`, output 1, input 0)
- Update task in Todoist1 → Get todoist ID (`main`, output 0, input 0)
- If event is not :deleted → Set tries2 (`main`, output 0, input 0)
- If event is not :deleted → Get Notion Task2 (`main`, output 1, input 0)
- Notion trigger reference → Globals2 (`main`, output 0, input 0)
- Notion trigger reference → Execution Data5 (`main`, output 0, input 0)
- Split out Notion changes → Extract IDs (`main`, output 0, input 0)
- Filter out status changes → Map Todoist to Notion (`main`, output 0, input 0)
- Todoist trigger reference → Execution Data (`main`, output 0, input 0)
- Todoist trigger reference → Globals1 (`main`, output 0, input 0)
- Update section (Sync API) → Loop Over Items1 (`main`, output 0, input 0)
- Exists/Completed in Notion → Map Notion to Todoist1 (`main`, output 0, input 0)
- Exists/Completed in Notion → Delete Task in Todoist (`main`, output 1, input 0)
- Mark as Focussed in Notion → Lock Notion ID (`main`, output 0, input 0)
- Mark as Obsolete in Notion → Lock Notion ID (`main`, output 0, input 0)
- Requires completion change → Has been completed? (`main`, output 0, input 0)
- Update section (Sync API)2 → Get todoist ID (`main`, output 0, input 0)
- Only continue if not locked → If event is not :deleted (`main`, output 0, input 0)
- Requires completion change1 → Has not been completed? (`main`, output 0, input 0)
- Check if Notion ID is locked → Only continue if not locked1 (`main`, output 0, input 0)
- Handle each block separately → Append Notion Block (`main`, output 0, input 0)
- Mark as Completed in Todoist → Prepare summary data1 (`main`, output 0, input 0)
- Neither focussed nor planned → Todoist ID exists (`main`, output 0, input 0)
- Neither focussed nor planned → Todoist ID exists? (`main`, output 1, input 0)
- Only continue if not locked1 → Get Notion task (`main`, output 0, input 0)
- Status changed but not empty → Generate UUID2 (`main`, output 0, input 0)
- Todoist Webhook Setup Helper → Generate security token (`main`, output 0, input 0)
- Check if Todoist ID is locked → Only continue if not locked (`main`, output 0, input 0)
- Check if creating flag exists → Only continue if flag does not exist (`main`, output 0, input 0)
- Mark as Completed in Todoist1 → Get todoist ID (`main`, output 0, input 0)
- Mark as In Progress in Notion → Lock Notion ID (`main`, output 0, input 0)
- Mark as Incomplete in Todoist → Update task in Todoist (`main`, output 0, input 0)
- Mark as Incomplete in Todoist → Lock Todoist ID (`main`, output 0, input 0)
- Neither focussed nor planned1 → Mark as Focussed in Notion (`main`, output 0, input 0)
- Check if creating flag exists1 → Only continue if flag does not exist1 (`main`, output 0, input 0)
- Mark as Incomplete in Todoist1 → Get todoist ID (`main`, output 0, input 0)
- Notion-Todoist Sync Setup Helper → Get Notion Databases (`main`, output 0, input 0)
- Turn Markdown into Notion Blocks → Handle each block separately (`main`, output 0, input 0)
- Description has changed in Todoist → Update Description in Todoist1 (`main`, output 0, input 0)
- Only continue if flag does not exist → Set creating flag (`main`, output 0, input 0)
- Only continue if flag does not exist1 → Set creating flag1 (`main`, output 0, input 0)
- Update task in Todoist before closing → Status is Done (`main`, output 0, input 0)
- Update task in Todoist before closing → Lock Todoist ID1 (`main`, output 0, input 0)

## Verification and provenance

Selected from 4 collected snapshots. Deduplication is not a runtime audit. Known selection findings: `{}`.

Source: [https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1897_Webhook_Filter_Sync_Webhook.json](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Webhook/1897_Webhook_Filter_Sync_Webhook.json). License: **MIT**; preserve [the notice](../../licenses/zie619-mit.txt) and embedded attribution. Matching source filename and node-name lineage; original nodes may precede upstream transformations.

Publication edits remove credential bindings, pinned/runtime data, detected secrets and selected personal/resource identifiers; they may require manual configuration. Annotation is a static inventory, not an AI-generated or runtime-verified explanation. Original source files are preserved locally.
