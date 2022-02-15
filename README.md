# SiliconCraft_NFC_CV_txt_reader

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
<img src="demo_pic/Real_NFC_setup.jpg" alt="report monitoring" width="500">
  </p>

After the NFC potentiostat perform electrochemical process the result can be show only in .txt format.
Therefore, this repository purpose is to help automate the process of viewing cyclic voltammogram from raw txt file of NFC portable potentiostat.


### Built With

* [seaborn](https://seaborn.pydata.org/index.html)
* [pandas](https://pandas.pydata.org/docs/index.html)

<!-- GETTING STARTED -->
## Getting Started

In order to use show_NFC_CV_plot.py to visualize cyclic voltammogram from raw txt file.
The following prerequisites are required.

### Prerequisites


* pandas
  ```sh
  pip install pandas
  ```
  
* seaborn
  ```sh
  pip install seaborn
  ```

<!-- USAGE EXAMPLES -->
## Usage

1. Run
  ```sh
  python show_NFC_CV_plot.py
  ```

2. Type the directory of data (Please make sure that there are only data file in that directory)
    <img src="demo_pic/input_dir.png" alt="report monitoring" width="500">

3. Choose plotting method between
3.1 Plot single data file
    
    This method will ask you to provide filename. (Please make sure you add .txt at the end) 
    <img src="demo_pic/select_1file.PNG" alt="report monitoring" width="500">
    
    This plot will display data of a single file with different color for each loop of cyclic voltammogram
    <img src="demo_pic/CV_pic_1data.png" alt="report monitoring" width="500">

3.2 Plot multiple data files
    This method will plot all data files in the directory with different color for each file
    <img src="demo_pic/select_all_file.PNG" alt="report monitoring" width="500">
    <br>
    <img src="demo_pic/CV_pic.png" alt="report monitoring" width="500">

<!-- CONTACT -->
## Contact

Narat M. - france.098@hotmail.com

Project Link: [https://github.com/NaratMa/SiliconCraft_NFC_CV_txt_reader](https://github.com/NaratMa/SiliconCraft_NFC_CV_txt_reader)





