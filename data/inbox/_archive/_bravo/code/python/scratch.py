import requests


#settings
burp = {
  'http': 'http://127.0.0.1:8080',
  'https': 'https://127.0.0.1:8080'
}

url = "http://www.google.com"

response = requests.get(url, proxies=burp)
if (response.status_code == 200):
    print("200")
else:
    print("booo, error")



