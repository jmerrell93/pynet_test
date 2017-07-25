import yaml
import json


with open('my_list.yml') as f:
    yaml_list =  yaml.load(f)

print yaml_list

with open('my_list.json') as f:
    json_list = json.load(f)

print json_list

