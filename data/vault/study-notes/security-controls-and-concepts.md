---
title: Security Controls and Concepts
aliases: []
tags:
- topic/security-controls
- topic/security-concepts
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: comptia-securityplus-701.md
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

# Security Controls and Concepts

## General Security Concepts
- Security controls
  - Security risks are out there
    - Many different categories and types to consider
  - Assets are also varied
    - Data, physical property, computer systems
  - Prevent security events, minimize the impact, and limit the damage
    - Security controls
  - Control categories
    - Technical controls
      - Controls implemented using systems
      - Operating system controls
      - Firewalls, anti-virus
    - Managerial controls
      - Administrative controls associated with security design and implementation
      - Security policies, standard operating procedures
    - Operational controls
      - Controls implemented by people instead of systems
      - Security guards, awareness programs
    - Physical controls
      - Limit physical access
      - Guard shack
      - Fences, locks
      - Badge readers
  - Preventive control types
    - Preventive
      - Block access to a resource
      - You shall not pass
        - Prevent access
      - Firewall rules
      - Follow security policy
      - Guard shack checks all identification
      - Enable door locks
    - Deterrent
      - Discourage an intrusion attempt
      - Does not directly prevent access
        - Make an attacker think twice
      - Application splash screens
      - Threat of demotion
      - Front reception desk
      - Posted warning signs
    - Detective
      - Identify and log an intrusion attempt
      - May not prevent access
        - Find the issue
          - Collect and review system logs
      - Review login reports
      - Regularly patrol the property
      - Enable motion detectors
    - Corrective
      - Apply a control after an event has been detected
      - Reverse the impact of an event
      - Continue operating with minimal downtime
        - Correct the problem
      - Restoring from backups can mitigate a ransomware infection
      - Create policies for reporting security issues
      - Contact law enforcement to manage criminal activity
      - Use a fire extinguisher
    - Compensating
      - Control using other means
      - Existing controls aren't sufficient
      - May be temporary
        - Prevent the exploitation of a weakness
          - Firewall blocks a specific application instead of patching the app
      - Implement a separation of duties
      - Require simultaneous guard duties
      - Generator used after power outage
    - Directive
      - Direct a subject towards security compliance
      - A relatively weak security control
        - Do this, please
      - Store all sensitive files in a protected folder
      - Create compliance policies and procedures
      - Train users on proper security policy
      - Post a sign for "Authorized Personnel Only"

## Control Categories
- Technical
  - Controls implemented using systems
  - Operating system controls
  - Firewalls, anti-virus
- Managerial
  - Administrative controls associated with security design and implementation
  - Security policies, standard operating procedures
- Operational
  - Controls implemented by people instead of systems
  - Security guards, awareness programs
- Physical
  - Limit physical access
  - Guard shack
  - Fences, locks
  - Badge readers

## Preventive Control Types
- Preventive
  - Block access to a resource
  - You shall not pass
    - Prevent access
  - Firewall rules
  - Follow security policy
  - Guard shack checks all identification
  - Enable door locks
- Deterrent
  - Discourage an intrusion attempt
  - Does not directly prevent access
    - Make an attacker think twice
  - Application splash screens
  - Threat of demotion
  - Front reception desk
  - Posted warning signs
- Detective
  - Identify and log an intrusion attempt
  - May not prevent access
    - Find the issue
      - Collect and review system logs
  - Review login reports
  - Regularly patrol the property
  - Enable motion detectors
- Corrective
  - Apply a control after an event has been detected
  - Reverse the impact of an event
  - Continue operating with minimal downtime
    - Correct the problem
  - Restoring from backups can mitigate a ransomware infection
  - Create policies for reporting security issues
  - Contact law enforcement to manage criminal activity
  - Use a fire extinguisher
- Compensating
  - Control using other means
  - Existing controls aren't sufficient
  - May be temporary
    - Prevent the exploitation of a weakness
      - Firewall blocks a specific application instead of patching the app
  - Implement a separation of duties
  - Require simultaneous guard duties
  - Generator used after power outage
- Directive
  - Direct a subject towards security compliance
  - A relatively weak security control
    - Do this, please
  - Store all sensitive files in a protected folder
  - Create compliance policies and procedures
  - Train users on proper security policy
  - Post a sign for "Authorized Personnel Only"

## Managing Security Controls
- These are not inclusive lists
  - There are many categories of control
  - Some organizations will combine types
- There are multiple security controls for each category and type
  - Some security controls may exist in multiple types or categories
  - New security controls are created as systems and processes evolve
  - Your organization may use very different controls
- Examples
  - Categories
    - Technical
      - Firewall
      - Splash screen
      - System logs
      - Backup recovery
      - Block instead of patch
      - File storage policies
    - Managerial
      - On-boarding policy
      - Demotion
      - Review login reports
      - Policies for reporting issues
      - Separation of duties
      - Compliance policies
    - Operational
      - Guard shack
      - Reception desk
      - Property patrols
      - Contact authorities
      - Require multiple security staff
      - Security policy training
    - Physical
      - Door lock
      - Warning signs
      - Motion detectors
      - Fire extinguisher
      - Power generator
      - Sign: Authorized Personnel Only

## The CIA Triad
- Combination of principles
  - The fundamentals of security
  - Sometimes referenced as the AIC Triad
