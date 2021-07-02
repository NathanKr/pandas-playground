import pandas as pd

df = pd.DataFrame([] , columns=['col0' , 'col1' , 'col2']) #choose columns

df['col0'] = [1,2,3] # set values to existing column
df['col1'] = [4,5,6] # set values to existing column
df['col2'] = [7,8,9] # set values to existing column

print (f'df\n{df}')

