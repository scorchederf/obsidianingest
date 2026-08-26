---
title: Broken Object Property Level Authorization
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 00-268-APIAttacks-05-BrokenObjectPropertyLevelAuthorization.pdf
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

# Broken Object Property Level Authorization

## Description
Broken Object Property Level Authorization is a category of vulnerabilities that encompasses two subclasses: Exposure and Mass Assignment. An API endpoint is vulnerable to Excessive Data Exposure if it reveals sensitive data to authorized users that they are not supposed to access. On the other hand, an API endpoint is vulnerable to Mass Assignment if it permits authorized users to manipulate sensitive object properties beyond their authorized scope, including modifying, adding, or deleting values.

## Exposure of Sensitive Information Due to Incompatible Policies
The first endpoint we will be practicing against is vulnerable to CWE-213, Exposure of Sensitive Information Due to Incompatible Policies. The admin of Inlanefreight E-Commerce Marketplace has provided us with the credentials of a customer, wanting us to assess what API vulnerabilities the user can exploit with their access roles. After invoking /api/v1/authentication/customers/sign-in to sign in as a customer and obtain a JWT, the user endpoint shows that we have the roles Suppliers_Get and Suppliers_GetAll. These sensitive fields should not be exposed to customers, as this allows them to circumvent the marketplace entirely and contact suppliers directly to purchase goods (at a discounted price). Additionally, this vulnerability benefits suppliers financially by enabling them to generate greater revenues without paying the marketplace fee. However, for the stakeholders of Inlanefreight E-Commerce Marketplace, this will negatively impact their revenues.

## Prevention
To mitigate the Excessive Data Exposure vulnerability, the /api/v1/suppliers endpoint should only return fields necessary for the customer's perspective. This can be achieved by returning a specific response Data Transfer Object (DTO) intended for customer visibility, rather than exposing the entire domain model used for database interaction.

## Improperly Controlled Modification of Dynamically-Determined Object
The /api/v1/supplier-companies/current-user endpoint shows that the supplier-company the currently authenticated supplier belongs to, 'PentesterCompany', has the isExemptedFromMarketplaceFee field set to 0, which equates to 0. Let us set it to 1, such that 'PentesterCompany' does not get included in the companies required to pay the marketplace fee; after doing so, the endpoint returns a success message. Because the endpoint mistakenly allows suppliers to update the value of a field that they should not have access to, this vulnerability allows supplier-companies to generate more revenue from all sales performed over the Inlanefreight E-Commerce Marketplace, as they will not be charged a marketplace fee. However, similar to the repercussions of the previous Exposure of Sensitive Information Due to Incompatible Policies vulnerability, the revenues of the stakeholders of Inlanefreight E-Commerce Marketplace will be negatively impacted.

## Prevention
To mitigate the Mass Assignment vulnerability, the /api/v1/supplier-companies/PATCH endpoint should restrict invokers from updating sensitive fields. Similar to addressing Excessive Data Exposure, this can be achieved by implementing a dedicated request DTO that includes only the fields intended for suppliers to modify.

## Exploitation
Connect to Pwnbox to exploit the vulnerabilities. The target is 94.237.49.212:57900 with user 'htbpentester5@hackthebox.com' and password 'HTBPentester5' to exploit another Excessive Data Exposure vulnerability and submit the flag. The target is 94.237.49.212:57900 with user 'htbpentester7@hackthebox.com' and password 'HTBPentester7' to exploit another Mass Assignment vulnerability and submit the flag.

## References
- https://academy.hackthebox.com/

