FALCON 100: Falcon Platform Architecture Overview
FALCON 101: Falcon Platform Technical Fundamentals
FALCON 104: Introduction to Endpoint Security
FALCON 106: Customizable Dashboards
FALCON 109: Using MITRE Att&ck and Falcon Detection Methods to Understand Security Risk

https://falcon.us-2.crowdstrike.com/documentation/page/e3ce0b24/events-data-dictionary

- For known threats, Falcon provides cloud-based antivirus (Cloud AV) and Indicators of Compromise (IOC) detection capabilities.
- For unknown and zero-day threats, Falcon applies IOA detection, using machine learning techniques to build predictive models that can detect never-before-seen malicious activities with high accuracy. 

# create new user
- Host setup and managenemtn
    - Use Management
        - Create User
            - if using sso 
                - the users email address must exactly match the information in you identity provider
                - the user will NOT receive an email from Crowdstrike after account creation
            - else
                - the user will recieve an email from Crowdstrike asking them to generate a new password and configure MFA

# Create prevention policy
- Endpoint Security
    - Prevention policies
        - Create new policy
            - Select platform, name and description
        - Modify policy
            - [ ] check current policy
        - Enable / disable policy

# Create Hosts
- Host setup and managment
    - Host groups
        - dynamic groups are defined by attributes which uatomatically add or remove hosts to groups
        - static groups are added manually via importing of hostnames or via the console


# Asign Hosts to Prevention Policies
- Endpoint Security
    - Prevention Policies
        - everything is covered by a default policy unless the sensor is targetted by a custom policy

# Detections
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-3.png>)
- Endpoint security
    - Endpoint Detections
        - Assign task to user by clicking `Edit Status` - select `Assigned To` ddl and update status
        - Can also do bulk status updates

- detection times are local times

# Incidents
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-2.png>)
- made up of detections and associated proceses
- clicking on the incident brings up the [NETWORK CONTAIN] button

# Investigate
- Hosts
    - search by hostname
        - host details
        - detections
- Hash search only works on binary files (not pdfs, docs, etc)
- User
- domain search

- detections drilldown
    - icons on the left highlight bad events
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image.png>)

## Manage API keys
- Support and resources
    - API clients and keys
        - ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-1.png>)


# falcon-104-getting-started-with-the-endpoint-security-module

# quarantined files
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-4.png>)

# on demand scans
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-5.png>)

# remediation
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-6.png>)

# firewall activity
- can be run in monitor mode temporarily
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-7.png>)

# dashboards
- Next-Gen SIEM> Log management > Dashboards and lookup 'SOC Efficacy'
- 





indicator of attack is a collection of suspicious behavours
indicator of compromise is for example a malicious file

aid = Every sensor in your environment is uniquely identified by its Agent ID (AID). This means that if you have 5,000 sensors, you will have 5,000 unique AIDs
cid = The Customer ID (CID) is used to identify customer environments. Every environment has a unique CID.
pattern id = Every detection is associated with a pattern, and each pattern has a unique ID, called a Pattern ID.

Icon color, which indicates severity
Critical: Red
High: Orange
Medium: Yellow
Low: Green
Informational: Blue

There are things that security tools detect on, display or record that don’t fit into the MITRE framework. These are referred to as the Falcon Detection Method (FDM). The FDM tactics and techniques highlight behavior considered suspicious and malicious, and worth investigating.
- examples
    - Signature based detections for things like known malware and adware like ransomware or other destructive malware.
    - Machine learning based detections.
    - Threat Intelligence based detections.
    - Detections discovered through the hunting efforts of our Overwatch team (which ultimately might fit other tactics and techniques as well).


Detections = objectives + tactics + techniques

To understand why a detection is triggering, an analyst must also understand the objective, the tactic and its technique
    Objective: The thing aimed at or sought after; a goal.
    Tactic: An action or strategy carefully planned to achieve a specific end.
    Technique: A skillful or efficient way of doing or achieving something.

