import pandas as pd
import numpy as np

dict={'col1' : ['1445','23','5'] , 'col2':['3','-677','abc']}
df = pd.DataFrame(dict)
print(f'\ndf\n{df}')

print(f'apply len per row\n{df.apply(len,axis=1)}')
print(f'apply len per col\n{df.apply(len,axis=0)}') # this is the default
print(f'apply len per df\n{df.applymap(len)}')
