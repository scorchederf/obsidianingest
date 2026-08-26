import xmltodict
import yaml

def xml_to_yaml(xml_string):
    # Convert XML to OrderedDict
    xml_dict = xmltodict.parse(xml_string)

    # Convert OrderedDict to YAML string
    yaml_string = yaml.dump(xml_dict)

    return yaml_string


# Example XML input
xml_input = """
<?xml version="1.0" ?>
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
</Pet>

"""

# Convert XML to YAML
yaml_output = xml_to_yaml(xml_input)

# Print YAML output
print(yaml_output)