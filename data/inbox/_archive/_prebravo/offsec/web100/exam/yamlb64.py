import yaml

def iterate_nested_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            iterate_nested_list(item)
        else:
            print(item)
            print("-----------")

# Load YAML content from a file or string
with open('C:\\dev\\git\\bravo\\offsec\\web100\\attempt1\\flag.yaml') as file:  # Replace 'example.yaml' with your YAML file path or provide YAML content as a string
    yaml_data = yaml.safe_load(file)

#print(yaml_data)
#print(type(yaml_data))

iterate_nested_list(yaml_data)



finalstring = ""
