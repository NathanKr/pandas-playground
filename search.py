import pandas as pd

dict = {'col1' : [10,20,33] , 
        'col2' : [11,21,31]
       }

df = pd.DataFrame(dict)

print(f'df\n{df}')

# filter dataframe
filt_df = df > 19
print (f'\nfilt_df\n{filt_df}') # return same size df with boolean
print(f'\ndf[filt_df]\n{df[filt_df]}')

# filter series
series_col_1 = df['col1']
filt_series = series_col_1 > 19
print(f'\nfilt_series\n{filt_series}')
print(f'\nseries_col_1[filt_series]\n{series_col_1[filt_series]}')
print(f'\nseries_col_1[filt_series].array\n{series_col_1[filt_series].array}')


