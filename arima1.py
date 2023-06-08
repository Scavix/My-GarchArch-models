import pandas as pd
import statsmodels.api as sm

# A stationary arma(1,1) model
data = pd.read_csv('data.csv', index_col='Date', parse_dates=True)
model = sm.tsa.ARIMA(data, order=(1, 1, 1))
results = model.fit()
print(results.summary())