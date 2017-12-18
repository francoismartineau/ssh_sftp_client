import os, pysftp


class Client:
    def __init__(self, user, host, key):
        self.host = host
        self.user = user
        self.key = key

    def upload_file(self, local_path):
        sftp = pysftp.Connection(host=self.host, user=self.user, private_key=self.key)
        remote_path = "/home/ffran/Desktop/testsftp/" + os.path.basename(local_path)
        sftp.put(local_path, remote_path)
        print('\t' + local_path + "    ----->     " + remote_path)
        sftp.close()
    
    def download_file(self, remote_path):
        sftp = pysftp.Connection(host=self.host, user=self.user, private_key=self.key)
        local_path = os.path.join("C:\\_util\\ffran@ffran.com\\deposit", os.path.basename(remote_path))
        sftp.get(remote_path, local_path)
        print('\t' + remote_path + "    ----->     " + local_path)
        sftp.close()

    def get_user(self):
        return self.user

    def get_host(self):
        return self.host



