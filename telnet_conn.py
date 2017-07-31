
import telnetlib
import time

TELNET_TIMEOUT = 6
TELNET_PORT = 23
ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'


#def send_command(remote_conn, cmd)
#    cmd = cmd.rstrip

remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
#read = remote_conn.read_until()

#write = remote_conn.write()

#output = read("sername:", TELNET_TIMEOUT)

output = remote_conn.read_until("sername:", TELNET_TIMEOUT)

print output

#write(username + '\n')

remote_conn.write(username + '\n')
output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
print output
remote_conn.write(password + '\n')
time.sleep(1)
remote_conn.write("terminal length 0" + '\n')
remote_conn.write("show ip int br" + '\n')
time.sleep(1)
output = remote_conn.read_very_eager()
print output
remote_conn.close()

