import pandas as pd
import os
from os.path import join 

current_dir = os.path.abspath(".")
file_name = join(current_dir, 'datasets','nba','players.csv')
df = pd.read_csv(file_name)
print(df)

# add styling -> not working on vs code but i guess it will work on notebook
df.style.set_table_styles(
    [{'selector': 'tr:hover',
      'props': [('background-color', 'yellow')]}]
)


print(df.head()) 

