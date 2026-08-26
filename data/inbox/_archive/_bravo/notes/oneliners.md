

## quiet os detect via port 80
`sudo nmap -sV -script=smb-os-discovery 10.129.2.80 --source-port 53`


## quiet dns server version 
`sudo nmap -sSU -p 53 --script dns-nsid 10.129.2.48 --source-port 53`

## nc connect to service
`sudo nc -nv -p 53 10.129.99.105 50000`
