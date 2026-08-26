# theharvester


## build a sources list
`cat sources.txt`
```
    baidu
    bufferoverun
    crtsh
    hackertarget
    otx
    projecdiscovery
    rapiddns
    sublist3r
    threatcrowd
    trello
    urlscan
    vhost
    virustotal
    zoomeye
```
## batch search
`cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done`