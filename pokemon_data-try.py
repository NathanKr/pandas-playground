import pandas as pd
print(pd.__version__)

#  *********** load data set into DataFrame ***********
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv
file_name = "pokemon_data.csv"

poke_dataFrame = pd.read_csv(file_name)
print("poke_dataFrame.shape : ",poke_dataFrame.shape)
# get by default first 5 data rows
print("poke_dataFrame.head()\n",poke_dataFrame.head())# how to see without ... ???
# get last 4 data rows (default is 5)
print("poke_dataFrame.tail(4)\n",poke_dataFrame.tail(4))# how to see without ... ???


#  *********** read data from DataFrame ***********
# get columns name
print("columns\n",poke_dataFrame.columns )


# get all data using iloc[:,:]
print("poke_dataFrame.iloc[:,:].shape : ",poke_dataFrame.iloc[:,:].shape)

# get first row
print("poke_dataFrame.iloc[0] : \n",poke_dataFrame.iloc[0])

# get second,third and forth rows
print("poke_dataFrame.iloc[1:4] : \n",poke_dataFrame.iloc[1:4])


# get first column shape by index
print("poke_dataFrame.iloc[:,0].shape : ",poke_dataFrame.iloc[:,0].shape)

# get second item on second row
print("poke_dataFrame.iloc[1,1] : ",poke_dataFrame.iloc[1,1])


# get column by name
print("poke_dataFrame['Name'] : \n",poke_dataFrame['Name'])

# get few columns by name
print("poke_dataFrame[['Name','Attack','Speed'] : \n",poke_dataFrame[['Name','Attack','Speed']])

# get statistics
print("poke_dataFrame.describe() : " , poke_dataFrame.describe())

# sort
print("poke_dataFrame.sort_values('Name')\n",poke_dataFrame.sort_values('Name'))

# change : add column
print("before add column poke_dataFrame.shape : ",poke_dataFrame.shape)
poke_dataFrame["Total_Sp"] = poke_dataFrame["Sp. Atk"] + poke_dataFrame["Sp. Def"] 
print("after add column poke_dataFrame.shape : ",poke_dataFrame.shape)
print(poke_dataFrame.head())

# change : remove column
print("before remove column poke_dataFrame.shape : ",poke_dataFrame.shape)
poke_dataFrame = poke_dataFrame.drop(columns = ["Total_Sp"])
print("after remove column poke_dataFrame.shape : ",poke_dataFrame.shape)
print(poke_dataFrame.head())

# save
poke_dataFrame.to_csv("pokemon_data_saved.csv")

