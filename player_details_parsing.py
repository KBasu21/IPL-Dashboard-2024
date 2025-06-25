from bs4 import BeautifulSoup
import csv

player_details = []

for i in range(1, 257):
    try:
        with open(f"players/players{i}.html", "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        continue  # Skip if file doesn't exist

    soup = BeautifulSoup(html, 'html.parser')

    # Extract fields using label -> next <p> pattern
    def get_detail(label):
        tag = soup.find('p', string=label)
        return tag.find_next('p').text.strip() if tag else 'N/A'

    name = get_detail('Full Name')
    batting_style = get_detail('Batting Style')
    bowling_style = get_detail('Bowling Style')
    playing_role = get_detail('Playing Role')

    # Extract photo link from meta tag
    img_tag = soup.find('meta', property='og:image')
    photo_link = img_tag['content'] if img_tag else 'N/A'

    player_details.append([name, batting_style, bowling_style, playing_role, photo_link])

# Print result
with open("player_details.csv", "w", newline="") as f:
    w = csv.writer(f)
    for i in player_details:
        w.writerow(i)
    f.close()
