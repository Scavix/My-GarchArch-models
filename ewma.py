import pandas as pd

data = pd.read_csv('data.csv', index_col='Date', parse_dates=True)
ewma = data.ewm(span=10).mean()

print(ewma)