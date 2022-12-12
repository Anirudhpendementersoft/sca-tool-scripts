#download_files

from __future__ import print_function
import requests
import pandas as pd
import json
import sys
import os
import ast
from os import listdir
from os.path import isfile, join
import zipfile36 as zipfile
from pandas import json_normalize as jnorm
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

    if (os.path.exists("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd")):
        pass
    else:
        os.mkdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd")
    d_path= "C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/"

    for year in range(2002,2023):
        file = 'nvdcve-1.1-' + str(year) + '.json.zip'       
        url = 'https://nvd.nist.gov/feeds/json/cve/1.1/' + file
        f = requests.get(url, allow_redirects=True)        
        f_path = d_path + file
        open(f_path, 'wb').write(f.content)
        f.close()
        # print(f)
    if (os.path.exists("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_json")):
        pass
    else:
        os.mkdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_json")
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
        with open("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_json/"+file_name,"w") as out:
            out.write(new_data)
        jsonfile.close()
    
except Exception as e:
            error = {}
            error_list=[]
            error['error'] = str(PrintException()).replace("'","\'")
            error_list.append(error)
            print(error_list)                 
       
    #print(cve_dict.keys())
    # print("CVE_data_timestamp: " + str(cve_dict['CVE_data_timestamp']))
    # print("CVE_data_version: " + str(cve_dict['CVE_data_version']))
    # print("CVE_data_format: " + str(cve_dict['CVE_data_format']))
    # print("CVE_data_numberOfCVEs: " + str(cve_dict['CVE_data_numberOfCVEs']))
    # print("CVE_data_type: " + str(cve_dict['CVE_data_type']))
    #print(json.dumps(cve_dict['CVE_Items']['lastModifiedDate'], sort_keys=True, indent=4, separators=(',', ': ')))

