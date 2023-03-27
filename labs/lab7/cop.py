#!/usr/bin/env python3
import csv
import json
import os
import shutil
import sys
from zipfile import ZipFile

import openpyxl
import pandas

def main():
    # src = '/src/file.txt'
    # dest = '/dest/dir'

    # shutil.copy2(src, dest)
    fn1 = 'oil-prices-master/data/brent-daily.csv'
    # ./data/oil-prices-master/data/'
    # ./src/oil-prices'

    os.path.join('oil-prices-master/data', 'brent-daily.csv'),

    '''print('./data/oil-prices-master/data')
    print('brent-daily.csv')
'''

    if os.path.exists('./src') == False:
        os.mkdir('./src')
        print(os.getcwd())
        paths_from = ['./data/oil-prices-master/data'] # , './data/population-master/data/','./data/ppp-master/data/']

        files_list = os.listdir(paths_from[0])
        print('files_list = os.listdir(paths_from[0])')
        print(files_list)

        paths_to = ['./src/oil-prices'] # , './src/population', './src/ppp']
        # os.mkdir('./src/oil-prices')
        # os.mkdir('./src/population')
        # os.mkdir('./src/ppp')
        for i in range(1):
            print(paths_from[i])
            print(files_list[0])
            # path_join = os.path.join(paths_from[i], files_list[0])
            f = './data/oil-prices-master/data'
            f2 = 'brent-daily.csv'
            path_join = os.path.join(f, f2)
            print(path_join)
            os.mkdir(paths_to[i])
            shutil.copy2(path_join, paths_to[i])



    src = './data/oil-prices-master/data/brent-daily.csv'
    dest = './src/oil-prices'
    # shutil.copy2(src, dest)


if __name__ == '__main__':
    main()