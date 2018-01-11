from sftp import Client
import util

user = 'ffran'
host = util.hosts['home_server_external']



client = Client(user=user, host=host, key='C:\\Users\\ffran\\.ssh\\home_server.id_rsa')
loop = True
while loop:
    loop = client.execute_command(input(client.getcwd() + "> ")) == None
