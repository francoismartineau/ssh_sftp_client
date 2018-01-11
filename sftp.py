import os, pysftp
import util


LOCALPATH = "C:\\_util\\home_server\\deposit"

class Client(pysftp.Connection):
    def __init__(self, user, host, key):
        pysftp.Connection.__init__(self, host=host, username=user, private_key=key)
        util.clear_console()
        util.print_title()
        self.chdir("/home/ffran")

    def execute_command(self, command):
        global LOCALPATH
        instruction = command.split(" ")
        command = instruction[0]
        arguments = instruction[1:]
        try:
            if command == "cd":
                self.cd(arguments)
            elif command == "help":
                self.help()
            elif command == "ls":
                self.ls()
            elif command == "clear":
                self.clear()
            elif command == "close":
                self.close()
                return False
            elif command == "upload":
                self.upload(arguments[0])
            elif command == "download":
                if not arguments:
                    arguments.append(self.getcwd())
                    self.cd("..")
                    self.download(arguments[0])
                    self.cd(arguments[0])
                elif len(arguments) == 1:
                    if not (self.isdir(arguments[0]) or self.isfile(arguments[0])):
                        LOCALPATH = arguments[0]
                        arguments[0] = self.getcwd()
                        self.cd("..")
                        self.download(arguments[0])
                        self.cd(arguments[0])
                    else:
                        self.download(arguments[0])
                elif len(arguments) == 2:
                    LOCALPATH = arguments[1]
                    self.download(arguments[0])
        except IndexError as e:
            print(command + " needs an argument")
            

    def cd(self, path):
        if not type(path) == type([]):
            path = [path]
        if path == []:
            self.chdir("/home/ffran")
        elif path == "..":
            self.chdir(os.path.dirname(self.getcwd()))
        else:
            path = os.path.join(self.getcwd(), path[0]).replace("\\", "/")
            if self.isdir(path):
                self.chdir(path)
            else:
                print("\t" + path + ": No such file or directory.")

    def ls(self):
        for i in self.listdir():
            print("\t" + i)
    def clear(self):
        util.clear_console()
        util.print_title()

    def upload(self, local_path, remote_path=""):
        if not remote_path: remote_path = self.getcwd()
        remote_path += "/" + os.path.basename(local_path)
        if os.path.isfile(local_path):
            self.put(local_path, remote_path)
        elif os.path.isdir(local_path):
            self.makedirs(remote_path)
            for (cwd, dirs, files) in os.walk(local_path):
                for d in dirs:
                    self.upload(os.path.join(cwd, d), remote_path)
                for f in files:
                    self.upload(os.path.join(cwd, f), remote_path)
                break
        else:
            print("invalid path provided")
        print('\t-->  ' + remote_path)
    

    def download(self, remote_path):
        local_path = LOCALPATH
        relative_path = remote_path.replace(self.getcwd(), "")
        if len(relative_path):
            if relative_path[0] == "/":
                relative_path = relative_path[1:]
        local_path = os.path.join(local_path, os.path.normpath(relative_path))
        if self.isdir(remote_path):
            if not os.path.isdir(local_path):
                os.makedirs(local_path)
            self.walktree(remote_path, self.download, self.download, self.download, recurse=False)
        elif self.isfile(remote_path):
            self.get(remote_path, local_path)
        print('\t-->  ' + local_path)

    @staticmethod
    def help():
        print("Commands:")
        print("\tcd path\tChange directory")
        print("\tls\tDisplay directory content")
        print("\tclear\tClear screen")
        print("\tupload localPath")
        print("\tdownload remotePath localDirectory")

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
        if path[-1] != '/':
            path += '/'
        return path
 
