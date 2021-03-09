import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)


# remove first row by index
df.drop([0],inplace=True)
print("df : \n",df)
