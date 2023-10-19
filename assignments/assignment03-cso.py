#script to pull data from CSO and write to .json file
#author: David Higgins - G00411302

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getData():
    response = requests.get(url, verify=False)  #work computer is causing issues with SSL so I have to set verify to false to get this to run
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getData()), file=fp)
