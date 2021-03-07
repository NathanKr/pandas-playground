import pandas as pd

labels = ['col1' , 'col2' , 'col3']
s1 = pd.Series(['a' , 'b' , 'c'] , index = labels)
print(f"s1\n{s1}")

s2 = pd.Series(['A' , 'B' , 'C'], index = labels)
print(f"s2\n{s2}")

df = pd.DataFrame(data=[],columns=labels)
df = df.append(s1,ignore_index=True)
df = df.append(s2,ignore_index=True)

print(f"df\n{df}")