Objective: Trying to Gain Access
Tactic: By Privilege Escalation
Technique: Using Process Injection


# falcon-114-falcon-fusion-soar-fundamentals
trigger -> condition -> action 
- The Content Library in Falcon Fusion SOAR serves as a centralized repository for predefined and reusable components used in creating and managing workflows and playbooks. It includes templates, actions, conditions, triggers, and other resources that streamline the development and deployment of automated workflows.
- Playbooks in Falcon Fusion SOAR are predefined or custom-configurable sets of automated workflows designed to streamline and orchestrate security operations. They integrate triggers, conditions, and actions to automate repetitive tasks, ensure consistent responses, and enhance the efficiency of security teams.
- In Falcon Fusion SOAR, Apps refer to modular, pre-built integrations or connectors that enable seamless communication between the Falcon platform and third-party tools, services, or systems. These apps allow users to automate workflows, exchange data, and execute actions across their security and IT ecosystems without requiring extensive custom development.
- trigger 
    - Falcon Fusion SOAR uses triggers to initiate workflows based on specific events, schedules, or on demand. Each trigger type serves a unique purpose and is highly configurable to fit various use cases.
    - Event: Based on an event
    - Schedule: Based on a schedule
    - On demand: Manual execution
    - ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-8.png>)
    - request input from the soc manager to isolate an endpoint
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-9.png>)
    - malicious file removal
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-10.png>)
- condition
    - Workflows can be refined by adding one or more conditions.
- action
    - define what happens when the trigger event occurs and any applicable conditions are met.
- Falcon Foundry is CrowdStrike’s low-code application platform for users to build security and IT solutions that CrowdStrike does not provide out-of-the-box. It is the delivery mechanism that allows customers to integrate their third-party tools through applications by connecting via cloud APIs.
- workflow examples
    - anytime a workflow doesnt trigger, notification gets sent
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-11.png>)
    - 3 parallel workflows that send an email notification to each of the analyst teams anytime a policy is updated
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-12.png>)
    - This workflow is set to trigger when a new Incident comes in with lateral movement occurring and it includes host tags. The workflow will perform 2 Real Time Response actions at the same time, including retrieving network connections and running processes. Once the Retrieve active network connections action completes, the workflow will add an incident tag and create a PagerDuty incident. If the machine does not have a host tag, the workflow will still run the Real Time Response commands and set the incident status, but also contain the device and send a message to Slack.
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-13.png>)
    - In this playbook, when a new Incident comes in with Lateral Movement and an Incident score equal to or greater than 7.4, Fusion SOAR performs a couple of Real time Response actions and requests human intervention. The workflow sends an email to either approve, decline or escalate the remediation of the Incident. There are conditional workflows for each potential response. Once the human responds, the rest of that branch will run as defined.
    - This On demand workflow will network contain a device once an analyst triggers it and provides the host information. It will then create a ServiceNow ticket to notify the team about the network containment.
