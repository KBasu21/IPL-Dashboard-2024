from bs4 import BeautifulSoup
import csv

bowling_data = []

for i in range(1, 75):
    with open(f"scorecard/score{i}.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Identify all <table> tags
    tables = soup.find_all('table')

    for table in tables:
        # Check if this is a bowling table
        thead = table.find('thead')
        if not thead:
            continue

        headers = [th.text.strip().upper() for th in thead.find_all('th')]
        if headers[:5] == ['BOWLING', 'O', 'M', 'R', 'W']:
            # Valid bowling table
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')

            for row in rows:
                if 'ds-hidden' in row.get('class', []):
                    continue  # skip commentary/images rows

                cols = row.find_all('td')
                if len(cols) < 11:
                    continue  # not a valid stat row

                name_tag = cols[0].find('span')
                name = name_tag.text.strip() if name_tag else cols[0].text.strip()

                # Clean up the name by removing unwanted newline characters, extra spaces
                name = name.replace('\n', ' ').strip()  # Remove newlines
                name = ' '.join(name.split())  # Replace multiple spaces with a single space

                try:
                    overs = float(cols[1].text.strip())
                    maidens = int(cols[2].text.strip())
                    runs = int(cols[3].text.strip())
                    wickets = int(cols[4].text.strip())
                    economy = float(cols[5].text.strip())
                    dots = int(cols[6].text.strip()) if cols[6].text.strip() else 0
                    fours = int(cols[7].text.strip()) if cols[7].text.strip() else 0
                    sixes = int(cols[8].text.strip()) if cols[8].text.strip() else 0
                    wides = int(cols[9].text.strip()) if cols[9].text.strip() else 0
                    no_balls = int(cols[10].text.strip()) if cols[10].text.strip() else 0

                    bowling_data.append([
                        name, overs, maidens, runs, wickets, economy,
                        dots, fours, sixes, wides, no_balls
                    ])
                except ValueError as e:
                    continue  # skip rows with bad data

with open("bowling_performances.csv", "w", newline="") as f:
    w = csv.writer(f)
    for i in bowling_data:
        w.writerow(i)
    f.close()
