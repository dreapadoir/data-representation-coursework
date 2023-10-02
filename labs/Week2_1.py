import requests


from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#print(doc.toprettyxml())

with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

dTrains = []
objTrainPositionNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionNode in objTrainPositionNodes:
    trainCodeNode = objTrainPositionNode.getElementsByTagName("TrainCode").item(0)
    trainCode = trainCodeNode.firstChild.nodeValue
    #print(trainCode)
    #for train in trainCode:
       # if train[0] == "D":
       #     print(trainCode)
        
#print(dTrains)



