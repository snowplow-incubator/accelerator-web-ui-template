import requests
import json

with open("data/component_versions.json") as jsonFile:
    data = json.load(jsonFile)
temp_json = data
jsonFile.close()
for package in temp_json["packages"]:
    res = requests.get("https://api.github.com/repos" + package["url"])
    version = res.json()["tag_name"]
    package["version"] = version
jsonFile = open("data/component_versions.json", "w+")
jsonFile.write(json.dumps(temp_json))
jsonFile.close()
