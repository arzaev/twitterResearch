import requests
import urllib3
urllib3.disable_warnings()

ses = requests.Session()


proxy = {
  'http': 'http://192.168.0.125:8080',
  'https': 'http://192.168.0.125:8080',
}

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

r = ses.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False, timeout=10)

url = 'https://twitter.com/i/js_inst?c_name=ui_metrics'
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
r = ses.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False, timeout=10)

url = 'https://twitter.com/sessions'
auth_token = '35eb8b00ff8e11eba7e1f1b522289c7b'
username = ''
password = ''
ses.cookies.set('_mb_tk', auth_token)
#ses.cookies.set('ct0', 'c7c51aeb98fc8f6fa0a0b21434e7132e')
data = "redirect_after_login=%2F&remember_me=1&authenticity_token={}&wfa=1&ui_metrics=%7B%22rf%22%3A%7B%22a9a1956960eed0839e1ec52f76b3779f1134edca2bbcf44452121000b08425c6%22%3A-100%2C%22c20e919f0383f67aff7439210d84edc65792c4570aab57d5e88dfe552c664456%22%3A112%2C%22a8da6af62113b517d12d343c4d5f4d4b27ec3826f7dcf6922b54806404bf43b5%22%3A-1%2C%22abef8784c25d2b9df56698b39f9b08b956b61b1fb72a59113566ffa94603aee6%22%3A16%7D%2C%22s%22%3A%22XJOjmaFgtNt4GJJ1HBB7zY5mTaGWgad8U7XZ0wVZEARXgEXJLcypljSvKGqj5mBxtUewdl0HVyUTXf0jK44cppOjtuD7Iu4giS84OrlG_q7_k7daVS3ZjxuzqlYVjJaVptP12X0yt5gAqD4m-S4EebwDHw1ffGH2pkYZJr3xlbqU2rrzWosh073ONmXvlsmipBGuS3rmKyjRbgh7wz3gv9qwjvuatBSRfV4gp7w4xl3e6cBEA4AMVQx1lLZXs1jUOIK4GNknrxAYOAhwNXYJshlYLCrYTTSHMwTtbMHsKqbNa0-n1nEl2Pds4e9djJuzzJJkPpwq1nY83ZFmp6DHVQAAAXtUEQ3N%22%7D&session%5Busername_or_email%5D={}&session%5Bpassword%5D={}".format(
auth_token, username, password
)
headers = {
    'Host': 'twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': str(len(data)),
    'Referer': 'https://twitter.com/login',
    'Origin': 'https://twitter.com',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Gpc': '1',
    'Te': 'trailers',
    'Connection': 'close',
}
r = ses.post(url, headers=headers, data=data, proxies=proxy, verify=False, allow_redirects=False, timeout=10)
if 'PhoneNumber' in r.text:
    url = r.headers['location']
    ref = url
    headers = {'Host': 'twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
						'Accept-Language': 'en-US,en;q=0.5',
						'Accept-Encoding': 'gzip, deflate',
						'Referer': 'https://twitter.com/login',
						'Upgrade-Insecure-Requests': '1',
						'Sec-Fetch-Dest': 'document',
						'Sec-Fetch-Mode': 'navigate',
						'Sec-Fetch-Site': 'same-origin',
						'Sec-Fetch-User': '?1',
						'Te': 'trailers',
						}
    r = ses.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False, timeout=10)
    authenticity_token = r.text.split('authenticity_token" value="')[1].split('"')[0]
    challenge_id = r.text.split('login_challenge?challenge_id=')[1].split('&amp')[0]
    enc_user_id = r.text.split('enc_user_id=')[1].split('"')[0]
    
    url = 'https://twitter.com/account/login_challenge'
    data = 'authenticity_token={}&challenge_id={}&enc_user_id={}&challenge_type=RetypePhoneNumber&platform=web&redirect_after_login=%2F&remember_me=&challenge_response=%2B79917902947'.format(authenticity_token, challenge_id, enc_user_id)
    headers = {'Host': 'twitter.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': str(len(data)),
                'Referer': ref,
                'Origin': 'https://twitter.com',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Te': 'trailers',
               }
    r = ses.post(url, headers=headers, data=data, proxies=proxy, verify=False, allow_redirects=False, timeout=10)
    