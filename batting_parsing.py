from bs4 import BeautifulSoup
import csv

players = []
def safe_int(text):
    return int(text) if text.isdigit() else 0

def safe_float(text):
    return float(text) if text.replace('.', '', 1).isdigit() else 0.0

for i in range(1, 75):
    with open(f"scorecard/score{i}.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    batting_blocks = soup.find_all("tr", class_="ds-table-row-compact-bottom ds-border-none")

    for block in batting_blocks:
        name_tag = block.find("a", title=True)
        name = name_tag["title"].strip().replace("Â", "") if name_tag else "Unknown"

        tds = block.find_all("td")
        if len(tds) >= 8:
            # Defensive parsing with fallback
            try:
                runs = safe_int(tds[2].text.strip())
                balls = safe_int(tds[3].text.strip())
                fours = safe_int(tds[5].text.strip())
                sixes = safe_int(tds[6].text.strip())
                strike_rate = safe_float(tds[7].text.strip())

                player_stats = [name, runs, balls, fours, sixes, strike_rate]
                players.append(player_stats)
            except Exception as e:
                print(f"Error in file {i}, player {name}: {e}")

with open("batting_performances.csv", "w", newline="") as f:
    w = csv.writer(f)
    for i in players:
        w.writerow(i)
    f.close()