- [highly recommend looking at these workflows ](https://university.crowdstrike.com/learn/courses/474/falcon-114-falcon-fusion-soar-fundamentals/lessons/2163:935/fusion-soar-workflow-examples)
- ngsiem -> Fusion SOAR -> Dashboard
    - Quickly see which workflows have executed and whether they failed. 
    - Workflows using the Human input action need a manual approval. Quickly see pending approvals and act without having to look through the whole workflow list. 
    - Stay informed on when the next scheduled workflow is set to run.
    - Build On demand workflows to take break-glass actions across any security tool from a single pane of glass. Quickly find and run an On demand workflow.
    ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-14.png>)
    - where to run on demand workflows
    - 
    ```
    Workflow dashboard
    ----------------------
    1.  Navigate to **Fusion SOAR** or **Next-Gen SIEM.**
    2.  Select **Fusion SOAR > Dashboard.**
    3.  Find the **On demand** widget.
    4.  Click the **Execute workflow** icon.
    ```    
    - All workflows tab
    ```
    ---------------------
    1.  Navigate to **Fusion SOAR** or **Next-Gen SIEM.**
    2.  Select **Fusion SOAR > Workflows.**
    3.  Find the **All workflows** tab.
    4.  Open the Action menu for any workflow that meets the following requirements:
        1.  Trigger = **On demand** or **Scheduled**
        2.  Toggled **On**
    5.  Select **Execute workflow.**
    ```
    - Execution log
    ```
    -----------------
    1.  Navigate to **Fusion SOAR** or **Next-Gen SIEM.**
    2.  Select **Fusion SOAR > Workflows.**
    3.  Find the **Execution log** tab.
    4.  Open the Action menu for an **On demand** or **Scheduled** workflow.
        *   Find the **Trigger** column to see the trigger type.
    5.  Select **Execute workflow.**
    ```
    - Workflow page
    ```
    -----------------
    1.  Navigate to **Fusion SOAR** or **Next-Gen SIEM.**
    2.  Select **Fusion SOAR > Workflows.**
    3.  Select an **On demand** or **Scheduled** workflow and view the workflow page.
    4.  Open the Action menu on the top-right corner of the page.
    5.  Select **Execute workflow.**
    ```
    - API call
    ```
    ------------

    Provide either a workflow definition ID or a workflow name to trigger an on-demand workflow with this endpoint:

    *   POST /entities/execute/v1

    ![This API call uses a workflow name to trigger an on-demand workflow.](assets/APICall.jpg)
    ```
    - Next-Gen SIEM's Incident workbench
    ```
    --------------------------------------
    1.  Navigate to **Next-Gen SIEM.**
    2.  Select **Monitor and investigate > Detections and incidents.**
    3.  Select a detection to open the details panel on the right.
    4.  Click **See full detection** to navigate to the _Incident workbench._
    5.  Select an object from the **Workbench** to open the details panel on the right.
    6.  Scroll down to **On-demand workflows.**
    7.  Click the **Execute workflow** icon.
    ```
    - workflow changes are auditied
    - workflow executions are logged and can be "walked through"




# FALCON 115: Create a Falcon Fusion SOAR Workflow
Creating a simple event-based workflow with a trigger, condition and action
Adding sequential or parallel branches to a workflow
Adding looping to a workflow
Adding Else, If conditions and Else actions to workflows
Configuring an action with the form-based schema builder
Creating an on demand workflow

# FALCON 120: Investigation Fundamentals
The Falcon platform tools to use during an investigation
How to analyze threats
Searching for events using Investigate

endpoint activity - tracks processes, file executions, applicaiton behaviour and other endpoint activiites to detect anomolies or suspicious actions
network activity - Monitors network connections, both internal and external, identifying communication with known malicious IPs or domains, unusual traffic patterns, or unauthorized data transfers.
file and hashes - Tracks file creation, modification, and execution, as well as the associated file hashes (MD5, SHA-1, SHA-256) to detect malware, ransomware, or unauthorized changes.
user behaviour - Monitors user login activities, access patterns, and privilege escalations to detect unauthorized actions that could indicate account compromise or insider threats.
system and host information - Keeps an eye on host details such as system configurations, BIOS data, and operating system versions to identify outdated software, vulnerabilities, or signs of tampering.
threat intel - Correlates activity against global threat intelligence feeds, such as known IOCs, including malware signatures, suspicious domains, and so on.
malware and exploit attempts - Monitors for malware execution and exploits attempts, identifies and blocks malicious files and behaviors in real time.


![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-15.png>)
Current Crowdscore - This widget provides a real-time assessment of your organization’s security posture. Your CrowdScore reflects the potential risk of hostile activity targeting your organization. It operates on a scale from 0 to 100 and dynamically adjusts based on the highest-risk incident currently detected. The higher the CrowdScore, the greater the likelihood that a serious threat is actively impacting your environment.

