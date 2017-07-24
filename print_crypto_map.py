
from ciscoconfparse import CiscoConfParse

cisco_conf = CiscoConfParse('cisco_ipsec.txt')

crypto_maps = cisco_conf.find_objects(r'crypto map')

print '\nThe following are the crypto maps defined in the file'
print '-----------------------------------------------------'
for i in crypto_maps:
    print i.text
    children = i.children
    for i in children:
        print i.text

print '\nThe following lists those crypto maps that use PFS group2'
print '---------------------------------------------------------'

pfs_group2_maps = cisco_conf.find_objects_w_child(parentspec=r'^crypto map', childspec=r'set pfs group2')

for i in pfs_group2_maps:
    print i.text
print '\n'
print 'The following are those maps that do not use AES encryption'
print '-----------------------------------------------------------'

non_AES_maps = cisco_conf.find_objects_wo_child(parentspec=r'^crypto map', childspec=r'set transform-set AES-SHA')

for i in non_AES_maps:
    print i.text
    children = i.children
    print children[1].text



