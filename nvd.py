#nvd
import json
from pymongo import MongoClient
import requests
import pandas as pd
import json
import sys
import os
from os.path import isfile,join
import zipfile36 as zipfile
from pandas import json_normalize as jnorm
import linecache

myclient = MongoClient("mongodb://localhost:27017/")
db= myclient["NVD"]
Collection =db["nvd_files"]
# fileDirectory =r"C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_mod_json/"
# fileExtension =".json"
# file =os.listdir(fileDirectory)
# file.sort
# for i in file:
# 	# print(i)
# 	if i.endswith(fileExtension):
# 		files = i
# 		# print(files)
# 		with open(files,"r") as f:
# 			data = f.read()
# 			print(data)
# 			data =json.loads(str(f))
files =[f for f in os.listdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/") if isfile(join("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/", f))]
files.sort()
for file_name in files:
	# print(file_name)
	with open(r"C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/"+file_name) as f:
		file_data = json.loads(f.read())
		# print((file_data))
		if isinstance(file_data,list):
			Collection.insert_many(file_data)
		else:
			Collection.insert_one(file_data)





