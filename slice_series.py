import pandas as pd

series = pd.Series([1,2,35,4,5])
print(f'series : {series}')
print(f'series.to_numpy() : {series.to_numpy()}')

filt = [True,False,True,False,False]
print(f'\nseries[filt]\n{series[filt]}')