# Simple file to check VELO Dataset
import sys,os
import pandas as pd

def make_dataframes(infile):
    datasets = {'VP0_Asic0':[],'VP0_Asic1':[],'VP0_Asic2':[],
                'VP1_Asic0':[],'VP1_Asic1':[],'VP1_Asic2':[],
                'VP2_Asic0':[],'VP2_Asic1':[],'VP2_Asic2':[],
                'VP3_Asic0':[],'VP3_Asic1':[],'VP3_Asic2':[]
    }
    timestamp=[]
    temp = []
    name = []
    voltage=[]
    offset=[]
    for line in infile:
        ts,n,v,t,o = line.split(',')
        o = float(o.strip(" \n"))
        v = float(v)
        t = float(t)
        #print (ts,n,v,t,o)
        n=n.strip()
        datasets[n].append([ts,v,t,o])
        #sys.exit()
    dfs = {}
    for dsk,ds in datasets.items():
        dfs[dsk]=pd.DataFrame(ds, columns=['Time','Voltage','Temp','Offset'])
        dfs[dsk]['Time'] = pd.to_datetime(dfs[dsk]['Time'])
        print (dfs[dsk].head())


if __name__ == "__main__":
    if len(sys.argv)<2:
        print('please pass a file to parse and quickly create plots')
        sys.exit()
    dfs = make_dataframes(open(sys.argv[1]))
    
