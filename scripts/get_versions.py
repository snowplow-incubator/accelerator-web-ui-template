import requests
import json
import os

with open("data/component_versions.json") as jsonFile:
    data = json.load(jsonFile)

temp_json = data

if os.path.exists("data/component_versions.json"):
    os.remove("data/component_versions.json")
else:
    print("The file does not exist")

for package in temp_json["packages"]:
    res = requests.get("https://api.github.com/repos" + package["url"])
    version = res.json()["tag_name"]
    package["version"] = version

print(temp_json)
jsonFile = open("data/component_versions.json", "w+")
jsonFile.write(json.dumps(temp_json))
jsonFile.close()
