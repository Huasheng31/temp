#!/usr/local/bin/python3

import sys
import warnings
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

# Display style
INFO = '\033[1;34;40m'
SUCCESS = '\033[1;32;40m'
ERROR = '\033[1;31;40m'
NORMAL = '\033[0;37;40m'

# Devices list
vqfx01 = {
  'host' : 'localhost',
  'user' : 'gilbert',
  'port' : '2222'
}
all_vqfx = [
  vqfx01
]

# Filter warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

# Get facts
for a_vqfx in all_vqfx:
  dev = Device(
    host=a_vqfx['host'],
    user=a_vqfx['user'],
    port=a_vqfx['port']
  )
  try:
    dev.open()
  except ConnectError as err:
    print (
      'Cannot connect to device: {0}'
      .format(err)
    )
    sys.exit(1)
  except Exception as err:
    print (err)
    sys.exit(1)
  # Print facts
  print (
    '\nDevice returned facts for: {0}{1}{2} {3}{4}{5}\n'
    .format(
      INFO,
      a_vqfx['host'],
      NORMAL,
      SUCCESS,
      a_vqfx['port'],
      NORMAL
     )
  )
  pprint (dev.facts)
  print (
    '\n{0}{1}: {2}{3}\n'
    .format(
      SUCCESS,
      dev.facts['hostname'],
      dev.facts['version'],
      NORMAL
     )
  )
  dev.close()
