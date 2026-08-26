---
title: Tines University
aliases: []
tags:
- topic/tines
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: tines.md
related_tools:
- '[[Case]]'
- '[[Group]]'
- '[[Note]]'
- '[[Page]]'
- '[[Record]]'
- '[[Run Script]]'
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

# Tines University

## Tines University Overview
Tines University provides information on the foundational concepts of Tines, including rules-based automation, AI-driven agents, and human-in-the-loop decisions.

## Tines Foundations

- **Rules-based automation**: Predictable, repeatable tasks that follow clear logic. Examples include routing tickets based on priority, enriching alerts with threat intelligence, or sending scheduled reports.

- **AI-driven agents**: Systems that can reason, adapt, and make decisions in uncertain contexts. Examples include summarizing incident reports, triaging alerts based on patterns, or drafting responses to common requests, handling tasks that would traditionally require human judgment.

- **Human-in-the-loop decisions**: Moments where human judgment, creativity, and oversight are essential. Some decisions are too important, too nuanced, or too high-stakes to be handled by automated systems alone.

The best intelligent workflow opportunities share the following key characteristics:

- **Repetitive**: The task happens regularly (daily, weekly, or triggered by specific events).
- **Time-consuming**: It takes significant time away from higher-value work.
- **Rule-based**: The task follows a predictable pattern or set of steps.
- **Multi-system**: It requires pulling data from or pushing data to multiple tools.
- **Error-prone**: Manual steps create opportunities for mistakes or inconsistencies.

## Introduction to Stories
A **story** is the core building experience in Tines. Each story represents a complete process that orchestrates multiple actions to achieve a specific outcome. The Storyboard is the literal location within the Tines UI where you design and build the workflow, similar to a blueprint.

## Kickoff
Every story starts with an initiating action or tool; something that says 'it's time to run!' This could be:
- A Webhook action receiving data from another service.
- A Receive Email action detecting a new message.
- A scheduled HTTP Request action.
- A Page where users submit information.

## Actions and Tools
##### actions

**Actions** are the individual steps that actually make things happen in your workflow. Tines offers eight action types, each performing different tasks. We'll delve into each action type in more detail later in the Actions module.

**AI Agent**
Uses a connected AI model to analyze/summarize data from multiple sources (Task mode), as well as act as an interactive AI-powered chat interface (Chat mode).
- **Task mode**
  - Intake support requests, summarize them, and recommend next steps.
- **Chat mode**
  - Empower employees to report suspicious activity, and the agent helps discern the type (i.e., phishing, vulnerability, etc.).

**Event Transform**
Modifies or restructures data. The Event Transform action (ETA for short) helps you clean, format, or reshape the data flowing through your story.
- Extract only key details (like usernames or timestamps) from an incoming event before sending it onward.

**HTTP Request**
Sends, retrieves, or updates data to/from an external tool using an API.
- Pull the latest alerts from a security platform or send updates to a ticketing tool.

**Receive Email**
Monitors a linked mailbox and pulls in incoming emails.
- Process incoming support emails and extract ticket numbers automatically.

**Send Email**
Sends an email to one or more recipients.
- Send an introduction email on a new hire's first day.

**Send to Story**
Reuse logic or processes by calling another story from within your current one.
- Feed alert data from multiple stories into one central 'notification' story that sends out communications.

**Condition**
Controls when the next step of a story runs based on defined conditions.
- Continue the story only if an alert’s severity is 'critical.'

**Webhook**
Receives pushed data from external tools. The Webhook action acts as a door into your story. It receives incoming data from external systems and turns it into an event.
- New pull request data coming in from your team's repository.

##### tools

**Tools** are features that extend what you can do beyond just the core logic of actions. They provide you with additional ways to interact with your stories and, more broadly, your workflows.

Tool | What it does
--- | ---
Case | (Paid feature) Mechanism for tracking investigation on an issue or workflow. Actions, notes, and records can be linked together within a case.
Group | A way to organize a sequence of actions within a story that can be executed from a single starting point to generate a specified output.
Note | An annotation you can add to the storyboard to provide context, reminders, or instructions for your story.
Page | A customizable web interface that can connect to actions and other tools within stories, allowing end users to provide input to and view output from stories.
Record | (Paid feature) Stores structured information in Tines, allowing you to track, update, and reference data across stories.
Run Script | Allows you to leverage the power of Python code and AWS CLI commands directly in your story. Recommended for users familiar with scripting languages.

