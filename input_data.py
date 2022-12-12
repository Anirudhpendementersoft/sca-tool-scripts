# # input_data
# import base64
# from github import Github
# from giturlparse import parse
# import sys
# import os

# #username ="Anusha Mutyala"
# #password =""

# repo_url= input("give repo url: ")
# p= parse(repo_url)

# # print(p.repo)
# #authenticate to github
# #get authenticated user
# #repo_list =[]
# #repos -g.get_user().get_repos()
# #for repo in repos:
# 	#repo_list.append(repo.name)

# #login
# path ="C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/"

# clone ="git clone "+repo_url
# os.chdir(path)
# os.system(clone)
# cmd ="syft dir:" + path +"/"+ p.repo +" -o spdx-json"
# # print(cmd)
# os.system(cmd)

import base64
from github import Github
from giturlparse import parse
import sys
import os

#username ="Anusha Mutyala"
#password =""

repo_url= input("give repo url: ")
p = parse(repo_url)

#print(p.repo)
#authenticate to github
#get authenticated user
#repo_list =[]
#repos -g.get_user().get_repos()
#for repo in repos:
	#repo_list.append(repo.name)

#login
path ="C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/"
clone ="git clone "+repo_url
os.chdir(path)
os.system(clone)
	#path ="C:/Users/HI/Desktop/"
	#clone =" git clone "+repo_url
# cmd ="syft dir:"+path +"/"+p.repo +" -o spdx-json >>C:/Users/aniru/OneDrive/Desktop/SCA-Scripts/sbom.txt"
# os.system(cmd)


