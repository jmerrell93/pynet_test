import yaml
import json

my_list = range(6)
my_list.append('poop')
my_list.append('dicks')
my_list.append({})
my_list[-1]["ip_address"] = '10.10.10.243'
my_list[-1]["booths"] = range(5)

print my_list


with open('my_list.yml', 'w') as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open('my_list.json', 'w') as f:
    json.dump(my_list, f)

print "the file was created"
