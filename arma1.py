import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('data.csv', index_col='Date', parse_dates=True)
model = sm.tsa.ARMA(data, order=(2, 1))
results = model.fit()

print(results.summary())