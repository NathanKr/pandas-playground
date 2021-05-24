import pandas as pd
import os

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
snp500_df = pd.read_html(url)[0]

file_path = os.path.join('temp','snp500_df_to_html.html')
print(f'write snp500_df to {file_path}')
snp500_df.to_html(file_path)

