---
title: "AGS4 Reference"
description: "A brief introduction to the AGS4 geotechnical data
format."
---

[AGS4](https://www.ags.org.uk/data-format/ags4-data-format/) is a
standardized text file format specifically designed for exchanging
geotechnical information between different software systems used in
geotechnical engineering. It organizes borehole logs, laboratory test
results, and field measurements into structured data tables with
validation rules to ensure consistent data quality across the
geotechnical industry.

## Groups

In the AGS4 format, **Groups** are organizational containers that
structure geotechnical data. Each Group represents a specific aspect of
geotechnical investigation, for example, project information (PROJ),
location details (LOCA), sample information (SAMP), or specific test
types like Standard Penetration Tests (ISPT).

AGS4 Groups are organised in a hierarchical manner. Each **sample**
(SAMP) belongs to a **location** (LOCA). Each **location** belongs to a
**project** (PROJ).

Here’s a visual of the hierarchy of groups commonly found in an AGS4
file.

<svg viewBox="-12,-24,402,424" style="max-width: 100%; height: auto; font: 13px sans-serif;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

<g fill="none" stroke="#999"><path d="&#10;M0,0&#10;V24&#10;h24&#10;"/><path d="&#10;M0,0&#10;V264&#10;h24&#10;"/><path d="&#10;M0,0&#10;V288&#10;h24&#10;"/><path d="&#10;M0,0&#10;V312&#10;h24&#10;      "/><path d="&#10;M0,0&#10;V336&#10;h24&#10;"/><path d="&#10;M24,24&#10;V48&#10;h24&#10;"/><path d="&#10;M24,24&#10;V144&#10;h24&#10;"/><path d="&#10;M24,24&#10;V192&#10;h24&#10;"/><path d="&#10;M24,24&#10;V216&#10;h24&#10;"/><path d="&#10;M24,24&#10;V240&#10;h24&#10;"/><path d="&#10;M48,48&#10;V72&#10;h24&#10;"/><path d="&#10;M48,48&#10;V120&#10;h24&#10;"/><path d="&#10;M48,144&#10;V168&#10;h24&#10;"/><path d="&#10;M72,72&#10;V96&#10;h24&#10;"/></g><g><g transform="translate(0,0)"><circle cx="0" r="2.5"/><text dy="0.32em" x="6"><tspan font-weight="600">PROJ</tspan><tspan dx="2">Project
information</tspan></text>
<title>

PROJ
</title>

</g><g transform="translate(0,24)"><circle cx="24" r="2.5"/><text dy="0.32em" x="30"><tspan font-weight="600">LOCA</tspan><tspan dx="2">Location
details</tspan></text>
<title>

PROJ/LOCA
</title>

</g><g transform="translate(0,264)"><circle cx="24" r="2.5" fill="#999"/><text dy="0.32em" x="30"><tspan font-weight="600">ABBR</tspan><tspan dx="2">Abbreviation
Definitions</tspan></text>
<title>

PROJ/ABBR
</title>

</g><g transform="translate(0,288)"><circle cx="24" r="2.5" fill="#999"/><text dy="0.32em" x="30"><tspan font-weight="600">TRAN</tspan><tspan dx="2">Data
File Transmission Information / Data Status</tspan></text>
<title>

PROJ/TRAN
</title>

</g><g transform="translate(0,312)"><circle cx="24" r="2.5" fill="#999"/><text dy="0.32em" x="30"><tspan font-weight="600">TYPE</tspan><tspan dx="2">Definition
of Data Types</tspan></text>
<title>

PROJ/TYPE
</title>

</g><g transform="translate(0,336)"><circle cx="24" r="2.5" fill="#999"/><text dy="0.32em" x="30"><tspan font-weight="600">UNIT</tspan><tspan dx="2">Definition
of Units</tspan></text>
<title>

PROJ/UNIT
</title>

</g><g transform="translate(0,48)"><circle cx="48" r="2.5"/><text dy="0.32em" x="54"><tspan font-weight="600">SAMP</tspan><tspan dx="2">Sample
information</tspan></text>
<title>

PROJ/LOCA/SAMP
</title>

</g><g transform="translate(0,144)"><circle cx="48" r="2.5"/><text dy="0.32em" x="54"><tspan font-weight="600">IPRG</tspan><tspan dx="2">In
Situ permeability</tspan></text>
<title>

PROJ/LOCA/IPRG
</title>

</g><g transform="translate(0,192)"><circle cx="48" r="2.5" fill="#999"/><text dy="0.32em" x="54"><tspan font-weight="600">GEOL</tspan><tspan dx="2">Geological
descriptions</tspan></text>
<title>

PROJ/LOCA/GEOL
</title>

</g><g transform="translate(0,216)"><circle cx="48" r="2.5" fill="#999"/><text dy="0.32em" x="54"><tspan font-weight="600">BKFL</tspan><tspan dx="2">Backfill
details</tspan></text>
<title>

PROJ/LOCA/BKFL
</title>

</g><g transform="translate(0,240)"><circle cx="48" r="2.5" fill="#999"/><text dy="0.32em" x="54"><tspan font-weight="600">ISPT</tspan><tspan dx="2">Standard
Penetration Test</tspan></text>
<title>

PROJ/LOCA/ISPT
</title>

</g><g transform="translate(0,72)"><circle cx="72" r="2.5"/><text dy="0.32em" x="78"><tspan font-weight="600">GRAG</tspan><tspan dx="2">Particle
size distribution analysis</tspan></text>
<title>

PROJ/LOCA/SAMP/GRAG
</title>

</g><g transform="translate(0,120)"><circle cx="72" r="2.5" fill="#999"/><text dy="0.32em" x="78"><tspan font-weight="600">LNMC</tspan><tspan dx="2">Water
content</tspan></text>
<title>

PROJ/LOCA/SAMP/LNMC
</title>

</g><g transform="translate(0,168)"><circle cx="72" r="2.5" fill="#999"/><text dy="0.32em" x="78"><tspan font-weight="600">IPRT</tspan><tspan dx="2">In
Situ permeability data</tspan></text>
<title>

PROJ/LOCA/IPRG/IPRT
</title>

</g><g transform="translate(0,96)"><circle cx="96" r="2.5" fill="#999"/><text dy="0.32em" x="102"><tspan font-weight="600">GRAT</tspan><tspan dx="2">Particle
size distribution analysis data</tspan></text>
<title>

PROJ/LOCA/SAMP/GRAG/GRAT
</title>

</g></g>
</svg>

<details>

<summary>

All Groups Hierarchy Tree
</summary>

While AGS defines a load of groups, not all of them are used in every
project. For reference, here is the full hierarchy tree of all groups.

<svg viewBox="-8,-12,404,1264" style="max-width: 100%; height: auto; font: 10px sans-serif; overflow: visible;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

<g fill="none" stroke="#999"><path d="&#10; M0,0&#10; V16&#10; h16&#10;"/><path d="&#10; M0,0&#10; V1152&#10; h16&#10;"/><path d="&#10; M0,0&#10; V1168&#10; h16&#10; "/><path d="&#10; M0,0&#10; V1184&#10; h16&#10; "/><path d="&#10; M0,0&#10; V1200&#10; h16&#10; "/><path d="&#10; M0,0&#10; V1216&#10; h16&#10; "/><path d="&#10; M0,0&#10; V1232&#10; h16&#10; "/><path d="&#10; M16,16&#10; V32&#10; h16&#10; "/><path d="&#10; M32,32&#10; V48&#10; h16&#10; "/><path d="&#10; M32,32&#10; V576&#10; h16&#10; "/><path d="&#10; M32,32&#10; V592&#10; h16&#10; "/><path d="&#10; M32,32&#10; V608&#10; h16&#10; "/><path d="&#10; M32,32&#10; V624&#10; h16&#10; "/><path d="&#10; M32,32&#10; V640&#10; h16&#10; "/><path d="&#10; M32,32&#10; V672&#10; h16&#10; "/><path d="&#10; M32,32&#10; V688&#10; h16&#10; "/><path d="&#10; M32,32&#10; V704&#10; h16&#10; "/><path d="&#10; M32,32&#10; V720&#10; h16&#10; "/><path d="&#10; M32,32&#10; V736&#10; h16&#10; "/><path d="&#10; M32,32&#10; V768&#10; h16&#10; "/><path d="&#10; M32,32&#10; V784&#10; h16&#10; "/><path d="&#10; M32,32&#10; V848&#10; h16&#10; "/><path d="&#10; M32,32&#10; V864&#10; h16&#10; "/><path d="&#10; M32,32&#10; V880&#10; h16&#10; "/><path d="&#10; M32,32&#10; V896&#10; h16&#10; "/><path d="&#10; M32,32&#10; V912&#10; h16&#10; "/><path d="&#10; M32,32&#10; V928&#10; h16&#10; "/><path d="&#10; M32,32&#10; V944&#10; h16&#10; "/><path d="&#10; M32,32&#10; V960&#10; h16&#10; "/><path d="&#10; M32,32&#10; V976&#10; h16&#10; "/><path d="&#10; M32,32&#10; V992&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1008&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1024&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1056&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1072&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1088&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1120&#10; h16&#10; "/><path d="&#10; M32,32&#10; V1136&#10; h16&#10; "/><path d="&#10; M48,48&#10; V64&#10; h16&#10; "/><path d="&#10; M48,48&#10; V80&#10; h16&#10; "/><path d="&#10; M48,48&#10; V96&#10; h16&#10; "/><path d="&#10; M48,48&#10; V112&#10; h16&#10; "/><path d="&#10; M48,48&#10; V128&#10; h16&#10; "/><path d="&#10; M48,48&#10; V144&#10; h16&#10; "/><path d="&#10; M48,48&#10; V160&#10; h16&#10; "/><path d="&#10; M48,48&#10; V176&#10; h16&#10; "/><path d="&#10; M48,48&#10; V192&#10; h16&#10; "/><path d="&#10; M48,48&#10; V208&#10; h16&#10; "/><path d="&#10; M48,48&#10; V224&#10; h16&#10; "/><path d="&#10; M48,48&#10; V240&#10; h16&#10; "/><path d="&#10; M48,48&#10; V272&#10; h16&#10; "/><path d="&#10; M48,48&#10; V288&#10; h16&#10; "/><path d="&#10; M48,48&#10; V320&#10; h16&#10; "/><path d="&#10; M48,48&#10; V352&#10; h16&#10; "/><path d="&#10; M48,48&#10; V432&#10; h16&#10; "/><path d="&#10; M48,48&#10; V448&#10; h16&#10; "/><path d="&#10; M48,48&#10; V464&#10; h16&#10; "/><path d="&#10; M48,48&#10; V480&#10; h16&#10; "/><path d="&#10; M48,48&#10; V512&#10; h16&#10; "/><path d="&#10; M48,48&#10; V528&#10; h16&#10; "/><path d="&#10; M48,48&#10; V544&#10; h16&#10; "/><path d="&#10; M48,640&#10; V656&#10; h16&#10; "/><path d="&#10; M48,736&#10; V752&#10; h16&#10; "/><path d="&#10; M48,784&#10; V800&#10; h16&#10; "/><path d="&#10; M48,784&#10; V832&#10; h16&#10; "/><path d="&#10; M48,1024&#10; V1040&#10; h16&#10; "/><path d="&#10; M48,1088&#10; V1104&#10; h16&#10; "/><path d="&#10; M64,240&#10; V256&#10; h16&#10; "/><path d="&#10; M64,288&#10; V304&#10; h16&#10; "/><path d="&#10; M64,320&#10; V336&#10; h16&#10; "/><path d="&#10; M64,352&#10; V368&#10; h16&#10; "/><path d="&#10; M64,352&#10; V416&#10; h16&#10; "/><path d="&#10; M64,480&#10; V496&#10; h16&#10; "/><path d="&#10; M64,544&#10; V560&#10; h16&#10; "/><path d="&#10; M64,800&#10; V816&#10; h16&#10; "/><path d="&#10; M80,368&#10; V384&#10; h16&#10;"/><path d="&#10; M96,384&#10; V400&#10; h16&#10;"/></g><g><g transform="translate(0,0)"><circle cx="0" r="2"/><text dy="0.32em" x="6"><tspan font-weight="600">AGS4
file</tspan><tspan dx="2">-</tspan></text>
<title>

AGS4 file
</title>

</g><g transform="translate(0,16)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">PROJ</tspan><tspan dx="2">Project
Information</tspan></text>
<title>

AGS4 file/PROJ
</title>

</g><g transform="translate(0,1152)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">ABBR</tspan><tspan dx="2">Abbreviation
Definitions</tspan></text>
<title>

AGS4 file/ABBR
</title>

</g><g transform="translate(0,1168)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">DICT</tspan><tspan dx="2">User
Defined Groups and Headings</tspan></text>
<title>

AGS4 file/DICT
</title>

</g><g transform="translate(0,1184)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">FILE</tspan><tspan dx="2">Associated
Files</tspan></text>
<title>

AGS4 file/FILE
</title>

</g><g transform="translate(0,1200)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">TRAN</tspan><tspan dx="2">Data
File Transmission Information / Data Status</tspan></text>
<title>

AGS4 file/TRAN
</title>

</g><g transform="translate(0,1216)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">TYPE</tspan><tspan dx="2">Definition
of Data Types</tspan></text>
<title>

AGS4 file/TYPE
</title>

</g><g transform="translate(0,1232)"><circle cx="16" r="2"/><text dy="0.32em" x="22"><tspan font-weight="600">UNIT</tspan><tspan dx="2">Definition
of Units</tspan></text>
<title>

AGS4 file/UNIT
</title>

</g><g transform="translate(0,32)"><circle cx="32" r="2"/><text dy="0.32em" x="38"><tspan font-weight="600">LOCA</tspan><tspan dx="2">Location
Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA
</title>

</g><g transform="translate(0,48)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">SAMP</tspan><tspan dx="2">Sample
Information</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP
</title>

</g><g transform="translate(0,576)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">BKFL</tspan><tspan dx="2">Exploratory
Hole Backfill Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA/BKFL
</title>

</g><g transform="translate(0,592)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">CDIA</tspan><tspan dx="2">Casing
Diameter by Depth</tspan></text>
<title>

AGS4 file/PROJ/LOCA/CDIA
</title>

</g><g transform="translate(0,608)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">CHIS</tspan><tspan dx="2">Chiselling
Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA/CHIS
</title>

</g><g transform="translate(0,624)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">CORE</tspan><tspan dx="2">Coring
Information</tspan></text>
<title>

AGS4 file/PROJ/LOCA/CORE
</title>

</g><g transform="translate(0,640)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DCPG</tspan><tspan dx="2">Dynamic
Cone Penetrometer Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DCPG
</title>

</g><g transform="translate(0,672)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DETL</tspan><tspan dx="2">Stratum
Detail Descriptions</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DETL
</title>

</g><g transform="translate(0,688)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DISC</tspan><tspan dx="2">Discontinuity
Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DISC
</title>

</g><g transform="translate(0,704)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DLOG</tspan><tspan dx="2">Driller
Geological Description</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DLOG
</title>

</g><g transform="translate(0,720)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DOBS</tspan><tspan dx="2">Drilling/Advancement
Observations & Parameters</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DOBS
</title>

</g><g transform="translate(0,736)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DPRG</tspan><tspan dx="2">Dynamic
Probe Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DPRG
</title>

</g><g transform="translate(0,768)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">DREM</tspan><tspan dx="2">Depth
Related Remarks</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DREM
</title>

</g><g transform="translate(0,784)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">FGHG</tspan><tspan dx="2">Field
Geohydraulic Testing - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FGHG
</title>

</g><g transform="translate(0,848)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">FLSH</tspan><tspan dx="2">Drilling
Flush Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FLSH
</title>

</g><g transform="translate(0,864)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">FRAC</tspan><tspan dx="2">Fracture
Spacing</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FRAC
</title>

</g><g transform="translate(0,880)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">GEOL</tspan><tspan dx="2">Field
Geological Descriptions</tspan></text>
<title>

AGS4 file/PROJ/LOCA/GEOL
</title>

</g><g transform="translate(0,896)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">HDIA</tspan><tspan dx="2">Hole
Diameter by Depth</tspan></text>
<title>

AGS4 file/PROJ/LOCA/HDIA
</title>

</g><g transform="translate(0,912)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">HDPH</tspan><tspan dx="2">Depth
Related Exploratory Hole Information</tspan></text>
<title>

AGS4 file/PROJ/LOCA/HDPH
</title>

</g><g transform="translate(0,928)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">HORN</tspan><tspan dx="2">Exploratory
Hole Orientation and Inclination</tspan></text>
<title>

AGS4 file/PROJ/LOCA/HORN
</title>

</g><g transform="translate(0,944)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">ICBR</tspan><tspan dx="2">In
Situ California Bearing Ratio Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/ICBR
</title>

</g><g transform="translate(0,960)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IDEN</tspan><tspan dx="2">In
Situ Density Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IDEN
</title>

</g><g transform="translate(0,976)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IFID</tspan><tspan dx="2">On
Site Volatile Headspace Testing Using Flame Ionisation
Detector</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IFID
</title>

</g><g transform="translate(0,992)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IPEN</tspan><tspan dx="2">In
Situ Hand Penetrometer Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IPEN
</title>

</g><g transform="translate(0,1008)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IPID</tspan><tspan dx="2">On
Site Volatile Headspace Testing by Photo Ionisation
Detector</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IPID
</title>

</g><g transform="translate(0,1024)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IPRG</tspan><tspan dx="2">In
Situ Permeability Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IPRG
</title>

</g><g transform="translate(0,1056)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IRDX</tspan><tspan dx="2">In
Situ Redox Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IRDX
</title>

</g><g transform="translate(0,1072)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IRES</tspan><tspan dx="2">In
Situ Resistivity Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IRES
</title>

</g><g transform="translate(0,1088)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">ISAG</tspan><tspan dx="2">Soakaway
Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/ISAG
</title>

</g><g transform="translate(0,1120)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">ISPT</tspan><tspan dx="2">Standard
Penetration Test Results</tspan></text>
<title>

AGS4 file/PROJ/LOCA/ISPT
</title>

</g><g transform="translate(0,1136)"><circle cx="48" r="2"/><text dy="0.32em" x="54"><tspan font-weight="600">IVAN</tspan><tspan dx="2">In
Situ Vane Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IVAN
</title>

</g><g transform="translate(0,64)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">AAVT</tspan><tspan dx="2">Aggregate
Abrasion Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/AAVT
</title>

</g><g transform="translate(0,80)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ACVT</tspan><tspan dx="2">Aggregate
Crushing Value Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ACVT
</title>

</g><g transform="translate(0,96)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">AELO
</tspan><tspan dx="2">-</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/AELO
</title>

</g><g transform="translate(0,112)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">AFLK</tspan><tspan dx="2">Aggregate
Flakiness Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/AFLK
</title>

</g><g transform="translate(0,128)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">AIVT</tspan><tspan dx="2">Aggregate
Impact Value Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/AIVT
</title>

</g><g transform="translate(0,144)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ALOS</tspan><tspan dx="2">Los
Angeles Abrasion Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ALOS
</title>

</g><g transform="translate(0,160)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">APSV</tspan><tspan dx="2">Aggregate
Polished Stone Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/APSV
</title>

</g><g transform="translate(0,176)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ARTW</tspan><tspan dx="2">Aggregate
Determination of the Resistance to Wear (micro-Deval)</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ARTW
</title>

</g><g transform="translate(0,192)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ASDI</tspan><tspan dx="2">Slake
Durability Index Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ASDI
</title>

</g><g transform="translate(0,208)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ASNS</tspan><tspan dx="2">Aggregate
Soundness Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ASNS
</title>

</g><g transform="translate(0,224)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">AWAD</tspan><tspan dx="2">Aggregate
Water Absorption Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/AWAD
</title>

</g><g transform="translate(0,240)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">CBRG</tspan><tspan dx="2">California
Bearing Ratio Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CBRG
</title>

</g><g transform="translate(0,272)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">CHOC</tspan><tspan dx="2">Chain
of Custody Information</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CHOC
</title>

</g><g transform="translate(0,288)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">CMPG</tspan><tspan dx="2">Compaction
Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CMPG
</title>

</g><g transform="translate(0,320)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">CONG</tspan><tspan dx="2">Consolidation
Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CONG
</title>

</g><g transform="translate(0,352)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">CTRG</tspan><tspan dx="2">Cyclic
Triaxial Test - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CTRG
</title>

</g><g transform="translate(0,432)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ECTN</tspan><tspan dx="2">Sample
Container Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ECTN
</title>

</g><g transform="translate(0,448)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ELRG</tspan><tspan dx="2">Environmental
Laboratory Reporting</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ELRG
</title>

</g><g transform="translate(0,464)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ERES</tspan><tspan dx="2">Environmental
Contaminant Testing</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ERES
</title>

</g><g transform="translate(0,480)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ESCG</tspan><tspan dx="2">Effective
Stress Consolidation Tests - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ESCG
</title>

</g><g transform="translate(0,512)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">FRST</tspan><tspan dx="2">Frost
Susceptibility Tests</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/FRST
</title>

</g><g transform="translate(0,528)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">GCHM</tspan><tspan dx="2">Geotechnical
Chemistry Testing</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/GCHM
</title>

</g><g transform="translate(0,544)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">GRAG</tspan><tspan dx="2">Particle
Size Distribution Analysis - General</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/GRAG
</title>

</g><g transform="translate(0,656)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">DCPT</tspan><tspan dx="2">Dynamic
Cone Penetrometer Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DCPG/DCPT
</title>

</g><g transform="translate(0,752)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">DPRB</tspan><tspan dx="2">Dynamic
Probe Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/DPRG/DPRB
</title>

</g><g transform="translate(0,800)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">FGHI</tspan><tspan dx="2">Field
Geohydraulic Testing - Instrumentation Details</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FGHG/FGHI
</title>

</g><g transform="translate(0,832)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">FGHS</tspan><tspan dx="2">Field
Geohydraulic Testing - Test Results (per stage)</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FGHG/FGHS
</title>

</g><g transform="translate(0,1040)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">IPRT</tspan><tspan dx="2">In
Situ Permeability Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/IPRG/IPRT
</title>

</g><g transform="translate(0,1104)"><circle cx="64" r="2"/><text dy="0.32em" x="70"><tspan font-weight="600">ISAT</tspan><tspan dx="2">Soakaway
Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/ISAG/ISAT
</title>

</g><g transform="translate(0,256)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">CBRT</tspan><tspan dx="2">California
Bearing Ratio Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CBRG/CBRT
</title>

</g><g transform="translate(0,304)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">CMPT</tspan><tspan dx="2">Compaction
Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CMPG/CMPT
</title>

</g><g transform="translate(0,336)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">CONS</tspan><tspan dx="2">Consolidation
Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CONG/CONS
</title>

</g><g transform="translate(0,368)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">CTRC</tspan><tspan dx="2">Cyclic
Triaxial Tests - Consolidation</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CTRG/CTRC
</title>

</g><g transform="translate(0,416)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">CTRS</tspan><tspan dx="2">Cyclic
Triaxial Test - Saturation</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CTRG/CTRS
</title>

</g><g transform="translate(0,496)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">ESCT</tspan><tspan dx="2">Effective
Stress Consolidation Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/ESCG/ESCT
</title>

</g><g transform="translate(0,560)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">GRAT</tspan><tspan dx="2">Particle
Size Distribution Analysis - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/GRAG/GRAT
</title>

</g><g transform="translate(0,816)"><circle cx="80" r="2"/><text dy="0.32em" x="86"><tspan font-weight="600">FGHT</tspan><tspan dx="2">Field
Geohydraulic Testing - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/FGHG/FGHI/FGHT
</title>

</g><g transform="translate(0,384)"><circle cx="96" r="2"/><text dy="0.32em" x="102"><tspan font-weight="600">CTRP</tspan><tspan dx="2">Cyclic
Triaxial Test - Derived Parameters</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CTRG/CTRC/CTRP
</title>

</g><g transform="translate(0,400)"><circle cx="112" r="2"/><text dy="0.32em" x="118"><tspan font-weight="600">CTRD</tspan><tspan dx="2">Cyclic
Triaxial Tests - Data</tspan></text>
<title>

AGS4 file/PROJ/LOCA/SAMP/CTRG/CTRC/CTRP/CTRD
</title>

</g></g>
</svg>

</details>

``` {ojs}
viewof groupSearch = Inputs.search(ags4, {
  placeholder: "Search groups..."
})
```

``` {ojs}
viewof groupTable = Inputs.table(groupSearch, {
  format: { headings: (d) => d.map((h) => h.heading).join(", ") },
  multiple: false,
  layout: "auto"
})
```

``` {ojs}
ags4 = FileAttachment("ags4_data_dictionary.json").json()
```

## Headings

Headings are the specific data fields (i.e. the columns) within each
group that define individual data items. Each heading represents a
specific piece of information that can be recorded during geotechnical
investigations, such as sample depth, moisture content, or test result
values

Headings follow a standardized naming pattern, typically beginning with
the group name as a prefix (e.g., “PROJ_ID” for project identifier in
the PROJ group). Some headings are marked as required (\*R or R),
indicating that they must be populated in a valid AGS file to maintain
data integrity. Headings include additional information like units of
measurement, descriptions, and example values to help users understand
their purpose.

``` {ojs}
groupTable ? md`### ${groupTable.group_name}\n${groupTable.group_description}` : md`### Select a group in the table above to view its headings.`
```

``` {ojs}
groupTable
  ? Inputs.table(groupTable.headings, {
      layout: "auto",
      columns: ["heading", "description", "type", "unit", "example"],
      format: {
        type: (d) => (d in types ? types[d] : d),
        status: (d) => {
          switch (d) {
            case "*":
              return "KEY";
            case "R":
              return "Required";
            default:
              return "";
          }
        }
      }
    })
  : md`In the table above, select a group on the left side to view its headings here.`
```

``` {ojs}
types = ({
  ...Object.fromEntries(
    Array.from({ length: 5 }, (_, i) => i).map((i) => [
      `${i}DP`,
      `Value with ${i} required decimal places`
    ])
  ),
  ...Object.fromEntries(
    Array.from({ length: 4 }, (_, i) => i).map((i) => [
      `${i}SF`,
      `${i} sign. figures`
    ])
  ),
  DT: "Datetime",
  T: "Time elapsed",
  X: "Text",
  YN: "Yes/no",
  ID: "Unique Identifier",
  XN: "Text/numeric",
  PA: "Text listed in ABBR Group",
  PU: "Text listed in UNIT Group",
  U: "Value with a variable format"
})
```
