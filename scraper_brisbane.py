import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

URL = "https://www.domain.com.au/sale/brisbane-qld/land/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

listings = []

for prop in soup.find_all("div"):
    try:
        text = prop.get_text(" ", strip=True)
        if len(text) > 60:
            link_tag = prop.find("a", href=True)
            link = "https://www.domain.com.au" + link_tag["href"] if link_tag else ""
            keywords = ["land", "vacant", "development", "subdivision"]
            note = "TARGET" if any(k in text.lower() for k in keywords) else ""
            listings.append({
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Title": text[:120],
                "Price": "",
                "Suburb": "",
                "Land Size": "",
                "Link": link,
                "Notes": note
            })
    except:
        continue

df = pd.DataFrame(listings).drop_duplicates()
df.to_excel("brisbane_land.xlsx", index=False)
print("✅ Brisbane scraper done")
