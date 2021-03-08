import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df before update : \n",df)

# use iloc to update first col in second row
df.iloc[1,0]=99
print("df after first update : \n",df)

# use loc to update second col in third row
df.loc[2,'col2']=88
print("df after second update : \n",df)

