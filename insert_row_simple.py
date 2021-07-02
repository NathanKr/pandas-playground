import pandas as pd

df = pd.DataFrame([])

# most simple insert row
df = df.append(pd.Series([1,2,3]) , ignore_index=True) # insert at the end
df = df.append(pd.Series([4,5,6]) , ignore_index=True) # insert at the end

print(df)