- Confidentiality
  - Prevent disclosure of information to unauthorized individuals or systems
  - Certain information should only be known to certain people
    - Prevent unauthorized information disclosure
  - Encryption
    - Encode messages so only certain people can read it
  - Access controls
    - Selectively restrict access to a resource
  - Two-factor authentication
    - Additional confirmation before information is disclosed
- Integrity
  - Messages can't be modified without detection
    - Data is stored and transferred as intended
      - Any modification to the data would be identified
  - Hashing
    - Map data of an arbitrary length to data of a fixed length
  - Digital signatures
    - Mathematical scheme to verify the integrity of data
  - Certificates
    - Combine with a digital signature to verify an individual
  - Non-repudiation
    - Provides proof of integrity, can be asserted to be genuine
- Availability
  - Systems and networks must be up and running
    - Information is accessible to authorized users
      - Always at your fingertips
  - Redundancy
    - Build services that will always be available
  - Fault tolerance
    - System will continue to run, even when a failure occurs
  - Patching
    - Stability
    - Close security holes

## Non-repudiation
- You can't deny what you've said
  - There's no taking it back
- Sign a contract
  - Your signature adds non-repudiation
  - You really did sign the contract
  - Others can see your signature
    - Adds a different perspective for cryptography
- Proof of integrity
  - Proof of origin, with high assurance of authenticity
    - Verify data does not change
      - The data remains accurate and consistent
    - In cryptography, we use a hash
      - Represent data as a short string of text
      - A message digest, a fingerprint
    - If the data changes, the hash changes
      - If the person changes, you get a different fingerprint
    - Doesn't necessarily associate data with an individual
      - Only tells you if the data has changed
- Proof of origin
  - Prove the message was not changed
    - Integrity
      - Prove the source of the message
    - Authentication
      - Make sure the signature isn't fake
    - Non-repudiation
      - Sign with the private key
        - The message doesn't need to be encrypted
        - Nobody else can sign this (obviously)
      - Verify with the public key
        - Any change to the message will invalidate the signature
- Create a digital signature
  ![[assets/attachments/kb/training/isc2-cissp/image-4.png]]
- Verifying a digital signature
  ![[assets/attachments/kb/training/isc2-cissp/image-5.png]]

## Authentication, Authorization, and Accounting (AAA)
- AAA framework
  - Identification
    - This is who you claim to be
    - Usually your username
  - Authentication
    - Prove you are who you say you are
    - Password and other authentication factors
  - Authorization
    - Based on your identification and authentication, what access do you have?
  - Accounting
    - Resources used: Login time, data sent and received, logout time
- Authenticating systems
  - You have to manage many devices
    - Often devices that you'll never physically see
  - A system can't type a password
    - And you may not want to store one
  - How can you truly authenticate a device?
    - Put a digitally signed certificate on the device
  - Other business processes rely on the certificate
  - Access to the VPN from authorized devices
  - Management software can validate the end device
- Certificate authentication
  - ![[assets/attachments/kb/training/isc2-cissp/image-6.png]]
  - An organization has a trusted Certificate Authority (CA)
    - Most organizations maintain their own CAs
  - The organization creates a certificate for a device
  - And digitally signs the certificate with the organization's CA
  - The certificate can now be included on a device as an authentication factor
  - The CA's digital signature is used to validate the certificate
- Using an Authorization Model
- The user or device has now authenticated
  - To what do they now have access?
  - Time to apply an authorization model
  - Users and services -> data and applications
  - Associating individual users to access rights does not scale
  - Put an authorization model in the middle
    - Define by Roles, Organizations, Attributes, etc.
  - No authorization model
    - A simple relationship
      - User -> Resource
    - Some issues with this method
      - Difficult to understand why an authorization may exist
      - Does not scale
  - Using an authorization model
    - Add an abstraction
      - Reduce complexity
      - Create a clear relationship between the user and the resource
      - Administration is streamlined
      - Easy to understand the authorizations
      - Support any number of users or resources

## Gap Analysis
- Where you are compared with where you want to be
  - The “gap” between the two
- This may require extensive research
  - There’s a lot to consider
- This can take weeks or months
  - An extensive study with numerous participants
  - Get ready for emails, data gathering, and technical research
- Choosing the framework
  - Work towards a known baseline
    - This may be an internal set of goals
    - Some organizations should use formal standards
  - Determine the end goal
    - NIST Special Publication 800-171 Revision 2,
    - Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations
    - ISO/IEC 27001
      - Information security management systems
- Evaluate people and processes
  - Get a baseline of employees
    - Formal experience
    - Current training
    - Knowledge of security policies and procedures
- Examine the current processes
  - Research existing IT systems
  - Evaluate existing security policies
- Compare and contrast
  - The comparison
    - Evaluate existing systems
  - Identify weaknesses
    - Along with the most effective processes
  - A detailed analysis
    - Examine broad security categories
    - Break those into smaller segments
- The analysis and report
  - The final comparison
  - Detailed baseline objectives
  - A clear view of the current state
  - Need a path to get from the current security to the goal
    - This will almost certainly include time, money, and lots of change control
- Time to create the gap analysis report
  - A formal description of the current state
  - Recommendations for meeting the baseline
- Example gap analysis overview
  ![[assets/attachments/kb/training/isc2-cissp/image-7.png]]

## References
- https://drive.google.com/file/d/1XqZeBOM6JeR83Nce-k9aUkAZQV2denWs/view