## Events
**Events** are the output generated by actions in Tines. Think of events as the information highway of your story. They carry the data from one action/tool to the next, ensuring that every step has the context it needs to do its job. We'll explain events in more detail later on in the Events module.

Each event represents a moment in your story. For example, when an HTTP Request action retrieves data from an API, the response data is captured as an event. When a Send Email action runs, the details of the sent email also become an event.

Every event in Tines is a JSON object, meaning that events have clear keys and values, making the data easy to read and reference. This structure also ensures that the data remains consistent as it moves through your story.

## Events and Story Runs
### Events and Story Runs
- Events are immutable, meaning once created, they can’t be changed. This provides a reliable audit trail.
- Each event is timestamped, so you always know when it was generated.
- Events are chainable, allowing information to flow smoothly between actions.

##### Story Runs
These individual action events are stored in the story’s runs, which serve as a history of everything that has happened during execution. You can view each story run completed via the three-dot menu > Story runs.

- A unique identifier called a Story Run GUID.
- How many events occurred during the story run.
- When the story run started and when it completed.
- The duration of the story run execution.

## Reference Upstream Event Data
##### Reference Upstream Event Data
Each new action in a story can reference data from previous events. This is known as referencing upstream event data. Essentially, you can tell a later action, 'Use this piece of data from a previous step.'

Tines handles this referencing automatically as your story runs. Each connected action reads the data it needs from earlier events, uses it, and then creates a new event with its own results. This “flow”, one event feeding the next, is what makes stories dynamic. Instead of every action working in isolation, your story becomes a living chain of connected data.

## Pills
##### Pills
Pills are placeholders for data that exists in your story. They let you quickly reference information created by prior connected action events. When your story runs, Tines replaces the pill with the actual data it represents. There are two main types of pills you’ll see:

- Value pills: Represent dynamic data coming from earlier events or data transformed by Tines functions.
- Tag pills: Represent specific, static values such as text you entered manually. It is also primarily used to implement Tags.

![alt text](_archive/_bravo/media/logscale/image-4.png)

## Resources
Library: A collection of prebuilt, ready-to-use Tines stories that demonstrate real-world intelligent workflows. Browse and clone templates to jump-start your own workflows; no need to start from scratch.

Tines API: A dedicated reference for the Tines REST API. Use it to understand available endpoints, authentication, and how to programmatically create, manage, or query Tines elements. Perfect for those integrating Tines with other systems.

Tines Community: A collaborative, free Slack space where Tines users connect, share ideas, ask questions, and learn from one another. Join discussions, showcase your stories, and see what others are building. You can sign up here.

Tines Docs: Your go-to hub for official Tines product documentation. Discover how every Tines feature works, from Actions and Stories to integrations and advanced configuration options. Ideal for exploring product manual material. Note: We also offer our documentation offline for self-hosted customers on v40.1 or later.

Tines Explained: A learning-focused knowledge base that breaks down Tines how-tos, best practices, frequently asked questions (FAQs), and troubleshooting in an approachable language. Great for quick reference and deeper understanding of how and why Tines works the way it does.

What's New: Stay up-to-date with the latest Tines product updates. This feed highlights everything new in Tines.

**Resources** store non-sensitive, reusable information that teams can reference across multiple workflows (contains configuration settings, lookup tables and reference data, lists of approved values (i.e., approved domains, email addresses)). They should be organised in folders as well. Resources are shared using the same process as credentials. When you share a resource, other teams can reference it in their workflows. If you update the resource, all workflows using it (across all teams) will automatically use the updated version.

As a tenant owner, consider these practices for effective management:
- **Establish naming conventions**: Create and enforce consistent naming standards across teams (for example, ServiceName_CredentialType_Environment).
- **Regular audits**: Periodically review which credentials and resources are shared tenant-wide and whether that access is still appropriate.
- **Folder standards**: Define standard folder structures that teams should use, making it easier to navigate credentials and resources across your tenant.
- **Change management**: For widely-shared resources, establish a process for communicating changes to affected teams before updates are made.
- **Access reviews**: Regularly review which teams have access to shared credentials and resources, especially after organizational changes.

## Team Menu
Team-specific elements: The following components will display for the team you are currently viewing (depending on your permissions):