new detections - This widget shows the number of newly identified threats or suspicious activities in your environment. These are fresh detection alerts generated by Falcon's detection engine. These can range from identifying a malicious file, flagged as an indicator of compromise (IOC), to recognizing more complex patterns of suspicious behavior, classified as an indicator of attack (IOA).

Prevented malware by host - This widget shows the number of malware attempts that Falcon has automatically blocked, broken down by individual hosts. It helps analysts identify which hosts have been targeted by malware and how effective the platform is at preventing those threats.

Total OverWatch-analyzed events - This widget shows the total number of security events that have been analyzed by CrowdStrike’s OverWatch team. It reflects the volume of events that have been reviewed and assessed by OverWatch analysts, helping you understand the level of expert human scrutiny applied to your environment and highlighting any high-risk activity that may require further investigation.

OverWatched detections triggered - This widget shows detections flagged by Falcon's OverWatch team—CrowdStrike's expert threat hunting service. These detections often involve sophisticated or stealthy threats that require human intelligence to identify. It provides visibility into high-priority threats that have been manually reviewed by security experts.

Total hunting leads requiring investigation - This widget displays the number of potential threats or indicators of compromise (IOCs) discovered during threat hunting that require further analysis. It highlights areas where proactive threat hunting has uncovered suspicious activities that need deeper investigation.

CrowdScore over time - This widget tracks the organization's CrowdScore, a real-time measure of the overall security health of your environment. It reflects the severity of active threats and incidents, helping analysts monitor how the threat landscape changes over time and prioritize response efforts based on risk.

Most recent detections - This widget allows you to quickly assess recent detections. Disposition icons indicate the severity of each detection and whether the activity was blocked, terminated, or flagged as an OverWatch alert. Most detections are generated in alignment with your prevention policy settings.


Step 1
Review Alerts on the Activity Dashboard
Falcon automatically flags suspicious behavior and generates detection alerts. Start by reviewing these alerts on the dashboard.

Step 2
Drill Down into Specific Alerts
Click on an alert to view its details, such as the type of threat (malware, ransomware, etc.), severity, and associated telemetry (e.g., process trees, file paths, etc.).

Step 3
Investigate the Detection
For each alert, investigate the origin of the event, such as the user, device, or process involved. Look for indicators of compromise (IOCs) like file hashes or IP addresses.

Step 4
Respond and Remediate
Based on the findings, take appropriate remediation actions such as isolating the device, terminating suspicious processes, or blocking certain network traffic.

![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/2025-07-16 10_49_37-FALCON 120_ Investigation Fundamentals - Module 1_ Investigation Fundamentals.png>)

![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-16.png>)

- investigate
    - bios tampering
        ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-18.png>)
    - hosts
        ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-17.png>)
        - **Host details** - View comprehensive information about the selected host, including system properties, user accounts, network interfaces, and installed software.
        - **Detections** - View the list of all security events or alerts associated with the host, allowing you to investigate and take action on specific detections like triaging, assigning, or resolving them.
        - **Processes and services** - View detailed information about running processes and services on the host. You can review active processes, check for any unusual or suspicious activity, and analyze services that may be associated with potential security risks.
        - **Command line and admin tools (Windows)** - Review the use of command-line actions and administrative tools on the host. You can detect and examine any potentially suspicious or unauthorized usage.
        - **Suspicious file activity** - View details about potentially malicious or unusual file actions on the host. These include executable activity and files written to removable media.  
        - **Registry, tasks and firewall** - View changes to the Windows registry, scheduled tasks on the host, and information about the host's firewall configuration and any modifications.
        - **Networking** - Review detailed information about the host's network connections. This includes active and historical connections, IP addresses, ports, protocols, and other relevant network activity, helping you identify potentially malicious or unauthorized connections.
    - geo location report
        ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-19.png>)


- Alerts
    - Notifications generated by the platform based on predefined rules that signal potential security incidents
- Detection
    - Refers to any event flagged by Falcon that indicates potential malicious behavior, requiring investigation.
