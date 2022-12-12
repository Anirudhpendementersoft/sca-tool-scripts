import requests

url = "https://cve.circl.lu/api/browse/microsoft/excel"

response = requests.get(url)

print(response.status_code)
print(response.content)