- Credentials: Your team's credentials.
- Collections: Your team's page collections.
- Pages: Pages that exist throughout your entire team's stories.
- Active change requests: (Paid feature) Currently active story change requests.
- Resources: Your team's resources.
- Archived stories: Stories that have been archived within the team.
- Manage team: Settings for managing team values, such as name, users, and notifications.
- Team selector: Switch between different teams you belong to, including your Personal team.
- Templates: Access to your private templates.
- Users: Tenant user list.
- Reporting: Analytics of build components, such as the number of license flows in use, most used resources and credentials, and AI credit usage.
- Tenant health: Health and monitoring of story run statistics across the tenant.
- Settings: More tenant-level settings.

## Storyboard
Editor panel: On the left-hand side of the storyboard, the Editor panel includes our eight actions, tools, and templates.

Storyboard: At the center stage, the storyboard is where you can drag-and-drop actions and tools, connect them together, and really bring your story to life.

Properties panel: On the right-hand side of the storyboard, the Properties panel includes configurable settings for the element of the storyboard you have selected. For example, if you click on an action on your storyboard, the Properties panel will display configuration settings for that action. If you ever need to view the story-level configuration, click on the white space of your storyboard.

## Platform Administrator
Users can only perform actions on objects owned by teams they're members of. If they're on the Marketing team, they can work with that team's workflows, credentials, and resources. But they can't touch what belongs to the IT Operations team unless they're also a member of that team.

Tenant owners, on the other hand, can perform actions on any object in the tenant, regardless of which team owns it. That includes:

- Viewing and editing any workflow (even other users' drafts)
- Managing all credentials and resources across the tenant
- Accessing pages created by any team
- Provisioning and removing user access
- Configuring tenant-wide security and authentication settings
- Deleting queued or retrying jobs (on dedicated tenants)
- Managing object sharing permissions across teams

## Tenant
This section contains your most frequently accessed settings (this section will be headed by your tenant domain):

**Users**: This is where you'll manage who has access to your tenant. You can invite new users, assign roles, adjust access levels, and organize people into teams. Think of this as your user directory.

**Roles**: Create and manage custom roles with specific permissions tailored to your organization's needs. Custom roles allow you to define granular access controls beyond the standard team roles.

**Credentials**: This gives you a bird's-eye view of all credentials connected across your tenant. You can search through them, control which teams can access specific credentials, filter by usage or domain restriction, and delete credentials that are no longer needed. (Note: you can't create new credentials from this view, only manage existing ones.)

**Page access**: This shows you all the pages created in Tines across your tenant. You can preview them, view them in their associated workflows, and customize settings.

**Custom Runtimes**: Configure custom runtime environments for executing code in your workflows. This allows you to define specialized execution environments when the default options don't meet your requirements.

**Billing**: View and manage your subscription, usage, and payment details for your Tines tenant (available for cloud tenants).

## Configurations
This section is all about how your tenant behaves:

**Action settings**: Configure default behaviors for actions across your environment. This includes settings for code execution, pages, and MCP servers.

**AI settings**: Manage how AI capabilities work within Tines. You'll control access to AI agents, configure which models to use, and set usage parameters.

**Change control**: Implement governance for workflow modifications. This is where you enable draft and approval processes to prevent unauthorized changes to production workflows.

**Feature flags**: Toggle experimental or optional capabilities on or off. This gives you control over new features and beta functionality as provided by the Tines team.

**Event limit settings**: Manage the maximum number of events your tenant can process. You can set threshold alerts and add notification recipients.

## Access & security
This is where you'll configure how people access your tenant and what security controls are in place:

**Authentication**: Configure how users log in. This includes setting up single sign-on (SSO), managing session timeouts, and configuring user provisioning.

**API keys**: Create, rotate, and revoke API keys that allow external systems to interact with your Tines instance.

**Login notice**: Customize messages displayed to users during login (useful for compliance notifications or important announcements).

**Command over HTTP**: Configure the command-over-http service that allows your Tines tenant to make programmatic calls to systems running on your private network, which may not have HTTP interfaces.

**Tunnel**: Manage tunnel containers that enable secure connections between Tines and resources on your private network. HTTP requests can be sent through tunnels to access internal systems.

**Action egress control rules**: Configure allowlists to restrict where HTTP Request Actions can send data. Control outbound connections by specifying approved IP addresses or domains.

