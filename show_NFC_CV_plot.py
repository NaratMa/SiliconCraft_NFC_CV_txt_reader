from cv_function.import_NFC_CV_data import import_NFC_CV_config,import_NFC_CV_data
from cv_function.plotting import multiplot, singleplot
from cv_function.format_loop_number import format_loop_number
from cv_function.format_file_name import format_file_name
import seaborn as sns
import matplotlib.pyplot as plt
import os

#input folder directory
print("Please input the directory of data's folder:")
path = input()

#Select plotting option 1 - one file or 2 - all files
print("Please select process option \n1 - one file\n2 - all files")
process_option = input()

if process_option == '1':
    print("Please input the selected file's name")
    filename=input()
    cv_data = import_NFC_CV_data(path+"\\"+filename)
    cv_config = import_NFC_CV_config(path+"\\"+filename)
    number_of_loop = int(cv_config['Loop'])
    cv_data_add_loop_column = format_loop_number(cv_data,number_of_loop)
    singleplot(cv_data_add_loop_column)


elif process_option == '2':
    file_arr=[]
    for filename in os.listdir(path):
        cv_data = import_NFC_CV_data(path+"\\"+filename)
        cv_config = import_NFC_CV_config(path+"\\"+filename)
        filename = cv_config['File']
        cv_data_add_filename = format_file_name(cv_data,filename)
        file_arr.append(cv_data_add_filename)        
    multiplot(file_arr) 

plt.show()

print("If the graph look unusual please make sure you input the correct path/filename and make sure that files in the path folder are all CV data from NFC sensor")