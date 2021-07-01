import pandas as pd

series = pd.Series([1,2,35,4,5])
print(f'\nseries\n{series}')
print(f'\nseries.to_numpy()\n{series.to_numpy()}')

filt = [True,False,True,False,False]
print(f'\nseries[filt]\n{series[filt]}')

print(f'\nseries[1:3]\n{series[1:3]}')