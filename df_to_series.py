import pandas as pd
import numpy as np

dict={'col1' : [1,np.nan,-3] , 'col2':[3,-6,np.nan]}
df = pd.DataFrame(dict)
print(f'\ndf\n{df}')

# apply len for each row
print(f'apply len per\n{df.apply(len,axis=1)}')

# get non nan on row
# print(df.loc[1].dropna())

# get first not nan on row

# get non nan on col

# get first not nan on col

