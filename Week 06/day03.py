import pandas as pd

df = pd.read_csv(r"C:\Users\shubi\Desktop\AI\shop_sales_daily.csv")

print(df.head())
print("From", df["date"],min().date(),"to", df["date"].max().date(),
      "|", len(df), "days")

df["daysoweek"] = df["date"].dt.dayofweek
df['month'] = df["date"].dt.month

print('\nAverage sales by day of week:')
print(df.groupby('dayofweek')['sales'].mean().round())
print('\nAverage sales by year:')
print(df.groupby(df['date'].df.year)['sales'].mean(round()))