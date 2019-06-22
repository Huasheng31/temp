#!/usr/local/bin/python3

import sys
import warnings
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
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

config_set = """
set vlans test1 vlan-id 10
set vlans test2 vlan-id 20
set vlans test3 vlan-id 30
"""

# Filter warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

# Create vlans
for a_vqfx in all_vqfx:
  dev = Device(
    host=a_vqfx['host'],
    user=a_vqfx['user'],
    port=a_vqfx['port']
  )
  try:
    dev.open()
    print (
      '\nConfiguring vlans for {0}{1} - {2}{3}\n'
      .format(
        INFO,
        a_vqfx['host'],
        a_vqfx['port'],
        NORMAL
       )
    )
    with Config(dev, mode='exclusive') as cu:
      cu.load(config_set, format="set", merge=True)
      cu.commit()
  except ConnectError as err:
    print (
      'Cannot connect to device: {0}'
      .format(err)
    )
    sys.exit(1)
  except Exception as err:
    print (err)
    sys.exit(1)
  dev.close()
