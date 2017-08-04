
import telnetlib
import time
from snmp_helper import snmp_get_oid,snmp_extract
import pickle
import filecmp
import email_helper
import smtplib
from email.mime.text import MIMEText
 
TELNET_TIMEOUT = 6
TELNET_PORT = 23
COMMUNITY = 'galileo'
SNMP_PORT = 161
username = 'pyclass'
password = '88newclass'
OID_NAME = dict()
OID_NAME['1.3.6.1.2.1.1.1.0'] = 'DEVICE DESCRIPTION'
OID_NAME['1.3.6.1.2.1.1.5.0'] = 'DEVICE NAME'
OID_NAME['1.3.6.1.4.1.9.9.43.1.1.1.0'] = 'UPTIME WHEN CONFIG LAST CHANGED'

recipient = 'jmerrell93@hotmail.com'
sender = 'josh.merrell@wwt.com'
subject = 'Notice of Configuration Change'

def send_email(recipient, subject, message, sender):
    email_helper.send_mail(recipient, subject, message, sender)


def config_poll_1(ip_address):
    remote_conn = telnetlib.Telnet(ip_address, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    time.sleep(1)
    remote_conn.write(password + '\n')
    remote_conn.write("terminal length 0" + '\n')
    time.sleep(1)
    remote_conn.write("show running-config" + '\n')
    time.sleep(3)
    poll_1 = remote_conn.read_very_eager()
    f = open('poll_1.py', 'wb')
    pickle.dump(poll_1, f)
    f.close()

def config_poll_2(ip_address):
    remote_conn = telnetlib.Telnet(ip_address, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    time.sleep(1)
    remote_conn.write(password + '\n')
    remote_conn.write("terminal length 0" + '\n')
    time.sleep(1)
    remote_conn.write("show running-config" + '\n')
    time.sleep(3)
    poll_2 = remote_conn.read_very_eager()
    f = open('poll_2.py', 'wb')
    pickle.dump(poll_2, f)
    f.close()

def snmp_query(OID, ip_address):
    device = (ip_address, COMMUNITY, SNMP_PORT)
    snmp_get = snmp_get_oid(device, OID)
    output = snmp_extract(snmp_get)
    print "\nFOR DEVICE %s" %ip_address
    print OID_NAME[OID]
    print output + '\n'

info_1 = snmp_query('1.3.6.1.2.1.1.5.0', '184.105.247.71')
info_2 = snmp_query('1.3.6.1.4.1.9.9.43.1.1.1.0', '184.105.247.71')
message = '%s' %info_1 + '%s' %info_2

config_poll_1('184.105.247.71')
time.sleep(480)
config_poll_2('184.105.247.71')
f = open('poll_1.py', 'rb')
a = pickle.load(f)
a
f = open('poll_2.py', 'rb')
b = pickle.load(f)
b
if filecmp.cmp('poll_1.py', 'poll_2.py'):
    print "no changes"
else:
#    print "This is an alert that the following device has changed:\n"
#    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#    snmp_query('1.3.6.1.2.1.1.5.0', '184.105.247.71')
#    snmp_query('1.3.6.1.4.1.9.9.43.1.1.1.0', '184.105.247.71')
    send_email(recipient, subject, message, sender)

