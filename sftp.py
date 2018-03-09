import os, pysftp
import util



class Client(pysftp.Connection):
    def __init__(self, user, host, key, default_local_deposit, default_remote_deposit):
        self.user = user
        self.host = host
        self.key = key
        self.default_local_deposit = default_local_deposit
        self.default_remote_deposit = default_remote_deposit

    def display_main_menu(self):
        util.clear_console()
        util.print_title()
        print("\n\n")
        self.tabs = "\t"
        print(self.tabs + "[1] Upload")
        print(self.tabs + "[2] Download")
        print(self.tabs + "[3] Navigate")
    
    def get_entry(self):
        answer = input(self.tabs)
        if answer == '1':
            pysftp.Connection.__init__(self, host=self.host, username=self.user, private_key=self.key)
            self.upload()
            self.close()
        elif answer == '2':
            pysftp.Connection.__init__(self, host=self.host, username=self.user, private_key=self.key)
            self.ori_remoth_path = input(self.tabs + "Remote path: ")
            self.ori_local_path = input(self.tabs + "Local destination(optional): ")
            if not self.ori_local_path: self.ori_local_path = self.default_local_deposit
            self.download(local_path=self.ori_local_path, remote_path=self.ori_remoth_path)
            self.close()
        elif answer == '3':
            util.git_bash()



    def upload(self, local_path="", remote_path=""):
        local_path, remote_path = self.upload_manage_paths(local_path, remote_path)
        if os.path.isfile(local_path):
            self.upload_file(local_path, remote_path)
        elif os.path.isdir(local_path):
            self.upload_dir(local_path, remote_path)
        else:
            input(self.tabs + "Wrong file name.")

    def upload_manage_paths(self, local_path, remote_path):
        if not local_path:
            local_path = input(self.tabs + "Local path: ")
        if not remote_path:
            remote_path = input(self.tabs + "Remote destination(optional): ")
            if not remote_path:
                print(self.tabs + "default deposit used")
                remote_path = self.default_remote_deposit
        remote_path = remote_path + "/" + os.path.basename(local_path)
        return local_path, remote_path

    def upload_file(self, local_path, remote_path):
        self.put(local_path, remote_path)
        print('\n' + self.tabs + os.path.basename(local_path) + "    ----->     " + remote_path)

    def upload_dir(self, local_path, remote_path):
        self.makedirs(remote_path)
        for (cwd, dirs, files) in os.walk(local_path):
            for d in dirs:
                self.upload(os.path.join(cwd, d), remote_path)
            for f in files:
                self.upload(os.path.join(cwd, f), remote_path)
            break





    def download(self, remote_path, local_path=""):
        local_path, remote_path = self.download_manage_paths(local_path, remote_path)
        if self.isfile(remote_path):
            os.chdir(os.path.dirname(local_path))
            local_path = os.path.join(os.getcwd(), os.path.basename(remote_path))
            self.download_file(local_path, remote_path)
        elif self.isdir(remote_path):
            if not os.path.exists(local_path):
                os.makedirs(local_path)
            os.chdir(local_path)
            self.walktree(remote_path, self.download, self.download, self.download, recurse=False)
        else:
            input(self.tabs + "Wrong file name.")


    def download_manage_paths(self, local_path, remote_path):
        if not local_path:
            local_path = os.getcwd()
        relative_remote_path = os.path.normpath(remote_path[len(os.path.dirname(self.ori_remoth_path)) + 1:])
        local_path = os.path.join(self.ori_local_path, relative_remote_path)
        return local_path, remote_path


    def download_file(self, local_path, remote_path):
        self.get(remote_path, local_path)
        print('\n' + self.tabs + os.path.basename(remote_path) + "    ----->     " + local_path)
