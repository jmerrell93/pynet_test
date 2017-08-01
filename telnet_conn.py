
import telnetlib
import time
from snmp_helper import snmp_get_oid,snmp_extract

TELNET_TIMEOUT = 6
TELNET_PORT = 23
#OID = '1.3.6.1.2.1.1.1.0'
#ip_addr = ['184.105.247.70', '184.105.247.71']
COMMUNITY = 'galileo'
SNMP_PORT = 161
username = 'pyclass'
password = '88newclass'

def connect_and_query(ip_address):
    remote_conn = telnetlib.Telnet(ip_address, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    time.sleep(2)
    remote_conn.write(password + '\n')
    remote_conn.write("terminal length 0" + '\n')
#    remote_conn.write("show ip int br" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    remote_conn.close()
    device = (ip_address, COMMUNITY, SNMP_PORT)
    OID = '1.3.6.1.2.1.1.1.0'
    snmp_get = snmp_get_oid(device, OID)
    output = snmp_extract(snmp_get)
    print "FOR DEVICE %s" %ip_address
    print "DEVICE DESCRIPTION"
    print output + '\n'
    OID = '1.3.6.1.2.1.1.5.0'
    snmp_get = snmp_get_oid(device, OID)
    output = snmp_extract(snmp_get)
    print "DEVICE NAME"
    print output

connect_and_query('184.105.247.70')
connect_and_query('184.105.247.71')
