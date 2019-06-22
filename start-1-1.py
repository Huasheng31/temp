#!/usr/local/bin/python3

from netmiko import ConnectHandler
from pprint import pprint
import warnings

# Display style
INFO = '\033[1;34;40m'
SUCCESS = '\033[1;32;40m'
ERROR = '\033[1;31;40m'
NORMAL = '\033[0;37;40m'

# Devices list
vqfx01 = {
  'device_type': 'juniper',
  'ip': 'localhost',
  'username' : 'root',
  'password' : 'Juniper',
  'port' : '2222'
}
all_vqfx = [
  vqfx01
]

# Filter warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

# Show command function
def show_command(command, search):
  output = net_connect.send_command(command)
  print (
    '\nCommand: {0}{1}{2} \n'
    .format(
      INFO,
      command,
      NORMAL
    )
  )
  for single_line in output.splitlines():
    if search in single_line:
      print (single_line)

# Set command function
def set_command(command):
  net_connect.send_command('cli')
  net_connect.config_mode()
  net_connect.send_command(command)
  net_connect.commit(comment='Enabled NETCONF service', and_quit=True)

# Main process
for a_vqfx in all_vqfx:
  try:
    net_connect = ConnectHandler(**a_vqfx)
    print (
      '\n\n{0}{1} Device: {2} port: {3} {4}{5}'
      .format(
         SUCCESS,
         '>'*10,
         a_vqfx['ip'],
         a_vqfx['port'],
         '<'*10,
         NORMAL
      )
    )
    show_command('show configuration', 'netconf')
    print (
      '\n{0}{1}{2} \n'
      .format(
        INFO,
        'Applying netconf configuration',
        NORMAL
      )
    )
    set_command('set system services netconf ssh')
    show_command('show configuration', 'netconf')
    print ('\n')
    net_connect.disconnect()
  except ConnectError as err:
    print (
      '\n\n{0}{1} Device: {2} port: {3} {4}{5}'
      .format(
        ERROR,
        '>'*10,
        a_vqfx['ip'],
        a_vqfx['port'],
        '<'*10,
        NORMAL
      )
    )
