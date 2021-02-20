import xml.dom.minidom

uglyxml = '<?xml version="1.0" encoding="UTF-8" ?><employees><employee><Name>Leonardo DiCaprio</Name></employee></employees>'
xml = xml.dom.minidom.parseString(uglyxml)
xml_pretty_str = xml.toprettyxml()
print(xml_pretty_str)