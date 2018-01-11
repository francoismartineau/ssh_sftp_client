import os, platform, subprocess


def print_title():
    print('                                           \n   _|_|_|  _|_|_|_|  _|_|_|_|_|  _|_|_|    \n _|        _|            _|      _|    _|  \n   _|_|    _|_|_|        _|      _|_|_|    \n       _|  _|            _|      _|        \n _|_|_|    _|            _|      _|        ')

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def git_bash():
    subprocess.Popen(['C:\\Program Files\\Git\\git-bash.exe'])


def clean_a_remote_path(path):
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
        path = self.home + path[1:]
    if path[-1] != '/':
        path += '/'
    return path
 
def error(e):
    print(e)
    print("Are you sure the CLIENT'S global variables are right?")
    os.system('start "C:\\Program Files (x86)\\Vim\\vim80\\gvim.exe" C:\\_util\\home_server\\CLIENT.py')
