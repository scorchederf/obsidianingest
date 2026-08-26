---
title: postgresql
---

# postgresql


- connect `psql -U christine -h machine.htb -p 5432`
- list databases `\list`
- change db `\connect secrets`
- list tables `\dt`
- select `SELECT * FROM flag;`      CASE SENSITIVE
- mitigations
    - [pg_escape_string](https://www.php.net/manual/en/function.pg-escape-string.php) `$escaped = pg_escape_string($data);`