- Event Timeline
    - A chronological view of events that allows analysts to trace back the origin and progression of an attack.
- Indicators of Compromise
    - A digital footprint left behind by malicious activity, such as a suspicious file hash, IP address, or domain.
- Process Tree
    - A hierarchical representation of processes initiated on an endpoint, which helps identify if malware has been executed.
- Remediation
    - Actions taken by administrators to neutralize a threat, such as isolating devices, terminating processes, or deleting malicious files.
- Telemetry Data
    - Detailed logs and data generated by endpoints that provide a rich source of information for threat analysis.
- 


# FALCON 140: Real Time Response Fundamentals
- not for chromeos
- roles
    - Real Time Response - Read Only Analyst: read only response commands to perform reconnaissance and triage
    - Real Time Responder - Active Responder: run all of the commands RTR Read Only Analyst can and more, including:
        - Extract files using the get command
        - Run commands that modify the state of the remote host
        - Run certain custom scripts 
    - Real Time Responder - Administrator 
        - This role can do everything RTR Active Responder can do, plus:
            - Create custom scripts
            - Upload files to hosts using the put command
            - Directly run executables using the run command
- commands and roles required

| Command   | RTR Read Only Analyst | RTR Active Responder | RTR Administrator |
|-----------|-----------------------|----------------------|-------------------|
| cat       | YES                   | YES                  | YES               |
| cd        | YES                   | YES                  | YES               |
| clear     | YES                   | YES                  | YES               |
| cp        | NO                    | YES                  | YES               |
| csrutil   | YES                   | YES                  | YES               |
| cswindiag | NO                    | NO                   | YES               |
| encrypt   | NO                    | YES                  | YES               |
| env       | YES                   | YES                  | YES               |
| eventlog  | YES                   | YES                  | YES               |
| falconscript | NO                  | NO                   | YES               |
| filehash  | YES                   | YES                  | YES               |
| get       | NO                    | YES                  | YES               |
| getsid    | YES                   | YES                  | YES               |
| help      | YES                   | YES                  | YES               |
| history   | YES                   | YES                  | YES               |
| ipconfig  | YES                   | YES                  | YES               |
| kill      | NO                    | YES                  | YES               |
| ls        | YES                   | YES                  | YES               |
| map       | NO                    | YES                  | YES               |
| memdump   | NO                    | YES                  | YES               |
| mkdir     | NO                    | YES                  | YES               |
| mount     | YES                   | YES                  | YES               |
| mv        | NO                    | YES                  | YES               |
| netstat   | YES                   | YES                  | YES               |
| ps        | YES                   | YES                  | YES               |
| put       | NO                    | NO                   | YES               |
| put-and-run | NO                   | NO                   | YES               |
| reg query | YES                   | YES                  | YES               |
| reg set   | NO                    | YES                  | YES               |
| reg delete| NO                    | YES                  | YES               |
| reg load  | NO                    | YES                  | YES               |
| reg unload| NO                    | YES                  | YES               |
| restart   | NO                    | YES                  | YES               |
| rm        | NO                    | YES                  | YES               |
| run       | NO                    | NO                   | YES               |
| runscript | NO                    | YES                  | YES               |
| shutdown  | NO                    | YES                  | YES               |
| tar       | NO                    | YES                  | YES               |
| unmount   | NO                    | YES                  | YES               |
| unmap     | NO                    | YES                  | YES               |
| update    | NO                    | YES                  | YES               |
| users     | YES                   | YES                  | YES               |
| xmemdump  | NO                    | YES                  | YES               |
| zip       | NO                    | YES                  | YES               |

- force reathentication for critical actions
![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-20.png>)
- response policies
    - If you need to prevent all RTR connections to a group of hosts, create and assign them to a response policy with RTR disabled.
