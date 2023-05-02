import requests
import os
from urllib import request
import wget
import time
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from zipfile import ZipFile
import pandas as pd
import zipfile
import glob

directory= "Downloads"

parent_dir="C:/Users/path/OneDrive/Desktop/"

path= os.path.join(parent_dir,directory)

#os.mkdir(path)
#print("Directory '% s' created" % directory)



download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]
fns = [r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2018_Q4.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2019_Q1.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2019_Q2.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2019_Q3.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2019_Q4.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2020_Q1.zip',
        r'C:\Users\path\OneDrive\Desktop\Downloads\Divvy_Trips_2220_Q1.zip'

]

inputs=zip(download_uris,fns)


def download_url(args):
    t0=time.time()
    url,fn=args[0],args[1]    
    try:
        r=requests.get(url)
        with open(fn,'wb') as f:
            f.write(r.content)
        return(url , time.time()-t0)
    except Exception as e:
        print("Problem Downloading", e)


t0=time.time()
for i in inputs:
    result=download_url(i)
    print('url: ',result[0], 'time (s):', result[1])
print('Total download time(s):', time.time()- t0)




with ZipFile('C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2018_Q4.zip','r') as obj:
   obj.extractall('C:\\Users\\path\\OneDrive\\Desktop\\albin\Python\\Downloads')


with ZipFile('C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2019_Q1.zip','r') as obj:
   obj.extractall('C:\\Users\\path\\OneDrive\\Desktop\\albin\Python\\Downloads')



files=['C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2018_Q4.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2019_Q1.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2019_Q2.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2019_Q3.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2019_Q4.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2020_Q1.zip','C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads\\Divvy_Trips_2220_Q1.zip']
for x in files:
    result=zipfile.ZipFile(x)
    result.extractall('C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads')
    
os.chdir('C:\\Users\\path\\OneDrive\\Desktop\\albin\\Python\\Downloads')
extension='csv'
all_filenames=[i for i in glob.glob('*.{}'.format(extension))]
combined=pd.concat([pd.read_csv(f) for f in all_filenames])
combined.to_csv("MainDataSet.csv",index=False,encoding='utf-8-sig')
