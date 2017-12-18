import util_ssh as ssh
from client import Client
import util

user = 'ffran'
local = '192.168.0.5'
extern = '70.80.147.138'

client = Client(user=user, host=extern, key='C:\\Users\\ffran\\.ssh\\home_server.id_rsa')

while True:
    util.main_menu()
    choix = input('\t')
    if choix == '1':
        client.upload_file(input('\n\tlocal file to upload: '))        
    elif choix == '2':
        client.download_file(input('\n\tremote file to download: '))
    elif choix == '3':
        util.navigate(client.get_user(), client.get_host())
