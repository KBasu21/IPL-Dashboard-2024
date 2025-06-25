from bs4 import BeautifulSoup
import csv

# Read HTML content
with open("results.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

match_blocks = soup.find_all(class_="ds-bg-fill-content-prime hover:ds-bg-ui-fill-translucent")

rows = []

for match in match_blocks:
    # Result text (margin)
    result_tag = match.find("p", class_="ds-text-tight-s ds-font-medium ds-line-clamp-2 ds-text-typo")
    margin = result_tag.get("title", "").strip() if result_tag else ""

    # Result type (check for abandoned)
    result_label = match.find(class_="ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5")
    is_abandoned = result_label and "abandoned" in result_label.get("title", "").lower()

    # Winning team
    win_block = match.find(class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")
    win_team = ""
    if win_block and not is_abandoned:
        team_tag = win_block.find(class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
        win_team = " ".join(team_tag.get_text(strip=True).split()) if team_tag else ""

    # Losing team
    lose_block = match.find(class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")
    lose_team = ""
    if lose_block and not is_abandoned:
        team_tag = lose_block.find(class_="ds-text-tight-m ds-font-bold ds-capitalize ds-truncate")
        lose_team = " ".join(team_tag.get_text(strip=True).split()) if team_tag else ""

    # Date
    date_tag = match.find(class_="ds-text-tight-s ds-font-medium ds-bg-ui-fill-alternate ds-py-1 ds-px-2 ds-rounded-2xl")
    match_date = date_tag.text.strip() if date_tag else ""

    # Scorecard link
    scorecard_tag = match.find("a", href=True)
    scorecard_link = ""
    if scorecard_tag and "full-scorecard" in scorecard_tag["href"]:
        scorecard_link = "https://www.espncricinfo.com" + scorecard_tag["href"]

    rows.append([win_team, lose_team, margin, match_date, scorecard_link])

# Sanity check
print(f"Total matches scraped: {len(rows)}")

# Write to CSV
with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Winning Team", "Losing Team", "Margin", "Date", "Scorecard Link"])
    writer.writerows(rows)

print("✅ CSV file written successfully.")
