# Realtime Notion Todoist 2-way Sync Template

Adapt the published “Realtime Notion Todoist 2-way Sync Template” workflow to other implementations while preserving its documented behavior.

**Specification: source-derived draft.** The source contains 174 executable nodes and 197 connections. This draft is derived from the n8n export; it needs a human-reviewed purpose, input/output contract, and behavioral tests before a port can claim equivalence.

[Specification](specification.md) · [Machine-readable record](agent.json) · [Schemas](schemas/README.md) · [Fixtures](fixtures/README.md) · [Evidence](evaluations/README.md)

## Workflow

This initial Mermaid map preserves the source graph, including non-main connections and port numbers. It is an implementation-derived starting point for the shared design; it does not execute the workflow or prove its behavior. Disabled-node details and exact expressions remain in the source.

```mermaid
flowchart LR
  n0["Get projects"]
  n1["Get sections"]
  n2["Get Notion Databases"]
  n3["Prep Dropdown"]
  n4["Prep Dropdown1"]
  n5["Generate config"]
  n6["Choose Notion Database"]
  n7["Choose Todoist Project"]
  n8["Verify security token"]
  n9["Generate security token"]
  n10["Store variables"]
  n11["Get variables"]
  n12["Redirect to Auth Page"]
  n13["OAuth redirect"]
  n14["Exchange Tokens"]
  n15["Respond with success"]
  n16["Respond with error"]
  n17["Get Notion Database ID"]
  n18["Get Todoist Project ID"]
  n19["Notion-Todoist Sync Setup Helper"]
  n20["Todoist Webhook Setup Helper"]
  n21["Return config JSON"]
  n22["Todoist"]
  n23["Notion"]
  n24["Compare Datasets"]
  n25["Exists/Completed in Notion"]
  n26["Get Todoist Task"]
  n27["If Todoist ID exists"]
  n28["Store Todoist ID"]
  n29["Mark as Incomplete in Todoist"]
  n30["Mark as Completed in Todoist"]
  n31["Delete Task in Todoist"]
  n32["Loop Over Items"]
  n33["Get Notion Task"]
  n34["Update Task in Todoist"]
  n35["Pick Todoist Fields"]
  n36["Map Notion to Todoist"]
  n37["Update task in Todoist before closing"]
  n38["Map Notion to Todoist1"]
  n39["Handle empty dates"]
  n40["Handle empty dates1"]
  n41["Handle empty dates2"]
  n42["Create task in Todoist"]
  n43["Add project ID"]
  n44["Lock Todoist ID"]
  n45["Generate UUID"]
  n46["Update section #40;Sync API#41;"]
  n47["Status changed"]
  n48["Aggregate"]
  n49["Prepare Batching Items"]
  n50["Loop Over Items1"]
  n51["Status is Done"]
  n52["Lock Todoist ID1"]
  n53["Lock Todoist ID2"]
  n54["Update task in Todoist"]
  n55["Get mapped item"]
  n56["Get mapped item1"]
  n57["Schedule Trigger"]
  n58["Prepare summary data"]
  n59["Prepare summary data1"]
  n60["Merge"]
  n61["Prepare summary data2"]
  n62["Filter out status changes"]
  n63["Map Todoist to Notion"]
  n64["Map summary fields"]
  n65["Convert to HTML Table"]
  n66["Generate email body"]
  n67["Get mapped item2"]
  n68["Gmail"]
  n69["Merge summary"]
  n70["Globals"]
  n71["Execute Workflow Trigger"]
  n72["Differences exist1"]
  n73["Requires completion change1"]
  n74["Create task in Notion"]
  n75["Update task in Notion"]
  n76["Mark as Done in Notion"]
  n77["Mark as Obsolete in Notion"]
  n78["Mark as In Progress in Notion"]
  n79["Only continue if not locked"]
  n80["Lock Notion ID"]
  n81["Check if Todoist ID is locked"]
  n82["Update Description in Todoist"]
  n83["Description has changed in Todoist"]
  n84["Update Description in Todoist1"]
  n85["Generate UUID1"]
  n86["Update section #40;Sync API#41;1"]
  n87["Get Backlog Section ID"]
  n88["Notion Task not found"]
  n89["Check if creating flag exists1"]
  n90["Only continue if flag does not exist1"]
  n91["Set creating flag1"]
  n92["Neither focussed nor planned1"]
  n93["Mark as Focussed in Notion"]
  n94["Todoist trigger reference"]
  n95["Get Notion Task2"]
  n96["Notion Task found1"]
  n97["Switch by Event"]
  n98["If event is not :deleted"]
  n99["Execution Data"]
  n100["Execution Data1"]
  n101["Execution Data2"]
  n102["Execution Data3"]
  n103["Execution Data4"]
  n104["Globals1"]
  n105["Map Todoist to Notion1"]
  n106["Get Todoist Task1"]
  n107["Get Notion Task1"]
  n108["Requires completion change"]
  n109["Has been completed#63;"]
  n110["Differences exist"]
  n111["Only continue if not locked1"]
  n112["Check if Notion ID is locked"]
  n113["Get Notion task"]
  n114["Check if creating flag exists"]
  n115["Only continue if flag does not exist"]
  n116["Set creating flag"]
  n117["Todoist ID exists#63;"]
  n118["Get todoist ID"]
  n119["Todoist ID exists"]
  n120["Get todoist ID1"]
  n121["Status changed but not empty"]
  n122["Status is Obsolete#63;"]
  n123["Status is not Done"]
  n124["Neither focussed nor planned"]
  n125["Notion trigger reference"]
  n126["Notion Webhook"]
  n127["Store Todoist ID1"]
  n128["Mark as Completed in Todoist1"]
  n129["Update task in Todoist1"]
  n130["Globals2"]
  n131["Mark as Incomplete in Todoist1"]
  n132["Generate UUID2"]
  n133["Update section #40;Sync API#41;2"]
  n134["Lock Todoist ID4"]
  n135["Delete Task in Todoist2"]
  n136["Map Notion to Todoist2"]
  n137["Get Todoist Task2"]
  n138["Create task in Todoist1"]
  n139["Execution Data5"]
  n140["Execution Data6"]
  n141["Todoist Webhook"]
  n142["Execute Workflow"]
  n143["Extract IDs"]
  n144["Split out Notion changes"]
  n145["Body is array#63;"]
  n146["Switch by project"]
  n147["Webhook"]
  n148["Switch"]
  n149["Execute Workflow1"]
  n150["Due date empty"]
  n151["Has not been completed#63;"]
  n152["End here"]
  n153["Retry limit reached"]
  n154["Set tries"]
  n155["Update tries"]
  n156["Wait"]
  n157["Catch known error"]
  n158["If tries left"]
  n159["Retry limit reached1"]
  n160["Set tries1"]
  n161["Update tries1"]
  n162["Wait1"]
  n163["Catch known error1"]
  n164["If tries left1"]
  n165["Set tries2"]
  n166["Update tries2"]
  n167["Wait2"]
  n168["Catch known error2"]
  n169["If tries left2"]
  n170["Retry limit reached2"]
  n171["Turn Markdown into Notion Blocks"]
  n172["Handle each block separately"]
  n173["Append Notion Block"]
  n156 -->|"main out 0 to in 0"| n155
  n60 -->|"main out 0 to in 0"| n50
  n60 -->|"main out 0 to in 0"| n69
  n162 -->|"main out 0 to in 0"| n161
  n167 -->|"main out 0 to in 0"| n166
  n23 -->|"main out 0 to in 0"| n36
  n148 -->|"main out 0 to in 0"| n142
  n148 -->|"main out 1 to in 0"| n149
  n22 -->|"main out 0 to in 0"| n35
  n147 -->|"main out 0 to in 0"| n148
  n48 -->|"main out 0 to in 0"| n46
  n154 -->|"main out 0 to in 0"| n26
  n160 -->|"main out 0 to in 0"| n137
  n165 -->|"main out 0 to in 0"| n106
  n143 -->|"main out 0 to in 0"| n125
  n0 -->|"main out 0 to in 0"| n4
  n1 -->|"main out 0 to in 0"| n5
  n155 -->|"main out 0 to in 0"| n158
  n45 -->|"main out 0 to in 0"| n49
  n11 -->|"main out 0 to in 0"| n8
  n158 -->|"main out 0 to in 0"| n154
  n158 -->|"main out 1 to in 0"| n153
  n69 -->|"main out 0 to in 0"| n62
  n3 -->|"main out 0 to in 0"| n6
  n161 -->|"main out 0 to in 0"| n164
  n166 -->|"main out 0 to in 0"| n169
  n43 -->|"main out 0 to in 0"| n27
  n145 -->|"main out 0 to in 0"| n144
  n145 -->|"main out 1 to in 0"| n125
  n150 -->|"main out 0 to in 0"| n93
  n99 -->|"main out 0 to in 0"| n81
  n85 -->|"main out 0 to in 0"| n86
  n132 -->|"main out 0 to in 0"| n133
  n118 -->|"main out 0 to in 0"| n134
  n164 -->|"main out 0 to in 0"| n160
  n164 -->|"main out 1 to in 0"| n159
  n169 -->|"main out 0 to in 0"| n165
  n169 -->|"main out 1 to in 0"| n170
  n126 -->|"main out 0 to in 0"| n145
  n13 -->|"main out 0 to in 0"| n11
  n4 -->|"main out 0 to in 0"| n7
  n47 -->|"main out 0 to in 0"| n56
  n51 -->|"main out 0 to in 0"| n30
  n51 -->|"main out 1 to in 0"| n31
  n14 -->|"main out 0 to in 0"| n15
  n14 -->|"main out 1 to in 0"| n16
  n100 -->|"main out 0 to in 0"| n107
  n101 -->|"main out 0 to in 0"| n82
  n101 -->|"main out 0 to in 0"| n80
  n102 -->|"main out 0 to in 0"| n97
  n103 -->|"main out 0 to in 0"| n77
  n139 -->|"main out 0 to in 0"| n112
  n140 -->|"main out 0 to in 0"| n122
  n5 -->|"main out 0 to in 0"| n21
  n33 -->|"main out 0 to in 0"| n32
  n113 -->|"main out 0 to in 0"| n136
  n55 -->|"main out 0 to in 0"| n60
  n120 -->|"main out 0 to in 0"| n134
  n32 -->|"main out 0 to in 0"| n25
  n32 -->|"main out 1 to in 0"| n33
  n10 -->|"main out 0 to in 0"| n12
  n97 -->|"main out 0 to in 0"| n72
  n97 -->|"main out 0 to in 0"| n83
  n97 -->|"main out 1 to in 0"| n73
  n97 -->|"main out 2 to in 0"| n73
  n141 -->|"main out 0 to in 0"| n146
  n24 -->|"main out 0 to in 0"| n41
  n24 -->|"main out 2 to in 0"| n39
  n24 -->|"main out 3 to in 0"| n32
  n107 -->|"main out 0 to in 0"| n88
  n95 -->|"main out 0 to in 0"| n96
  n26 -->|"main out 0 to in 0"| n29
  n26 -->|"main out 1 to in 0"| n157
  n56 -->|"main out 0 to in 1"| n60
  n67 -->|"main out 0 to in 1"| n69
  n50 -->|"main out 1 to in 0"| n45
  n57 -->|"main out 0 to in 0"| n23
  n57 -->|"main out 0 to in 0"| n22
  n57 -->|"main out 0 to in 0"| n70
  n28 -->|"main out 0 to in 0"| n67
  n157 -->|"main out 0 to in 0"| n42
  n157 -->|"main out 1 to in 0"| n156
  n110 -->|"main out 0 to in 0"| n129
  n106 -->|"main out 0 to in 0"| n105
  n106 -->|"main out 1 to in 0"| n168
  n137 -->|"main out 0 to in 0"| n110
  n137 -->|"main out 0 to in 0"| n108
  n137 -->|"main out 0 to in 0"| n121
  n137 -->|"main out 1 to in 0"| n163
  n116 -->|"main out 0 to in 0"| n138
  n146 -->|"main out 0 to in 0"| n94
  n119 -->|"main out 0 to in 0"| n135
  n163 -->|"main out 0 to in 0"| n123
  n163 -->|"main out 1 to in 0"| n162
  n168 -->|"main out 0 to in 0"| n152
  n168 -->|"main out 1 to in 0"| n167
  n72 -->|"main out 0 to in 0"| n75
  n72 -->|"main out 0 to in 0"| n150
  n39 -->|"main out 0 to in 0"| n34
  n64 -->|"main out 0 to in 0"| n65
  n96 -->|"main out 0 to in 0"| n103
  n91 -->|"main out 0 to in 0"| n87
  n123 -->|"main out 0 to in 0"| n114
  n117 -->|"main out 0 to in 0"| n160
  n117 -->|"main out 1 to in 0"| n114
  n173 -->|"main out 0 to in 0"| n80
  n66 -->|"main out 0 to in 0"| n68
  n40 -->|"main out 0 to in 0"| n37
  n41 -->|"main out 0 to in 0"| n43
  n109 -->|"main out 0 to in 0"| n128
  n109 -->|"main out 1 to in 0"| n131
  n35 -->|"main out 0 to in 1"| n24
  n122 -->|"main out 0 to in 0"| n119
  n122 -->|"main out 1 to in 0"| n124
  n2 -->|"main out 0 to in 0"| n3
  n27 -->|"main out 0 to in 0"| n154
  n27 -->|"main out 1 to in 0"| n42
  n58 -->|"main out 0 to in 2"| n69
  n65 -->|"main out 0 to in 0"| n66
  n74 -->|"main out 0 to in 0"| n101
  n74 -->|"main out 0 to in 0"| n171
  n36 -->|"main out 0 to in 0"| n24
  n63 -->|"main out 0 to in 0"| n64
  n88 -->|"main out 0 to in 0"| n89
  n88 -->|"main out 1 to in 0"| n102
  n59 -->|"main out 0 to in 3"| n69
  n61 -->|"main out 0 to in 4"| n69
  n75 -->|"main out 0 to in 0"| n80
  n8 -->|"main out 0 to in 0"| n14
  n8 -->|"main out 1 to in 0"| n16
  n6 -->|"main out 0 to in 0"| n17
  n7 -->|"main out 0 to in 0"| n18
  n42 -->|"main out 0 to in 0"| n28
  n42 -->|"main out 0 to in 0"| n44
  n31 -->|"main out 0 to in 0"| n61
  n87 -->|"main out 0 to in 0"| n85
  n87 -->|"main out 0 to in 0"| n74
  n17 -->|"main out 0 to in 0"| n0
  n18 -->|"main out 0 to in 0"| n1
  n38 -->|"main out 0 to in 0"| n40
  n136 -->|"main out 0 to in 0"| n140
  n105 -->|"main out 0 to in 0"| n100
  n76 -->|"main out 0 to in 0"| n80
  n49 -->|"main out 0 to in 0"| n48
  n34 -->|"main out 0 to in 0"| n47
  n34 -->|"main out 0 to in 0"| n53
  n34 -->|"main out 0 to in 0"| n58
  n54 -->|"main out 0 to in 0"| n55
  n138 -->|"main out 0 to in 0"| n127
  n138 -->|"main out 0 to in 0"| n134
  n135 -->|"main out 0 to in 0"| n120
  n9 -->|"main out 0 to in 0"| n10
  n151 -->|"main out 0 to in 0"| n78
  n151 -->|"main out 0 to in 0"| n92
  n151 -->|"main out 1 to in 0"| n76
  n129 -->|"main out 0 to in 0"| n118
  n98 -->|"main out 0 to in 0"| n165
  n98 -->|"main out 1 to in 0"| n95
  n125 -->|"main out 0 to in 0"| n130
  n125 -->|"main out 0 to in 0"| n139
  n144 -->|"main out 0 to in 0"| n143
  n62 -->|"main out 0 to in 0"| n63
  n94 -->|"main out 0 to in 0"| n99
  n94 -->|"main out 0 to in 0"| n104
  n46 -->|"main out 0 to in 0"| n50
  n25 -->|"main out 0 to in 0"| n38
  n25 -->|"main out 1 to in 0"| n31
  n93 -->|"main out 0 to in 0"| n80
  n77 -->|"main out 0 to in 0"| n80
  n108 -->|"main out 0 to in 0"| n109
  n133 -->|"main out 0 to in 0"| n118
  n79 -->|"main out 0 to in 0"| n98
  n73 -->|"main out 0 to in 0"| n151
  n112 -->|"main out 0 to in 0"| n111
  n172 -->|"main out 0 to in 0"| n173
  n30 -->|"main out 0 to in 0"| n59
  n124 -->|"main out 0 to in 0"| n119
  n124 -->|"main out 1 to in 0"| n117
  n111 -->|"main out 0 to in 0"| n113
  n121 -->|"main out 0 to in 0"| n132
  n20 -->|"main out 0 to in 0"| n9
  n81 -->|"main out 0 to in 0"| n79
  n114 -->|"main out 0 to in 0"| n115
  n128 -->|"main out 0 to in 0"| n118
  n78 -->|"main out 0 to in 0"| n80
  n29 -->|"main out 0 to in 0"| n54
  n29 -->|"main out 0 to in 0"| n44
  n92 -->|"main out 0 to in 0"| n93
  n89 -->|"main out 0 to in 0"| n90
  n131 -->|"main out 0 to in 0"| n118
  n19 -->|"main out 0 to in 0"| n2
  n171 -->|"main out 0 to in 0"| n172
  n83 -->|"main out 0 to in 0"| n84
  n115 -->|"main out 0 to in 0"| n116
  n90 -->|"main out 0 to in 0"| n91
  n37 -->|"main out 0 to in 0"| n51
  n37 -->|"main out 0 to in 0"| n52
```

[Diagram source](workflow.mmd)

## Implementations

| Implementation | Status |
|---|---|
| [n8n](implementations/n8n/README.md) | Sanitized source available; not runtime-tested |
| [Plain Python](implementations/python/README.md) | Planned |
| [Pydantic AI](implementations/pydantic-ai/README.md) | Planned |
| [CrewAI Flow](implementations/crewai-flow/README.md) | Planned |
| [CrewAI Crew](implementations/crewai-crew/README.md) | Planned |
| [LangGraph](implementations/langgraph/README.md) | Planned |

## Build or operate with an assistant

[Claude](prompts/claude.md) · [Codex](prompts/codex.md) · [Grok Bot](prompts/grok-bot.md) · [Muse](prompts/muse.md) · [Dots](prompts/dots.md)

Build instructions and operating instructions are separate. These are untested prompts, not additional working implementations.

## Attribution

Curated by Nik Bear Brown. Preserve the [n8n source provenance](implementations/n8n/provenance.json), [configuration record](implementations/n8n/configuration.json), and [license notice](../../licenses/zie619-mit.txt). Ported implementations must retain applicable upstream attribution; the repository has no blanket license replacing source licenses.
