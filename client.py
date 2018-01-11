import os
from sftp import Client
import util

####################################################
USER = 'pi'
HOST = '192.168.0.6'
KEY = 'C:\\Users\\ffran\\.ssh\\raspberrypi.id_rsa'
DEFAULT_LOCAL_DEPOSIT = "C:\\Users\\ffran\\Downloads"
DEFAULT_REMOTE_DEPOSIT = "/home/pi/Downloads"
####################################################




try:
    client = Client(user=USER,
                    host=HOST,
                    key=KEY,
                    default_local_deposit=DEFAULT_LOCAL_DEPOSIT,
                    default_remote_deposit=DEFAULT_REMOTE_DEPOSIT)
    while True:
        client.display_main_menu()
        client.get_entry()

except Exception as e:
    util.error(e)
