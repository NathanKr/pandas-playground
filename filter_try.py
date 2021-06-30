import pandas as pd

dict = {'col1' : [10,17,20] , 
        'col2' : [11,21,31]}

df = pd.DataFrame(dict)
print(f'\ndf\n{df}')


# search for values > 19 in the dataframe
print (f'\ndf[df > 19]\n{df[df > 19]}')


# search for values using logical and
filt = (df > 19) & (df < 22)
print (f'\nfilt\n{filt}')
print (f'\ndf[filt]\n{df[filt]}')
print (f'\ndf[~filt]\n{df[~filt]}') # not ( > 19 and < 22)



