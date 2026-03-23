import pandas as pd

# Example: VIC government land CSV feed
URL = "https://www.property.vic.gov.au/land-sales/available-land.csv"

df = pd.read_csv(URL)
# Filter relevant columns and mark TARGET if needed
df["Notes"] = df["Description"].apply(lambda x: "TARGET" if "vacant" in str(x).lower() else "")
df.to_excel("gov_vic_land.xlsx", index=False)
print("✅ VIC government scraper done")
