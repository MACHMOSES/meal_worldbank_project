
import requests
import pandas as pd
import os

def fetch_world_bank_indicator(country_code, indicator, per_page=20000):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}"
    params = {"format": "json", "per_page": per_page}
    r = requests.get(url, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()

    rows = []
    for obs in data[1]:
        rows.append({
            "country": obs["country"]["value"],
            "country_code": obs["country"]["id"],
            "indicator": obs["indicator"]["value"],
            "indicator_code": obs["indicator"]["id"],
            "year": int(obs["date"]),
            "value": obs["value"]
        })

    df = pd.DataFrame(rows)
    df = df.dropna(subset=["value"]).sort_values("year")
    return df

os.makedirs("data/raw", exist_ok=True)

poverty = fetch_world_bank_indicator("KEN", "SI.POV.DDAY")
unemp   = fetch_world_bank_indicator("KEN", "SL.UEM.TOTL.ZS")

poverty.to_csv("data/raw/kenya_poverty_raw.csv", index=False)
unemp.to_csv("data/raw/kenya_unemployment_raw.csv", index=False)

print("Raw data downloaded.")
