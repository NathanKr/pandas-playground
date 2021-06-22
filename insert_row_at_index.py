from typing import List
import pandas as pd


def insert_row_to_new_df(i_row : int, df : pd.DataFrame, row : List)->pd.DataFrame:
    # Slice the upper half of the dataframe
    
    # use copy because df[0:i_row] is a view which we update and it is NOT allowed
    df1 = df[0:i_row].copy() 


    # Store the result of lower half of the dataframe
    df2 = df[i_row:]

    # Inser the row in the upper half dataframe
    df1.loc[i_row]=row
   
    # Concat the two dataframes
    new_df = pd.concat([df1, df2])
   
    # Reassign the index labels
    new_df.index = [*range(new_df.shape[0])]
   
    # Return the updated dataframe
    return new_df