- rtr
    - multiple users can connect to the same host at the same time
    - sessions end after 10 mins of inactivity
    - details panel
        - Host info tab - View attributes and metadata for the connected host, including: Response policy name: View the host’s associated response policy settings and Host ID: View the host details on the Host management page
        - Scripts tab - View Falcon scripts and your CID’s custom scripts that you can run on the host. Search for a script by name or sort the list of scripts by most recently used date or alphabetically by name. Click a script name to populate the command field. View details, insert, edit, or delete from the three-dot menu on the right of a specific script.
        - Files tab - View your CID’s existing list of uploaded “put” files that you can put onto the host. (Note that "put" files get uploaded from Host setup and management > Response and containment > Response scripts and files.) Click a file name to populate the command field.
    - Detections tab - View recent detections (within the last 90 days) that have occurred on the host. This is also helpful to be able to reference recent activity without leaving RTR.
    - run commands
        - general command format `command [subcommand] <arguments> <-Flags>`
            - `reg set "HKLM\Software\Some Key" MyNewValue -ValueType=REG_SZ -Value=MyStringValue`
        - `help`
        - type in command to see arguments
            ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-21.png>)
        - you can cancel commands (if taking to long) and they will continue to run in the background but you will not get any output
        - case sensitivity
            - Commands and subcommands are case sensitive and must be written with lowercase letters. (ls vs LS – only lowercase works)
            - Arguments referring to things on the host (such as file names, directories) are only case-sensitive if your OS is case-sensitive.
            - Arguments referring to files or scripts in the repository are case-sensitive.
            - Flags aren’t case-sensitive on Windows but are on macOS and Linux.
        - When running a command that includes a file path with a space, wrap the path in quotation marks, such as `"C:\Program Files\myprogram.exe"`.
        - Be aware when working with files that are on a network share. If the host loses access to the network share, unexpected behavior might result.
        - max file size when using the get command
            - Windows/Mac: The max file size is 4 GB
            - Linux: The max file size is 2 GB
    - Run custom scripts
        - Real Time Response also has Falcon Scripts, which are a preset collection of scripts.
        - Users with the RTR Administrator role can create custom scripts, edit existing scripts from the Edit & Run Scripts tab, and save them to the cloud.
        - You can run any command from the Edit & Run Scripts tab of a response session without saving.
            - Then, when you are ready to add a script to your list of custom scripts, click Save As.
        - create script
        Navigate to Host setup and management > Response and containment > Response scripts and files.
        1. From the Custom scripts tab, click + Create script.
        2. Enter a Name and Description.
        3. Select the Shell type. 
        4. Select the Script access. 
        5. Optional: Click the Share script with workflows checkbox if you intend to use this script with Workflows.
        6. Enter your script in the Script textbox.
        7. Optional: Click the Comments tab to enter comments (which get added to the log). 
        8. Click Create.
        ![alt text](<../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-22.png>)
        - execute custom scripts via
            - panel
            - `runscript –CloudFile="name of saved script"`
            - `runscript –RAW=```script_goes_here``` `       raw is surrounded by triple backticks
            - `runscript –HostPath=C:\folder\file.exe`
        - execute falcon script
            - `falconscript -Name="LocalUser"`
            - with input args
                - `falconscript -Name="FileInfo"  -JsonInput=```'{"path":"C:\\myfile.txt"}'``` `
        - PowerShell code cannot be used in -CommandLine arguments.
        - requote special characters in command line arguments
            ```md
            | Validity        | Example Command                                                                                  |
            |------------------|-----------------------------------------------------------------------------------------------|
            | **Valid command**   | `runscript -CloudFile=test_script -CommandLine=-TestArg 'semi_colon;_in_arg'`                 |
            | **Valid command**   | `runscript -CloudFile=test_script -CommandLine=-TestArg "{arg_val_in_curly_bracket}"`         |
            | **Invalid command** | `runscript -CloudFile=test_script -CommandLine=-TestArg pipe|in_arg`                          |
            |------------------|-----------------------------------------------------------------------------------------------|
            ```
        - To work around script size limitations, run the script directly from the remote host’s file system. Use the put command to load the script onto the remote host, then use runscript with the -HostPath flag to run the script.
        - Treat scripts as “stateless,” meaning each invocation of the script is independent of any and all prior runs.
        - If script content is provided as part of the -Raw flag or if command line arguments are provided as part of the -CommandLine flag enclose the supplied arguments in triple-backticks (for example, ```\\`) to avoid any strange special character interpretation issues.
        - Edit the -Timeout flag to longer than the default 60 seconds if you need the sensor to wait longer for script execution to complete.
        - For PowerShell scripts: The scripts run in the local system context of the remote host as a separate PowerShell background job.
            - Because of this, some commands, such as write-host are not displayed in the Real Time Response session.
            - For more info about PowerShell background jobs, see Microsoft’s documentation.
        - put
            - The put command works with the existing list of “put” files uploaded on the Response scripts and files page. 
            - Files uploaded for "put" are stored securely in the CrowdStrike cloud, separated from both your other Falcon data and from all other customer data.
            - "Put" files cannot exceed 4 GB in size.
            - "Put" file names cannot contain single quote characters or exceed 128 characters in length.
            - File upload time is limited to 5 minutes. If the upload will take longer than 5 minutes, use the POST /real-time-response/entities/put-files/v1 API endpoint to upload your file without the timeout restriction.
        - Network containment
            - If a host has been compromised, you can network contain the host to isolate it from all network activity.
            - Falcon Container does not support network containment for pods.
            - The network connections that can be blocked on Android and iOS hosts depend on how the hosts are deployed and configured.
            - You can automatically network contain Android and iOS hosts if the sensor detects a man-in-the-middle attack.
            - You can update a host's containment status in the host’s summary panel or contain Windows, Mac, and Linux hosts from the detection summary panel. 
            - how to
                1. Navigate to Host setup and management > Manage endpoint > Host management.
                2. Locate a host and click on it to open the host details panel.
                3. Click the Actions drop down.
                4. Click Update containment status.
                5. Optional: Enter any audit log notes.
                6. Click Contain.
            - On the Containment Policy page, you can allow IP addresses over which your hosts will always be allowed to communicate, even if a host is contained.
        - audit logs
            - response scripts and files
            - commands from every session
            - can see how crowdstrike investigates via workflows
                - https://falcon.us-2.crowdstrike.com/real-time-response/sessions/audit-logs

