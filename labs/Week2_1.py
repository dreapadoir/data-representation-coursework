import requests
import csv

from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]


#print(doc.toprettyxml())

with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)


with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    #dataList = []
    objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionNode in objTrainPositionNodes:
        #trainLatNode = objTrainPositionNode.getElementsByTagName("TrainLatitude").item(0)
        #trainLat = trainLatNode.firstChild.nodeValue.strip()
        #print(trainLat)
        
        dataList = []
        for retrieveTag in retrieveTags:
                datanode = objTrainPositionNode.getElementsByTagName(retrieveTag).item(0)
                if objTrainPositionNode.getElementsByTagName("TrainCode").item(0).firstChild.nodeValue.strip()[0] == "D":
                    dataList.append(datanode.firstChild.nodeValue.strip())

        train_writer.writerow(dataList)


    



