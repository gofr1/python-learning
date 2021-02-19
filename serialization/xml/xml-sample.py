from os import chdir
import xml.etree.ElementTree as xml
from datetime import datetime

# de-serialize
tree = xml.parse('metric.xml')
root = tree.getroot()
print(root.tag)
#* metric

for child in root: # iterate over children
    print(child.tag)
#* time
#* name
#* value
#* labels

# find child by tag
value = root.find('value')
print('value:', value.text)
#* value: 3.14 

# find children by XPATH
for label in root.findall('./*/label'): 
    key, value = label.get('key'), label.get('value')
    print(f'key = {key!r}, value = {value!r}')
#* key = 'host', value = 'prod'
#* key = 'version', value = '1.2.6'

# serialize
metric = {
    'time': datetime.now(),
    'name': 'metric',
    'value': 3.14,
    'labels': {
        'host': 'prod9',
        'version': '1.4.5'
    }
}

def new_element(tag, text):
    """Helper function to create an element with text"""
    elem = xml.Element(tag)
    elem.text = text
    return elem

root = xml.Element('metric')
root.append(new_element('time', metric['time'].isoformat()))
root.append(new_element('name', metric['name']))
root.append(new_element('value', str(metric['value'])))
labels = xml.Element('labels')
for key, value in metric['labels'].items():
    labels.append(xml.Element('label', key=key, value=value))
root.append(labels)

data = xml.tostring(root)
print('xml:', data.decode('utf-8'))
#* xml: 
#* <metric>
#*     <time>2021-02-19T20:51:11.955824</time>
#*     <name>metric</name><value>3.14</value>
#*     <labels>
#*         <label key="host" value="prod9" />
#*         <label key="version" value="1.4.5" />
#*     </labels>
#* </metric>
