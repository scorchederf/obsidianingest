---
aliases:
tags:
source: https://github.com/RedSiege/EyeWitness
desc: EyeWitness is a tool used to capture screenshots from a list of URLs
---
EyeWitness is designed to take screenshots of websites, provide server header info, and identify default credentials if known. Powered by Chromium browser for better reliability and easier installation.

- installation via sudo
	- `sudo apt install eyewitness`
	- navigate to `Python/setup` directory and execute `setup.sh`
- options
	- `eyewitness -h`
- execute using output from nmap
	- `eyewitness --web -x web_discovery.xml -d inlanefreight_eyewitness`


