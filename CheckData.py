# Simple file to check VELO Dataset
import sys,os
import pandas as pd

if __name__=='main':
    if len(sys.argv)<1:
        print(please pass a file to parse and quickly create plots)
        sys.exit()
    # create dataset from input file
    df = pd.read_csv(sys.argv[1],names='Timestamp, Name, Voltage, Temperature, Offset',header=None) 
    #split dataframes by name
    VPA = {}
