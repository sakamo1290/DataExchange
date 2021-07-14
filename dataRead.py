# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:27:09 2021

@author: sakam
"""


import pandas as pd

def ReadData(past, log):
    try:
        a = pd.read_csv('Unity2Python.csv', encoding="ms932" ,sep=",")
    except:
        return past, log
    if past == a.columns[0]: return past, log
    log = log.append([int(a.columns[0])])
    print(a.columns[0])
    past = a.columns[0]
    return past, log

def WriteData(past):
    try:
        pd.DataFrame([past]).to_csv(path_or_buf = 'Python2Unity.csv', header=False, index=False)
    except:
        return        

def main():
    log = pd.DataFrame(columns = [0], index = [0], data = [0])
    past = -1
    while True:
        past, log = ReadData(past, log)
        WriteData(past)
        
    
if __name__ == "__main__":
    main()
    