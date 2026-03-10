# HR Attrition Analytics & Predictive Data Modeling

## Executive Summary
This project outlines an enterprise-grade analytical model focused on Human Resources attrition metrics. By synthesizing organizational data points traversing demographic factors, compensation parity, and corporate tenure, this analysis isolates core drivers of voluntary employee turnover. The fundamental objective is augmenting the human capital strategy by transitioning from reactive backfilling to proactive organizational retention.

## Business Context
Employee attrition incurs significant operational costs stemming from expedited recruitment, onboarding cycles, and systemic domain knowledge depletion. Identifying correlational root causes and modeling future flight risk enables localized, strategic HR interventions. This repository houses the data engineering pipeline, analytical models, and visualization schematics designed to extract actionable intelligence on workforce stability.

## Data Architecture Profile
The underlying data model relies on a structured workforce dataset configured to encapsulate the following dimensions:
- **Employee Identifiers:** Unique alphanumeric enterprise tags ensuring row-level operational granularity.
- **Demographics:** Age profiling to ascertain generational turnover trends across the labor continuum.
- **Organizational Hierarchy:** Departmentation and functional Job Roles mapped to internal operations.
- **Geospatial Factors:** Distance From Home, serving as an empirical proxy for commute fatigue.
- **Compensation & Tenure:** Monthly Income scales and continuous Years At Company.
- **Target Variable:** Binary Attrition flag (Yes/No) representing historical turnover.

*(Note: The primary dataset is synthetically engineered via a Python pipeline utilizing Pandas and NumPy to mimic representative enterprise distributions under strict data privacy constraints.)*

## Analysis & Formulation Methodology
The reporting layer is driven by dimensional data models configured via Data Analysis Expressions (DAX). The suite of KPIs is formulated to calculate absolute attrition, measure departmental variance against overarching corporate averages, and identify multi-factor high-risk employee populations.

For comprehensive architectural details concerning DAX definitions and dashboard topological schema, refer to `DAX_and_Dashboard_Architecture.md`.

## Dashboard Output Modality
The resulting strategic Power BI dashboard operates on the following analytical pillars:
1. **Executive Scorecard:** Macro-level performance indicators tracking total headcount and enterprise-level turnover rates.
2. **Departmental Diagnostics:** Granular decomposition of retention baseline performance across independent business units.
3. **Flight Risk Cross-Sections:** Correlational evaluations demonstrating the intersection of commute proximity, compensation tiers, and turnover predictability.
