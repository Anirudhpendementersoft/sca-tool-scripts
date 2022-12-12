# #fetch_data
# import json
# from pymongo import MongoClient
# import requests
# import pandas as pd
# import json
# import sys
# import os
# from os.path import isfile,join

# myclient = MongoClient("mongodb://localhost:27017/")
# db= myclient["NVD"]
# Collection =db["nvd_files"]


# final_list =[]

# for x in Collection.find({},{"_id":0,"CVE_Items.cve":1}):
# 	for i in x.keys():
# 		for j in x['CVE_Items']:
# 			for k in j.values():
# 				for ref_value in k['references'].values():
# 					for l in ref_value:
# 						cve_url = {}
# 						cve_url["cve_id"] = k['CVE_data_meta']['ID']
# 						cve_url['cve_url'] = l['url']
# 						final_list.append(cve_url)
# id_list = []
# final_list1 = []
# final_list2 = []
# for i in final_list:
#     already = []
#     for j in final_list:
#         if i['cve_id'] == j['cve_id']:
#             already.append(j['cve_url'])
#     dict1 = {}
#     dict1['cve_id'] = i['cve_id']
#     dict1['cve_url'] = already
#     final_list1.append(dict1)
# # print(final_list1)
# for k in final_list1:
#     if k['cve_id'] not in id_list:
#         id_list.append(k['cve_id'])
# # print(id_list)
#         final_list2.append(k)
# print(final_list2)


# # for i in final_list:
# # 	var_id = i['cve_id']
# # 	var_url = i['cve_url']
# # 	url_list =[]
# # 	for j in final_list:
# # 		new_var_id = i['cve_id']
# # 		if var_id == new_var_id:
# # 			if var_url != j['cve_url']:
# # 				url_list.append(j['cve_url'])
# # print(url_list)

# # print(final_list)
from pymongo import MongoClient
import gridfs
import os
import ast
import json
from os.path import isfile,join
final_list =[]
db=MongoClient().NVD_DB
fs=gridfs.GridFS(db)
files =[f for f in os.listdir("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/") if isfile(join("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/",f))]
files.sort()
for file_name in files:
    with open("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd_json/"+file_name,'rb') as file1:
        grid =fs.put(file1)
        eye=fs.get(grid).read()
        dict_grid = eye.decode("UTF-8")
        final_grid= json.loads(dict_grid)
        # print(type(final_grid))
        for i in final_grid.keys():
            for j in final_grid['CVE_Items']:
                id_cve =j['cve']['CVE_data_meta']['ID']
                #print(j['cve']['references']['reference_data'])
                for k in j['cve']['references']['reference_data']:
                    url=k['url']
                    cve_url = {}
                    cve_url["cve_id"] = id_cve
                    cve_url['cve_url'] = url
                    final_list.append(cve_url)
                    print(final_list)