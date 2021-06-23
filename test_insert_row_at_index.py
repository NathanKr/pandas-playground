from insert_row_at_index import insert_row_to_new_df
import pandas as pd

def test_insert_row_to_new_df_seperate_df_true():
    df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])

    orig_df = df.copy()
    new_df = insert_row_to_new_df(1,df,[-1,-2,-3,-4])
    new_df.iloc[0,0]= 999
    new_df.iloc[-1,-1]= -999

    expected_new_df = pd.DataFrame([[999, 2, 3, 4],[-1,-2,-3,-4], [4, 5, 6 , 7], [7, 8, 9 , -999]],
                  columns=['col1', 'col2', 'col3' , 'col4'])


    assert(new_df.equals(expected_new_df))        
    assert(df.equals(orig_df))           
    assert(len(new_df) == 4)
    assert(len(df) == 3)      
    assert(new_df.index.tolist() == [0,1,2,3])         

