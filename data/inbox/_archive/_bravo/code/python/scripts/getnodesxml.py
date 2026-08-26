
import xml.etree.ElementTree as ET

# Parse the XML file
xmlfile = "/home/student/flag.xml"
# Parse the XML file
tree = ET.parse(xmlfile)

# Get the root element
root = tree.getroot()

# Find and extract comment nodes
comments = root.findall('.//User/comment')

for comment in comments:
    d = comment.text
    if d is not None:
        print (d)
        # then paste to cyberchef and use "From Hex"

