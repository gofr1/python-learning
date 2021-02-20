import xml.etree.ElementTree as xml
from datetime import datetime
import csv
import xml.dom.minidom as minidom

def new_element(tag, text):
    elem = xml.Element(tag)
    elem.text = text
    return elem

root = xml.Element('records')

with open('ufo.csv') as sampleFile:
    sampleDictReader = csv.DictReader(sampleFile)
    for row in sampleDictReader:
        sighting = xml.Element('sighting')
        #print(row['LATITUDE'], row['LONGITUDE'], row['CITY'], row['DATE_OCCUR'], row['STATE'], row['UFO_SHAPE'], row['DURATION'] )
        sighting.append(new_element('time', row['DATE_OCCUR']))
        sighting.append(new_element('lat', row['LATITUDE']))
        sighting.append(new_element('lng', row['LONGITUDE']))
        sighting.append(new_element('shape', row['UFO_SHAPE']))
        root.append(sighting)
    

data = xml.tostring(root)
xml_dom = minidom.parseString(data)
xml_pretty = xml_dom.toprettyxml()

with open('ufo.xml', 'w') as out:
    out.write(xml_pretty)