import requests
import json

with open("data/component_versions.json", "w+") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.write(json.dumps({"temp": "json"}))

temp_json = data

for package in temp_json["packages"]:
    res = requests.get("https://api.github.com/repos" + package["url"])
    version = res.json()["tag_name"]
    package["version"] = version

print(temp_json)
jsonFile = open("data/component_versions.json", "w+")
jsonFile.write(json.dumps(temp_json))
jsonFile.close()
