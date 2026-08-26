import xmltodict
import yaml
import json

def serialize_file(input_file, output_file, output_format):
    with open(input_file, 'r') as f:
        content = f.read()
    
    if output_format == 'xml':
        if input_file.lower().endswith('.json'):
            data = json.loads(content)
            xml_content = xmltodict.unparse(data, pretty=True)
        elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
            data = yaml.safe_load(content)
            xml_content = xmltodict.unparse(data, pretty=True)
        else:
            raise ValueError("Unsupported input file format")
        
        with open(output_file, 'w') as f:
            f.write(xml_content)
    
    elif output_format == 'yaml':
        if input_file.lower().endswith('.xml'):
            data = xmltodict.parse(content)
            yaml_content = yaml.dump(data)
        elif input_file.lower().endswith('.json'):
            data = json.loads(content)
            yaml_content = yaml.dump(data)
        else:
            raise ValueError("Unsupported input file format")
        
        with open(output_file, 'w') as f:
            f.write(yaml_content)
    
    elif output_format == 'json':
        if input_file.lower().endswith('.xml'):
            data = xmltodict.parse(content)
            json_content = json.dumps(data, indent=4)
        elif input_file.lower().endswith('.yaml') or input_file.lower().endswith('.yml'):
            data = yaml.safe_load(content)
            json_content = json.dumps(data, indent=4)
        else:
            raise ValueError("Unsupported input file format")
        
        with open(output_file, 'w') as f:
            f.write(json_content)
    
    else:
        raise ValueError("Unsupported output format")

# Example usage
output_file = 'C:\\tmp\output.xml'  # Path to the input file
input_file = 'c:\\tmp\\output.json'  # Path to the output file
output_format = 'xml'  # Desired output format: xml, yaml, or json

serialize_file(input_file, output_file, output_format)
