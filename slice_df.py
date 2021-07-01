import pandas as pd

dict = {'col1' : [1,2,3] , 'col2' : [4,5,6]}
df = pd.DataFrame(dict)
print(f'\ndf\n{df}')
print(f'last row\n{df.iloc[-1]}')
print(f'last col\n{df.iloc[:,-1]}')