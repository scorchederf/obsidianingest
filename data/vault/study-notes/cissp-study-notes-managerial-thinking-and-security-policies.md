---
title: CISSP Study Notes - Managerial Thinking and Security Policies
aliases: []
tags:
- topic/cissp
- topic/security-policy
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: isc2-cissp.md
related_tools: []
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# CISSP Study Notes - Managerial Thinking and Security Policies

## Introduction
- **You - advise- , you do not “do”**
- **Focus on**:
  - **Strategy**
  - **Priorities**
  - **Human safety**
  - **Business continuity**
  - **Protecting profits**
  - **Reducing liability and risk**
- **Due diligence (Do Detect)**: Practising the activities that maintain the due care effort.
- **Due care (Do Correct)**: Doing what a reasonable person would do in a given situation. It is sometimes called the “prudent man” rule.

## Due Diligence vs Due Care
- **Due Diligence (Do Detect)**: Doing appropriate research, planning, and evaluation before decisions. “Think before you act” Activities largely before the decision is made.
- **Due Care (Do Correct)**: Doing what a reasonable person would do in a given situation (“prudent man” rule). Actions that maintain and enforce security after decisions “Actions speak louder than words”
- Together they reduce senior management's culpability and downstream liability when a loss occurs.
- **Management Roles and Planning Horizons**
  - **IT Engineer**: Short-term, operational focus
  - **IT Director/Manager**: Midrange, tactical focus
  - **CISO**: Long-term, strategic focus, risk escalation point

## Risk Management
- **Risk Categories**:
  - **Damage**: Results in the physical loss of an asset or the inability to access the asset
  - **Disclosure**: Disclosing critical information regardless of where or how it was disclosed
  - **Losses**: These might be permanent or temporary and may include altered data or inaccessible data
- **Risk Factors**:
  - **Physical**: Such as natural disaster, power loss, or vandalism
  - **Malfunctions**: Failure of systems, networks, or peripherals
  - **Attacks**: Purposeful acts whether from the inside or the outside such as authorized disclosure
  - **Human errors**: Accidental incidents
  - **Application errors**: Failures of the application including the operating system
- **Risk Management Frameworks**:
  - **NIST SP 800-37 - Risk Management Framework (RMF)**: 
    1. **Prepare**: Set the stage, define goals, roles, risk limits, and strategies for the organization and specific system
    2. **Categorize**: Label the system's info by impact if something goes wrong (low, moderate, or high for confidentiality, integrity, or availability)
    3. **Select**: Choose security measures (from NIST SP 800-53) tailored to your system's risks, environment, and needs
    4. **Implement**: Install those controls and record how you did it, noting any shared parts or ongoing checks
    5. **Assess**: Test independently if controls do their job right, spotting gaps
    6. **Authorize**: A leader reviews risks and green-lights operation, owning any leftover issues
    7. **Monitor**: Track changes, threats, and control performance over time, fixing issues as they pop up

## Risk Analysis
- **Simple Risk Formula**: **Risk = Threat x Vulnerability**
- **Total Risk Formula**: **Total Risk = Threats x Vulnerabilities x Asset Value**
- **Quantitative vs Qualitative**
  - **Quantitative Risk Analysis**: Assigns dollar values to evaluate countermeasure effectiveness
    1. **Inventory assets and assign a value (Asset Value (AV))**
    2. **Identify threats. Research each asset and produce a list of all possible threats of each asset (and calculate Exposure Factor (EF) and Single Loss Expectancy (SLE))**
      - **Exposure Factor (EF)**: Percentage of loss an organization would experience if a specific asset were compromised in one incident (expressed as a percentage)
      - **Single Loss Expectancy (SLE)**: Cost associated with a single realized risk against a specific asset
      - **Example**: AV = $100,000, EF = 30% (as a decimal 0.30) → SLE = $30,000
    3. **Perform a threat analysis to calculate the likelihood of each threat being realized within a single year (the Annualized Rate of Occurrence (ARO))**
      - **Annualized Rate of Occurrence (ARO)**: Expected frequency with which a threat will occur in a single year (once every 10 years = 0.10, once a year = 1)
    4. **Estimate the potential loss by calculating the annualized loss expectancy (Annualized Loss Expectancy (ALE))**
      - **Annualized Loss Expectancy (ALE)**: Possible yearly cost of all instances of a specific realized threat against an asset
      - **Example**: AV = $200,000; EF = 50% → SLE = $100,000; ARO = 0.10 → ALE = $10,000
      - **The safeguards we put in place better not cost more than $10,000.**

## References
- https://www.youtube.com/playlist?list=PL7XJSuT7Dq_XPK_qmYMqfiBjbtHJRWigD

