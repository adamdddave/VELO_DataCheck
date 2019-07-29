# Simple file to check VELO Dataset
import sys,os
import pandas as pd

def make_dataframes(infile):
    print('constructing datasets')
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
        #print (dfs[dsk].head())
    print('done')
    return dfs

def average_data(time_start, time_stop,dfs):
    tstart,tstop = pd.to_datetime([time_start,time_stop])
    print('averaging between',tstart,tstop)
    for k in dfs.keys():
        print('now on dataset',k)
        mask = (dfs[k]['Time'] > tstart) & (dfs[k]['Time'] <= tstop)
        #print( dfs[k].loc[mask])
        print(dfs[k].loc[mask].mean(axis = 0))
        
if __name__ == "__main__":
    if len(sys.argv)<2:
        print('please pass a file to parse')
        sys.exit()
    dfs = make_dataframes(open(sys.argv[1]))
    print(dfs.keys())
    tstart=input('please give a start time in hh:mm:ss format: ')
    tstop=input('please give a start time in hh:mm:ss format: ')
    average_data(tstart,tstop,dfs)
