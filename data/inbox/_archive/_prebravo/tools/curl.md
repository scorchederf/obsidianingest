---
id: tools-curl
tags: ["linux", "tool", "curl", "windows"]
created: 2023-01-12 11:56
---
# tools - curl

backlinks: [[]]

---

curl is used in command lines or scripts to transfer data

## flags

- -o output

Post data:

```shell
curl -d password=x http://x.com/y
```

```shell
Auth/data:
curl -u user:pass -d status="Hello" http://twitter.com/statuses/update.xml
```

multipart file upload

```shell
curl -v -include --form key1=value1 --form upload=@localfilename URL
```

multipart form: send data from text field and upload file

```shell
curl -F person=anonymous -F secret=@file.txt http://example.com/submit.cgi
```

Use Curl to Check if a remote resource is available

details: <https://matthewsetter.com/check-if-file-is-available-with-curl/>

```shell
curl -o /dev/null --silent -Iw "%{http_code}" https://example.com/my.remote.tarball.gz
```
