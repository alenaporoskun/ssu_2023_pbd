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

    print_header("Create folder 'src' and copy the csv files.")
    fun_copy_csv_files()

def print_header(msg):
    line = '=' * (len(msg) + 2)
    print(f'\n{line}')
    print(f' {msg} ')
    print(f'{line}')

def fun_copy_csv_files():
    # Create folder 'src' and copy the csv files
    if os.path.exists('./src') == False:
        print("Copy the csv files...\n")
        os.mkdir('./src')
        # print(os.getcwd())
        paths_from = ['./data/oil-prices-master/data', './data/population-master/data/', './data/ppp-master/data/']
        paths_to = ['./src/oil-prices', './src/population', './src/ppp']

        for i in range(len(paths_from)):
            os.mkdir(paths_to[i])
            k = 0
            for file in os.listdir(paths_from[i]):
                k += 1
                print("#", k)
                print('name of file: ', file)
                path_join = os.path.join(paths_from[i], file)
                print('path_join: ', path_join, '\n')
                shutil.copy2(path_join, paths_to[i])

            if os.listdir(paths_from[i]) == os.listdir(paths_to[i]):
                print("All files from folder '{}' to folder '{}' are copied.\n".format(paths_from[i], paths_to[i]))

        print("The process of copying files is complete.\n")


if __name__ == '__main__':
    main()