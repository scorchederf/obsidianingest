import requests, bs4
import yaml

yamlConfig = """
---
name: http
port: [80,443]
category:
  - name: adult
    ioc:
      - "https://www.playboyplus.com"
      - "https://www.redtube.com"

  - name: drugs
    ioc:
      - "https://www.cannabis.com"
      - "https://www.getkush.ca"
      - "https://www.magicmushroom.com"

  - name: dating
    ioc:
      - "https://www.match.com"
      - "https://www.eharmony.com"
      - "https://www.okcupid.com"      

---
name: ssh
port: [22]

"""

docs = yaml.safe_load_all(yamlConfig)
for doc in docs:
    docName = doc['name']
    if docName == "http":
        for category in doc['category']:
            catName = category['name']
            for ioc in category['ioc']:
                try:
                    r = requests.get(ioc)
                    html = bs4.BeautifulSoup(r.text, features="lxml")
                    print(catName, "\t", ioc, "\t", html.title.text)
                except:
                    print("exception")