---
id: passiveinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# passive-information-gathering

backlinks: [[snippets-bash]]

sources:

---

- website - https://www.megacorpone.com
  - about.html reveals emails and twitter accounts
  - emails
    - tell us email address format - initiallastname@megacorpone.com
    - ceo joe@megacorpone.com uses a different format - maybe startup emails were different
    - theHarvester
  - look for social media platforms
  - recon-ng ```modules discovery/info_disclosure/interesting_files```
    - robots.txt
- whois 
  - ```whois megacorpone.com```
    - Registrant names and roles
    - addresses 
    - name servers
  - ```whois 149.56.244.87``` if known
  - if we have ip addresses, we can use reverse whois 
- [google hacking database](https://www.exploit-db.com/google-hacking-database)
  - site:megacorpone.com
    - index of / for open directories
      - https://www.megacorpone.com/assets
      - https://www.megacorpone.com/old-site
    - other sites
  - site:megacorpone.com filetype:txt
    - http://www.megacorpone.com/robots.txt
  - site:megacorpone.com ext:php
    - search for programming languages may be used on the server
- [netcraft.com/tools](https://www.netcraft.com/tools/)
  - [site reports matching *.megacorpone.com](https://searchdns.netcraft.com/?host=*.megacorpone.com)
    - [Site report for http://www.megacorpone.com](https://sitereport.netcraft.com/?url=http://www.megacorpone.com)
- [recon-ng](https://github.com/lanmaster53/recon-ng)
  - ```modules recon/domains-hosts/google_site_web```
  - ```modules recon/hosts-hosts/resolve```
  - ```modules discovery/info_disclosure/interesting_files```
- Open source code
  - [github (manual)](https://github.com/megacorpone)
    - search filename:users
      - xampp.users exists and contains creds
        - trivera:$apr1$A0vSKwao$GV3sgGAj53j.c3GkS4oUC0
  - github automated
    - [Gitleaks #todo](https://github.com/zricethezav/gitleaks)
    - gitrob
  - [showdan #todo](https://www.shodan.io/)
  - [security headers](https://securityheaders.com/)
    - if score is low, may indicate that server admins are not familiar with server hardening practices
  - [ssl server test](https://www.ssllabs.com/ssltest/)
    - can indicate vulnerablities such as Poodle, HeartBleed or just weak key exchanges
  - [pastebin](https://pastebin.com/)
    - exposed credentials, ip addresses, etc
- User information gathering
  - theHarvester
    - ```theHarvester -d www.megacorpone.com -b all > theHarvester.megacorpone```
- password dumps
  - [rockyou](https://en.wikipedia.org/wiki/RockYou#Data_breach)
  - [haveibeenpwned](https://haveibeenpwned.com/PwnedWebsites) 
- social media
  - [socialsearcher](https://www.social-searcher.com/)
  - twitter? use [Twofi1](https://digi.ninja/projects/twofi.php)
  - linkedin? use [linkedin2username](https://github.com/initstring/linkedin2username)
  - stack overflow
- [OSINT Framework](https://osintframework.com/)
- [Maltego](https://www.maltego.com)
