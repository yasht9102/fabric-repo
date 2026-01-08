hey, this is RAG\_CI-CD sytem



\# Fabric Git RAG POC



\## Overview



This repository is a \*\*proof of concept (POC)\*\* that mimics how a \*\*Microsoft Fabric workspace\*\* integrates with \*\*Git\*\* to enable \*\*enterprise-grade CI/CD\*\* and \*\*AI-assisted development using RAG (Retrieval-Augmented Generation)\*\*.



The repository structure represents Fabric artifacts such as Lakehouse tables, data pipelines, notebooks, and Power BI metadata, all managed through Git as the \*\*single source of truth\*\*.



---



\## Objectives



The main goals of this POC are:



\- Demonstrate \*\*Git-centric development\*\* similar to Fabric Git integration

\- Enable \*\*branch-based CI/CD workflows\*\* (feature → main)

\- Build a \*\*RAG system\*\* that understands repository metadata

\- Enable an \*\*AI assistant\*\* to:

&nbsp; - Answer questions about data lineage and artifacts

&nbsp; - Propose safe changes via feature branches

&nbsp; - Raise Pull Requests instead of modifying production directly



---



\## Repository Structure



```text

fabric-repo/

│

├── lakehouse/

│   └── tables/

│       └── sales.sql              # Lakehouse Delta table definition

│

├── pipelines/

│   └── pl\_sales\_ingestion.json    # Data pipeline metadata

│

├── notebooks/

│   └── nb\_sales\_transform.py      # Transformation logic

│

├── powerbi/

│   └── sales\_report.md            # Power BI semantic metadata

│

├── metadata/

│   └── workspace.md               # Workspace-level documentation

│

└── README.md                      # Repository overview (this file)



