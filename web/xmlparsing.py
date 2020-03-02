import xml.dom.minidom as xml_dom

# use parse() function to load and parse an xml file
doc = xml_dom.parse("samplexml.xml")

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of xml tags
skills = doc.getElementsByTagName('skill')
print("{} skills:".format(skills.length))
for skill in skills:
    print(skill.getAttribute('name'))

# create a new xml tag and add it to document
new_skill = doc.createElement('skill')
new_skill.setAttribute('name', 'jQuery')
doc.firstChild.appendChild(new_skill)

skills = doc.getElementsByTagName('skill')
print("{} skills:".format(skills.length))
for skill in skills:
    print(skill.getAttribute('name'))

