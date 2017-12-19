import os, pysftp


class Client:
    def __init__(self, user, host, key):
        self.host = host
        self.user = user
        self.key = key

    def upload_file(self, local_path, remote_path):
        remote_path = self.clean_remote_path(remote_path) + os.path.basename(local_path)
        sftp = pysftp.Connection(host=self.host, username=self.user, private_key=self.key)
        input('\t' + local_path + "    ----->     " + remote_path)
        sftp.put(local_path, remote_path)
        sftp.close()
    
    def download_file(self, remote_path):
        remote_path = self.clean_remote_path(remote_path)
        sftp = pysftp.Connection(host=self.host, username=self.user, private_key=self.key)
        local_path = os.path.join("C:\\_util\\home_server\\deposit", os.path.basename(remote_path))
        input('\t' + remote_path + "    ----->     " + local_path)
        sftp.get(remote_path, local_path)
        sftp.close()

    @staticmethod
    def clean_remote_path(path):
        while True:
            if path[0] == ' ':
                path = path[1:]
            else:
                break
        i = len(path) - 1
        while True:
            if path[i] == ' ':
                path = path[:i]
            else:
                break
            i -= 1
        if path[0] == '~':
            path = '/home/ffran' + path[1:]
        return path
 
    def get_user(self):
        return self.user

    def get_host(self):
        return self.host



