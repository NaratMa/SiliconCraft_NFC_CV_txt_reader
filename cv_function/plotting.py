
from turtle import color
from matplotlib import style
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from cv_function.format_loop_number import format_loop_number

#incomplete
def singleplot(data:pd.DataFrame):
    """_summary_
        create scatter plot from dataframe
    Args:
        df (pd.DataFrame): dataframe of cv using import_NFC_CV_data and modified with format_loop_number   
    """

    sns.scatterplot(x='V (mV)', y='I (uA)',data=data, s=3, hue='Loop')


def multiplot(pd_arr:list):
    """_summary_
        create scatter plot from a list of dataframe
    Args:
        list of pd.DataFrame: dataframe of cv using import_NFC_CV_data and modified with format_file_name   
    """
    merged_df = pd.DataFrame()
    for eachdf in pd_arr:
        merged_df = merged_df.append(eachdf)
        
    sns.scatterplot(x='V (mV)', y='I (uA)',data=merged_df, s=3, hue='Filename')


"""
    #Convert voltage range config from str to float value
    xlowerlim = float(config['VStart'][0:-1])
    xupperlim = float(config['VMid'][0:-1])
    #Change from V to mV
    xlowerlim = xlowerlim * 1000
    xupperlim = xupperlim * 1000
    
    cv_plot.set(xlim=(xlowerlim,xupperlim))
    
    #Standard current range for NFC sensor
    cv_plot.set(ylim=(-40,40))
"""     
    
"""
fig, ax = plt.subplots()
sns.scatterplot(data = df, x='V (mV)', y='I (uA)', size=1, ax=ax)
plt.show()
"""