import requests
import time
from fake_useragent import UserAgent

url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results"

session = requests.Session()
headers = {
    'User-Agent' : UserAgent().random,
    'Accept-Language' : 'en-US,en;q=0.9,bn;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, br, zstd',
    'Connection' : 'keep-alive',
    'Referer' : 'https://www.google.com/'
}
auth = "156.228.90.134:3128"
proxies = {
    'http' : f'http://{auth}'
}

time.sleep(2)
r = session.get(url, proxies=proxies, headers=headers)
with open("results.html", "w") as f:
    f.write(r.text)
