import requests
import pandas as pd
from datetime import datetime

def convert_to_years(maturity_str):
  if "Mo" in maturity_str:
    return int(maturity_str.split()[0])/12
  elif "Yr" in maturity_str:
    return int(maturity_str.split()[0])
  return 0.0

def fetch_yield_curve():
  url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2025"

  #read tables from Treasury site
  tables = pd.read_html(url)
  df = tables[0]

  #get the most recent row
  latest = df.iloc[0]
  date = pd.to_datetime(latest["Date"])
  yields = latest[1:].astype(float) #skip the date column

  #convert maturities to years
  maturities_years = [convert_to_years(m) for m in yields.index]

  #build dataframe
  data = pd.DataFrame({
    "Maturity": maturities_years,
    "Yield": yields.values,
    "Date": date
  })
  return data
  





