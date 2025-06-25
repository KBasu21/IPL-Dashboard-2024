from bs4 import BeautifulSoup
import re

links = []
base_url = "https://www.espncricinfo.com"

def clean_name(name):
    name = name.strip()                    # Remove leading/trailing whitespace
    name = re.sub(r'\s+', ' ', name)       # Collapse multiple spaces/newlines into one
    name = re.sub(r'\(.*?\)', '', name)    # Remove anything in brackets like (c)
    name = re.sub(r'[†,]', '', name)       # Remove symbols like dagger or trailing commas
    return name.strip()

for i in range(1, 75):
    with open(f"scorecard/score{i}.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith("/cricketers/"):
            full_url = base_url + href
            raw_name = a_tag.get_text()
            player_name = clean_name(raw_name)
            if player_name:  # Only add if name isn't empty
                links.append([player_name, full_url])

# Optional: Deduplicate
unique_links = []
seen = set()
for name_url in links:
    if tuple(name_url) not in seen:
        seen.add(tuple(name_url))
        unique_links.append(name_url)

print(unique_links[248])
