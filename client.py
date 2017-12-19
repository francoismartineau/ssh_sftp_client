from sftp import Client
import util

user = 'ffran'
host = util.hosts['local']


client = Client(user=user, host=host, key='C:\\Users\\ffran\\.ssh\\home_server.id_rsa')
while True:
    util.main_menu()
    choix = input('\t')
    if choix == '1':
        client.upload_file(input('\n\tlocal file to upload: '), input('\n\tserver directory: '))        
    elif choix == '2':
        client.download_file(input('\n\tserver file to download: '))
    elif choix == '3':
        util.navigate(user, host)
