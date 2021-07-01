import pandas as pd
import numpy as np

dict={'col1' : [1,np.nan,-3] , 'col2':[3,-6,np.nan]}
df = pd.DataFrame(dict)
print(f'\ndf\n{df}')


print(f'\nfirst not nan on row\n{df.apply(lambda row_series : row_series.dropna()[0] ,axis=1)}')

print(f'\nfirst not nan on col\n{df.apply(lambda row_series : row_series.dropna()[0] ,axis=0)}')


