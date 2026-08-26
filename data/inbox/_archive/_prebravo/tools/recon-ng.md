---
id: tools-recon-ng
tags: ["kali", "tool", "passive", "recon"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

```shell
#start recon-ng
recon-ng

#help
help

#search for modules that contain the term github
[recon-ng][default] > marketplace search github
[*] Searching module index for 'github'...

  +------------------------------------------------------------------------------------------------+
  |                       Path                      | Version |     Status    |  Updated   | D | K |
  +------------------------------------------------------------------------------------------------+
  | recon/companies-multi/github_miner              | 1.1     | not installed | 2020-05-15 |   | * |
  | recon/profiles-contacts/github_users            | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/profiles-profiles/profiler                | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/profiles-repositories/github_repos        | 1.1     | not installed | 2020-05-15 |   | * |
  | recon/repositories-profiles/github_commits      | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/repositories-vulnerabilities/github_dorks | 1.0     | not installed | 2019-06-24 |   | * |
  +------------------------------------------------------------------------------------------------+

  D = Has dependencies. See info for details.
  K = Requires keys. See info for details.


# find out futher information about a module
[recon-ng][default] > marketplace info recon/domains-hosts/google_site_web

  +---------------------------------------------------------------------------------------------------------------------------------+
  | path          | recon/domains-hosts/google_site_web                                                                             |
  | name          | Google Hostname Enumerator                                                                                      |
  | author        | Tim Tomes (@lanmaster53)                                                                                        |
  | version       | 1.0                                                                                                             |
  | last_updated  | 2019-06-24                                                                                                      |
  | description   | Harvests hosts from Google.com by using the 'site' search operator. Updates the 'hosts' table with the results. |
  | required_keys | []                                                                                                              |
  | dependencies  | []                                                                                                              |
  | files         | []                                                                                                              |
  | status        | not installed                                                                                                   |
  +---------------------------------------------------------------------------------------------------------------------------------+


# install a module
[recon-ng][default] > marketplace install recon/domains-hosts/google_site_web
[*] Module installed: recon/domains-hosts/google_site_web
[*] Reloading modules...

# we can now load the module
[recon-ng][default] > modules load recon/domains-hosts/google_site_web

# what information do we need to provide?
[recon-ng][default][google_site_web] > info

      Name: Google Hostname Enumerator
    Author: Tim Tomes (@lanmaster53)
   Version: 1.0

Description:
  Harvests hosts from Google.com by using the 'site' search operator. Updates the 'hosts' table with
  the results.

Options:
  Name    Current Value  Required  Description
  ------  -------------  --------  -----------
  SOURCE  default        yes       source of input (see 'info' for details)

Source Options:
  default        SELECT DISTINCT domain FROM domains WHERE domain IS NOT NULL
  <string>       string representing a single input
  <path>         path to a file containing a list of inputs
  query <sql>    database query returning one column of inputs


#the source option is required so let set it
[recon-ng][default][google_site_web] > options set SOURCE megacorpone.com
SOURCE => megacorpone.com

# run the module
[recon-ng][default][google_site_web] > run

---------------
MEGACORPONE.COM
---------------
[*] Searching Google for: site:megacorpone.com
[*] Country: None
[*] Host: www.megacorpone.com
[*] Ip_Address: None
[*] Latitude: None
[*] Longitude: None
[*] Notes: None
[*] Region: None
[*] --------------------------------------------------
[*] Searching Google for: site:megacorpone.com -site:www.megacorpone.com
[*] No New Subdomains Found on the Current Page. Jumping to Result 201.
[*] Searching Google for: site:megacorpone.com -site:www.megacorpone.com
[*] No New Subdomains Found on the Current Page. Jumping to Result 301.
[*] Searching Google for: site:megacorpone.com -site:www.megacorpone.com
[*] No New Subdomains Found on the Current Page. Jumping to Result 401.


.......

[*] No New Subdomains Found on the Current Page. Jumping to Result 7001.
[*] Searching Google for: site:megacorpone.com -site:www.megacorpone.com
[!] Google CAPTCHA triggered. No bypass available.

-------
SUMMARY
-------
[*] 1 total (1 new) hosts found.


# show what hosts are currently stored in the database

[recon-ng][default][google_site_web] > show hosts

  +--------------------------------------------------------------------------------------------------------------+
  | rowid |         host        | ip_address | region | country | latitude | longitude | notes |      module     |
  +--------------------------------------------------------------------------------------------------------------+
  | 1     | www.megacorpone.com |            |        |         |          |           |       | google_site_web |
  +--------------------------------------------------------------------------------------------------------------+

[*] 1 rows returned


# it would be good if the ip_address information was added, is there a module that can do that?
[recon-ng][default] > marketplace info recon/hosts-hosts/resolve

  +-------------------------------------------------------------------------------------------------+
  | path          | recon/hosts-hosts/resolve                                                       |
  | name          | Hostname Resolver                                                               |
  | author        | Tim Tomes (@lanmaster53)                                                        |
  | version       | 1.0                                                                             |
  | last_updated  | 2019-06-24                                                                      |
  | description   | Resolves the IP address for a host. Updates the 'hosts' table with the results. |
  | required_keys | []                                                                              |
  | dependencies  | []                                                                              |
  | files         | []                                                                              |
  | status        | not installed                                                                   |
  +-------------------------------------------------------------------------------------------------+

[recon-ng][default] > marketplace install recon/hosts-hosts/resolve
[*] Module installed: recon/hosts-hosts/resolve
[*] Reloading modules...


# load info
[recon-ng][default][resolve] > info

      Name: Hostname Resolver
    Author: Tim Tomes (@lanmaster53)
   Version: 1.0

Description:
  Resolves the IP address for a host. Updates the 'hosts' table with the results.

Options:
  Name    Current Value  Required  Description
  ------  -------------  --------  -----------
  SOURCE  default        yes       source of input (see 'info' for details)

Source Options:
  default        SELECT DISTINCT host FROM hosts WHERE host IS NOT NULL AND ip_address IS NULL
  <string>       string representing a single input
  <path>         path to a file containing a list of inputs
  query <sql>    database query returning one column of inputs

Comments:
  * Note: Nameserver must be in IP form.


# execute it
[recon-ng][default][resolve] > run
[*] www.megacorpone.com => 149.56.244.87

#show hosts, can now see ip address added
[recon-ng][default][resolve] > show hosts

  +-----------------------------------------------------------------------------------------------------------------+
  | rowid |         host        |   ip_address  | region | country | latitude | longitude | notes |      module     |
  +-----------------------------------------------------------------------------------------------------------------+
  | 1     | www.megacorpone.com | 149.56.244.87 |        |         |          |           |       | google_site_web |
  +-----------------------------------------------------------------------------------------------------------------+

[*] 1 rows returned




```




## interesting_files

```shell
[recon-ng][default] > marketplace install discovery/info_disclosure/interesting_files
[*] Module installed: discovery/info_disclosure/interesting_files
[*] Reloading modules...
[recon-ng][default] > modules load discovery/info_disclosure/interesting_files
[recon-ng][default][interesting_files] > info

      Name: Interesting File Finder
    Author: Tim Tomes (@lanmaster53), thrapt (thrapt@gmail.com), Jay Turla (@shipcod3), and Mark Jeffery
   Version: 1.2

Description:
  Checks hosts for interesting files in predictable locations.

Options:
  Name      Current Value                                           Required  Description
  --------  -------------                                           --------  -----------
  CSV_FILE  /home/kali/.recon-ng/data/interesting_files_verify.csv  yes       custom filename map
  DOWNLOAD  True                                                    yes       download discovered files
  PORT      80                                                      yes       request port
  PROTOCOL  http                                                    yes       request protocol
  SOURCE    default                                                 yes       source of input (see 'info' for details)

Source Options:
  default        SELECT DISTINCT host FROM hosts WHERE host IS NOT NULL
  <string>       string representing a single input
  <path>         path to a file containing a list of inputs
  query <sql>    database query returning one column of inputs

Comments:
  * Files: robots.txt, sitemap.xml, sitemap.xml.gz, crossdomain.xml, phpinfo.php, test.php, elmah.axd,
  server-status, jmx-console/, admin-console/, web-console/
  * CSV Default: /home/kali/.recon-ng/data/interesting_files_verify.csv
  * Google Dorks:
    - inurl:robots.txt ext:txt
    - inurl:elmah.axd ext:axd intitle:"Error log for"
    - inurl:server-status "Apache Status"

[recon-ng][default][interesting_files] > run
[*] http://www.megacorpone.com:80/robots.txt => 200. 'robots.txt' found!
[*] http://www.megacorpone.com:80/sitemap.xml => 404
[*] http://www.megacorpone.com:80/sitemap.xml.gz => 404
[*] http://www.megacorpone.com:80/crossdomain.xml => 404
[*] http://www.megacorpone.com:80/phpinfo.php => 404
[*] http://www.megacorpone.com:80/test.php => 404
[*] http://www.megacorpone.com:80/elmah.axd => 404
[*] http://www.megacorpone.com:80/server-status => 403
[*] http://www.megacorpone.com:80/jmx-console/ => 404
[*] http://www.megacorpone.com:80/admin-console/ => 404
[*] http://www.megacorpone.com:80/web-console/ => 404
[*] 1 interesting files found.
[*] Files downloaded to '/home/kali/.recon-ng/workspaces/default/'






```