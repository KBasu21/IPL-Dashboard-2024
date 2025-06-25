import requests
import time
from fake_useragent import UserAgent
from parsing import scorecard_links

session = requests.Session()
headers = {
    'User-Agent' : UserAgent().random,
    'Accept-Language' : 'en-US,en;q=0.9,bn;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, br, zstd',
    'Connection' : 'keep-alive',
    'Referer' : 'https://www.google.com/'
}
auth = "156.253.172.103:3128"
proxies = {
    'http' : f'http://{auth}'
}
file_no = 1
for link in scorecard_links:
    link = link[:-18] + 'full-scorecard'
    url = f"{link}"
    time.sleep(2)
    r = session.get(url, proxies=proxies, headers=headers)
    with open(f"scorecard/score{file_no}.html", "w", encoding="utf-8") as f:
        f.write(r.text)
        file_no += 1
