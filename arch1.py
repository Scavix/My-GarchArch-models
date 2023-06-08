import pandas as pd
from arch import arch_model

returns = pd.read_csv('data.csv', index_col='Date', parse_dates=True)
model = arch_model(returns, vol='ARCH', p=1)
results = model.fit()

print(results.summary())