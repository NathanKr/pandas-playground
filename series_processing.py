import pandas as pd

# get the string which represent integers
s1 = pd.Series(['$' , '11' , 'a1', '123'])
print(f'\ns1\n{s1}')
res_bool : pd.Series = s1.apply(lambda string : string.isnumeric())
print(f'\nis numeric in series : {res_bool}')

# get the numeric based on res
res_series = s1[res_bool]
print(f'\nres_series : {res_series}')
print(f'\nres_series.array : {res_series.array}')
print(f'\ntype(res_series) : {type(res_series)}')
