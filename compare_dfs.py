import pandas as pd

df1 = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])

df2 = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])

df3 = pd.DataFrame([[11, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])

df_compare_result : pd.DataFrame = df1 == df2
print(df_compare_result == True)
                  
df_compare_result : pd.DataFrame = df1 == df3
print(df_compare_result.all(axis=None) == True)
