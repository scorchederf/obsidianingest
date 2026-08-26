---
aliases:
tags:
source:
  - https://github.com/drego85/JoomlaScan
desc:
---
 A free software to find the components installed in Joomla CMS, built out of the ashes of [Joomscan](https://github.com/OWASP/joomscan).

! requires [[python2.7]]

```sh
python2.7 -m pip install urllib3
python2.7 -m pip install certifi
python2.7 -m pip install bs4
```

# usage
- standard scan
	- `python2.7 joomlascan.py -u http://dev.inlanefreight.local`
- 