# from pymongo import MongoClient

# # # Creating a client
# myclient = MongoClient('mongodb://localhost:27017/')
# # print(myclient)

# # # Creating a database name as "anirudh_db"
# mydb = myclient["anirudh_db"]

# # #check database exist or not
# # print(myclient.list_database_names())

# # # create collection in anirudh_db name as "Student"
# mycoll = mydb["Student"]

# # # check collections exist or not
# #print(mydb.list_collection_names())

# # # insert values in collections 
# # dictionary = {"id" : 1 ,"name" : "Anirudh","marks" : 97}
# # mycoll.insert_one(dictionary)
# # mycoll.insert_many([
# # 	{"Eid" : 1 , "name" : "Anirudh", "marks" : 95,"location":"HYD"},
# # 	{"Eid" : 2 , "name" : "shiva", "marks" : 92,"location":"MUMBAI"},
# # 	{"Eid" : 3 , "name" : "raj", "marks" : 97,"location":"PUNE"},
# # 	{"Eid" : 4 , "name" : "surya", "marks" : 89,"location":"DELHI"}
# # 	])

# for i in mycoll.find():
# 	print(i['Eid'])


import json
# with open("C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/nvd/nvd_mod_json/nvdcve-1.1-2002.json","r") as f:
# 	data = json.load(f)
with open('C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/sample/test1.json') as f:
	data = json.dumps(f.read())
	new_data = json.loads(data)

