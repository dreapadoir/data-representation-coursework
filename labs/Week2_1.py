import requests


from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

print(doc.toprettyxml())

with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)
