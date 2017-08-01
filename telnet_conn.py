
import telnetlib
import time
from snmp_helper import snmp_get_oid,snmp_extract

TELNET_TIMEOUT = 6
TELNET_PORT = 23
COMMUNITY = 'galileo'
SNMP_PORT = 161
username = 'pyclass'
password = '88newclass'
OID_NAME = dict()
OID_NAME['1.3.6.1.2.1.1.1.0'] = 'DEVICE DESCRIPTION'
OID_NAME['1.3.6.1.2.1.1.5.0'] = 'DEVICE NAME'

def connect_and_query(ip_address):
    remote_conn = telnetlib.Telnet(ip_address, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    time.sleep(1)
    remote_conn.write(password + '\n')
    remote_conn.write("terminal length 0" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    snmp_query('1.3.6.1.2.1.1.1.0', ip_address)
    snmp_query('1.3.6.1.2.1.1.5.0', ip_address)

def snmp_query(OID, ip_address):
    device = (ip_address, COMMUNITY, SNMP_PORT)
    snmp_get = snmp_get_oid(device, OID)
    output = snmp_extract(snmp_get)
    print "\nFOR DEVICE %s" %ip_address
    print OID_NAME[OID]
    print output + '\n'

connect_and_query('184.105.247.70')
connect_and_query('184.105.247.71')
