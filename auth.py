import requests


proxies = {
  'http': 'http://192.168.0.125:8080',
  'https': 'http://192.168.0.125:8080',
}

ses = requests.Session()
ses.proxies.update(proxies)

url = 'https://twitter.com/login'

headers = {
    'Host': 'twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Gpc': '1',
    'Te': 'trailers',
    'Connection': 'close',
}

r = ses.get(url, headers=headers, verify=False, allow_redirects=False)
print(r.text)
print('one')

print(ses.cookies)

