import pysftp as sftp


def push_file_to_server():
    s = sftp.Connection(host='192.168.0.5',
                        username='ffran')
    local_path = "test.txt"
    remote_path = "/home/ffran/testsftp.txt"
    s.put(local_path, remote_path)
    print(local_path + "    ----->     " + remote_path)
    s.close()

def get_file_from_server():
    s = sftp.Connection(host='192.168.0.5',
                        username='ffran')
    local_path = "test_retour.txt"
    remote_path = "/home/ffran/testsftp.txt"
    s.get(remote_path, local_path)
    print(remote_path + "    ----->     " + local_path)
    s.close()


if __name__ == '__main__':
    #push_file_to_server()
    get_file_from_server()
    #sshCommand('192.168.0.5', 22, 'ffran')

