import pandas as pd



def import_NFC_CV_data(path:str):
    """
    This function return formated dataframe using raw CV.txt file from path or print message if file cannot be process
    """
    try:
        df = pd.read_csv(path, sep = "\t" , header = 48 ,index_col=0, usecols=[0,1,2,3])
        df.rename(columns= lambda name: name.strip(), inplace=True)
        df.rename(columns={'I(uA)': 'I (uA)'}, inplace=True)
        df.dropna(inplace=True)
        return df
    except:
        print("File not found or Cannot be read")
        
def import_NFC_CV_config(path:str):
    """
    This function return dictionary of configuration using in the raw CV.txt from path or print message if file cannot be process
    """
    try:
        config_arr_str=[]
        config_dict={}
        with open(path) as file:
            #Selecting line with config infomation
            lines_to_read = [0,*range(4,14,1)]

            for line_index, line in enumerate(file):
                if line_index in lines_to_read:
                    translator = str.maketrans({'\n': '', '\t': '', ' ':''})
                    line=line.translate(translator)
                    config_arr_str.append(line)
        for each_config in config_arr_str:
            colon_index = each_config.find(":")
            config_name = each_config[0:colon_index]
            config_value = each_config[(colon_index + 1):]
            config_dict[config_name] = config_value
        return config_dict
    except:
        print("File not found or Cannot be read")
                