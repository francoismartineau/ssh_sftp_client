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
        print(self.tabs + "[3] Git bash")
    
    def get_entry(self):
        answer = input(self.tabs)
        if answer == '1':
            self.upload_file()
        elif answer == '2':
            self.download_file()
        elif answer == '3':
            util.git_bash()

    def upload_file(self):
        pysftp.Connection.__init__(self, host=self.host, username=self.user, private_key=self.key)
        local_file = input(self.tabs + "Local file: ")
        if os.path.isfile(local_file):
            remote_deposit = input(self.tabs + "Remote folder(optional): ")
            if not remote_deposit or not self.isdir(remote_deposit):
                print(self.tabs + "default deposit used")
                remote_deposit = self.default_remote_deposit
            remote_file = remote_deposit + "/" + os.path.basename(local_file)
            self.put(local_file, remote_file)
            input('\n' + self.tabs + local_file + "    ----->     " + remote_file)
            self.close()
        else:
            input(self.tabs + "Wrong file name.")
            

    def download_file(self):
        pysftp.Connection.__init__(self, host=self.host, username=self.user, private_key=self.key)
        remote_file = input(self.tabs + "Remote file: ")
        if self.isfile(remote_file):
            local_file_deposit = input(self.tabs + "Local folder(optional): ")
            if not local_file_deposit or not os.path.isdir(local_file_deposit):
                print(self.tabs + "default deposit used")
                local_file_deposit = self.default_local_deposit
            local_file = os.path.join(local_file_deposit, remote_file.split('/')[-1])
            self.get(remote_file, local_file)
            input('\n' + self.tabs + remote_file + "    ----->     " + local_file)
            self.close()
        else:
            input(self.tabs + "Wrong file name.")



