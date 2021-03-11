import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 3, 2, 1], [4, 5, -6 , 7], [7, 8, -9 , 10], [11, 23, 13, 14]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)


# remove first row by index
df.drop([0],inplace=True)
print("df : \n",df)


# remove rows with negative values on 'col3'
indexes = df[df['col3'] < 0].index
print (f'indexes : {indexes}')
df.drop(indexes, inplace = True) 
print("df : \n",df)
