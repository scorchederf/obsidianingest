import yaml

yamlfile = "C:\\dev\\git\\bravo\\offsec\\web100\\attempt1\\flag.yaml"
# Open the YAML file
with open(yamlfile, 'r') as file:
    # Load the YAML content
    yaml_content = yaml.load(file, Loader=yaml.FullLoader)
    print (yaml_content)
    # Iterate through the YAML content
    for key, value in yaml_content.items():
        print(f"Key: {key}")
        print(f"Value: {value}")