import pandas as pd

files = [
    "melbourne_land.xlsx",
    "sydney_land.xlsx",
    "brisbane_land.xlsx",
    "gov_vic_land.xlsx",
    "gov_nsw_land.xlsx"
]

dfs = [pd.read_excel(f) for f in files]
master = pd.concat(dfs).drop_duplicates(subset=["Link"])
master.to_excel("all_land_master.xlsx", index=False)
print("✅ Master Excel file ready")