# FALCON 150: Incidents Fundamentals
- Introduction to CrowdScore
    - A CrowdScore is the single, simple metric designed to allow security leaders to understand their organization's threat level on a continuous basis. 
    - Incidents -> increase/decrease crowdscore
    - Incident priority is based on scores, with higher scores indicating greater urgency. CrowdScore evaluates evidence within each incident, where elevated scores signal increased confidence in a potential attack.
    - CrowdScore Incidents bring together related detections, associated processes, and the connections between them to show coordinated activity you should prioritize for investigation. Each incident is scored 0 - 10 based on analysis of all it's contextual data, such as how common behaviors are for your organization.
    - 
- overwatch detections
    - CrowdScore Incidents that include an OverWatch detection are automatically assigned the highest CrowdScore (10/10) due to their critical nature.
    - CrowdScore Incidents are system-generated based on detection severity. OverWatch Incidents are analyst-generated and provide deeper analysis from human threat hunters.
    - OverWatch incidents include a curated timeline of observed attacker behavior instead of just a list of detections.
    - OverWatch Incidents highlight the most pressing, sophisticated threats that require immediate action.
    - When OverWatch Incidents are reported, they appear at the top of the CrowdScore Incidents list, prioritized above any CrowdScore Incidents. OverWatch Incidents DO NOT affect the overall CrowdScore.
    - OverWatch Incidents enrich CrowdScore-based triage by adding insights such as attacker TTPs (Tactics, Techniques, and Procedures) and potential objectives. This additional intelligence helps improve response strategies and reduce investigation time.
