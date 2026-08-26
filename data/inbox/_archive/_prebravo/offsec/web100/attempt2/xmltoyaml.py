import xmltodict
import yaml
xml_string="""<?xml version="1.0"?>
<Pet>
    <animal type="str">Cat</animal>
    <breed type="str">Donskoy</breed>
    <name type="str">Bailey</name>
    <age type="int">2</age>
    <vaccinations type="list">
        <item type="str">VAC-B235EB</item>
        <item type="str">VAC-2D0723</item>
        <item type="str">VAC-452605</item>
    </vaccinations>
</Pet>"""
print("The XML string is:")
print(xml_string)
python_dict=xmltodict.parse(xml_string)
yaml_string=yaml.dump(python_dict)
print("The YAML string is:")
print(yaml_string)