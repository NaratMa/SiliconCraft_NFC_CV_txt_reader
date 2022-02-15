import pandas as pd

def format_file_name(df:pd.DataFrame, filename:str):
    """_summary_
        create new datafram then add filename column to dataframe 
    Args:
        df (pd.DataFrame): dataframe of cv using import_NFC_CV_data
        filename: filename of this data (can be acquire from import_NFC_CV_config)
    """
    extended_df = df.copy()
    extended_df['Filename'] = [filename]*df.shape[0]
    return extended_df    