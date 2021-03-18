import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
snp500_df = pd.read_html(url)[0]
symbols =  snp500_df . Symbol 
print(symbols)