- Working with CrowdScore Incidents
    - The CrowdScore incidents page provides valuable high level information about your organization's current threat level. 
    - incident graph ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/image.png>)
    - legend and incident tabs ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-1.png>)
    - processes tab - Click the processes tab to perform quick actions for processes in the Falcon platform.
        - kill process - Click the Real Time Response quick Kill process or Prepare file for download button to start a kill or get command workflow.
        - event search - Click event search to launch an Investigate > Hosts Search in a new browser tab.
        - file path - Copy the File path for investigation elsewhere in the Falcon platform.
        - network contain - Click Network Contain to change the host's network containment status.
    - lateral movement connection ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{E6CE70AD-D315-4981-8FC8-267ED8CF8581}.png>)

# FALCON 151: Incident Workbench Fundamentals
- ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-2.png>)
- allows you to 
    - Visualize an incident in the interactive, customizable graph view in the incident workbench. 
    - See exactly how and when an incident started with the inline timeline widget
    - Zoom in to see what happened during a specific period of time in the incident chronology.
    - Add and manage your own custom nodes, and remove irrelevant items to your investigation.
    - Collaborate with multiple contributors in real-time or asynchronously.
    - Perform basic case management for your incidents. Assign analysts, change incident status, or apply tags.
- nav
    - submenu - Each icon in the submenu represents a tool that can enhance the workbench experience. We’ll discuss these in detail in a future section.
    - icons - The nodes are the various icons you see throughout the graph. The icons represent endpoint indicators, processes, hosts, and more. In the next section, we take a closer look at the individual icons and cover all the other nodes you may encounter while working on the incident workbench. 
    - timeline - Here at the bottom of the screen, users can view the events timeline. The timeline is visualized with similar icons that users see in the graph. Users can adjust the timeline to view specific blocks of time by zooming in and out and dragging the timeline left and right. Selecting a node, indicated by a number of icons relevant to the graph, will allow you to view that specific moment and the related entities via sidebar.
    - Collaboration - To the right of the incident status, users can view if others have worked or are currently working on the same incident. This gives additional insight to analysts to improve collaboration aspects during remediation. This section will also inform you if other analysts are logged on and viewing this incident in real time.
- ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{A5E15F41-4E6C-4EAF-9C47-78D7D0326BEF}.png>)
- ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{0145D17D-3F66-47BA-B32C-75005BB4A307}.png>)
- Incident Workbench Remediation Tools - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/image-3.png>)
    - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{30F62268-049B-4B81-99B0-AE45CAC57227}.png>)
    - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{E03FE173-2BA3-4FE7-B9EE-957AB2C7A10F}.png>)
    - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{B15A55DC-5A37-4D02-9DF7-A6E40B83B192}.png>)
    - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{9362C46F-E3FB-4BA2-8CCA-2333657689AD}.png>)
    - ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{D1E78FAE-ED7D-441D-AB0C-52326BED3FCA}.png>)
- workflow
- ![alt text](<../../../../media/FALCON 100 - Falcon Platform Architecture Overview/{0D99AD98-6FDD-44B8-8C43-D718492F1226}.png>)
    1. Collaboration - We see we have one collaborator who has already begun working on or viewing this incident. We will keep that in mind and make sure to remember to communicate with them while working through this process. 
    2. MITRE Tactic & Technique - The adversary in this case is attempting impact via data encrypted for impact. For additional information, you can click the hyperlinks to pivot to Falcon Support for documentation. 
    3. Identifying problem process - Now looking at the incident, we see a lot of red arrows pointing at this process. But what exactly happened and where did it come from? We can follow the arrows and work backwards. 
    4. see the summary - Hovering your mouse over endpoint indicators and devices gives us summarized information to review.
    5. Clicking on any node will open the sidebar menu with all the detailed information related to that node including tactic & technique, available workflows, contextual behaviors, and more. 
    6. You can also click on the arrows to view process activity details.
- 


































        