**Custom cert authority**: Upload custom CA certificates for connections with internal systems using self-signed certificates.

**Story syncing**: Set up automatic synchronization of stories to destination teams or tenants. When changes are published to the live version of synced stories, they're automatically updated in all configured destinations.

**Credential access**: Manage how credentials can be accessed and used across your tenant. This is where you configure domain restrictions and credential usage policies.

**Story allocation**: Manage the number of stories each team can create.

**Sender emails**: Add custom email addresses for notifications sent from Tines.

## Monitoring
This section helps you keep tabs on what's happening in your tenant:

**Audit logs**: Review a comprehensive history of activities within your environment. This is essential for security monitoring, compliance reporting, and troubleshooting.

## First steps
1. Review authentication settings

Authentication is your tenant's front door. Understanding how it's currently configured helps you know whether users log in with email and password, or if your organization uses a different method. You'll learn how to configure these settings in detail in the Authentication module.

2. Review current user base

This gives you a snapshot of your tenant's user community. You might discover users who no longer need access, or realize you need to invite new team members. You'll learn the details of user management and provisioning in the Roles and user management module.

3. Explore the team structure

Teams determine who can access which workflows, credentials, and resources. You'll learn how to manage teams and their components in detail in the Team component management module.

4. Audit logs

Audit logs are essential for security monitoring and troubleshooting. Getting comfortable with where they are and what they look like will help you later when you need to investigate an issue or track down a change. You'll learn more about using audit logs for security and compliance in the Security and compliance module.

5. Check event usage

Understanding your event usage helps you know if your tenant is operating within normal capacity or if you're approaching limits. You'll learn more about monitoring and managing tenant operations in the Tenant health and operations module.

6. Documentation

Documentation provides a reference for the future and helps track the evolution of your tenant. As you continue through this learning path, you'll find yourself adding more detail to this documentation.

## Team component management
Teams in Tines provide logical separation of users, credentials, resources, and stories. Think of teams as containers that organize your workflows and other Tines interactions. Team members can only access the components of teams they belong to, unless they're a tenant owner. This means a member of the Finance team won't be able to see or modify the IT Operations team's credentials or stories, keeping work organized and secure.

Every user in Tines automatically gets their own personal team when they join your tenant, called **Personal**. Personal teams function as private, individual workspaces where users can build, test, and experiment with workflows before they're ready for production.

Team members will only be able to access components (credentials, resources, stories, cases, and records) that belong to and/or are explicitly shared with teams they're part of. However, tenant owners have a special status: they can access and manage all teams across the entire tenant, regardless of whether they're explicitly added as members.

## Credentials
Credentials store sensitive information like API tokens and passwords. As a tenant owner, your role with credentials isn't always about using them in workflows (that's covered more in our Builder learning path series). While builders create and reference credentials in their workflows, you ensure they're organized properly, shared appropriately, and secured in accordance with your organization's policies. Organise credentials with folders. Folders help you group related credentials together, making them easier to find and manage. When you share a credential with another team, that team can use the credential in their workflows without seeing the actual sensitive value. This maintains security while enabling collaboration.

Credential access control - credentials are only accessible to the team that created them. However, you can configure access control to share credentials across teams.

Some credentials and resources need to be available across your entire organization. These are called tenant-wide credentials or global resources. Common examples include:
- Company-wide API keys for shared services
- Enterprise authentication tokens
- Shared service account credentials
- Standard configuration settings that apply to all teams
- Shared lookup data used across departments

## Send to Story
Send to Story is a Tines feature that allows one workflow to trigger another workflow. When you enable Send to Story for a workflow and configure its access, other teams can call that workflow from their own stories.

## Important
While credentials, resources, and stories can be shared across teams, some components are team-specific and cannot be shared. Cases and Records belong to the team where they were created and cannot be shared with other teams. This means:
- Cases created by the Finance team can only be accessed by Finance team members.
- Records associated with a team's workflows remain within that team.
- Tenant owners can access cases and records across all teams, but individual teams cannot share these components with each other.

https://bold-haze-7214.tines.com/webhook/story-a/14636928c8232e77a7e5c44ac314a423

## References
- https://www.tines.com/university/
- https://www.tines.com/university/platform-administrator/team-component-management/team-limits-and-allocations/

