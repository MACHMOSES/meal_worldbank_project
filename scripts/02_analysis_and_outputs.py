
import pandas as pd
import matplotlib.pyplot as plt
import os

def data_quality_report(df):
    return {
        "rows": len(df),
        "min_year": df["year"].min(),
        "max_year": df["year"].max(),
        "missing": df["value"].isna().sum(),
        "duplicates": df.duplicated(["country_code","indicator_code","year"]).sum()
    }

def add_changes(df):
    df = df.copy()
    df["yoy_change"] = df["value"].diff()
    df["yoy_pct_change"] = df["value"].pct_change() * 100
    return df

poverty = pd.read_csv("data/raw/kenya_poverty_raw.csv")
unemp   = pd.read_csv("data/raw/kenya_unemployment_raw.csv")

poverty = add_changes(poverty)
unemp   = add_changes(unemp)

os.makedirs("outputs/csv", exist_ok=True)
os.makedirs("outputs/parquet", exist_ok=True)

poverty.to_csv("outputs/csv/kenya_poverty_worldbank.csv", index=False)
unemp.to_csv("outputs/csv/kenya_unemployment_worldbank.csv", index=False)

poverty.to_parquet("outputs/parquet/kenya_poverty_worldbank.parquet", index=False)
unemp.to_parquet("outputs/parquet/kenya_unemployment_worldbank.parquet", index=False)

def plot(df, title, filename):
    plt.figure()
    plt.plot(df["year"], df["value"])
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def bar_chart(df, title, filename):
    plt.figure()
    plt.bar(df["year"], df["value"])
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(axis="y")
    plt.savefig(filename)
    plt.close()

bar_chart(poverty, "Kenya Poverty Bar Chart", "outputs/kenya_poverty_bar_chart.png")
bar_chart(unemp, "Kenya Unemployment Bar Chart", "outputs/kenya_unemployment_bar_chart.png")

plot(poverty, "Kenya Poverty Trend", "outputs/kenya_poverty_trend.png")
plot(unemp, "Kenya Unemployment Trend", "outputs/kenya_unemployment_trend.png")

print("Analysis complete. Outputs saved.")
