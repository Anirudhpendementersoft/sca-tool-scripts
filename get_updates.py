#get_updates

from __future__ import print_function
import requests
import os.path
import time
import shutil
import sys
import pandas as pd
import json
import os
from os import listdir
from os.path import isfile, join
import zipfile36 as zipfile
from pandas import json_normalize as jnorm
import linecache
#import schedule
from apscheduler.schedulers.blocking import BlockingScheduler
import linecache
def PrintException():
    sys.exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(),sys.exc_type, exc_obj)
try:
    def get_updates():
        # if (os.path.exists("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd")):
        #     pass
        # else:
        #     os.mkdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd")

        d_path= "C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/"
        for year in range(2002,2023):
            file = 'nvdcve-1.1-' + str(year) + '.json.zip'
            # print(file)
            #need the URL, which for NVD files is an embedding of the year
            url = 'https://nvd.nist.gov/feeds/json/cve/1.1/' + file
            # print(url)
            r = requests.get(url)
            meta = r.headers['last-modified']
            #print(type(meta))             
            filetime =  time.ctime(os.path.getmtime("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/"+file))
            # print(meta,filetime)
            #print("Tue, 22 Nov 2022 08:15:11 GMT" <= "Tue, 29 Nov 2022 15:32:38 GMT")

            if meta >= filetime:
                print("modified,new file Downloading....")       
                ff = requests.get(url, allow_redirects=True)
                # print(f.raw)
                f_path = d_path + file
                # print(f_path)
                with open (f_path, 'wb') as out_file:
                    out_file.write(r.content)
                    shutil.copyfileobj(ff.raw,out_file)                   
                del ff              
            else:
                print('No new version found. You got the latest file!')

        if (os.path.exists("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_mod_json")):
            pass
        else:
            os.mkdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_mod_json")
        
        files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
        #print(files)
        files.sort()
        for file in files:
            file_name = file.replace('.json.zip', '.json')
            # print(filename)
            archive = zipfile.ZipFile(join("nvd/",file), 'r')
            jsonfile = archive.open(archive.namelist()[0])
            data = json.loads(jsonfile.read())
            new_data = json.dumps(data)
            #print(type(data)
            with open("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_mod_json/"+file_name,"w") as out:
                out.write(new_data)
            jsonfile.close()

    get_updates()
     
    # schedule.every(1).hours.do(job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    
except Exception as e:
            error = {}
            error_list=[]
            error['error'] = str(PrintException()).replace("'","\'")
            error_list.append(error)
            print(error_list)                 
# else: 
#     scheduler = BlockingScheduler()
#     scheduler.add_job(get_updates, 'interval',seconds=2)
#     scheduler.start()  
