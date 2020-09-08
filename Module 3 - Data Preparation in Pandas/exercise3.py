import pandas as pd


df = pd.read_csv("https://data.heatonresearch.com/data/t81-558/datasets/series-31.csv")
df['date'] = pd.to_datetime(df['time'], errors='coerce')

# print(df.groupby('time').mean())


first = df.set_index('date').resample('d')["value"].first().dropna(how='all').rename('starting')
maximun = df.set_index('date').resample('d')["value"].max().dropna(how='all').rename('max')
minimun = df.set_index('date').resample('d')["value"].min().dropna(how='all').rename('min')
last = df.set_index('date').resample('d')["value"].last().dropna(how='all').rename('ending')

df = pd.concat([first, maximun, minimun, last], axis=1).reset_index()

print(df)
