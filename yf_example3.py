""" yf_example3.py

Download stock price data for Qantas for a given year and save the information in a CSV file
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    tic = "QAN.AX"
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    path= os.path.join(cfg.DATADIR,f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic,path,start,end)

if __name__ == "__main__":
    year=2020
    qan_prc_to_csv(year)