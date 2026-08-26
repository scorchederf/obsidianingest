---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

Simple Network Management Protocol (SNMP) is not well-understood by many network administrators. This often results in SNMP misconfigurations, which can result in significant information leakage.

SNMP is based on UDP, a simple, stateless protocol, and is therefore susceptible to IP spoofing and replay attacks. In addition, the commonly used SNMP protocols 1, 2, and 2c offer no traffic encryption, meaning that SNMP information and credentials can be easily intercepted over a local network. Traditional SNMP protocols also have weak authentication schemes and are commonly left configured with default public and private community strings.

The SNMP Management Information Base (MIB) is a database containing information usually related to network management. The database is organized like a tree, where branches represent different organizations or network functions. The leaves of the tree (final endpoints) correspond to specific variable values that can then be accessed, and probed, by an external user. The IBM Knowledge Center1 contains a wealth of information about the MIB tree.

For example, the following MIB values correspond to specific Microsoft Windows SNMP parameters and contains much more than network-based information:
	
1.3.6.1.2.1.25.1.6.0 	System Processes
1.3.6.1.2.1.25.4.2.1.2 	Running Programs
1.3.6.1.2.1.25.4.2.1.4 	Processes Path
1.3.6.1.2.1.25.2.3.1.4 	Storage Units
1.3.6.1.2.1.25.6.3.1.2 	Software Name
1.3.6.1.4.1.77.1.2.25 	User Accounts
1.3.6.1.2.1.6.13.1.3 	TCP Local Ports

    Table 1 - Windows SNMP MIB values
