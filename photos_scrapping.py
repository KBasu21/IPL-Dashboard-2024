import os
import requests
import time
from fake_useragent import UserAgent
from players_scrapping import unique_links  # Importing your player names and URLs

# Proxy list
proxy_list = [
    "156.228.90.134:3128",
    "156.253.172.103:3128",
    "156.233.87.200:3128",
    "156.233.95.254:3128",
    "156.228.174.251:3128",
    "156.242.32.1:3128",
    "156.228.85.46:3128",
    "156.242.47.90:3128",
    "156.249.56.182:3128",
    "154.213.197.135:3128",
    "156.228.100.97:3128",
    "154.213.204.225:3128",
    "156.228.178.22:3128",
    "156.228.85.3:3128",
    "156.242.33.103:3128",
    "156.228.99.75:3128",
    "156.242.38.24:3128",
    "154.213.167.130:3128",
    "156.228.115.210:3128",
    "156.253.169.190:3128",
    "156.249.57.9:3128",
    "156.233.86.222:3128",
    "156.228.116.201:3128",
    "156.248.82.206:3128",
    "156.242.47.21:3128",
    "156.228.0.19:3128",
    "156.248.83.223:3128",
    "156.253.175.162:3128",
    "154.213.199.58:3128",
    "154.94.14.166:3128",
    "156.228.111.160:3128",
    "156.249.57.68:3128",
    "156.242.40.230:3128",
    "156.228.117.89:3128",
    "156.228.190.142:3128",
    "156.228.77.219:3128",
    "156.228.96.194:3128",
    "156.228.176.224:3128",
    "154.213.204.226:3128",
    "156.228.90.46:3128",
    "156.228.78.242:3128",
    "156.228.100.58:3128",
    "156.249.56.241:3128",
    "156.233.72.36:3128",
    "156.228.119.172:3128",
    "154.91.171.222:3128",
    "156.253.177.105:3128",
    "154.94.12.204:3128",
    "156.228.85.56:3128",
    "156.228.87.158:3128",
    "156.228.103.163:3128",
    "156.253.165.153:3128",
    "154.94.13.238:3128",
    "156.253.175.1:3128",
    "154.213.194.47:3128",
    "156.242.40.178:3128",
    "156.242.47.205:3128",
    "156.253.166.201:3128",
    "156.228.112.136:3128",
    "156.228.100.236:3128",
    "156.253.165.40:3128",
    "156.233.87.247:3128",
    "156.228.181.116:3128",
    "156.228.92.208:3128",
    "156.228.180.190:3128",
    "154.214.1.90:3128",
    "156.248.84.169:3128",
    "156.233.89.200:3128",
    "156.253.177.228:3128",
    "154.213.166.251:3128",
    "156.240.99.60:3128",
    "156.228.96.89:3128",
    "156.228.110.106:3128",
    "156.242.35.211:3128",
    "154.213.163.162:3128",
    "156.248.87.37:3128",
    "156.228.174.31:3128",
    "154.213.161.174:3128",
    "154.213.204.39:3128",
    "156.253.178.143:3128",
    "154.213.198.252:3128",
    "156.233.90.52:3128",
    "156.248.86.104:3128",
    "156.228.102.203:3128",
    "156.228.81.60:3128",
    "156.240.99.162:3128",
    "156.228.189.60:3128",
    "156.233.89.109:3128",
    "156.228.78.234:3128",
    "156.233.92.144:3128",
    "45.202.79.174:3128",
    "156.242.36.212:3128",
    "156.253.170.181:3128",
    "156.228.179.33:3128",
    "154.213.164.139:3128",
    "154.94.14.154:3128",
    "156.233.84.216:3128",
    "156.228.112.29:3128",
    "156.233.85.159:3128",
    "154.213.167.196:3128"
]

# Generate random headers
def get_random_headers():
    return {
        'User-Agent': UserAgent().random,
        'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection' : 'Upgrade',
        'Referer' : 'https://www.espncricinfo.com/',
        'Method': 'GET',
        'Scheme': 'https'
    }

# Get random proxy
def get_proxy_from_list():
    # Keep track of the index globally, so we can use the next proxy in sequence
    if not hasattr(get_proxy_from_list, "proxy_index"):
        get_proxy_from_list.proxy_index = 0  # Initialize index on first call

    proxy = proxy_list[get_proxy_from_list.proxy_index]  # Get proxy based on current index
    get_proxy_from_list.proxy_index += 1  # Move to the next proxy for the next call
    if get_proxy_from_list.proxy_index >= len(proxy_list):
        get_proxy_from_list.proxy_index = 0  # Reset to the first proxy if we've exhausted the list
    return {
        'http': f'http://{proxy}',
    }

# Fetch player's HTML content with retry logic
def fetch_player_html(url, max_retries=len(proxy_list)):
    attempt = 0

    while attempt < max_retries:
        proxies = get_proxy_from_list()  # Get the next proxy in the list
        headers = get_random_headers()  # Get random headers
        print(f"[🧭] Attempt #{attempt + 1} - Using proxy: {proxies['http']}")
        print(f"[🎭] User-Agent: {headers['User-Agent']}")

        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()
            print(f"[✅] Successfully fetched {url}")
            return response.text  # return the raw HTML content
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"[❌] Failed to fetch {url} (Attempt {attempt}): {e}")

            # If we've exhausted our retry limit, return None
            if attempt >= max_retries:
                print(f"[❌] Maximum retries reached for {url}. Skipping.")
                return None

            # Delay between retries (optional)
            time.sleep(2)

    return None


# Save HTML to a file
def save_html_to_file(html, filename):
    # Ensure 'players' directory exists
    if not os.path.exists('players'):
        os.makedirs('players')

    with open(f'players/{filename}', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[✅] HTML saved as {filename}")

# Main loop over players
if __name__ == "__main__":
    for idx, (name, url) in enumerate(unique_links, start=1):
        filename = f"players{idx}.html"
        filepath = os.path.join('players', filename)

        # ✅ Skip if file already exists
        if os.path.exists(filepath):
            print(f"[⏭️] Skipping {name} (already exists as {filename})")
            continue

        print(f"\n[#{idx}] Fetching profile for: {name}")
        html = fetch_player_html(url.strip())
        if html:
            save_html_to_file(html, filename)
