import pandas as pd

def format_loop_number(df:pd.DataFrame, loopno:int):
    """_summary_
        create new datafram then add loopno column to dataframe 
    Args:
        df (pd.DataFrame): dataframe of cv using import_NFC_CV_data
        loopno (int): number of loop in this data (can be acquire from import_NFC_CV_config)
    """
    extended_df = df.copy()
    record_per_loop = int(df.shape[0]/loopno)
    loop_arr =[]
    for loop in range(1,loopno+1):
        loop_arr.extend(['Loop'+str(loop)]*record_per_loop)
    extended_df['Loop'] = loop_arr
    return extended_df    